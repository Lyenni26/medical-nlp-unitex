import os
from os import path
if os.path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt Dela_fr.bin subst.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt -a Alphabet.txt posologie.fst2 -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")


#le fichier Alphabet.txt liste tous les carcateres de la langue (francais dans notre cas) et précise les correspondances entre 
#les majuscules et les miniscules et il est indispensable pour le bon fonctionnement d'unitex 

#Utilisation :
#Dans la tokenization (ligne 7): pour définir les regles de segmentation
#Dans la création du dictionnaire (ligne 9) : pour creer le dictionnaire tout en respectant les regles dans le fichier Alphabet.txt
#Dans la recherche des occurences (ligne 11) : en se basant toujours sur les regles définies dans le fichier Alphabet.txt

#exemple de corespondance de lettre
#Yy
#Yÿ
#Ÿÿ
#YŸ

#Aa
#Aà
#Àà
#AÀ
#Aâ
#Ââ
#AÂ
#Aä
#Ää
#AÄ

# Des exemple du text:
# Infirmières, Artères, Bâtiment, Châtellier, Sjögren, ...etc
