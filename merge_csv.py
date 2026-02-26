#merge all the results 

import pandas as pd 
import numpy as np
import os
import sys
import time
from prettytable import PrettyTable
# Merge all the results 

# dossier = "./ectracted_data"

# fichiers_csv = sorted([f for f in os.listdir(dossier) if f.endswith(".csv")])
# df_list = [pd.read_csv(os.path.join(dossier, fichier)) for fichier in fichiers_csv]
# df_final = pd.concat(df_list, ignore_index=True)

# print(len(df_final))
# print(df_final.head())
# df_final.to_csv("./ectracted_data/result_merged.csv", index=False)



# Data management 

data = pd.read_csv('./ectracted_data/data_management.csv', sep=',')

# print(data.columns)
# print(data["age"].head())
# print(data["sexe"].head())
# print(data["medicament"].head())
# print(data["indications"].head())
# print(data["efficacite"].head())
# print(data["effets_secondaires"].head())
# print(data["avis"].head())

# Data visualisation

# print('25% :', np.percentile(data["age"], 25), 
#       '50% :' ,np.median(data["age"]), 
#       '75% :', np.percentile(data["age"], 75))

# data_indications = pd.DataFrame(data["indications"].unique() )
# data_indications.to_csv("./ectracted_data/indications.csv", index=False)    

# data_indications = pd.read_csv("./ectracted_data/indications.csv", sep=',')
# print(data_indications.head())
# for indication in data_indications[0] in 'Ac':
#     print(indication)
#     time.sleep(0)

# data['indications'] = data['indications'].str.lower()
# data['medicament'] = data['medicament'].str.lower()
# data['efficacite'] = data['efficacite'].str.lower()
# data['effets_secondaires'] = data['effets_secondaires'].str.lower()
# data['avis'] = data['avis'].str.lower()
# data['sexe'] = data['sexe'].str.lower()

# data.to_csv("./ectracted_data/result_merged.csv", index=False)
# data['indications'] = data['indications'].str.lower()
# acne_related = data[data['indications'].str.contains(r'\bacn[eé]\b', regex=True, na=False)]
# print(acne_related["indications"].head())

# print(data["indications"].str.contains(r'acn[eé]'))
# print(data["indications"].str.contains(r'acn[eé]' or r'bouton[s]', regex=True))
mots_cles = ['acné',
'acné (visage)',
'boutons',
'acné / nombreux boutons',
'acné et douleurs de menstruation',
'taches rouges et petits boutons rouges',
'acne']
# condition = data['indications'].str.contains(r'\bbpoc?', regex=True, na=False)
# printer  = data[condition]['indications'] 
# for i in printer.unique():
#     print(i)
#     time.sleep(0.5)
# data['indications'] = data['indications'].apply(lambda x: 'acné' if x in r"sérieuses crises d'acnée" else x)

# data.to_csv("./ectracted_data/data_management.csv", index=False)
# condition = data['indications'].str.startswith('b', na=False)

# for indic in sorted(data[condition]['indications'].unique()):
#     print(indic)
#     time.sleep(0.25)

accident_vasculaire_transitoire = ['a i t']
abces_dentaire = ['abces dentaire',
'abcès bouche et mal de dent',
'absces dentaires inclus sous dent sagesse',
'absces dentaire, dent de sagesse incoluse et couronne infectée',
'abscès dentaire']
thyroidectomie = ['ablation de la thyroide',
'ablation thyroide',
'ablation thyroïde']
acouphene = ['accouphène',
'acouphene',
'acouphenes ; pour baisser niveau sonore',
'acouphène',
'acouphènes',
f"acouphènes et baisse d'audition"]
acidite= ['acidité',
          'acidité gastrique',
          'acidité gastrique et brulures',
          'acidité et flatulence',
          f"acidité problèmes d'oesophage",
          'acidité, brûlures d’estomac',
          'acide gastrique',
          f"brûlure d'estomac - acidité gastrique",
          'brûlures acides',
          f"brûlures d'estomac",
          'brulures estomac'
]


allergies = ['allergie',
'allergie (poil, plume,pollen, poussière, acarien)',
'allergie /rhume des foins',
'allergie acariens',
'allergie alimentaire',
'allergie alimentaire et inhalation',
'allergie annuelle',
'allergie aux acariens',
'allergie aux accariens',
'allergie aux coquillages/crustacés',
'allergie aux noix et eczéma sévère',
'allergie aux piqûres de tous les insectes',
'allergie aux pollens et graminés',
'allergie chat',
'allergie particules fines',
'allergie pollen',
'allergie solaire',
'allergie, ashme',
'allergies',
'allergies saisonnieres',
'allérgie']
accident_vasculaire_cerebral = ['avc',
                                'avc post-op']

asthme = [
    'asthme',
'asthme - bronchite',
'asthme / allergie',
'asthme / bpco',
'asthme /bronchite / haleine courte',
'asthme allergie',
'asthme allergie acariens',
'asthme allergique',
'asthme bronchique',
'asthme bronchiteux',
'asthme chronique',
'asthme et bopc',
'asthme et rhume des foins',
'asthme léger',
'asthme modéré',
'asthme non-allergique',
'astjme / bpco',
'astme',
'asme et allergie et rhinite chronique'
]
artrite = ['a,rtrite',
'artrite , goutte'
'artrite juvénile',
'artrite psoriatique',
'artrite rhumatismale',
'artrite, arthorose, calcification tendon',
'arterite',
'arterite obliterante des membres inférieurs',
'arthrite chronique juvénile',
'arthrite psoriatique',
'atritres reumotiode']
arthrose = [
    'arthrose',
'arthrose bas du dos',
'arthrose colonne vertébrale',
'arthrose de la hanche et du genou',
'arthrose des mains',
'arthrose du genou',
'arthrose et osteoporose',
'arthrose pieds',
'arthrose talon',
'arthrose vertebres cevicle',
'arthrose, douleur hanche, picotements jambes, bursite hanche, problèmes genoux',
'arthrose, lombalgie, douleurs articulaires,...',
'artrose  a l epaule gauche      asthme',
'artrose bas du dos',
'athrose scapulo humérale droite'
]
bpco=[
    'bpco',
'bpco / asthme',
'bopc emphysème',
'bopc, asthme et autres maladies des bronches',
'bopc légère',
'bpco asthme et emphysème pulmonaire',
'bpco - emphysème pulmonaire',
'bopc emphysème',
'bopc, asthme et autres maladies des bronches'
]

brochite = [
    'bronchite',
'bronchite aigue',
'bronches (poumons)',
'bronchite chronique asthme',
'bronchite chronique',
'bronchites asthmatique',
'bronchite asthmatique',
'bronches /poumons (glaire)',
'bronchite, toux']

bursite = [
    'bursite',
    'bursite (hanche)',
    'bursite hanche',
    'bursite épaule']

borderline = [
    'borderline / émotions',
    'borderline - agitation intérieure']

brulure = [
    'brûlure',
    'brulure 1 et 2ème degré'
]
    
colon_irritable = [
    'côlon irritable',
]
# condition = data['indications'].str.contains(r'bopc', regex=True, na=False)
condition = data['indications'].str.startswith('c', na=False)
printer  = data[condition]['indications'] 
for i in printer.unique():
    print(i)
    time.sleep(0.5)
