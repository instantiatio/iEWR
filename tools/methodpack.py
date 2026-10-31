#!/usr/bin/env python3
"""Read-only schema-2 MethodPack checks and guarded POSIX activation of a saved pair.

Shipped JSON-form YAML needs only Python. Other YAML requires supplied PyYAML.
Index/source content is data, never executable code.
"""
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import uuid

BOOK, INDEX = 'methods/METHOD_PACK.md', 'methods/index.yaml'
PENDING = 'methods/.activation/pending.json'
LIMIT = 32 * 1024 * 1024
EDITION = re.compile(r'[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z')
METHOD_EDITION = re.compile(r'v?[0-9][A-Za-z0-9._-]{0,126}\Z')

class Refusal(Exception):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)

def need(ok, code, message):
    if not ok: raise Refusal(code, message)

def sha(data): return hashlib.sha256(data).hexdigest()

def local(root, name):
    need(isinstance(name, str) and name and '\\' not in name and '\x00' not in name,
         'path', 'Expected project-relative path')
    need(not PurePosixPath(name).is_absolute() and not re.match(r'^[A-Za-z]:', name)
         and all(x not in ('', '.', '..') for x in name.split('/')), 'path', 'Unsafe path: ' + name)
    path = root
    for part in PurePosixPath(name).parts:
        path /= part
        need(not path.is_symlink(), 'symlink', 'Symlink unsupported: ' + name)
    need(path.resolve().is_relative_to(root), 'path', 'Path escapes root')
    return path

def read_bytes(root, name):
    path = local(root, name)
    need(path.is_file(), 'missing', 'Missing file: ' + name)
    need(path.stat().st_size <= LIMIT, 'size', 'File exceeds limit: ' + name)
    return path.read_bytes()

def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'duplicate_key', 'Duplicate mapping key: ' + str(key))
        result[key] = value
    return result

def load(data):
    text = data.decode('utf-8')
    def nonfinite(value): raise Refusal('syntax', 'Non-finite JSON value')
    try: return json.loads(text, object_pairs_hook=unique, parse_constant=nonfinite)
    except json.JSONDecodeError:
        try: import yaml
        except ImportError: raise Refusal('yaml_parser_unavailable', 'Use JSON-form YAML or supply PyYAML; nothing is installed')
        try:
            need(not any(isinstance(e, yaml.AliasEvent) for e in yaml.parse(text)), 'yaml_alias', 'Aliases unsupported')
            class Loader(yaml.SafeLoader): pass
            def mapping(loader, node):
                return unique((loader.construct_object(k), loader.construct_object(v)) for k, v in node.value)
            Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
            return yaml.load(text, Loader=Loader)
        except yaml.YAMLError as exc: raise Refusal('yaml_syntax', str(exc))

def structural_lines(text):
    """Preserve line numbers while excluding CommonMark fenced code from structure."""
    result, fence, width = [], None, 0
    for line in text.splitlines():
        if fence:
            if re.fullmatch(r' {0,3}' + re.escape(fence) + '{' + str(width) + r',}[ \t]*', line):
                fence = None
            result.append('')
            continue
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if match and not (match[1][0] == '`' and '`' in match[2]):
            fence, width = match[1][0], len(match[1]); result.append('')
        else: result.append(line)
    return result

def anchors(text, anchor):
    pattern = r'[ \t]*<a[ \t]+id=[\"\']' + re.escape(anchor) + r'[\"\'][ \t]*>[ \t]*</a>[ \t]*'
    return [i+1 for i,line in enumerate(structural_lines(text)) if not line.startswith(('    ','\t')) and re.fullmatch(pattern,line)]

def body_end(lines, start):
    structure = structural_lines('\n'.join(lines))
    heading = re.match(r'^(#{1,6})\s+', structure[start - 1])
    need(heading is not None, 'location', 'Body must start at heading')
    end = len(lines)
    for i in range(start, len(lines)):
        h = re.match(r'^(#{1,6})\s+', structure[i])
        if re.match(r'^ {0,3}<a\s+id=', structure[i]) or (h and len(h[1]) <= len(heading[1])):
            end = i; break
    while end > start and not lines[end - 1].strip(): end -= 1
    return end

