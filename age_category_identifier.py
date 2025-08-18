#Prompt user to Input Age
age = int(input("Enter your age: "))

#Process
if age <= 12:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 59:
    print("You are an Adult.")
else:

#Output - print
    print("You are a Senior Citizen.")


