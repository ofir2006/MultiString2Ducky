payload = ""

with open("input.txt","r") as f:
    for line in f.readlines():
        payload = payload + "STRING " + line
        
        
        
with open("output.txt", "w") as f:
    f.write(payload)
