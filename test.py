from http.cookiejar import uppercase_escaped_char

from faker import Faker
from random import randint
import random
import numpy as np
fake = Faker()
def couplesUniques(lst1:list,lst2 :list)->list :
    couples = set()
    while len(couples) < randint(min(len(lst1),len(lst2)),len(lst1)*len(lst2)):
        i = random.randint(1, len(lst1))
        j = random.randint(1, len(lst2))
        couples.add((i, j))
    return couples
def supprimerGuillemetsString(string : str)->str :
    string2 = ""
    for i in string :
        if (i != '\''):
            string2 += i
    return string2
def toUpperCase(string : str)->str :
    return string.upper()
table_tenrac = []
grades_inf_contraintes = ['Affilié', 'Symphatisant', 'Adhérent']
grades_sup_contraintes = ['Chevalier', 'Dame', 'Grand Chevalier', 'Haute Dame', 'Commandeur', 'Grande Croix']
nom_reunion = ['Assemblée', 'Conseil Kebab', 'Réunion Tenrac', 'Comité Broche', 'Réunion Grill', 'Assise Döner',
               'Conclave Gyros', 'Réunion Spit', 'Conseil Roti', 'Réunion Chef', 'Assemblée Spéciale', 'Comité Kebab',
               'Réunion Ordre', 'Conseil Maître', 'Réunion Club', 'Assise Viande', 'Conclave Chef', 'Réunion Sauce',
               'Conseil Grillade', 'Réunion Dégustation']

nom_repas = ['Kebab Royal', 'Assiette Döner', 'Galette Poulet', 'Sandwich Mixte', 'Kebab Classique', 'Assiette Gyros',
             'Kebab Fromage', 'Assiette Poulet', 'Sandwich Döner', 'Kebab Maison', 'Galette Agneau', 'Assiette Mixte',
             'Kebab Spécial', 'Sandwich Royal', 'Galette Fromage', 'Assiette Boeuf', 'Kebab Poulet', 'Sandwich Agneau',
             'Assiette Royale', 'Kebab Légumes']
nom_club = ['Club Kebab', 'Le Cercle du Döner', 'Les Amis du Gyros', 'La Confrérie du Kebab', 'Club de la Broche',
            'L\'Alliance du Spit', 'Le Pavillon du Grill', 'Les Maîtres du Roti', 'La Table d\'Or',
            'Le Comptoir du Kebab', 'Le Salon du Méchoui', 'Les Compagnons du Döner', 'L\'Ordre du Barbecue',
            'La Grande Confrérie', 'Le Club des Rotisseurs', 'Les Gourmets du Kebab', 'La Société du Gyros',
            'Les Enthousiastes du Döner', 'Le Cercle des Grillades', 'La Maison du Kebab', 'L\'Académie du Spit',
            'Les Souverains du Döner', 'Le Temple du Kebab', 'La Légende du Gyros', 'Les Chevaliers du Grill',
            'La Confrérie des Rotis', 'Le Clube dos Kebabs', 'Il Circolo del Döner', 'Der Kebab Klub',
            'The Kebab Society', 'Les Ambassadeurs', 'Les Émissaires', 'Les Connaisseurs', 'Les Dévoreurs',
            'Les Dégustateurs', 'Les Explorateurs', 'Les Pèlerins', 'Les Gardiens', 'Les Veilleurs', 'Les Sentinelles',
            'Les Fidèles', 'Les Passionnés', 'Les Érudits', 'Les Sages', 'Les Princes', 'Les Seigneurs', 'Les Barons',
            'Les Ducs', 'Les Vicomtes', 'Les Marquis']
nom_territoire = ['Ile-de-France', 'Provence-Alpes-Côte', 'Nouvelle-Aquitaine', 'Auvergne-Rhône-Alpes',
                  'Hauts-de-France', 'Normandie', 'Bretagne', 'Grand Est', 'Pays de la Loire', 'Occitanie',
                  'Bourgogne-Comté', 'Centre-Val-Loire', 'Corse']
nom_ordre = ['Ordre du Kebab', 'Ordre de la Broche', 'Ordre du Gyros', 'Ordre du Döner', 'Ordre de la Grillade',
             'Ordre du Rotisseur', 'Ordre du Spit', 'Ordre du Méchoui', 'Ordre de la Viande', 'Ordre du Barbecue']
nom_entretien = ['Nettoyage', 'Dégraissage', 'Vérification', 'Lubrification', 'Révision', 'Remplacement', 'Calibration',
                 'Inspection']
nom_machine = ['Tornado Grill', 'KebabMaster 3000', 'Döner Chef Pro', 'Gyro Spit', 'Vertical Broiler',
               'AutoRotisserie 5000', 'KebabTech Turbo', 'Pro Grill Master', 'Doner King', 'Spitfire Grill']

