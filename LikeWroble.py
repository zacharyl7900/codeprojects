name = input("What is your name? ")
likeWroble = input("Do you like Mr. Wroblewski? (yes/no/YES/NO) ")
print("Got it! Calculating your results...")

if likeWroble.lower() == "yes":
    print(name + " likes Mr. Wroblewski!")
elif likeWroble.lower() == "no":
    print(name + " does not like Mr. Wroblewski!")
else:
    print(name + " does not like or dislike Mr. Wroblewski.")

periodWroble = input("What period Wroblewski do you have? (2/3/4/5/6/7)")
print("Calculating...")

if periodWroble.lower() == "2":
    print(name + " is in PERIOD 2 Science 7 Non-GATE")

elif periodWroble.lower() == "3":
    print(name + " is in Science 7 Gate")
elif periodWroble.lower() == "4":
    print(name + " is in Science 7 Gate")
elif periodWroble.lower() == "5":
    print(name + " is in Science 7 Gate")
elif periodWroble.lower() == "6":
    print(name + " is not in Science 7 Non-GATE or GATE!" + name + " is in AVID 7!")
elif periodWroble.lower() == "7":
    print(name + " is in Science 7 Gate")
else:
    print(name + " is not in any classes with Wroblewski! (he/she is lucky!)")