def raw_current(root):
    result = []
    for name in (BOOK, INDEX):
        path = local(root, name)
        need(not path.exists() or path.is_file(), 'file_type', 'Current path is not a regular file: ' + name)
        result.append(read_bytes(root, name) if path.is_file() else None)
    return result

def token(pair):
    return 'absent' if pair == [None, None] else ':'.join(sha(x) if x is not None else 'absent' for x in pair)

def current(root):
    pair = raw_current(root)
    need(all(x is None for x in pair) or all(x is not None for x in pair), 'partial_current', 'Only one current file exists')
    return pair

def inspect(root, snapshot=None, ignore_pending=False):
    """No writes. Checks are qualified only for captured bytes and dependencies."""
    root = Path(root).resolve()
    result = {'passed': False, 'root': str(root), 'selection': snapshot or 'current', 'errors': [], 'warnings': [],
              'scope': 'File/description consistency; not method quality, authority or ADE isolation'}
    seen, cached = {}, {}
    def read(name):
        if name in cached: return cached[name]
        data = read_bytes(root, name)
        need(name not in seen or seen[name] == sha(data), 'input_changed', 'Changed during check: ' + name)
        seen[name] = sha(data)
        cached[name] = data
        return data
    try:
        result['current_token'] = token(raw_current(root))
        need(ignore_pending or not local(root, PENDING).exists(), 'pending_activation', 'Recover unfinished attempt before use')
        if snapshot is None:
            pair = current(root)
            if pair == [None, None]:
                result.update(passed=True, state='absent', active_methods=0, dependencies={})
                return result, pair
            book_bytes, index_bytes = read(BOOK), read(INDEX)
        else:
            need(isinstance(snapshot, str) and bool(EDITION.fullmatch(snapshot)), 'edition', 'Invalid snapshot name')
            base = 'methods/snapshots/' + snapshot
            book_bytes, index_bytes = read(base + '/METHOD_PACK.md'), read(base + '/index.yaml')
        index = load(index_bytes)
        need(isinstance(index, dict) and index.get('schema_version') == 2 and index.get('path_base') == 'project_root',
             'schema', 'Expected schema 2 / project_root mapping')
        pack = index.get('pack', {})
        need(isinstance(pack, dict), 'schema', 'pack must be a mapping')
        need(isinstance(pack.get('id'), str) and pack['id'].strip(), 'schema', 'Missing pack ID')
        edition = pack.get('edition')
        need(isinstance(edition, str) and bool(EDITION.fullmatch(edition)), 'edition', 'Invalid pack edition')
        saved = 'methods/snapshots/' + edition
        need(pack.get('description') == BOOK, 'description', 'Pack must point to current book')
        need(pack.get('snapshot') == saved + '/METHOD_PACK.md' and (snapshot is None or snapshot == edition),
             'snapshot_binding', 'Selected directory / pack edition / snapshot disagree')
        need(read(saved + '/METHOD_PACK.md') == book_bytes, 'book_pair', 'Book differs from declared saved pair')
        need(read(saved + '/index.yaml') == index_bytes, 'index_pair', 'Index differs from declared saved pair')
        text = book_bytes.decode('utf-8'); lines = text.splitlines()
        need(lines and re.search(r'(?<![A-Za-z0-9._-])' + re.escape(edition) + r'(?![A-Za-z0-9._-])', lines[0]),
             'book_edition', 'Book title does not identify pack edition')
        methods = index.get('methods')
        need(isinstance(methods, list), 'schema', 'methods must be a list, possibly empty')
        entries, ranges = {}, []
        for method in methods:
            need(isinstance(method, dict), 'schema', 'Method must be a mapping')
            for key in ('id','name','edition','description','anchor','preserved_body','use_when','status'):
                need(isinstance(method.get(key), str) and method[key].strip(), 'schema', 'Missing method string: ' + key)
            for key in ('keywords','basis','evidence','limits'):
                need(isinstance(method.get(key), list), 'schema', 'Missing method list: ' + key)
            ident, ed = method['id'], method['edition']
            need(ident not in entries, 'duplicate_id', 'Duplicate active ID: ' + ident)
            need(bool(EDITION.fullmatch(ident)) and bool(METHOD_EDITION.fullmatch(ed)), 'method_identity', 'Invalid method ID/edition')
            entries[ident] = ed
            need(method['preserved_body'].startswith('methods/snapshots/'), 'preserved_body', 'Active body must have an immutable snapshot return')
            need(method['description'] == BOOK, 'description', 'Active description differs from book: ' + ident)
            loc = method.get('location', {})
            need(isinstance(loc, dict), 'location', 'Location must be mapping')
            start, end = loc.get('start_line'), loc.get('end_line')
            need(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), 'location', 'Invalid range: ' + ident)
            found = anchors(text, method['anchor'])
            need(len(found) == 1, 'anchor', 'Method anchor must be unique: ' + ident)
            heading = found[0] + 1
            while heading <= len(lines) and not lines[heading-1].strip(): heading += 1
            need(heading <= len(lines) and re.match(r'^#{1,6}\s+' + re.escape(ident) + r'\s+' + re.escape(ed) + r'(?:\s|$)', lines[heading-1]),
                 'method_heading', 'Actual title ID/edition differs: ' + ident)
            need(start in (found[0], heading), 'location', 'Range must start at anchor or exact heading: ' + ident)
            need(body_end(lines, heading) == end, 'location', 'Range omits or includes other content: ' + ident)
            need(not any(start <= b and a <= end for a,b in ranges), 'location', 'Overlapping ranges')
            ranges.append((start,end))
            preserved = read(method['preserved_body']).decode('utf-8'); found = anchors(preserved, method['anchor'])
            need(len(found) == 1, 'preserved_body', 'Saved method anchor unavailable: ' + ident)
            pl = preserved.splitlines(); ps = found[0] + 1
            while ps <= len(pl) and not pl[ps-1].strip(): ps += 1
            need(ps <= len(pl), 'preserved_body', 'Saved method heading unavailable')
            need('\n'.join(pl[ps-1:body_end(pl,ps)]) == '\n'.join(lines[heading-1:end]),
                 'preserved_body', 'Same edition has different saved method body: ' + ident)
            for kind in ('basis','evidence','external_relations'):
                refs = method.get(kind, [])
                need(isinstance(refs, list), 'schema', kind + ' must be a list')
                for ref in refs:
                    if isinstance(ref, str) and ref.strip():
                        file_like = '://' not in ref and ('/' in ref or '\\' in ref or re.search(r'\.[A-Za-z][A-Za-z0-9]{0,9}$', ref) or (len(ref)<256 and (root/ref).is_file()))
                        if file_like:
                            ref = {'path': ref}
                        else:
                            result['warnings'].append({'code': 'citation_not_file_checked', 'method': ident, 'field': kind, 'reference': ref})
                            continue
                    need(isinstance(ref, dict) and isinstance(ref.get('path'), str) and ref['path'], 'reference', 'File reference must name a path or be a nonempty citation')
                    if ref.get('path'):
                        data = read(ref['path']); expected = ref.get('source_sha256') or ref.get('sha256')
                        if expected: need(sha(data) == expected, 'source_digest', 'Pinned source changed: ' + ref['path'])
                        if ref.get('anchor'): need(len(anchors(data.decode('utf-8'), ref['anchor'])) == 1, 'reference_anchor', 'Missing referenced anchor')
        structure = structural_lines(text)
        previous = ''
        for number, line in enumerate(structure, 1):
            title = re.match(r'^#{1,6}\s+([A-Za-z0-9][A-Za-z0-9._-]*)\s+(v?[0-9][A-Za-z0-9._-]*)(?:\s|$)', line)
            marked = re.match(r'^ {0,3}<a\s+id=', previous)
            if number > 1 and title and marked and not any(a <= number <= b for a,b in ranges):
                need(False, 'unindexed_method', 'Anchored method entry absent from active index: ' + title[1])
            if line.strip(): previous = line
        for method in methods:
            refs = method.get('relations', [])
            need(isinstance(refs, list), 'relation', 'relations must be a list')
            for ref in refs:
                need(isinstance(ref, dict) and isinstance(ref.get('target'),str) and '@' in ref['target'], 'relation', 'Use exact active ID@edition')
                ident, ed = ref['target'].rsplit('@',1)
                need(entries.get(ident) == ed, 'relation', 'Dangling/stale relation: ' + ref['target'])
        retired = index.get('retired_methods', [])
        need(isinstance(retired, list), 'retired', 'retired_methods must be a list')
        retired_ids = set()
        for entry in retired:
            need(isinstance(entry, dict), 'retired', 'Retirement record must be a mapping')
            for key in ('id', 'edition', 'anchor', 'reason'):
                need(isinstance(entry.get(key), str) and entry[key].strip(), 'retired', 'Retirement needs ' + key)
            need(entry['id'] not in entries and entry['id'] not in retired_ids, 'retired', 'Duplicate/active retirement ID')
            need(bool(METHOD_EDITION.fullmatch(entry['edition'])), 'retired', 'Retired description edition needs a numeric version')
            retired_ids.add(entry['id'])
            path = entry.get('saved_body') or entry.get('body')
            need(isinstance(path, str) and path.startswith('methods/'), 'retired', 'Retirement needs saved body')
            saved_method(read(path).decode('utf-8'), entry)
            path = entry.get('saved_index') or entry.get('index')
            if path: read(path)
        for name, expected in seen.items(): need(sha(read_bytes(root,name)) == expected, 'input_changed', 'Checked input changed: ' + name)
        result.update(passed=True, state='consistent', edition=edition, active_methods=len(methods),
                      book_sha256=sha(book_bytes), index_sha256=sha(index_bytes), dependencies=seen)
        return result, [book_bytes,index_bytes]
    except (Refusal,OSError,ValueError,TypeError,KeyError,RecursionError) as exc:
        result['errors'].append({'code':getattr(exc,'code','read_or_syntax'),'message':str(exc)})
        return result, None

