list = ["Hannes, Casper, Adrian, Sebastian, Alice, Sam, Adham, Snasker"]
LetterA=0
for name in list:
    for letter in name:
        if letter == "a":
            LetterA=LetterA+1
print("Letter A's:", LetterA)
