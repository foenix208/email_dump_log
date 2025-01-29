import requests
import sys



if len (sys.argv ) > 1:
    url = sys.argv[1]
else:
    url = input("Rentrer un url : ")
r = requests.get(url=url)
lignes = r.text.split("\n")

cmp = 0
emails = []

for i in lignes: 
    for y in i.split(" "):
        if "@" in y:
            if not y in emails:
                emails.append(y)

fichier = open("email.txt","w")
for email in emails:
    fichier.write(f"{email}\n")    
    
fichier.close()
print(len(emails))
                

