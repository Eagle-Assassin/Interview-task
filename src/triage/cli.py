# src/triage/cli.py

import argparse
import sys
from triage.predict import run_pipeline


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
        help="Path to gold cases CSV"
    )

    run_parser.add_argument(
        "--outdir",
        required=True,
        help="Directory to write outputs"
    )

    # ---------------- test command ----------------
    test_parser = subparsers.add_parser(
        "test",
        help="Run tests"
    )

    args = parser.parse_args()

    if args.command == "run":
        run_pipeline(
            input_path=args.input,
            gold_path=args.gold,
            outdir=args.outdir
        )

    elif args.command == "test":
        import pytest
        sys.exit(pytest.main(["src/triage"]))
