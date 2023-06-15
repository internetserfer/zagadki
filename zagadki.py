a = input("what is the language are we learning? ")
score = 0
if a == "python":
    print("great!")
    score = score + 1
    print(score)
elif a == "Python":
    print("great!")
    score = score + 1
    print(score)
else:
    print("no! learning better)")
    print(score)
b = input("how much bits contain the 1 symbol without - ? ")
if b == "8":
    print("great!")
    score = score + 1
    print(score)
print("that`s all!")
print(score)