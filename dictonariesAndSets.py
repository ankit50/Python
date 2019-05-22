movie = {"sultan": "Salman Khan Movie",
         "PK": "Aaamir kHan movie",
         "veer zara": "Sarukhan movie",
         "Gully boy": "Ranveer singh movie",
         "Barfi": "Ranvir kapoor movie"}

keys = input("Enter the key:")
if keys in movie:
    desc = movie.get(keys)
    print(desc)
else:
    print("Key not found")