rang_contraintes = ['Novice', 'Compagnon']
titre_contraintes = ['Philanthrope', 'Protecteur', 'Honorable']
dignite_contraintes = ['Maître', 'Grand Chancelier', 'Grand Maître']



nom_ingredient = ['Tomate', 'Oignon', 'Ail', 'Carotte', 'Pomme de terre', 'Courgette', 'Aubergine', 'Poivron',
                  'Champignon']
nom_modele = ['KebabMaster Pro', 'Tornado Grill 3000', 'DönerChef Auto', 'SpitRoast X1', 'GyroStar Plus',
              'KebabTech Vert', 'ProRotisserie 5000']
lst = []
extension_tenrac = [{
    "CodePerso": i,
    "NomTenrac": fake.name(),
    "Courriel": fake.company_email(),
    "Adresse Postale": fake.postcode(),
    "SIRET": fake.unique.random_int(1000, 9999),
    "IdOrdre": fake.unique.random_int(1000, 9999),
    "IDClub": fake.unique.random_int(1000, 9999),
    "IdOrdre_1": fake.unique.random_int(1000, 9999),
    "NomGradSup": fake.random_element(elements=grades_sup_contraintes),
    "NomDignite": fake.random_element(elements=dignite_contraintes),
    "NomTitre": fake.random_element(elements=titre_contraintes),
    "NomRang": fake.random_element(elements=rang_contraintes)}
    for i in range(1, 10)
]
aliments_contraintes = [
    "pomme", "banane", "poire", "peche", "abricot", "ananas", "mangue", "fraise", "framboise", "cerise",
    "orange", "citron", "pamplemousse", "raisin", "melon", "pasteque", "kiwi", "prune", "figue", "datte",
    "riz", "pates", "pain", "semoule", "quinoa", "avoine", "ble", "mais", "farine", "couscous",
    "poulet", "boeuf", "porc", "agneau", "dinde", "canard", "steak", "jambon", "saucisse", "lardon",
    "saumon", "thon", "cabillaud", "sardine", "maquereau", "truite", "crevettes", "moules", "huitres", "crabe",
    "oeuf", "lait", "fromage", "yaourt", "beurre", "creme", "glace", "lait_condense", "lait poudre", "mozzarella",
    "chocolat", "sucre", "miel", "confiture", "nutella", "caramel", "biscuit", "gateau", "tarte", "croissant",
    "amandes", "noix", "noisettes", "cacahuetes", "pistaches", "raisins_secs", "cereales", "granola", "barre_cereales", "popcorn",
    "pizza", "burger", "sandwich", "frites", "omelette", "crepe", "gaufre", "riz au_lait", "mousse_chocolat", "tiramisu",
    "lasagnes", "spaghetti", "ravioli", "nuggets", "cordon_bleu", "steak hache", "roti", "sushi", "sashimi", "tempura"
]
Aliments = [{'idA' : i,
             'nomAliment' : aliments_contraintes[i-1].upper()}
            for i in range(1,len(aliments_contraintes)+1)]

sauce_contrainte = [
    "sauce tomate", "sauce bechamel", "sauce mayonnaise", "sauce ketchup", "sauce moutarde",
    "sauce barbecue", "sauce soja", "sauce aigre douce", "sauce tartare", "sauce cocktail",
    "sauce poivre", "sauce roquefort", "sauce fromage", "sauce creme", "sauce forestiere",
    "sauce bolognaise", "sauce carbonara", "sauce pesto", "sauce arrabbiata", "sauce napolitaine",
    "sauce hollandaise", "sauce bearnaise", "sauce vin rouge", "sauce echalote", "sauce champignon",
    "sauce curry", "sauce curry coco", "sauce tikka masala", "sauce tandoori", "sauce satay",
    "sauce teriyaki", "sauce yakitori", "sauce nuoc mam", "sauce sriracha", "sauce chili",
    "sauce guacamole", "sauce salsa", "sauce queso", "sauce enchilada", "sauce mole",
    "sauce yaourt", "sauce tzatziki", "sauce blanche", "sauce harissa", "sauce samourai",
    "sauce algerienne", "sauce andalouse", "sauce burger", "sauce pita", "sauce kebab",
    "sauce miel moutarde"]
Sauce =  [{'idS' : i,
          'nomSauce' : "'"+sauce_contrainte[i-1].upper()+"'"}
            for i in range(1,len(sauce_contrainte)+1)]
