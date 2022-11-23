# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:55:11 2021

@author: coline
"""
from random import randint
#permet de trouver des nombres aléatoires

tab1 = ['£',2,3,'$',1,3,'¿','¥',3,2] #rouleau 1
tab2 = [3,2,'¥',1,'¿',2,2,'$',1,'£'] #rouleau 2
tab3 = [2,'£','¿',1,'$',3,1,1,3,'¥'] #rouleau 3

print(" ")
print('\033[44m'+"1","2","3"+'\033[49m')
#affiche les numéros des rouleaux
print('\033[47m')
print((tab1[0]),(tab2[0]),(tab3[0]))
print('\033[34m',"\033[4m")
print((tab1[1]),(tab2[1]),(tab3[1]))  
print('\033[0m','\033[47m')
print((tab1[2]),(tab2[2]),(tab3[2]))
print('\033[48;2m')
#affiche le tableau 3x3 qui sera affiché et la ligne bleu qui sera lue
print((tab1[3]),(tab2[3]),(tab3[3]))
print((tab1[4]),(tab2[4]),(tab3[4]))
print((tab1[5]),(tab2[5]),(tab3[5]))
print((tab1[6]),(tab2[6]),(tab3[6]))
print((tab1[7]),(tab2[7]),(tab3[7]))
print((tab1[8]),(tab2[8]),(tab3[8]))
print((tab1[9]),(tab2[9]),(tab3[9]))
#affiche le reste des roues (ne sera plus affiché, permet juste de savoir les symboles des roues)



def jeu1():
    for a in range (0,randint(20,80)):
        tab1.insert(0,tab1.pop())
#le rouleau 1 tourne, soit en décalant les valeurs de son tableau entre 20 et 80 fois vers la droite

def jeu2():
    for a in range (0,randint(80,120)):
        tab2.insert(0,tab2.pop())
#le rouleau 2 tourne, soit en décalant les valeurs de son tableau entre 80 et 120 fois vers la droite

def jeu3():
    for a in range (0,randint(120,200)):
        tab3.insert(0,tab3.pop())
#le rouleau 3 tourne, soit en décalant les valeurs de son tableau entre 120 et 200 fois vers la droite

#Les trois définitions jeu1(),jeu2() et jeu3() indiquent le roulement de chaque rouleau, soit un déplacement de toutes leur valeurs vers la droite x fois(x1,x2,x3).
#ce x est un nombre aléatoire et de différent intervalles en fonction du rouleau, permettant une plus grande déséquilibration entre les déplacements.x1=/=x2=/=x3
#ces définitions nous permettent aussi de faire tourner les rouleaux indépendamment des autres

def tableau():
    print(" ")
    print('\033[44m'+"1","2","3"+'\033[49m')
    print('\033[47m')
    print((tab1[0]),(tab2[0]),(tab3[0]))
    print('\033[34m',"\033[4m")
    print((tab1[1]),(tab2[1]),(tab3[1]))  
    print('\033[0m','\033[47m')
    print((tab1[2]),(tab2[2]),(tab3[2]))
    print('\033[49m')
    print(" ")  
#le programme imprime le tableau 3x3 ainsi obtenu en mettant en valeur la ligne centrale en bleu

def jetons():
    print('\033[42m'+"vous possédez donc ",N," jetons."+'\033[49m')
#indique combien de jetons le joueur possède après chaque round
    

print('\033[44m'+"Vos gains de jetons dépendent de la combinaison obtenue en ligne bleue(2ème ligne).\n")
print("Vous gagnez :\n_3 jetons pour 3'£', \n_4 jetons pour 3'$',\n_5 jetons pour 3'¥',\n_6 jetons pour 3 '¿', \n_3 pour 3 autres symboles identiques \n_1 jeton pour 2 symboles identiques \n Vous perdez 1 jetons si aucun symbole n'est identique."+'\033[49m')
#règles générales de la machine à sous

n=int(input("\033[3m"+"combien de jetons voulez- vous miser ? \n")) #nombre jetons que l'utilisateur mise
N=n
#N sera la somme après n-rounds


#la machine à sous peut se déclencher

for i in range (0,n): #le programme se réitérera donc n fois
    jeu1()
    jeu2()
    jeu3()
    tableau()
    print(("\033[3m"+"voulez-vous refaire tourner un rouleau pour un jeton? \nSi oui, lequel ?(non/1/2/3)"))
    an = input()
    if an =="non":
        print(" ")
    elif an == "1":
        N=N-1
        jeu1()
        tableau()
    elif an == "2":
        N=N-1
        jeu2()
        tableau()
    elif an == "3":
        N=N-1
        jeu3()
        tableau()
    else:
        print("considéré comme un 'non'.")
    if tab1[1]==tab2[1]==tab3[1]=='£':
        print("c'est gagné, vous gagnez 3 jetons !")
        N=N+3
        jetons()
    elif tab1[1]==tab2[1]==tab3[1]=='$':
        print("c'est gagné, vous gagnez 4 jetons !")
        N=N+4
        jetons()
    elif tab1[1]==tab2[1]==tab3[1]=='¥':
        print("c'est gagné, vous gagnez 5 jetons !")
        N=N+5
        jetons()
    elif tab1[1]==tab2[1]==tab3[1]=='¿':
        print("c'est gagné, vous gagnez 6 jetons !")
        N=N+6
        jetons()
    elif tab1[1]==tab2[1]==tab3[1]:
        print("c'est gagné, vous gagnez 3 jetons !")
        N=N+3
        jetons()
    elif tab1[1]==tab2[1] :
        print("Vous gagnez 1 jeton !")
        N=N+1
        jetons()
    elif  tab2[1]==tab3[1] :
        print("Vous gagnez 1 jeton !")
        N=N+1
        jetons()
    elif  tab1[1]==tab3[1] :
        print("Vous gagnez 1 jeton !")
        N=N+1
        jetons()
    elif tab1[1]!=tab3[1]!=tab2[1]:
        print("Vous perdez 1 jeton :(")
        N=N-1
        jetons()
    if N <1 :
        print("perdu :( ")
        print("veuillez racheter des jetons si vous voulez rejouer.")
        break  
    if N>0:
        print("il vous reste ",N," jeton(s).")
print("  ")    
    
a=0
#à chaque itération de la boucle pour rejouer une partie, les gains et les pertes augmenterons
while N>0:
    print("\033[3m"+"Voulez-vous rejouer une partie ? \nVos gains seront augmentés sauf pour deux symboles identiques mais vos pertes le seront aussi.(oui/non)")
    answer = input()
    if answer == "non":
        print("Vous possédez finalement ",N," jeton(s).")
        print("Vous pourrez échanger vos jetons restants contre des gains si vous le souhaiter.")
        break
    elif answer == "oui":
        j=int(input("combien de vos jetons voulez vous jouez ? "))
        if j<=N:
           for i in range (0,j): #le programme se réitère donc n fois
                jeu1()
                jeu2()
                jeu3()
                tableau()
                print("\033[3m"+"voulez-vous refaire tourner un rouleau pour un jeton? \nSi oui, lequel ?(non/1/2/3)")
                an = input()
                if an =="non":
                    print(" ")
                elif an == "1":
                    N=N-1
                    jeu1()
                    tableau()
                elif an == "2":
                    N=N-1
                    jeu2()
                    tableau()
                elif an == "3":
                    N=N-1
                    jeu3()
                    tableau()
                else:
                    print("considére comme un 'non'")
                if tab1[1]==tab2[1]==tab3[1]=='£':
                    print("c'est gagné, vous gagnez",4+a,"jetons !")
                    N=N+4+a
                    jetons()
                    a=a+1
                elif tab1[1]==tab2[1]==tab3[1]=='$':
                    print("c'est gagné, vous gagnez",5+a,"jetons !")
                    N=N+5+a
                    jetons()
                    a=a+1
                elif tab1[1]==tab2[1]==tab3[1]=='¥':
                    print("c'est gagné, vous gagnez",6+a,"jetons !")
                    N=N+6+a
                    jetons()
                    a=a+1
                elif tab1[1]==tab2[1]==tab3[1]=='¿':
                    print("c'est gagné, vous gagnez",7+a,"jetons !")
                    N=N+7+a
                    jetons()
                    a=a+1
                elif tab1[1]==tab2[1]==tab3[1]:
                    print("c'est gagné, vous gagnez" ,4+a,"jetons !")
                    N=N+4+a
                    jetons()
                    a=a+1
                elif tab1[1]==tab2[1] :
                    N=N+1
                    print("Vous gagnez 1 jetons !")
                    jetons()
                    a=a+1
                elif  tab2[1]==tab3[1] :
                    N=N+1
                    print("Vous gagnez 1 jetons !")
                    jetons()
                    a=a+1
                elif  tab1[1]==tab3[1] :
                    N=N+1
                    print("Vous gagnez 1 jetons !")
                    jetons()
                    a=a+1
                elif tab1[1]!=tab3[1]!=tab2[1]:
                    print("Vous perdez",-4-a,"jetons :(")
                    N=N-4-a
                    jetons()
                    a=a+1
                if N <1 :
                    print("perdu :( ")
                    print("veuillez racheter des jetons si vous voulez rejouer.")
                    break         
        else:
                print('\033[41m' + "impossible, réessayer"+'\033[49m')                          
    else:
        print("Considéré comme 'non'")
        print("Vous possédez finalement ",N," jeton(s).")
        print("Vous pourrez échanger vos jetons restants contre des gains monétaires si vous le souhaitez.")
        break

    
print("Passez une bonne journée :) !!!")    
 