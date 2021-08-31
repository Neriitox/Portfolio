tour_locations = ['Netherlands', 'France', 'Switzerland', 'Italy', 'Spain', 'Denmark', 'Sweden', 'Finland']

# Add your code after this.
c = input("Country: ")
if c.title() in tour_locations:
    print(f"{c} is on the list!")
else: 
    print(f"We will not be in {c} this time.")