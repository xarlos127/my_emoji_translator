
thisdict = {
    "dog":"🐶",
    "cat":"🐱",
    "tree":"🌳",
    "car":"🚗",
    "hawk":"🦅",
    "Done":"😭",
    "dead":"💀",
    "james": "👴",
    "olivia": "👰‍♀️",
    "drpep": "❤️😍🥰",
    "zyaden":"🛹🥶💧",
    "victor":"🤠🛹🦅",
    "david":"🥭💧🛹",
    "cheap":"🫵",
    "think": "🤔💭",
    

}

while True:
    inp = input("enter in a sentince: ")
    print(inp)
    words = inp.split()
    emojisentince = " "
    for word in words :
        if word in thisdict:
            emojisentince += thisdict[word]
        else:
            emojisentince += word
        emojisentince += " "
    print(emojisentince)
        