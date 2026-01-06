import re

file = """
tellraw @a "Message {"a"*100}"
#! sleep(1s);
tellraw @a "Message Two"
"""

# this works. don't ask how, it just does.
file = eval(f"f'''{file.replace("\\", "\\\\").replace("'", "\\'")}'''")

groups = re.search(r"(?<=^#!).*",file).groups()

for match in groups:
    print(match)