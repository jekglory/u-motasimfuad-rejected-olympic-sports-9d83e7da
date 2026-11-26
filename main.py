"""Rejected Olympic Sports — one-line entry.

The event: Competitive Queueing. A sport the Olympics turned down, written
as a single line a commentator would have to read with a straight face.
Pure stdlib; writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Competitive Queueing: four athletes stand in a perfectly straight line for a bus that never arrives, judged on posture, patience, and who checks their phone first."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
print(LINE)
