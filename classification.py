import pandas as pd

# === CONFIG ===
INPUT_FILE = "noms_extraits.csv"   # ton fichier actuel
OUTPUT_FILE = "noms_structures.csv"

def split_name(full_name):
    if pd.isna(full_name):
        return pd.Series(["", "", ""])

    parts = str(full_name).strip().split()

    if len(parts) == 1:
        return pd.Series([parts[0], "", ""])

    elif len(parts) == 2:
        return pd.Series([parts[0], "", parts[1]])

    elif len(parts) == 3:
        return pd.Series([parts[0], parts[1], parts[2]])

    else:
        # 4 mots ou plus
        nom = parts[0]
        post_nom = parts[1]
        prenom = " ".join(parts[2:])  # fusionne le reste
        return pd.Series([nom, post_nom, prenom])


def main():
    print("Lecture du fichier...")

    df = pd.read_csv(INPUT_FILE)

    # Supposons que ta colonne s'appelle "Nom"
    # adapte si besoin
    source_column = df.columns[0]

    print(f"Colonne détectée : {source_column}")

    df[["Nom", "Post-nom", "Prénom"]] = df[source_column].apply(split_name)

    # Optionnel : supprimer la colonne originale
    df = df[["Nom", "Post-nom", "Prénom"]]

    # Sauvegarde
    df.to_csv(OUTPUT_FILE, index=False)

    print("✅ Transformation terminée")
    print(f"Fichier généré : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()