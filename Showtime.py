band = input("Band: ")

songs = input("Songs: ")
print(f"Please welcome to the stage, {band}!")
print("They will be playing...")

songs = songs.split(" ")
songs = str(songs)
songs = songs.replace("[","šµ ")
songs = songs.replace("'","")
songs = songs.replace("]","")
songs = songs.replace(", ","\nšµ ")

print(songs)
print(f"Give it up for {band}!")