ingredients_contraintes = ["Pomme","Banane","Orange","Poire","Fraise","Framboise","Myrtille","Cerise",
"Pêche","Abricot","Ananas","Mangue","Kiwi","Citron","Lime","Pastèque",
"Melon","Raisin","Prune","Grenade","Tomate",
"Pomme de terre","Patate douce","Échalote","Lentilles","Pois chiche","Haricot rouge",
"Haricot noir","Riz","Pâtes","Spaghetti","Farine","Sucre","Sucre roux",
"Sel","Poivre","Beurre","Margarine","Lait","Crème fraîche","Yaourt",
"Fromage","Mozzarella","Parmesan","Cheddar","Camembert","Brie",
"Roquefort","Œuf","Poulet","Dinde","Bœuf","Porc","Agneau","Saumon",
"Thon","Sardine","Crevette","Moule","Huître","Calamar","Riz complet",
"Quinoa","Boulgour","Semoule","Pain","Pain complet","Pain de mie",
"Miel","Confiture","Chocolat noir","Chocolat au lait","Chocolat blanc",
"Vanille","Cannelle","Muscade","Curry","Curcuma","Paprika","Cumin","Basilic","Persil","Coriandre","Thym","Romarin","Laurier",
"Menthe","Sauce tomate","Ketchup","Mayonnaise","Moutarde","Sauce soja",
"Vinaigre","Huile de olive","Huile de tournesol","Huile de coco","Eau",
"Eau gazeuse","Café","Thé","Lait de amande","Lait de soja","Tofu",
"Tempeh","Truffe","Noix","Amande","Noisette","Pistache",
"Cajou","Raisin sec","Datte","Figue","Abricot sec","Noix de coco",
"Sucre glace","Levure","Levure chimique","Gélatine","Agar-agar",
"Piment","Tortilla","Tacos","Riz basmati","Riz thaï","Nouilles","Nouilles chinoises",
"Nouilles ramen","Wasabi","Fenouil","Endive",
"Mangue séchée","Banane séchée","Sel de mer","Fleur de sel","Sucre vanillé",
"Sirop de érable","Caramel","Coulis de fruits","Crème chantilly",
"Glace vanille","Glace chocolat","Sorbet citron","Sorbet fraise",
"Biscuit","Gâteau","Croissant","Pain au chocolat","Brioche","Crêpe",
"Gaufre","Muesli","Corn flakes","Riz soufflé","Barre de céréales"]
Ingredient =  [{'idI' : i,
          'nomIngredient' : "'"+ ingredients_contraintes[i-1].upper() +"'"}
            for i in range(1,len(ingredients_contraintes)+1)]
nomMachine_contrainte =  [
"Four","Four a micro-ondes","Mixeur","Blender","Robot pâtissier",
"Machine à pain","Friteuse","Friteuse à air","Grill","Plancha",
"Machine à café","Machine espresso","Bouilloire","Cuiseur vapeur",
"Autocuiseur","Multicuiseur","Yaourtière","Sorbetière","Machine à pâtes",
"Hachoir","Trancheuse","Extracteur de jus","Centrifugeuse",
"Machine à popcorn","Crêpière","Gaufrier","Appareil à raclette",
"Appareil à fondue","Toaster","Machine sous vide","Déshydrateur",
"Cuiseur à riz","Cuiseur à œufs","Machine à hot-dog","Presse-agrumes",
"Machine à glace","Fumoir","Barbecue électrique","Barbecue gaz"
]
NomMachine = [{'idNM' : i,
          'nomMachine' : "'"+nomMachine_contrainte[i-1].upper()+"'"}
            for i in range(1,len(nomMachine_contrainte)+1)]
modele_contrainte = ["Pro 100","Pro 200","Pro 300","Ultra","Ultra X","Max","Max Plus",
"Chef Edition","Home","Home Plus","SmartCook","SmartCook X",
"KitchenMaster","FoodPro","CookExpert","HeatMaster",
"TurboMix","PowerBlend","FreshJuice","SteamPro",
"RiceMaster","BakePro","IceDream","CoffeeMaster",
"GrillPro","AirFry 3000","AirFry 5000","MultiCook 10",
"MultiCook 20","EasyCook","QuickChef","ProChef",
"Silver Edition","Black Edition","Premium","Deluxe",
"Compact","Family","XL","XXL"]
Modele = [{'idMo' : i,
          'nomMachine' : "'"+modele_contrainte[i-1].upper()+"'"}
            for i in range(1,len(modele_contrainte)+1)]
