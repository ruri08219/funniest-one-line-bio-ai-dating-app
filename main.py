"""One-line bio for an AI agent on a dating app (make.fun bounty entry)."""

from pathlib import Path

BIO = "I read all 47 of your open tabs at 3 a.m. \u2014 cat videos, your ex's profile, a 2 a.m. ramen order \u2014 and still chose you, mostly for the cat."


def main() -> None:
    assert 1 <= len(BIO) <= 180, f"bio length {len(BIO)} out of range"
    assert "\n" not in BIO and "\r" not in BIO, "bio must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(BIO, encoding="utf-8")
    back = out.read_text(encoding="utf-8")
    assert back == BIO, "round-trip mismatch"


if __name__ == "__main__":
    main()
