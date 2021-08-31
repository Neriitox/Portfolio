def cups_to_grams(cups, density):
  # Convert cups to grams here.
  # The density is in grams-per-cup.
  # Grams = Cups * Density

  a = round(cups * density,1 )
  return(a)

# Write the rest of your program here
fud = input("What food? ")
cups = float(input("How much in cups? "))
dens = float(input("How many grams per cup? "))
a = cups_to_grams(cups, dens)
wilbur = f"{cups} cups of {fud} is {a} grams."
print(wilbur)
