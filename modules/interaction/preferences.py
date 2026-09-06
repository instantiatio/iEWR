"""I owns presentation-only scoped preferences, never execution permissions."""
from hashlib import sha256


class Preferences:
    def __init__(self, store, project, initiative=None):
        self.store, self.project, self.initiative = store, project, initiative
        self.transient = {}

    def key(self, scope):
        identity = self.project if scope == "project" else self.initiative
        if not identity:
            raise ValueError("preference_scope_identity_missing")
        return sha256(("preference:" + scope + ":" + identity).encode()).hexdigest()

    def set(self, guidance, progress, scope="session", explicit_persistence=False):
        if guidance not in ("guided", "standard", "compact") or progress not in ("detailed", "milestone"):
            raise ValueError("unsupported_presentation_preference")
        value = {"guidance": guidance, "progress": progress}
        if scope in ("command", "session"):
            self.transient[scope] = value
        elif scope in ("initiative", "project") and explicit_persistence:
            key = self.key(scope)
            self.store.write(key, {"kind": "preferences", "scope": scope, **value}, self.store.read(key))
        else:
            raise ValueError("explicit_persistent_scope_required")
        return {"scope": scope, **value, "limit": "presentation_only"}

    def resolve(self):
        for scope in ("command", "session", "initiative", "project"):
            if scope in self.transient:
                return dict(self.transient[scope])
            if scope == "initiative" and not self.initiative:
                continue
            if scope in ("initiative", "project"):
                saved = self.store.read(self.key(scope))
                if saved:
                    return {k: saved[k] for k in ("guidance", "progress")}
        return {"guidance": "standard", "progress": "milestone"}

    def end_command(self):
        self.transient.pop("command", None)
