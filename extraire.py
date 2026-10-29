import sys
import re
import os

x = open ("infos1.txt", "w", encoding="utf-8")
a = open ("subst.dic", "w", encoding="utf-16-le")
a.write ('\ufeff')
medicaments = []
total = 0
reg = 'Substance/.*>(.+)<'
for fichier in sorted (os.listdir(sys.argv[1])) :
    f = open(os.path.join(sys.argv[1], fichier), "r", encoding="utf-8").read()
    chemain = os.path.join(sys.argv[1], fichier)
    kifkif = (re.findall(reg, f))
    same = kifkif[0]
    lettre = same[0].upper()
    nbr = len(kifkif)
    print(chemain, "--> Nombre de substances actives :", nbr)
    total = total + nbr
    
    #ouverture de subst.dict
    #---------------------------------------------------------------------
    for same in kifkif:
        a.write (f"{same},.N+subst\n")

    #ouverture du fichier infos1.txt
    #---------------------------------------------------------------------
    x.write (f"Lettre :  {lettre} --> Nombre de substances actives : {nbr} \n")



print("total = ",total)
x.write (f"Total : {total} \n")
