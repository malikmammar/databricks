import pandas as pd
import requests
from tqdm import tqdm
import time



liens = pd.read_csv('./url/urls_cleaned.csv', sep=',',encoding='utf-8')
# liens = liens[1:1000]
fonctionnels = pd.DataFrame(columns=['URL', 'Statut'])
# Fonction pour tester un lien
def check_link(url):
    try:
        response = requests.get(url, timeout=5)  # Timeout de 5 secondes
        if response.status_code == 200:
            fonctionnels = pd.DataFrame({'URL': [url], 'Statut': ['✅ Fonctionnel']})
            return "✅ Fonctionnel"
        else:
            return f"⚠️ Problème ({response.status_code})"
    except requests.RequestException:
        return "❌ Inaccessible"

# Initialiser la barre de progression
results = []
with tqdm(total=len(liens), desc="Vérification des liens", unit=" lien") as pbar:
    for index, row in liens.iterrows():
        url = row['liens_urls']
        
        status = check_link(url)  # Vérifier le lien
        results.append((url, status))  # Stocker le résultat
        
        pbar.update(1)  # Mise à jour de la progression
        

# Convertir les résultats en DataFrame
df_results = pd.DataFrame(results, columns=["URL", "Statut"])
# df_results.to_csv('./url/test_liens_validation.csv', index=False, encoding='utf-8')
# fonctionnels.to_csv('./url/iens_fonctionnels.csv', index=False, encoding='utf-8')
# Afficher les résultats
print(df_results)