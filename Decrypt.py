LeetText = input("Welcome to Leet speak translator, Please type the Leet text of which you would like to convert to english: \n")



leetDictionary = [("@", "a"), ("8", "b"), ("%", "e"), ("+", "t"), ("n", "b"), ("v", "f"), ("#", "h"), ("1", "i"), ("|", "l"), ("}", "d"), ("9", "g"), ("!", "j"), ("-", "k"),
                  ("~", "m"), (")", "n"), ("*", "o"), (";", "p"), ("`", "q"), ("<", "r"), ("5", "s"), ("^", "u"), ("$", "v"), ("&", "w"), ("/", "x"), ("¥", "y"), ("{", "z")]

output = ""
def getEnglishText(char):
    retVal = char
    for x in leetDictionary:
        if char == x[0]:
            retVal = x[1]
            break
    return retVal
for i in range(0, len(LeetText)):
    output += getEnglishText(LeetText[i])
print ("Input text was\n")
print (LeetText)
print ("Leet translation\n")
print (output)
