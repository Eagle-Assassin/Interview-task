import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "triage", "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Insurance Claim Triage System" in result.stdout
