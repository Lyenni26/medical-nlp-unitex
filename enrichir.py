import re
import sys

# Charger le fichier
total = 0
verify = []
string = ""
medicaments = []
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = open (sys.argv[1], "r", encoding="utf-8").readlines()
f1 = open ("infos2.txt", "w")
f2 = open ("infos3.txt", "w")
f3 = open ("subst_corpus.dic", "w", encoding = "utf-16-le")
f3.write ("\ufeff")
words = ['vichy', 'le', 'aspegic','vvp', 'mdz', 'puis', 'kt',  'hémoglobine']

print("Veillez patienter cette opération peut prendre quelques secondes ...\n")

reg = r'''^[-*Ø]?\s?(\w+)\s:?\s?(\d+|,|\d+.\d)+\s?:?(\s(mg\s|MG|UI|ml|mcg|amp|iu|flacon|g|sachet|un\s|1/j|/j)(.+|\n)|(g|/j)\n|(mg)\s.+)'''

for i in file :
    kifkif = re.search(reg,i,re.VERBOSE|re.I)

    if kifkif :
        if  kifkif.group(1).lower() not in words:
                    medicaments.append (kifkif.group(1).lower())
for i in file:
    kifkif=re.search(r'((vitamine|VITAMINE|Vitamine) [A-Za-b](\d| \d)*)',i)
    if kifkif:
        medicaments.append (kifkif.group(1).lower())


#subst_corpus.txt
for i in medicaments :
    chaine = i+",.N+subst"
    f3.write(chaine+"\n")
    
    if i not in string :
        verify.append(i)
        string = string + i
        

#infos2.txt
total_total = 0
for lettre in lettres :
    
    total_lettre = 0
    for i in verify :
        if (lettre == i[0].upper()) :
            f1.write(i+",.N+subst\n")
            total_lettre = total_lettre + 1
    
    f1.write("----------------------------------------------------------\n")
    f1.write(f"total de la lettre {lettre} est {total_lettre}\n")
    f1.write("----------------------------------------------------------\n")
    total_total = total_total + total_lettre

f1.write(f"\n\nle total est {total_total}")

#enrichissement subst.dic
subst = []
with open("subst.dic", "r", encoding = "utf-16-le") as f4 :
    subst = f4.readlines()
    if subst and subst[0].startswith("\ufeff"):
        subst[0] = subst[0][1:]
   

liste = []
f4write = open ("subst.dic", "w", encoding = "utf-16-le")
f4write.write('\ufeff')

for i in verify :
    chaine = i+",.N+subst"+"\n"
    existe = 0
    for j in subst :
        if chaine == j :
            existe = 1
    if existe == 0 :
        subst.append(chaine)
        liste.append(chaine)

subst.sort()
for i in subst :
    f4write.write(f"{i}")

#infos3.txt
liste.sort()
total_total = 0
for lettre in lettres :
    
    total_lettre = 0
    for i in liste :
        if (lettre == i[0].upper()) :
            f2.write(i)
            total_lettre = total_lettre + 1
    
    f2.write("----------------------------------------------------------\n")
    f2.write(f"total de la lettre {lettre} est {total_lettre}\n")
    f2.write("----------------------------------------------------------\n")
    total_total = total_total + total_lettre
f2.write(f"\n\nle total est {total_total}")