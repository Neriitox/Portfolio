# (yeast 1 hr later) = (yeast now) + 0.6× (yeast now)
s = float(input("Start (g): "))
e = float(input("Finish (g): "))
n = s
hrs = 0

while n < e:
    hrs += 1
    na = n + 0.6 * n
    n = na
print(f"The loaf would need to rise for {hrs} hours.")

# Tells you how long it would take for a loaf of bread to rise to a certain weight