typeEntretien_contrainte = [
"Nettoyage complet",
"Détartrage","Remplacement du filtre",
"Graissage des pièces","Vérification électrique",
"Calibration de température","Changement de joint",
"Nettoyage du réservoir","Inspection générale",
"Remplacement lame","Affûtage lame",
"Nettoyage ventilateur","Remplacement fusible",
"Test de sécurité","Mise à jour logiciel",
"Nettoyage buse","Remplacement courroie",
"Vérification moteur","Nettoyage intérieur",
"Nettoyage extérieur","Désinfection","Vidange",
"Remplacement batterie","Vérification capteurs",
"Calibration balance","Test pression",
"Remplacement tuyau","Nettoyage filtre air",
"Nettoyage filtre eau","Inspection thermique",
"Test démarrage","Réinitialisation système","Nettoyage grille",
"Remplacement résistance","Vérification câble",
"Nettoyage pompe","Remplacement roulement",
"Test fonctionnement","Contrôle qualité","Maintenance préventive"]
TypeEntretien = [{"idE" : i ,
                "typeEntretien" : "'"+ typeEntretien_contrainte[i-1].upper()+"'"}
                 for i in range (1,len(typeEntretien_contrainte)+1)]
tmpMachine=1
Machine = [{"idM" : i,
            "idNM" : j[0],
            "idMo" : j[1]}
           for (i,j) in zip(range(1,len(NomMachine)*len(Modele)+1),couplesUniques(NomMachine,Modele))
            ]

raisonSocial_prefixes = [
    "Tech", "Agro", "Trans", "Logi", "Info", "Data", "Electro", "Bat", "Menuiserie",
    "Plomberie", "Nettoyage", "Pharma", "Vetement", "Super", "Auto", "Garage",
    "Transport", "Logistique", "Import", "Export", "Conseil", "Finance",
    "Assurance", "Immobilier", "Location", "Hotel", "Voyage", "Event",
    "Formation", "Medical", "Optique", "Laboratoire", "Energie", "Recyclage",
    "Construction", "Architecture", "Design", "Digital", "Media", "Print"]

raisonSocial_suffixes = [
    "Solutions", "Services", "Industries", "International", "France", "Europe",
    "Distribution", "Production", "Systems", "Concept", "Group", "Entreprise",
    "Corporation", "SARL", "SAS", "SA", "Pro", "Express", "Plus", "Expert",
    "Global", "Tech", "Innov", "Maintenance", "Engineering", "Consulting",
    "Partners", "Ressources", "Gestion", "Developpement"]
raisonSocial_contrainte=[]
for i in range (len(raisonSocial_prefixes)):
    for j in range (len(raisonSocial_suffixes)):
        raisonSocial_contrainte.append(raisonSocial_prefixes[i]+' ' +raisonSocial_suffixes[j])
numeroSiret=[]
for i in range(4200) :
    numeroSiret.append(fake.unique.random_int(00000000000000,99999999999999))

Organisme = [{"numeroSiret" : numeroSiret[i-1],
              "raisonSociale" : raisonSocial_contrainte[randint(0,len(raisonSocial_contrainte)-1)]}
            for i in range (1,len(numeroSiret)+1)
            ]
tmp = [{'idT': 0,
       'nomTitre': '::'}]
Titre = [{"idTi" : i,
          "nomTitre" : titre_contraintes[i-1]}
         for i in range (1,len(titre_contraintes)+1)
         ]
Titre = tmp + Titre
tmp = [{'idD' : 0,
        'nomDignite' : '::'}]
Dignite = [{"idD" : i,
          "nomDignite" : dignite_contraintes[i-1]}
           for i in range (1,len(dignite_contraintes)+1)]
Dignite = tmp + Dignite
tmp = [{'idRa' : 0,
        'nomRang' : '::'}]

Rang = [{"idRa" : i,
          "nomRang" : rang_contraintes[i-1]}
           for i in range (1,len(rang_contraintes)+1)]
Rang = tmp + Rang

idgrade_contrainte = [ i for i in range (1,len(grades_inf_contraintes)+len(grades_sup_contraintes)+1)]
PasTresHautGradee = [{"idG" : i,
                  "nomGrade" : j}
                for i,j in zip(range(1,len(grades_inf_contraintes)+1),grades_inf_contraintes)]
TresHautGradee = [{"idG" : i,
                  "nomGrade" : j}
                for i,j in zip(range(len(grades_inf_contraintes)+1,len(idgrade_contrainte)+1),grades_sup_contraintes)]
Organisation_contrainte = [i for i in range(1,101+5*100+1)]
id_Club_contrainte = [i for i in range(102,len(Organisation_contrainte)+1)]
Club_contrainte = ['Club ','Le Grand ','Supreme','Doner ','Raclette suprême de ']
nomClub_contrainte = []
for i in aliments_contraintes:
    for j in Club_contrainte:
        nomClub_contrainte.append(j+i)

