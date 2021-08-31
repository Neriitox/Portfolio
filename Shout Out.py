s  = input("Sentence: ")
w = s.split()
c = 0

for i in range(len(w)):
    if w[i].isupper():
        c+=1
print(f"Number of shouted words: {c}")

# Tells you how many words were typed in all caps