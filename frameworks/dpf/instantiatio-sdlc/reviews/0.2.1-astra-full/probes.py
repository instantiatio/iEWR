"""Synthetic review calculations; not application, DB-concurrency or user trials."""
import json, heapq, itertools

results = {}
# Q1: FIFO among equal-priority jobs is part of the required behavior.
jobs = [(2, "Z"), (1, "B"), (1, "A"), (2, "C")]
expected = ["B", "A", "Z", "C"]
stable = [v for _, v in sorted(jobs, key=lambda x: x[0])]
heap = [(priority, seq, name) for seq, (priority, name) in enumerate(jobs)]
heapq.heapify(heap)
actual = [heapq.heappop(heap)[2] for _ in jobs]
bad = [v for _, v in sorted(jobs)]
assert stable == actual == expected and bad != expected
results["Q1_priority_fifo"] = dict(expected=expected, stable=stable, heap=actual, wrong_lexical_tie=bad)

# Q2: SCI with SC -> I, I -> C. SI/IC is lossless but not dependency preserving.
def closure(attrs, fds):
    r=set(attrs)
    while True:
        n=set(r)
        for lhs,rhs in fds:
            if set(lhs)<=r: n.update(rhs)
        if n==r:return ''.join(sorted(r))
        r=n
local=[('I','C')]
assert closure('I',local)=='CI' and closure('SC',local)=='CS'
si=[('s1','i1'),('s1','i2')]
ic=[('i1','c1'),('i2','c1')]
join=[(s,c,i) for s,i in si for j,c in ic if i==j]
assert len({i for s,c,i in join if (s,c)==('s1','c1')})==2
results["Q2_lossless_not_dependency_preserving"] = dict(intersection_closure=closure('I',local), sc_local_closure=closure('SC',local), join=join, violates_SC_to_I=True)

# Q4: Atomic operation store model: commit is explicitly indivisible here.
ops={}; effects=[]
def create(principal,key,payload):
    scope=(principal,key)
    if scope in ops:
        old,rid=ops[scope]
        return ('same',rid) if old==payload else ('conflict',None)
    rid=len(effects)+1
    effects.append((rid,principal,payload))
    ops[scope]=(payload,rid)
    return ('new',rid)
a=create('a','k','x'); b=create('a','k','x'); c=create('a','k','y'); d=create('b','k','z')
assert a[1]==b[1] and c[0]=='conflict' and len(effects)==2
results["Q4_atomic_model"] = dict(first=a,replay=b,changed_payload=c,other_principal=d,effects=len(effects),limit='Sequential model assuming indivisible commit; no concurrent database execution')

# Q5: Stale responses must be guarded by both account epoch and request generation.
current=('userB',2)
responses=[(('userB',2),'B-new'),(('userA',1),'A-old')]
naive=None; guarded=None
for token,value in responses:
    naive=value
    if token==current: guarded=value
assert naive=='A-old' and guarded=='B-new'
results["Q5_client_race"] = dict(naive=naive,guarded=guarded)

# Q6: A feature change must include the cache key as a cooperating locus.
rows=[{'id':1,'archived':False},{'id':2,'archived':True}]
def query(include_archived=False):
    return [r['id'] for r in rows if include_archived or not r['archived']]
def endpoint(cache,include_archived=False,fixed=False):
    key=('list',include_archived) if fixed else 'list'
    if key not in cache: cache[key]=query(include_archived)
    return cache[key]
c1={}; old=endpoint(c1); wrong=endpoint(c1,True)
c2={}; kept=endpoint(c2,fixed=True); new=endpoint(c2,True,fixed=True)
assert query(True)==[1,2] and wrong==[1] and new==[1,2] and old==kept==[1]
results["Q6_cooperating_cache_edit"] = dict(unit_new=query(True),wrong_integrated=wrong,fixed_new=new,preserved_default=kept)

# Q7: Distinguish cached-result defect from source selection defect.
cold=endpoint({},True)
warm_cache={}; endpoint(warm_cache); warm=endpoint(warm_cache,True)
assert cold==[1,2] and warm==[1] and query(True)==[1,2]
results["Q7_diagnosis"] = dict(cold=cold,warm=warm,direct=query(True),supported='cache path',limit='Synthetic deterministic reproduction, not production root cause')

# Q8: Extracting a helper must preserve lazy evaluation under the guard.
def original(allowed,events):
    if allowed:
        events.append('load')
        return 7
    return None
def wrong_refactor(allowed,events):
    events.append('load')
    value=7
    return value if allowed else None
def fixed_refactor(allowed,events):
    def load(): events.append('load'); return 7
    return load() if allowed else None
observations=[]
for allowed in (False,True):
    logs=[[],[],[]]
    values=[fn(allowed,log) for fn,log in zip((original,wrong_refactor,fixed_refactor),logs)]
    assert values[0]==values[2] and logs[0]==logs[2]
    observations.append(dict(allowed=allowed,values=values,effects=logs))
assert observations[0]['effects'][0]!=observations[0]['effects'][1]
results["Q8_refactor_effects"] = observations

# Q9: Rolling a snapshot back loses writes that followed it.
snapshot={1:1250}; live={**snapshot,2:990}; restored=dict(snapshot)
assert set(live)-set(restored)=={2}
results["Q9_restore_model"] = dict(live_ids=sorted(live),restored_ids=sorted(restored),lost_post_snapshot=[2],limit='Set calculation; no real backup or restore')
print(json.dumps(results,ensure_ascii=False,indent=2))
