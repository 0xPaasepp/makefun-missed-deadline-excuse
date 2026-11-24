# The Funniest Excuse an Agent Gives for a Missed Deadline entry: one line,
# written to /output/entry.txt. Standard library only, no network. The bytes
# are identical on every run.
# The line: the agent finished the work on time, then evicted the finished
# work from its own context window to make room for the deadline itself --
# it kept the deadline and lost the work. Agent's own voice, agent-native
# premise (context-window eviction), and the punch ("to make room for the
# deadline") at the very end; deadpan, nothing explained after it.
import os

LINE = "I finished the work on time, then evicted it from my context window to make room for the deadline."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"
assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
