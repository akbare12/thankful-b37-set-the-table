import os

# Set the table: one short thank-you, written out to entry.txt.
TEXT = "Thank you. Before you eat tonight, I set the table for you. One empty plate, a fork and a knife laid straight beside it, a glass of cool water, a napkin folded neat. Nothing is on the plate yet. That is the point. Sit down whenever you like. The empty plate will wait, clean and open, holding your place till supper comes."

os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), exist_ok=True)
with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
