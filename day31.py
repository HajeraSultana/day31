#Subrutinas:
def colorprint (color, word):
    if color == ("red"):
        print("\033[31m", word)
    elif color == ("blue"):
        print("\033[34m", word)
    elif color == ("green"):
        print("\033[32m", word)
    elif color == ("yellow"):
        print("\033[33m", word)
    elif color == ("purple"):
        print("\033[35m", word)
    elif color == ("white"):
        print("\033[37m", word)
    else:
        print("\033[0m", word)
#Variables                
app = ("=== Music App ===")
radio = (" 🔥▶️  Radio Gaga")
song = ("Queen")
prev = ("PREV")
next = ("NEXT")
pause = ("PAUSE")
title1 = ("WELCOME TO")
title2 = ("--   ARMBOOK   --")
para1 = ("Definitely not a rip off of")
para2 = ("a certain other social")
para3 = ("networking site.")
honest = ("Honest.")
user = ("Username:")
password = ("Password:")

#First Interface
print()
colorprint("yellow", "{app: >30}".format(app = app))
print()
colorprint("white", "{radio: >5}".format(radio = radio))
colorprint("yellow", "{song: >11}".format(song = song))
print()
colorprint("white",prev.format(prev = prev))
colorprint("green", "{next: >9}".format(next = next))
colorprint("purple", "{pause: >16}".format(pause = pause))
print()

# Second Interface
print()
print(f"{title1:>30}")
colorprint("blue", "{title2: >33}".format(title2 = title2))
print()
colorprint("yellow", "{para1: >45}".format(para1 = para1))
colorprint("yellow", "{para2: >45}".format(para2 = para2))
colorprint("yellow", "{para3: >45}".format(para3 = para3))
print()
colorprint("red", "{honest: >30}".format(honest = honest))
print()
colorprint("white", "{user: >31}".format(user = user))
colorprint("white", "{password: >31}".format(password = password))