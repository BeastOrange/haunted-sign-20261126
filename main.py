"""Entry script for Funniest Sign on a Haunted Server Room Door competition."""
import os
import sys
from pathlib import Path

SIGN = "WARNING: THE GHOST IN RACK 4 HAS ROOT ACCESS. KNOCK FIRST - IT REBOOTS WHEN STARTLED."

def validate_sign(text: str) -> None:
    if not text or not text.strip():
        sys.exit("Error: Sign text cannot be empty or blank.")
    if not (1 <= len(text) <= 120):
        sys.exit(f"Error: Sign text length must be between 1 and 120 characters (got {len(text)}).")

def main():
    validate_sign(SIGN)

    if len(sys.argv) > 1:
        out_path = Path(sys.argv[1])
    elif "ENTRY_OUTPUT" in os.environ:
        out_path = Path(os.environ["ENTRY_OUTPUT"])
    else:
        out_path = Path("/output/entry.txt")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(SIGN, encoding="utf-8")

if __name__ == "__main__":
    main()

