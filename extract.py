import pdfplumber
import pandas as pd
import re

PDF_PATH = "./journal_exetat_2020.pdf"

def is_bold(char):
    """Détecte si un caractère est en gras via son nom de police"""
    return "Bold" in char["fontname"]

def extract_non_bold_lines(pdf_path):
    results = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            chars = page.chars

            current_line = ""
            current_fonts = []

            last_y = None

            for char in chars:
                y = round(char["top"], 1)

                # Nouvelle ligne si changement de position verticale
                if last_y is not None and abs(y - last_y) > 2:
                    if current_line.strip():
                        results.append((current_line.strip(), current_fonts))
                    current_line = ""
                    current_fonts = []

                current_line += char["text"]
                current_fonts.append(char["fontname"])

                last_y = y

            # dernière ligne
            if current_line.strip():
                results.append((current_line.strip(), current_fonts))

    return results


def filter_non_bold_names(lines):
    names = []

    for text, fonts in lines:
        # Vérifie si la ligne contient DU BOLD
        has_bold = any("Bold" in f for f in fonts)

        # On veut uniquement NON BOLD
        if not has_bold:
            # Filtrer les lignes qui ressemblent à des noms
            # Exemple: "BUANGA MUDIASA NOELLA1 F 69"
            if re.search(r"[A-Z]{2,}", text):
                # Nettoyage : enlever numéros, sexe, notes
                clean = re.sub(r"\d+.*", "", text).strip()

                # éviter lignes parasites
                if len(clean.split()) >= 2:
                    names.append(clean)

    return names


def main():
    print("Extraction en cours...")
    
    lines = extract_non_bold_lines(PDF_PATH)
    names = filter_non_bold_names(lines)

    df = pd.DataFrame(names, columns=["Nom"])

    # Sauvegarde
    df.to_csv("noms_extraits.csv", index=False)

    print(f"{len(names)} noms extraits")
    print("Fichier sauvegardé : noms_extraits1.csv")


if __name__ == "__main__":
    main()