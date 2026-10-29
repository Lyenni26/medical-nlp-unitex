# 🩺 Clinical NLP & Medical Information Extraction (Unitex & Python)

This project implements an end-to-end Natural Language Processing (NLP) pipeline tailored for the biomedical and clinical domains. It combines the rule-based linguistic power of the **Unitex/GramLab** engine with **Python** automation scripts to extract named clinical entities (active pharmaceutical substances, drug names) and parse complex dosage patterns (*posologie*) from raw medical corpora.

---

## 📌 Objectives & Key Features

- **Lexical Resource Construction:** Automated scraping, extraction, and structuring of active substances from VIDAL medical reference directories (indexes A through Z).
- **Morphological Enrichment:** Electronic dictionary management conforming to the DELA format (`Dela_fr`), with automatic compilation of domain-specific lexicons (`subst.dic`, `subst_corpus.dic`).
- **Dosage & Posology Pattern Recognition:** Local syntactic analysis powered by finite-state automata represented as grammar graphs (`posologie.grf`).
- **End-to-End Pipeline Automation:** Integrated execution orchestrating text preprocessing, tokenization, dictionary lookups, graph parsing, and structured report exports (`infos*.txt`).

---

## 🗂️ Project Structure

- `VIDAL/`: Raw HTML source pages from the VIDAL medical drug summaries (A to Z).
- `corpus-medical.txt`: Unstructured medical text corpus containing clinical notes.
- `subst.dic`: Global dictionary of extracted pharmaceutical substances.
- `subst_corpus.dic`: Filtered dictionary containing substances specifically matched against the corpus.
- `Dela_fr.bin` / `Dela_fr.inf`: Compiled French morphological electronic dictionary for Unitex.
- `posologie.grf`: Unitex finite-state graph for clinical dosage and administration pattern detection.
- `Alphabet.txt` / `Norm.txt`: Tokenization, character set definitions, and text normalization rules.
- `extraire.py`: Python script parsing HTML sources to compile substance inventories.
- `enrichir.py`: Script handling DELA dictionary alignment and vocabulary enrichment.
- `unitex.py`: Pipeline automation script executing Unitex command-line processing routines.
- `infos1.txt` – `infos3.txt`: Final extracted entity outputs, matches, and structured analytical reports.

---

## 🛠️ Tech Stack

- **Linguistic Engine:** Unitex / GramLab
- **Core Language:** Python 3
- **Lexical & Grammar Formats:** DELA (LADL Electronic Dictionaries), Finite-State Automata Graphs (`.grf`)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Extract substances from VIDAL sources
```bash
python extraire.py
```

### 3. Enrich and build DELA dictionaries
```bash
python enrichir.py
```

### 4. Run the Unitex linguistic processing pipeline
```bash
python unitex.py
```

Extraction outputs, matched clinical entities, and dosage analysis reports are automatically written to `infos1.txt`, `infos2.txt`, and `infos3.txt`.