def to_kmh(knots):
  # Calculate the speed in km/h
  # km/h = 1.852 × knots
  km = 1.852 * knots
  rounded = round(km,1)
  if rounded < 60:
    print(f"{rounded} km/h - Go faster!")
  elif rounded >= 60 and rounded < 100:
    print(f"{rounded} km/h - Nice one.")
  elif rounded >= 100 and rounded < 120:
    print(f"{rounded} km/h - Radical!")
  elif rounded >= 120:
    print(f"{rounded} km/h - Whoa! Slow down!")
  
  

# Write the rest of your program here
kk = float(input("Speed (kn): "))
to_kmh(kk)(

# Converts knots per hours to kilometers per hours
