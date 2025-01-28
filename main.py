
file = open("teste.txt")
lignes = file.readlines()

cmp = 0
emails = []
for i in lignes: 
    for y in i.split(" "):
        if "@" in y:
            if not y in emails:
                emails.append(y)
                
print(len(emails))
                