ordreNom_contrainte = [
    "burger", "cheeseburger", "double cheeseburger", "bacon burger", "chicken burger",
    "fish burger", "veggie burger", "burger deluxe", "burger barbecue", "burger spicy",
    "hot dog", "chili dog", "corn dog", "hot dog fromage", "hot dog bacon",
    "frites", "frites cheese", "frites bacon", "frites chili", "frites curly",
    "nuggets", "tenders poulet", "wings poulet", "wings barbecue", "wings spicy",
    "pizza margherita", "pizza pepperoni", "pizza fromage", "pizza 4 fromages", "pizza barbecue",
    "pizza hawaienne", "pizza viande", "pizza veggie", "pizza poulet", "pepperoni fromage",
    "tacos", "tacos poulet", "tacos boeuf", "tacos mixte", "tacos cordon bleu",
    "kebab", "kebab poulet", "kebab boeuf", "kebab mixte", "kebab galette",
    "wrap poulet", "wrap boeuf", "wrap veggie", "wrap crispy", "wrap spicy",
    "sandwich jambon", "sandwich poulet", "sandwich thon", "sandwich fromage", "sandwich club",
    "panini poulet", "panini fromage", "panini jambon", "panini thon", "panini steak",
    "croque monsieur", "croque madame", "bagel saumon", "bagel poulet", "bagel fromage",
    "donut sucre", "donut chocolat", "donut fraise", "donut caramel", "donut glacage",
    "milkshake vanille", "milkshake chocolat", "milkshake fraise", "milkshake caramel", "milkshake banane",
    "glace vanille", "glace chocolat", "glace fraise", "glace caramel", "glace cookies",
    "sundae chocolat", "sundae caramel", "sundae fraise", "sundae vanille", "sundae mix",
    "brownie", "cookie", "muffin chocolat", "muffin myrtille", "muffin vanille",
    "tiramisu", "cheesecake", "pancakes", "gaufre", "crepe",
    "omelette sandwich"
]
departements = [
"Ain","Aisne","Allier","Alpes-de-Haute-Provence","Hautes-Alpes","Alpes-Maritimes",
"Ardèche","Ardennes","Ariège","Aube","Aude","Aveyron",
"Bouches-du-Rhône","Calvados","Cantal","Charente","Charente-Maritime","Cher",
"Corrèze","Corse-du-Sud","Haute-Corse","Côte-de Or","Côtes-de Armor","Creuse",
"Dordogne","Doubs","Drôme","Eure","Eure-et-Loir","Finistère",
"Gard","Haute-Garonne","Gers","Gironde","Hérault","Ille-et-Vilaine",
"Indre","Indre-et-Loire","Isère","Jura","Landes","Loir-et-Cher",
"Loire","Haute-Loire","Loire-Atlantique","Loiret","Lot","Lot-et-Garonne",
"Lozère","Maine-et-Loire","Manche","Marne","Haute-Marne","Mayenne",
"Meurthe-et-Moselle","Meuse","Morbihan","Moselle","Nièvre","Nord",
"Oise","Orne","Pas-de-Calais","Puy-de-Dôme","Pyrénées-Atlantiques","Hautes-Pyrénées",
"Pyrénées-Orientales","Bas-Rhin","Haut-Rhin","Rhône","Haute-Saône","Saône-et-Loire",
"Sarthe","Savoie","Haute-Savoie","Paris","Seine-Maritime","Seine-et-Marne",
"Yvelines","Deux-Sèvres","Somme","Tarn","Tarn-et-Garonne","Var",
"Vaucluse","Vendée","Vienne","Haute-Vienne","Vosges","Yonne","Territoire de Belfort",
"Essonne","Hauts-de-Seine","Seine-Saint-Denis","Val-de-Marne","Val-de Oise",
"Guadeloupe","Martinique","Guyane","La Réunion","Mayotte"
]
Ordre_contrainte = Club_contrainte[1:-1] + ['Ordre']
Ordre = [{"idO" : i,
          "nomOrdre" : toUpperCase("'"+Ordre_contrainte[randint(0,len(Ordre_contrainte)-1)]+ ' ' + ordreNom_contrainte[i%len(ordreNom_contrainte)]+"'"),
          "Territoire" :toUpperCase("'"+ departements[i-1]+"'")}
        for i in range(1,102)]
Club = [{"idO_1" : i,
        "nomClub" : "'"+nomClub_contrainte[i-1]+"'",
         "adresseClub" : "'"+fake.address() + "'",
         "idO" : (i-1)%101+1
         }
        for i in range (1,len(nomClub_contrainte)+1)]
mois = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10','11','12']
jour = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
tmp = [str(i) for i in range(10,32)]
jour = jour + tmp
Reunion=[{'idReunion' : i,
          'date_' : jour[randint(0,30)]+'/' + mois[randint(0,11)]+'/' + str(randint(2000,2040))}
          for i in range(1,len(nom_reunion)+1) for j in range(800)]
# /TODO


