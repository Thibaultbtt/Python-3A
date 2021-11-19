# ---------- Exercice Calendrier ----------#

def Test_bisextile (liste_date):
    annee = int(liste_date[2])
    if (annee % 4 ==0 and annee%100==0) or annee % 400==0 :
        return True
    return False

def Nbre_jour_mois (liste_date):
    bisextile = Test_bisextile(liste_date)
    mois = int(liste_date[1])
    nb_jour =0
    if mois in [1,3,5,7,8,10,12]:
        nb_jour=31
    elif mois in [4,6,9,11] :
        nb_jour=30
    elif mois== 2 and bisextile == True :
        nb_jour=29
    else :
        nb_jour=28
    return nb_jour
    
def Verif_date (liste_date):
    jour = int(liste_date[0])
    nb_jour = Nbre_jour_mois(liste_date)
    mois = int(liste_date[1])
    if mois >12 :
        return False
    if nb_jour < jour :
        return False
    return True




# Programme principal #

date = input("Renseignez une date au format jour/mois/année : ")
liste_date=date.split('/')

verif = Verif_date(liste_date)
if verif == True :
    print('date valide')
else :
    print('date invalide')