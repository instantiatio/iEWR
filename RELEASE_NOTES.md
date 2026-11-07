# iEWR 7.0.8 Eternal Alpha

This release includes the changes developed after the public 7.0.6 release. See [README.md](README.md) for the purpose of iEWR and how to get started.

- A short cue ties method choice to the intended result and actual conditions. It helps the agent check an uncertainty that could change the choice, reuse a sufficient basis, and reopen a choice when its conditions change.
- Ordinary projects keep a [method-use log](docs/METHOD_USE_LOG.md) of actual FPF and MethodPack applications. The default is one line per distinct application. A detailed entry can be added on request. The log retains significant failed, interrupted, and revised applications.
- The agent saves accessible original chat attachments in the active project, verifies their bytes, and keeps distinct originals that share a name.
- The FPF index generator stages writes in a private temporary directory. It replaces the index after a successful write and preserves the previous index on a write failure.
- When input from Human is required, the agent completes useful independent work first. It can ask sooner when work can continue while waiting and the overlap is likely to save time. A handoff opens with a short status.
- The startup instructions lead directly from README to AGENTS.md. The ZIP opens into the `iEWR-7.0.8-Eternal-Alpha` folder.

See [STATUS.md](STATUS.md) for the checks and their scope.