def sync_dir(path):
    fd = os.open(path, os.O_RDONLY)
    try: os.fsync(fd)
    finally: os.close(fd)

def atomic_write(path, data):
    tmp = path.with_name('.'+path.name+'-'+uuid.uuid4().hex+'.tmp')
    try:
        with tmp.open('xb') as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
        os.replace(tmp,path); sync_dir(path.parent)
    finally: tmp.unlink(missing_ok=True)

@contextmanager
def writer_lock(root):
    try: import fcntl
    except ImportError: raise Refusal('lock_unsupported','Activation needs POSIX flock; read-only check is available')
    path = local(root,'methods/.activation.lock')
    with os.fdopen(os.open(path,os.O_RDWR|os.O_CREAT|getattr(os,'O_NOFOLLOW',0),0o600),'a+b') as stream:
        try: fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: raise Refusal('writer_busy','Another cooperating writer holds the pack lock')
        try: yield
        finally: fcntl.flock(stream,fcntl.LOCK_UN)

def record(path, data): atomic_write(path,(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode())

def saved_method(text, entry):
    found = anchors(text, entry['anchor'])
    need(len(found) == 1, 'retired', 'Saved retired anchor unavailable')
    lines = text.splitlines(); start = found[0] + 1
    while start <= len(lines) and not lines[start-1].strip(): start += 1
    need(start <= len(lines) and re.match(r'^#{1,6}\s+' + re.escape(entry['id']) + r'\s+' + re.escape(entry['edition']) + r'(?:\s|$)', lines[start-1]), 'retired', 'Retired ID/edition and saved heading differ')
    return '\n'.join(lines[start-1:body_end(lines,start)])

def method_accounts(root, pair):
    if pair == [None, None]: return []
    index = load(pair[1]); lines = pair[0].decode('utf-8').splitlines(); result = []
    need(isinstance(index, dict) and isinstance(index.get('methods'), list), 'history', 'Invalid recorded index')
    for method in index['methods']:
        result.append(((method['id'], method['edition']), saved_method(pair[0].decode('utf-8'), method)))
    for entry in index.get('retired_methods', []):
        path = entry.get('saved_body') or entry.get('body')
        result.append(((entry['id'], entry['edition']), saved_method(read_bytes(root,path).decode('utf-8'),entry)))
    return result

def transition(root, old_pair, new_pair):
    # Reuse the existing immutable attempt receipts; no second method catalogue.
    known = {}
    def add(pair):
        for key,body in method_accounts(root,pair):
            need(key not in known or known[key] == body, 'history_conflict', 'Different recorded bodies for ' + '@'.join(key))
            known[key] = body
    add(old_pair)
    history = local(root, 'methods/.activation')
    if history.exists():
        for folder in sorted(history.iterdir()):
            if not re.fullmatch('[0-9a-f]{32}', folder.name): continue
            prefix = 'methods/.activation/' + folder.name
            journal = load(read_bytes(root,prefix+'/record.json'))
            need(isinstance(journal,dict) and journal.get('attempt')==folder.name and journal.get('state') in ('prepared','published','restored'), 'history', 'Invalid attempt receipt')
            for label in (['before','after'] if journal['state']=='published' else ['before']):
                hashes = journal.get(label)
                need(isinstance(hashes,list) and len(hashes)==2, 'history', 'Invalid recorded pair hashes')
                contents=[]
                for name,expected in zip(('METHOD_PACK.md','index.yaml'),hashes):
                    data = read_bytes(root,prefix+'/'+label+'/'+name) if expected is not None else None
                    need((sha(data) if data is not None else None)==expected,'history','Recorded pair bytes changed')
                    contents.append(data)
                need(all(x is None for x in contents) or all(x is not None for x in contents),'history','Partial history pair')
                add(contents)
    for key,body in method_accounts(root,new_pair):
        need(key not in known or known[key]==body,'method_edition_reused','Changed body must have a new description edition: '+'@'.join(key))
    if old_pair != [None,None]:
        old_index,new_index=load(old_pair[1]),load(new_pair[1])
        new_ids={m['id'] for m in new_index['methods']}
        retired={m['id']:m for m in new_index.get('retired_methods',[])}
        for method in old_index['methods']:
            if method['id'] not in new_ids:
                need(method['id'] in retired and retired[method['id']]['edition']==method['edition'], 'retirement_required','Removed ID needs its exact retirement return: '+method['id'])
    return len(known)

def activate(root, snapshot, expected):
    root = Path(root).resolve()
    checked,pair = inspect(root,snapshot)
    need(checked['passed'] and pair is not None,'candidate_failed',json.dumps(checked['errors'],ensure_ascii=False))
    with writer_lock(root):
        need(not local(root,PENDING).exists(),'pending_activation','Recover unfinished attempt first')
        before = current(root)
        need(token(before)==expected,'stale_current','Current token differs; inspect actual current')
        old_check, old_pair = inspect(root)
        need(old_check['passed'] and old_pair == before, 'current_failed', 'Current is inconsistent; preserve/reconcile before activation')
        history_count = transition(root, before, pair)
        again,captured = inspect(root,snapshot)
        need(again['passed'] and captured==pair and again['dependencies']==checked['dependencies'], 'input_changed','Checked candidate/dependency changed')
        if before==pair: return dict(again,action='already_current',changed=False,current_token=token(before))
        ident = uuid.uuid4().hex; folder = local(root,'methods/.activation/.prepare-'+ident);folder.mkdir(parents=True,exist_ok=False)
        for label,contents in [('before',before),('after',pair)]:
            (folder/label).mkdir()
            for name,data in zip(('METHOD_PACK.md','index.yaml'),contents):
                if data is not None: atomic_write(folder/label/name,data)
        journal = {'attempt':ident,'state':'prepared','snapshot':snapshot,
                   'before':[sha(x) if x is not None else None for x in before], 'after':[sha(x) for x in pair],
                   'dependencies':checked['dependencies']}
        record(folder/'record.json',journal)
        committed = local(root,'methods/.activation/'+ident)
        folder.rename(committed);folder=committed;sync_dir(folder.parent)
        record(local(root,PENDING),{'attempt':ident})
        need(token(current(root))==expected,'stale_current','Current changed before replacement')
        for name,data in zip((BOOK,INDEX),pair): atomic_write(local(root,name),data)
        final,actual = inspect(root,ignore_pending=True)
        need(final['passed'] and actual==pair,'postcheck_failed','Published pair failed; recover same attempt')
        journal['state']='published';record(folder/'record.json',journal)
        local(root,PENDING).unlink();sync_dir(folder.parent)
        return dict(final,action='activated',changed=True,attempt=ident,current_token=token(pair),
                    previous_state='methods/.activation/'+ident+'/before',history_method_editions_checked=history_count,sequential_not_atomic=True)

def recover(root, expected):
    """Explicitly restore one incomplete attempt, holding unknown foreign edits."""
    root=Path(root).resolve()
    with writer_lock(root):
        marker=load(read_bytes(root,PENDING))
        need(isinstance(marker, dict), 'journal', 'Invalid pending marker')
        ident=marker.get('attempt','')
        need(isinstance(ident,str) and re.fullmatch('[0-9a-f]{32}',ident),'journal','Invalid attempt')
        prefix='methods/.activation/'+ident;journal=load(read_bytes(root,prefix+'/record.json'))
        need(isinstance(journal, dict) and journal.get('attempt')==ident and isinstance(journal.get('before'),list) and isinstance(journal.get('after'),list) and len(journal['before'])==len(journal['after'])==2,'journal','Invalid recovery record')
        need(all(x is None or (isinstance(x,str) and re.fullmatch('[0-9a-f]{64}',x)) for x in journal['before']) and all(isinstance(x,str) and re.fullmatch('[0-9a-f]{64}',x) for x in journal['after']), 'journal', 'Invalid recovery hashes')
        actual=raw_current(root);need(token(actual)==expected,'stale_current','Recovery current token differs')
        for i,data in enumerate(actual):
            need((sha(data) if data is not None else None) in (journal['before'][i],journal['after'][i]),'foreign_current','Unrecorded edit; hold recovery')
        old=[]
        for i,name in enumerate(('METHOD_PACK.md','index.yaml')):
            data=read_bytes(root,prefix+'/before/'+name) if journal['before'][i] is not None else None
            need((sha(data) if data is not None else None)==journal['before'][i],'journal','Recorded before bytes changed')
            old.append(data)
        for name,data in zip((BOOK,INDEX),old):
            path=local(root,name)
            if data is None: path.unlink(missing_ok=True);sync_dir(path.parent)
            else: atomic_write(path,data)
        need(raw_current(root)==old,'restore_failed','Restored bytes differ; pending retained')
        journal['state']='restored';record(local(root,prefix+'/record.json'),journal)
        local(root,PENDING).unlink();sync_dir(local(root,'methods/.activation'))
        return {'passed':True,'action':'restored_exact_before','attempt':ident,'current_token':token(old),
                'scope':'Byte restoration only, not previous method consistency/quality'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['check','activate','recover'])
    parser.add_argument('--root',default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument('--snapshot')
    parser.add_argument('--expect-current',help='Token from check; required for mutations')
    parser.add_argument('--json',action='store_true');args=parser.parse_args()
    try:
        if args.command=='check': result,_=inspect(args.root,args.snapshot)
        else:
            need(bool(args.expect_current),'expected_current_required','Mutation requires current token from check')
            if args.command=='activate':
                need(bool(args.snapshot),'snapshot_required','Activation requires --snapshot')
                result=activate(args.root,args.snapshot,args.expect_current)
            else:
                need(args.snapshot is None,'arguments','Recovery restores recorded before, not another snapshot')
                result=recover(args.root,args.expect_current)
    except (Refusal,OSError,ValueError,TypeError,KeyError,RecursionError) as exc:
        result={'passed':False,'errors':[{'code':getattr(exc,'code','operation_failed'),'message':str(exc)}]}
    if args.json: print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print(('OK' if result['passed'] else 'HOLD')+': '+result.get('action',result.get('state','check failed')))
        for error in result.get('errors',[]): print(error['code']+': '+error['message'])
        if result.get('current_token'): print('current_token: '+result['current_token'])
    return 0 if result['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
