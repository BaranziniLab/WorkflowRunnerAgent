---
name: workflow-runner
description: "Moved: use workflow-management instead. This skill no longer holds instructions."
---

# workflow-runner has moved

This skill was bundled with WorkflowRunnerAgent. Its content now lives in `workflow-management`. Install `workflow-management` from BAAM in Biorouter and use it instead.

WorkflowRunnerAgent was retired on 2026-11-22 and no longer calls any service. Why: It ran local commands without the secret guard. The Developer extension is the one command runner and carries the guard. Use instead: Use the Developer extension with the workflow-management skill.
