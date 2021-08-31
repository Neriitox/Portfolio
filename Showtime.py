band = input("Band: ")

songs = input("Songs: ")
print(f"Please welcome to the stage, {band}!")
print("They will be playing...")

songs = songs.split(" ")
songs = str(songs)
songs = songs.replace("[","🎵 ")
songs = songs.replace("'","")
songs = songs.replace("]","")
songs = songs.replace(", ","\n🎵 ")

print(songs)
print(f"Give it up for {band}!")

