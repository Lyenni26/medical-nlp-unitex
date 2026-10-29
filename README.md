# 🩺 Extraction d'Informations Médicales & TAL (Unitex & Python)

Ce projet implémente une chaîne de traitement automatique du langage naturel (TALN / NLP) dédiée au domaine biomédical et clinique. Il combine la puissance linguistique du moteur **Unitex/GramLab** et des scripts d'automatisation en **Python** pour extraire des entités nommées (substances actives, médicaments) et analyser les structures posologiques dans un corpus textuel médical.

---

## 📌 Objectifs & Fonctionnalités

- **Constitution de ressources lexicales :** Extraction et structuration des substances médicamenteuses issues des dictionnaires VIDAL (lettres A à Z).
- **Enrichissement morphologique :** Gestion des dictionnaires électroniques au format DELA (`Dela_fr`) et génération de lexiques spécifiques (`subst.dic`, `subst_corpus.dic`).
- **Reconnaissance de motifs posologiques :** Analyse syntaxique locale basée sur des automates à états finis représentés par des graphes (`posologie.grf`).
- **Pipeline de traitement :** Exécution coordonnée du parsing, du filtrage et de la génération des rapports d'extraction (`infos*.txt`).

---

## 🗂️ Structure du Projet

- VIDAL/ : Pages sources des sommaires VIDAL (A à Z)
- corpus-medical.txt : Corpus textuel brut contenant les données cliniques
- subst.dic : Dictionnaire global des substances actives extraites
- subst_corpus.dic : Substances identifiées spécifiquement dans le corpus
- Dela_fr.bin / .inf : Dictionnaire morphologique français compilé pour Unitex
- posologie.grf : Graphe Unitex pour la détection des posologies
- Alphabet.txt / Norm.txt : Règles de segmentation et de normalisation textuelle
- extraire.py : Script d'extraction des substances à partir des pages HTML
- enrichir.py : Script d'enrichissement et d'alignement des dictionnaires
- unitex.py : Script d'orchestration et d'exécution des modules Unitex
- infos1.txt à infos3.txt : Données extraites et résultats des analyses

---

## 🛠️ Technologies Utilisées

- Linguistique computationnelle : Unitex / GramLab
- Langage : Python 3
- Formats lexicaux : DELA (Dictionnaires Électroniques du LADL), Graphes d'automates (.grf)

---

## 🚀 Utilisation

1. Cloner le dépôt :
   git clone https://github.com/<ton-pseudo>/<nom-du-repo>.git
   cd <nom-du-repo>

2. Extraction des substances depuis les sources VIDAL :
   python extraire.py

3. Enrichissement des dictionnaires :
   python enrichir.py

4. Lancement du pipeline linguistique Unitex :
   python unitex.py

Les résultats d'analyse et les correspondances de posologie sont générés dans les fichiers infos1.txt, infos2.txt et infos3.txt.
