  
englishText = input \
    ("Welcome to Leet speak translator, Please type the english text of which you would like to convert: \n")
def getLeetSpeak(char):
    retVal = char
    for x in leetDictionary:
        if char == x[0]:
            retVal = x[1]
            break
    return retVal


leetDictionary = [("a", "@"), ("b", "8"), ("e", "%"), ("t", "+"), ("b", "N"), ("f", "v"), ("h", "#"), ("i", "1"), ("l", "|"), ("d", "}"), ("g", "9"), ("j", "!"), ("k", "-"),
                  ("m", "~"), ("n", ")"), ("o", "*"), ("p", ";"), ("q", "`"), ("r", "<"), ("s", "5"), ("u", "^"), ("v", "$"), ("w", "&"), ("x", "/"), ("y", "¥"), ("z", "{")]

output = ""

for i in range(0, len(englishText)):
    output += getLeetSpeak(englishText[i])

print ("Input text was\n")
print (englishText)
print ("Leet translation\n")
print (output)
