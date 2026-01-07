import re

class _Internal():
    def sleep(time=str):
        match time[-1]:
            case "s":
                return f"waited {time[0:-1]} second(s)"
            case "m":
                return f"waited {time[0:-1]} minute(s)"
            case _:
                return f"waited {time[0:-1]} tick(s)"

file = """
tellraw @a "Message One"
#! sleep(1s);
#! sleep(2s);
tellraw @a "Message Two"
"""

matches = re.findall(r"^#! *(.*)",file,re.MULTILINE)

for match in matches:
    for command in str(match).split(";"):
        try:
            res = eval(f"_Internal.{command}".replace("(","('").replace(")","')"))
            print(res)
        except Exception as e:
            pass