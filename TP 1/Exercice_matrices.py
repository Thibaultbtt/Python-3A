
matrice_lin_A = [[1,2,3],[4,5,6],[7,8,9]]
matrice_col_B = [[1,2,3],[1,2,3],[1,2,3]]


def Produit_matriciel (matrice_col_B,matrice_lin_A) :
    matrice_ligne_C=[]
    for i in range(len(matrice_col_B)) :
        matrice_ligne_C.append(0)
    p=0
    for n in range(len(matrice_lin_A)) :
        if p==0 or p%3 !=0:
            produit=Produit_lign_col(matrice_lin_A[n], matrice_col_B[p])
            matrice_ligne_C[n]=produit
            p+=1
        else :
            p=0
    return matrice_ligne_C


def Produit_lign_col (ligne, colonne) :
    produit=0
    for i in range(len(ligne)) :
        produit += ligne[i]*colonne[i]
    print(produit)
    return produit


matrice_C = Produit_matriciel (matrice_col_B,matrice_lin_A)

print(matrice_C)
