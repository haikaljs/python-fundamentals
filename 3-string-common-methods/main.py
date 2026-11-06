
text = "    Hello, World    "

text.strip()            #  "Hello World"
text.lower()            #  "   hello, world    "
text.upper()            #  "   HELLO, WORLD    "
text.replace("l", "L")  #  "   HeLLo, WorLd    "
text.split(",")         #  ["   Hello", "World  "]

# f-strings (modern formatting)
name = "Alice"
greeting = f"Hi, my name is {Alice}!"