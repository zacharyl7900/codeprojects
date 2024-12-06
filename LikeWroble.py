name = input("What is your name? ")
likeWroble = input("Do you like Mr. Wroblewski? (yes/no/YES/NO) ")
print("Got it! Calculating your results...")

if likeWroble.lower() == "yes":
    print(name + " likes Mr. Wroblewski!")
elif likeWroble.lower() == "no":
    print(name + " does not like Mr. Wroblewski!")
else:
    print(name + " does not like or dislike Mr. Wroblewski.")