import matplotlib.pyplot as plt

dates = []
prix=[]



with open('bitcoin_history.txt','r') as f:
    for ligne in f:
        morceaux=ligne.split(',')
        dates.append(morceaux[0])
        prix.append(float(morceaux[1]))

        
total = 0
for p in prix:
    total += p  # N'oublie pas l'indentation ici !

moyenne = total / len(prix)

print("Prix Max:",max(prix))
print("Prix Min:",min(prix))
print("Prix moyen :", moyenne) 

plt.plot(dates, prix, color='red', marker='o')
plt.title("courbe d'evolution du prix du Bitcoin")
plt.xlabel('Date')
plt.ylabel('Prix ($)')
plt.xticks(rotation=90)
plt.grid(True)
plt.savefig("courbe_bitcoin.png")
plt.show()
