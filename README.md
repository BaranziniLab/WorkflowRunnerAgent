# WorkflowRunnerAgent

MCP helper for Nextflow, nf-core, Snakemake, CWL, WDL, container/runtime checks, and reproducible workflow run manifests.

This repository is a BioRouter `.brxt` extension following the same root-manifest, Python-package, and bundled-skill convention used by `SPOKEAgent` and `UCSFOMOPAgent`.

## Tools

- `get_workflowrunneragent_status`: show configured environment, API targets, and local command availability without revealing secrets.
- `list_workflowrunneragent_api_targets`: list named external API bases.
- `call_workflowrunneragent_api`: call a guarded API endpoint; write-capable HTTP methods require `allow_mutation=true`.
- `plan_workflowrunneragent_command`: inspect whether a local command is allowlisted and what approval is needed.
- `run_workflowrunneragent_command`: run an allowlisted command without shell expansion after explicit `allow_execute=true` approval.
- `summarize_workflowrunneragent_resource`: summarize a JSON payload or export while preserving provenance fields.

## Configuration

| Variable | Required | Secret | Purpose |
|---|---:|---:|---|
| `WORKFLOW_RUNNER_LOG_LEVEL` | false | false | Logging level |


## Build

```bash
uv sync
scripts/build_brxt.sh
```

The bundle is written to `dist/workflowrunneragent.brxt`.

## Install in BioRouter

```bash
biorouter extension install dist/workflowrunneragent.brxt
```

## License

Apache-2.0. See `LICENSE`.
