l = []
for i in range(4):
    nb = int(input("Entrer l'entier : "))
    l.append(nb)
somme = sum(x**2 for x in l if x % 2!= 0)
print(somme)