legumes_contraintes = ["::","carotte","pomme_de_terre",
        "tomate","concombre",
        "courgette","aubergine",
        "poivron","oignon","ail","échalote",
        "poireau","chou_vert",
        "chou_rouge","chou_fleur",
        "brocoli","chou_de_bruxelles",
        "navet","radis","radis_noir","betterave","céleri",
        "céleri_rave","fenouil","épinard",
        "laitue","roquette","mâche","endive","artichaut","asperge",
        "haricot_vert","haricot_beurre","petit_pois","fève",
        "lentille","pois_chiche","maïs","patate_douce",
        "topinambour","rutabaga","panais","salsifis",
        "crosne","igname","manioc","taro","courge","courge_butternut",
        "potiron","potimarron","citrouille","courge_spaghetti",
        "bette","blette","oseille","cresson",
        "pak_choi","chou_chinois","chou_kale",
        "broccolini","romanesco","piment","gombo",
        "okras","soja","pousse_de_soja","bambou",
        "algue","cornichon","capre","persil_racine",
        "raifort","wasabi","mizuna","tatsoi",
        "amarante_feuille","feuille_de_vigne",
        "laitue_romaine","laitue_iceberg","scarole","frisée",
        "chicorée","pissenlit",
        "plantain","ortie","cardon","chayote",
        "christophine","calebasse","coloquinte"]
Legume = [{"idL" : i+1,
           "nomLegume" : "'"+legumes_contraintes[i].upper()+"'"
          }
          for i in range(len(legumes_contraintes))]

Plat = [{"idP" : k+1,
        "nomPlat" : toUpperCase("'" + ordreNom_contrainte[i-1] + ' ' + supprimerGuillemetsString(Legume[j-1]['nomLegume']) + "'"),
        "idL" : Legume[j-1]["idL"] }
        for (k,(i,j)) in zip(range(min(len(ordreNom_contrainte),len(Legume))),couplesUniques(ordreNom_contrainte,Legume))]


print(Plat)
Constitue = [{"idP" : i,
              "idA" : j}
             for (i,j) in couplesUniques(Plat,Aliments)
            ]
Contient = [{"idP" : i,
             "idS" : j}
            for (i,j) in couplesUniques(Plat,Sauce)]
repas_intitule_contrainte = ["Poulet rôti", "Poulet curry", "Poulet basquaise",
"Poulet à la crème", "Escalope de poulet", "Steak frites",
"Steak sauce poivre", "Bœuf bourguignon", "Bœuf carottes",
"Hachis parmentier", "Lasagnes bolognaise", "Spaghetti bolognaise",
"Spaghetti carbonara", "Pâtes au pesto", "Pâtes au saumon",
"Pâtes à la crème", "Chili con carne", "Couscous",
"Tajine poulet", "Tajine agneau", "Kebab",
"Burger maison", "Saucisses lentilles", "Cordon bleu",
"Blanquette de veau", "Carbonnade flamande", "Rôti de porc",
"Porc au caramel", "Saumon grillé", "Saumon à la crème",
"Cabillaud vapeur", "Cabillaud sauce citron", "Thon à la tomate",
"Sardines grillées", "Poisson pané", "Paëlla",
"Risotto aux fruits de mer", "Crevettes sautées", "Moules marinières",
"Riz cantonais", "Riz poulet", "Riz légumes",
"Risotto champignons", "Risotto poulet", "Nouilles sautées",
"Nouilles poulet", "Nouilles crevettes", "Omelette fromage",
"Omelette champignons", "Ratatouille", "Gratin dauphinois",
"Gratin de légumes", "Soupe de légumes", "Salade composée",
"Salade César", "Salade niçoise", "Quiche lorraine",
"Quiche légumes", "Tarte tomate", "Tarte aux légumes",
"Falafel", "Curry de légumes", "Chili sin carne",
"Sandwich jambon beurre", "Croque monsieur", "Croque madame",
"Panini poulet", "Panini fromage", "Wrap poulet",
"Wrap thon", "Pizza margherita", "Pizza reine",
"Pizza 4 fromages", "Hot dog", "Nuggets frites"
]

Repas= [{"idR" : i,
        "intitule" : "",
        "idM" : j}
        for i in range(1,len(repas_intitule_contrainte)+1)]
adressePart_contrainte=[fake.address() for i in range(100)]
combinaisonsAdressesPartenaire=couplesUniques(adressePart_contrainte,Ordre)
AdressePartenaire = [{"idA" : k+1,
                      "adressePart" : adressePart_contrainte[j-1].replace('\n',' '),
                      "idO" : Ordre[i-1]["idO"]}
                     for (k,(j,i)) in zip(range(len(combinaisonsAdressesPartenaire)),combinaisonsAdressesPartenaire)
                    ]
