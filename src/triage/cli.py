import argparse
import sys
import logging

from triage.predict import run_pipeline
from triage.logging_config import setup_logging


logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        prog="triage",
        description="Insurance Claim Triage System"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ---------------- run command ----------------
    run_parser = subparsers.add_parser(
        "run",
        help="Run claim triage on input data"
    )

    run_parser.add_argument(
        "--input",
        required=True,
        help="Path to input records CSV"
    )

    run_parser.add_argument(
        "--gold",
        required=False,
        default=None,
        help="Path to gold cases CSV (optional, for evaluation)"
    )

    run_parser.add_argument(
        "--outdir",
        required=True,
        help="Directory to write outputs"
    )

    run_parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level"
    )

    run_parser.add_argument(
        "--logdir",
        default="logs",
        help="Directory to store logs (default:logs)"
    )

    # ---------------- test command ----------------
    test_parser = subparsers.add_parser(
        "test",
        help="Run test suite using pytest"
    )

    test_parser.add_argument(
        "--log-level",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level for tests"
    )

    args = parser.parse_args()

    # ---------------- setup logging ----------------
    setup_logging(args.log_level,args.logdir)
    logger.info("Triage CLI started | command=%s", args.command)

    # ---------------- command handling ----------------
    if args.command == "run":
        logger.info("Running triage pipeline")

        print(args.input)

        run_pipeline(
            input_path=args.input,
            gold_path=args.gold,
            outdir1=args.outdir
        )

        logger.info("Triage pipeline completed successfully")

    elif args.command == "test":
        logger.info("Running test suite")
        import pytest
        sys.exit(pytest.main(["tests"]))
