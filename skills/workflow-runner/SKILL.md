---
name: workflow-runner
description: Use WorkflowRunnerAgent when working with workflow execution data, APIs, local tools, provenance, or reproducibility checks from inside BioRouter.
license: Apache-2.0
user-invocable: false
---

# WorkflowRunnerAgent Skill

Use this extension to inspect workflow engines, plan runs, validate versions, and execute only explicitly approved local workflow commands.

## Operating rules

- Start with `get_workflowrunneragent_status` to confirm configured API targets, optional credentials, and command availability.
- Use `list_workflowrunneragent_api_targets` before constructing API paths.
- Prefer read-only `GET` API calls while exploring.
- Do not use mutation-capable API methods unless the user explicitly approves the exact platform, resource, and expected side effect.
- Use `plan_workflowrunneragent_command` before local or remote execution.
- Do not run `run_workflowrunneragent_command` unless the user has approved the exact command, arguments, working directory, and side effects.
- Preserve accession IDs, DOIs, PMIDs, PMCID, versions, timestamps, file paths, command lines, and URLs in final reports.
- Never print API tokens, passwords, bearer headers, cookies, SSH keys, or session secrets.
