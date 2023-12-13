def srvr(matrica):
    """funkcija koja određuje srednju vrednost negativnih članova matrice n x m
    argument funkcije je samo matrica"""
    suma = 0
    br = 0
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            if A[i][j] < 0:
                suma = suma + matrica[i][j]     # isto kao suma += matrica[i][j]
                br = br + 1                     # isto kao  br += 1
            else: return None                   # vraća None ako nema negativnih članova
    return suma/br
    
def srvr1(matrica,n,m):
    """funkcija koja određuje srednju vrednost negativnih članova matrice n x m
    argument funkcije je matrica, broj vrsta i broj kolona"""
    suma = 0
    br = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] < 0:
                suma = suma + matrica[i][j]     # isto kao suma += matrica[i][j]
                br = br + 1                     # br += 1
            else: return None                   # vraća None ako nema negativnih članova
    return suma/br

def unesi_matricu_nxm():                               # glavni program za unošenje matrice n x m
    """funkcija za unošenje matrice n x m, vraća matricu i broj vrsta i kolona, n i m"""
    n = (int(input("Uneti broj vrsta matrice n = ")))
    m = (int(input("Uneti broj kolona matrice m = ")))
    A = []
    for i in range(n):
        red = []
        for j in range(m):
            red.append(float(input(f"Uneti element A[{i}][{j}] = ")))
        A.append(red)
    return A,n,m
A,n,m = unesi_matricu_nxm()         # ako vraćamo broj vrsta i kolona n i m

print(f"Srednja vrednost negativnih članova matrice {A} je {srvr(A)}.")
print(f"Srednja vrednost negativnih članova matrice {A} je {srvr1(A,n,m)}.")

def unesi_matricu_nxn():
    """funkcija za unošenje matrice n x n, vraća matricu A i dimenziju n"""
    n = (int(input("Uneti dimenziju kvadratne matrice matrice n = ")))
    A = []
    for i in range(n):
        red = []
        for j in range(n):
            red.append(float(input(f"Uneti element A[{i}][{j}] = ")))
        A.append(red)
    return A,n

B,n = unesi_matricu_nxn()

def proizvod_X_Y(A):
    """funkcija koja glavnom programu vraća
    vrednost proizvoda zbira clanova (X) na glavnoj i sporednoj dijagonali kvadratne matrice A
    proizvoljne dimenzije n i zbira članova (Y) uz dijagonalu matrice.
       -----------------------------
       | X | Y | Y | Y | Y | Y | X |
       | Y | X |   |   |   | X | Y |
       | Y |   | X |   | X |   | Y |
       | Y |   |   | X |   |   | Y |
       | Y |   | X |   | X |   | Y |
       | Y | X |   | X |   | X | Y |
       | X | Y | Y | Y | Y | Y | X |
       -----------------------------
       """
    zbirx = 0
    zbiry = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == j or i + j == n - 1:
                zbirx = zbirx + A[i][j]
    for k in range(1,n-1):
        zbiry = zbiry + A[0][k] + A[k][0] + A[n-1][k] + A[k][n-1]
    return zbiry * zbirx

print(proizvod_X_Y(B))

def manje_od_srv(niz):
    """funkcija koja vrednostima niza manjim od srednje vrednosti dodeljuje 0 i vraća novodobijeni niz"""
    print(f"Pocetni niz je {niz}")
    srvr = sum(niz)/len(niz)
    for i in range(len(niz)):
        if niz[i] < srvr:
            niz[i] = 0
    print(f"Srednja vrednost niza je {srvr}")
    return niz
print("Novodobijeni niz je", manje_od_srv([1,2,3,4,5,6,7,8,9,10]))
    
def manje_od_X(niz,X):
    """funkcija koja vrednostima manjim od zadate vrednosti X dodeljuje 
    srednju vrednost niza i vraća broj izmenjenih  članova niza"""
    print("Početni niz je", niz)
    br = 0
    srvr = sum(niz)/len(niz)
    for i in range(len(niz)):
        if niz[i] < X:
            niz[i] = srvr
            br += 1
    print("Novi niz je", niz)
    return br
print("Broj izmenjenih članova je", manje_od_X([1,2,3,4,5,6,7,8,9,10],6))