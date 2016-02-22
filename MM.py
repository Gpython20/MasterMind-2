# -*- coding: utf-8 -*
import random

def aleatoire():
    L=[0,0,0,0]
    for i in range(4):
        L[i]=random.randint(1,6)
    return L

def noir_blanc(List1,List2):
    L = [0,0]
    L1 = list(List1)
    L2 = list(List2)
    for i in range(4):
        if L1[i] == L2[i]:
            L[0]=L[0]+1
            L1[i]=7
            L2[i]=0
    for i in range(4):
        for j in range(4):
            if L1[i]==L2[j]:
                L1[i]=7
                L2[j]=0
                L[1]=L[1]+1
    return L
    
def jouer(List_E):
    i = 1
    while i != 10:
        e = int(input("Entrez votre valeur e :"))
        f = int(input("Entrez votre valeur f :"))
        g = int(input("Entrez votre valeur g :"))
        h = int(input("Entrez votre valeur h :"))
        L =[e,f,g,h]
        noirs=noir_blanc(List_E,L)[0]
        blancs=noir_blanc(List_E,L)[1]
        if noirs==4:
            print("Gagné ! La combinaison était ", List_E)
            break
        else:
            print(L ,"donne ",noirs," bons et ",blancs," mal placés.")
            i=i+1
    if i==10:
        print("Perdu, c’était", List_E)

def coup_suivant(a,b,c,d):
    L = [1,1,1,1]
    if min(a,b,c,d) >= 1 and max(a,b,c,d) <= 6:
        if d < 6:
            L = [a, b,c, d+1]
        elif c < 6:
            L = [a,b,c+1,1]
        elif b < 6:
            L = [a,b+1,1,1]
        elif a < 6:
            L = [a+1,1,c,d]
        else:
            L = [7,1,1,1]
    else:
        print(L)
    return L

def correcte(L, partie):
    play = 0
    nb_partie = len(partie)
    for i in range(nb_partie):
        if noir_blanc(L,partie[i][:4])!=partie[i][4:]:
            play = 1
    return play

def jeuOrdi():
    List_E = aleatoire()
    L = [1,1,1,1]
    partie = []
    i = 1
    while i != 10:
        print("Je joue avec ", L)
        noirs=noir_blanc(List_E,L)[0]
        blancs=noir_blanc(List_E,L)[1]
        if noirs==4:
            print("Gagné ! La combinaison était ", List_E)
            break
        else:
            print(L ,"donne ",noirs," bons et ",blancs," mal placés.")
            partie.append([L[0], L[1], L[2], L[3], noirs, blancs])
            L = coup_suivant(L[0], L[1], L[2], L[3])
            print(L, partie)
            while correcte(L, partie) == 1 and L != [7,1,1,1]:
                L = coup_suivant(L[0], L[1], L[2], L[3])
        i=i+1
    if i==10:
        print("Perdu, c’était", List_E)

jeuOrdi()