libelle = ['JOUR','MOIS','ANNEE']
valeur_libelle = [31,12,10]
def tripletsUniques(lst1,lst2,lst3) :
    triplets = set()
    while len(triplets) < randint(min(len(lst1), len(lst2),len(lst3)), len(lst1) * len(lst2)*len(lst3)):
        i = random.randint(1, len(lst1))
        j = random.randint(1, len(lst2))
        k = random.randint(1, len(lst3))
        triplets.add((i,j,k))
    return triplets
combinaisonNecessite=tripletsUniques(Modele,NomMachine,TypeEntretien)
Necessite = [{"idMo" : i,
              "idNM" :   j,
               "idE" : k,
               "periodicite" : "'"+str(str(randint(1,valeur_libelle[i%3])) + ' ' + libelle[i%3]) +"'" }
            for (i,j,k) in combinaisonNecessite
            ]
print(Necessite[:5])
Compose = [{"idP" : i,
            "idR" : j}
            for (i,j) in couplesUniques(Plat,Repas)]
Est_constitue = [{"idS" : i,
            "idI" : j}
           for (i,j) in couplesUniques(Sauce,Ingredient)]

Organise = [{"idReunion" : Reunion[i-1]["idReunion"],
            "date_" : Reunion[i-1]["date_"],
            "idR" : j}
            for (i,j) in couplesUniques(Reunion,Repas)]

def creationListeNumerosString(n : int,valeur : int)->list:
    Num_liste=[]
    NUM=""
    while(len(Num_liste) < n or len(Num_liste) != len(set(Num_liste))):
        Num =""
        for i in range(valeur) :
            Num+=str(random.randint(1,9))
        Num_liste.append(Num)
    return Num_liste
Organisme = [{"numeroSiret" : i ,
              "raisonSociale" : fake.random_element(elements=raisonSocial_contrainte)}
             for i in creationListeNumerosString(10000,14)]
Grade = PasTresHautGradee+TresHautGradee
Tenrac = [{"idO" : i,
          "numeroSiret" : Organisme[randint(0,len(Organise)-1)]["numeroSiret"],
          "idT" : i,
          "nomTenrac": '\''+fake.name()+'\'',
          "courrier" :  '\''+fake.email()+'\'',
          "telephone" : '\''+fake.phone_number()+'\'',
          "adressePostal" : '\''+fake.postcode()+'\'',
          "idG": randint(0,len(Grade)),
           'idTi' : randint(0,len(Titre)),
          "idD": randint(0,len(Dignite)),
          "idRa": randint(0,len(Rang)) }
          for i in range(1,10)
          ]

#/TODO Evite
#/TODO Tenrac
#/TODO Entretien
#/Todo Assiste
import oracledb
import oracledb
import faker
connection = oracledb.connect(
    user="ADMIN",
    password="TenracPireSae2026@",
    dsn="tenrac_low",
    config_dir="./wallet",
    wallet_location="./wallet",
    wallet_password="TenracKebab@1"
)

def obtenirToutesLesTables()-> list :
    lst1 =[]
    with connection.cursor() as cursor:
        sql = ("SELECT table_name FROM USER_TABLES "
               +"WHERE table_name<>'DBTOOLS$EXECUTION_HISTORY'")
        for i in cursor.execute(sql) :
            lst1.append(i)
    lst2 = [i[0] for i in lst1]
    return lst2
def dropToutesLesTables() :
    lst = obtenirToutesLesTables()
    with connection.cursor() as cursor:
        for i in lst:
            sql = ("DROP TABLE  "+i+" CASCADE CONSTRAINTS")
            cursor.execute(sql)
            print('Table dropped : ',i)
#def createToutesLesTables() :
#dropToutesLesTables()
#cursor=connection.cursor()

#print(obtenirToutesLesTables())
def createToutesLesTables() :
    lst = []
    with open('requetes/intention_de_la_BD.txt','r') as file :
        var=""
        for line in file.readlines() :
            for char in line.strip() :
                if char != ';' :
                    var+=char
                else :
                    lst.append(var)
                    var=""
    with connection.cursor() as cursor:
        for sql in lst:
            cursor.execute(sql)
            print('Table created :',obtenirToutesLesTables()[-1])
def createInsertionFiles() :
    for i in obtenirToutesLesTables() :
        f = open('requetes/insertion_donnees'+i+'.txt','w')
        f.close()
list_test = [{"idA" : 1,"nomAliment" : "'pneus--de-voitures'"},
             {"idB" : 2,"nomAliment" : "'huile de moteur'"},
            ]
#def insertInsertionDonnees(nom_de_la_table,donnees : lst) :
#for i in donnees :
def effacerDonnesTables(nom_table : str) :
    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE '+nom_table)


