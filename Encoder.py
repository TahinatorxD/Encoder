User_Input = input("Enter the sentence you wanna encode: ")
print("Before Encoding: " + User_Input )
User_Input = User_Input.replace(" ", "")

encoding = {
# Lower Case Letters

            "a":"z",    "b":"y",    "c":"x",    "d":"w",
            "e":"v",    "f":"u",    "g":"t",    "h":"s",
            "i":"r",    "j":"q",    "k":"p",    "l":"o",
            "m":"n",    "n":"m",    "o":"l",    "p":"k",
            "q":"j",    "r":"i",    "s":"h",    "t":"g",
            "u":"f",    "v":"e",    "w":"d",    "x":"c",
            "y":"b",    "z":"a",

# Upper case letters

            "A" : "Z",  "B" : "Y",  "C" : "X",  "D" : "W",
            "E" : "V",  "F" : "U",  "G" : "T",  "H" : "S",
            "I" : "R",  "J" : "Q",  "K" : "P",  "L" : "O",
            "M" : "N",  "N" : "M",  "O" : "L",  "P" : "K",
            "Q" : "J",  "R" : "I",  "S" : "H",  "T" : "G",
            "U" : "F",  "V" : "E",  "W" : "D",  "X" : "C",
            "Y" : "B",  "Z" : "A",
            }

Decoded_Message = ""

for i in range(0, len(User_Input)) :
    if User_Input[i] in encoding :
        Decoded_Message += encoding[User_Input[i]]
    else:
        Decoded_Message += User_Input

print("After Encoding: " + Decoded_Message)