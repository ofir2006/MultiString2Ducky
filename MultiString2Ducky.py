payload = ""

with open("input.txt","r") as f:
    for line in f.readlines():
        for letter in line:
            if letter == "\n":
                break
            payload = payload + "STRING " + letter + "\nDELAY 100\n"
        payload = payload + "ENTER\n"
        
        
        
with open("output.txt", "w") as f:
    f.write(payload)