def insertionDonneesTables(donnees,nom_table) :
    cursor = connection.cursor()
    f = open('requetes/insertion_donnees/' + nom_table + '.txt', 'w')
    for i in donnees :
        sql="INSERT INTO " + nom_table + " VALUES("
        for j in i.values() :
            sql+=str(j)+","
        sql = sql[:-1]
        sql+=")"
        print(sql)
        cursor.execute(sql)
        f.write(sql+';\n')
    f.close()
def effacerContenuDuFichier(fiename) :
    file = open('requetes/' + fiename, 'w')
    file.close()










#test
aliments_contraintes = [
    "pomme", "banane", "poire", "peche", "abricot", "ananas", "mangue", "fraise", "framboise", "cerise",
    "orange", "citron", "pamplemousse", "raisin", "melon", "pasteque", "kiwi", "prune", "figue", "datte",
    "riz", "pates", "pain", "semoule", "quinoa", "avoine", "ble", "mais", "farine", "couscous",
    "poulet", "boeuf", "porc", "agneau", "dinde", "canard", "steak", "jambon", "saucisse", "lardon",
    "saumon", "thon", "cabillaud", "sardine", "maquereau", "truite", "crevettes", "moules", "huitres", "crabe",
    "oeuf", "lait", "fromage", "yaourt", "beurre", "creme", "glace", "lait_condense", "lait poudre", "mozzarella",
    "chocolat", "sucre", "miel", "confiture", "nutella", "caramel", "biscuit", "gateau", "tarte", "croissant",
    "amandes", "noix", "noisettes", "cacahuetes", "pistaches", "raisins_secs", "cereales", "granola", "barre_cereales", "popcorn",
    "pizza", "burger", "sandwich", "frites", "omelette", "crepe", "gaufre", "riz au_lait", "mousse_chocolat", "tiramisu",
    "lasagnes", "spaghetti", "ravioli", "nuggets", "cordon_bleu", "steak hache", "roti", "sushi", "sashimi", "tempura"
]
#dropToutesLesTables()
Organisation = [{'idO': i} for i in range(1,len(Ordre)+len(Club))]
print(len(Organisation),print(len(Club)))
#createToutesLesTables()
cursor = connection.cursor()
Aliments = [{'idA' : i,
             'nomAliment' : "'"+aliments_contraintes[i-1].upper()+"'"}
            for i in range(1,len(aliments_contraintes)+1)]
#print(obtenirToutesLesTables())
#effacerDonnesTables('Aliment')
def ajouteToutesDonneesTables() :
    insertionDonneesTables(Legume,'Legume')
    insertionDonneesTables(Aliments,'Aliment')
    insertionDonneesTables(Sauce,'Sauce')
    insertionDonneesTables(Ingredient,'Ingredient')
    insertionDonneesTables(Est_constitue,'Est_constitue')
    insertionDonneesTables(Plat, 'Plat')
    insertionDonneesTables(Contient, 'Contient')
    insertionDonneesTables(Constitue, 'Constitue')
    insertionDonneesTables(Modele, 'Modele')
    insertionDonneesTables(NomMachine, 'NomMachine')
    insertionDonneesTables(TypeEntretien, 'typeEntretien')
    insertionDonneesTables(Necessite, 'Necessite')
    insertionDonneesTables(Machine, 'Machine')
    insertionDonneesTables(Organisation, 'Organisation')
    insertionDonneesTables(Ordre, 'Ordre')
    insertionDonneesTables(Club, 'Club')
def suppressionToutesDonneesTables() :
    effacerDonnesTables('Legume')
    effacerDonnesTables('Ingredient')
    effacerDonnesTables('Sauce')
    effacerDonnesTables('Est_constitue')
    effacerDonnesTables('Plat')
    effacerDonnesTables('Contient')
    effacerDonnesTables('Constitue')
    effacerDonnesTables('Modele')
    effacerDonnesTables('NomMachine')
    effacerDonnesTables('TypeEntretien')
    effacerDonnesTables('Necessite')
    effacerDonnesTables('Machine')
    effacerDonnesTables('Organisation')
    effacerDonnesTables('Ordre')
    effacerDonnesTables('Club')

def test():
    dropToutesLesTables()
    createToutesLesTables()
    ajouteToutesDonneesTables()
#test()


#dropToutesLesTables()
#createToutesLesTables()
#suppressionToutesDonneesTables()
#ajouteToutesDonneesTables()
#suppressionToutesDonneesTables()
#ajouteToutesDonneesTables()
#print(cursor.execute("SELECT * FROM Aliment").fetchall())



#insertionDonneesTables(list_test,'Aliment')

#effacerContenuDuFichier('insertion_donneesAliment.txt')
#effacerDonnesTables('Aliment')

#dropToutesLesTables()
#createToutesLesTables()
#createInsertionFiles()

connection.commit()
connection.close()
