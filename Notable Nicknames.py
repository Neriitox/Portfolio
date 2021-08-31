def is_notable(name):
  if name.lower()[0] == "n":
        if len(name) >= 5:
            print("That nickname is notable!")
        else: 
            print("That nickname is not so notable!")
  else: 
    print("That nickname is not so notable!")

# Write the rest of your program here.
nick = input("Type a nickname: ")
is_notable(nick)

# Tells you if a nickname is notable or not