import matplotlib.pyplot as plt

dates = []
prix=[]

with open('bitcoin_history.txt','r') as f:
    for ligne in f:
        morceaux=ligne.split(',')
        dates.append(morceaux[0])
        prix.append(float(morceaux[1]))
    
plt.plot(dates,prix)
plt.title("courbe d'evolution du prix du Bitcoin")
plt.xlabel('Date')
plt.ylabel('Prix ($)')
plt.xticks(rotation=45)
plt.show()