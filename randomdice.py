import secrets

würfel = [1,2,3,4,5,6]

def selectRandom(würfel):
    return secrets.choice(würfel)


Eingabe = input("willst würfeln?   y: zum bestätigen\n                  n: für nein\n")


if Eingabe == "y":
     Zahl1 = input("Drücke x zum würfeln\n")
if Zahl1 == "x":
     print("Deine Zahl ist: ", selectRandom(würfel))

else:
    print("bye")