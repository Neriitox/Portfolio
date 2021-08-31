ani = input("What animal would you like? ")
num = int(input("How many? "))

if ani.isupper():
    print("Woah! No need to shout, you'll scare the animals!")
else:
    if num == 0:
        print("That's sad. No pet for you today.")
    if num == 1:
        print(f"Great, here's your {ani}!")
    if num > 1:
        print(f"Ok! {num} {ani}s coming right up!")


# Don't shout you won't get any animals        