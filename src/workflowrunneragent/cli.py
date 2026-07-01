"""Command-line entry point for WorkflowRunnerAgent."""

import logging
import os

from workflowrunneragent.server import main as server_main

logger = logging.getLogger("WorkflowRunnerAgent")


def main() -> None:
    log_level = os.getenv("WORKFLOW_RUNNER_LOG_LEVEL", "INFO")
    logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO))
    logger.info("Starting WorkflowRunnerAgent")
    server_main(log_level=log_level)


if __name__ == "__main__":
    main()
