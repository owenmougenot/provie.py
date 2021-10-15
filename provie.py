homme = input("homme ou femme ?\n")  # je demande a l'utilisateur si c'est une femme ou un homme
t = input("le degre d'alcool: ")  # le degre d'alcool de la boisson
v = int(input("volume d'alcool: "))  # le volume d'alcool
m = int(input("ta masse(poids) : "))  # la masse de l'utilisatuer

t = float(float(int(t[0:-1])/100))  # pour mettre le % en 0...
if homme == "homme":  #si l'utilisateur est un homme 
    print(f" tu est a {(v*t*0.8)/(0.7*m)}")  # je realise un calcul pour le taux d'alcoolemie 
    if (v*t*0.8)/(0.7*m) < 0.51:  # si il est inferieur a 0.51 
        print("tu peux prendre ta voiture")  #alors l'utilisateur peut prendre la voiture 
    elif (v*t*0.8)/(0.7*m) > 0.51:  # si il est superieur a 0.51 je lui affiche un message pour lui dire qu'il ne peut conduire
        print("ton taux est trop haut je te conseil d'appeler un taxi ou de te faire rammener ou encore attendre tout en sechant qu'il faut 2h pour un verre pour faire retomber sont taux a 0")
elif homme == "femme":  # si l'utilisatuer est une femme 
    print(f"tu est a {(v*t*0.8)/(0.6*m)}")  # je realise un calcul pour le taux d'alcoolemie 
    if (v*t*0.8)/(0.6*m) < 0.51:  # si il est inferieur a 0.51
        print("tu peux prendre ta voiture")  #alors l'utilisateur peut prendre la voiture
    elif (v*t*0.8)/(0.6*m) > 0.51:   # si il est superieur a 0.51 je lui affiche un message pour lui dire qu'elle ne peut conduire
        print("ton taux est trop haut je te conseil d'appeler un taxi ou de te faire rammener ou encore attendre tout en sechant qu'il faut 2h pour un verre pour faire retomber sont taux a 0")
