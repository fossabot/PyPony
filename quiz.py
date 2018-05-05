#!/usr/bin/python
print('''

 ____        _
/ __ \      (_)
| |  | |_   _ _ ____
| |  | | | | | |_  /
| |__| | |_| | |/ /
 \___\_\\__,_|_/___|

''')
Score = 0
print("====================================================")
print("Question 1")
Question1 = input("What is the native pony breed of the county of Devon? ")
if Question1.lower() in ['dartmoor pony', 'dartmoor', 'dartmoor ponies']:
    print("Well Done!")
    Score = Score + 1
else:
    print("Oops, the answer was Dartmoor Ponies")
print("====================================================")
print("Question 2")
print("a) 1919           c) 1927")
print("b) 1923           d) 1934")
print("When was The Connemara Pony Breeders Society founded?")
Question2 = input()
if Question2.lower() in ['b', '1923']:
    print("Well Done!")
    Score = Score + 1
else:
    print("Oops, the answer was 1923")
print("====================================================")
print("Question 3")
Question3 = input("Do the coats of Shetland Ponies change with the weather [y/n] ")
if Question3.lower() in ['no', 'n']:
    print("Well Done!")
    Score = Score + 1
else:
    print("Oops, their coats change with the season, not the weather!")
print("====================================================")
print("Question 4")
Question4 = input("What is the scientific name of ponies? ")
if Question4.lower() == "equus ferus caballus":
    print("Well Done!")
    Score = Score + 1
else:
    print("Oops, the answer was Equus Ferus Caballus")
print("====================================================")
print("Your score was",Score)
if (Score==4):
    print("Wow, you got everything right!")
elif (Score==3):
    print("That's really good!")
elif (Score==2):
    print("Not bad, you got half of it correct!")
elif (Score==1):
    print("This test is really tough, so well done on getting one right!")
else:
    print("This test is extremely tough. Try and get a better score next time")
print("====================================================")

exec(open("menu.py").read())
