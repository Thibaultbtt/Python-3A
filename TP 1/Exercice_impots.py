def mesImpots(revenu) :
    impots = 0
    if revenu < 10084 :
        return impots
    elif revenu in range(10085, 25710):
        return (revenu - 10085) * 11/100
    elif revenu in range(25711, 73516):
        return ((revenu - 25711) * 30/100) + ((25710 - 10085) * 11/100)
    elif revenu in range(73517, 158122):
        return (revenu - 73517) * 41/100 + ((73516 - 25711) * 30/100)+ ((25710 - 10085) * 11/100)
    elif revenu > 158123:
        return (revenu - 158123) * 45/100 + (158122 - 73517) * 41/100  + ((73516 - 25711) * 30/100) + ((25710 - 10085) * 11/100)







revenu = int(input ("Indiquez le montant de votre revenu annuel : "))

impots = mesImpots(revenu)

print(impots)