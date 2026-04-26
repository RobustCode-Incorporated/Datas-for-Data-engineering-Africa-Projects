import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Données basées sur les projections 2025-2026 (Estimations en milliers)
# Les poids reflètent la hiérarchie démographique réelle : Kimbanseke > Ngaliema > Masina...
population_data = {
    'Commune': [
        'Kimbanseke', 'Ngaliema', 'Masina', 'Kisenso', 'Nsele', 'Mont-Ngafula',
        'Limete', 'Lemba', 'Makala', 'Matete', 'Bumbu', 'Ndjili',
        'Ngaba', 'Ngiri-Ngiri', 'Kalamu', 'Bandalungwa', 'Selembao', 'Kintambo',
        'Barumbu', 'Lingwala', 'Kasa-Vubu', 'Kinshasa', 'Maluku', 'Gombe'
    ],
    'Population (Est. 2026)': [
        2600, 1400, 1200, 1100, 1050, 950, 
        850, 750, 650, 580, 550, 520,
        480, 450, 420, 380, 350, 280,
        250, 220, 180, 160, 150, 95
    ]
}

# Création du DataFrame
df_kin = pd.DataFrame(population_data)

# Calcul du pourcentage pour la simulation de pondération
total_pop = df_kin['Population (Est. 2026)'].sum()
df_kin['Weight (%)'] = (df_kin['Population (Est. 2026)'] / total_pop) * 100

# Tri par population pour un graphique clair
df_kin = df_kin.sort_values(by='Population (Est. 2026)', ascending=False)

# --- VISUALISATION SEABORN ---
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 10))

# Palette de couleurs "Magma" pour souligner la densité
plot = sns.barplot(
    x='Population (Est. 2026)', 
    y='Commune', 
    data=df_kin, 
    palette='magma'
)

# Personnalisation
plt.title('Simulation e-Gov : Répartition de la Population de Kinshasa (Proj. 2026)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Nombre d\'habitants (en milliers)', fontsize=12)
plt.ylabel('Les 24 Communes', fontsize=12)

# Ajout des étiquettes de poids à droite des barres
for i, p in enumerate(plot.patches):
    width = p.get_width()
    plt.text(width + 20, p.get_y() + p.get_height()/2 + 0.1, 
             f'{df_kin.iloc[i]["Weight (%)"]:.1f}%', ha="center", fontsize=10)

plt.tight_layout()
plt.savefig('repartition_kinshasa_2026.png', dpi=300)
plt.show()

# Affichage des premières lignes pour vérification
print(df_kin.head())