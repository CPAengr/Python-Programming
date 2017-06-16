#  Write a program that introduces yourself
print("Hello world!")
print("What is your name?")
myName = input()    # asks your name
print("It's good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))
print("What is your age?")  # asks for your age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year from now.")
