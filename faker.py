from faker import Faker

fake = Faker()

table_tenrac = []
nom_reunion = ['Assemblée', 'Conseil Kebab', 'Réunion Tenrac', 'Comité Broche', 'Réunion Grill', 'Assise Döner', 'Conclave Gyros', 'Réunion Spit', 'Conseil Roti', 'Réunion Chef', 'Assemblée Spéciale', 'Comité Kebab', 'Réunion Ordre', 'Conseil Maître', 'Réunion Club', 'Assise Viande', 'Conclave Chef', 'Réunion Sauce', 'Conseil Grillade', 'Réunion Dégustation']
nom_repas = ['Kebab Royal', 'Assiette Döner', 'Galette Poulet', 'Sandwich Mixte', 'Kebab Classique', 'Assiette Gyros', 'Kebab Fromage', 'Assiette Poulet', 'Sandwich Döner', 'Kebab Maison', 'Galette Agneau', 'Assiette Mixte', 'Kebab Spécial', 'Sandwich Royal', 'Galette Fromage', 'Assiette Boeuf', 'Kebab Poulet', 'Sandwich Agneau', 'Assiette Royale', 'Kebab Légumes']
nom_club = ['Club Kebab', 'Le Cercle du Döner', 'Les Amis du Gyros', 'La Confrérie du Kebab', 'Club de la Broche', 'L\'Alliance du Spit', 'Le Pavillon du Grill', 'Les Maîtres du Roti', 'La Table d\'Or', 'Le Comptoir du Kebab', 'Le Salon du Méchoui', 'Les Compagnons du Döner', 'L\'Ordre du Barbecue', 'La Grande Confrérie', 'Le Club des Rotisseurs', 'Les Gourmets du Kebab', 'La Société du Gyros', 'Les Enthousiastes du Döner', 'Le Cercle des Grillades', 'La Maison du Kebab', 'L\'Académie du Spit', 'Les Souverains du Döner', 'Le Temple du Kebab', 'La Légende du Gyros', 'Les Chevaliers du Grill', 'La Confrérie des Rotis', 'Le Clube dos Kebabs', 'Il Circolo del Döner', 'Der Kebab Klub', 'The Kebab Society', 'Les Ambassadeurs', 'Les Émissaires', 'Les Connaisseurs', 'Les Dévoreurs', 'Les Dégustateurs', 'Les Explorateurs', 'Les Pèlerins', 'Les Gardiens', 'Les Veilleurs', 'Les Sentinelles', 'Les Fidèles', 'Les Passionnés', 'Les Érudits', 'Les Sages', 'Les Princes', 'Les Seigneurs', 'Les Barons', 'Les Ducs', 'Les Vicomtes', 'Les Marquis']
nom_territoire = ['Ile-de-France', 'Provence-Alpes-Côte', 'Nouvelle-Aquitaine', 'Auvergne-Rhône-Alpes', 'Hauts-de-France', 'Normandie', 'Bretagne', 'Grand Est', 'Pays de la Loire', 'Occitanie', 'Bourgogne-Comté', 'Centre-Val-Loire', 'Corse']
nom_ordre = ['Ordre du Kebab', 'Ordre de la Broche', 'Ordre du Gyros', 'Ordre du Döner', 'Ordre de la Grillade', 'Ordre du Rotisseur', 'Ordre du Spit', 'Ordre du Méchoui', 'Ordre de la Viande', 'Ordre du Barbecue']
nom_entretien = ['Nettoyage', 'Dégraissage', 'Vérification', 'Lubrification', 'Révision', 'Remplacement', 'Calibration', 'Inspection']
nom_machine = ['Tornado Grill', 'KebabMaster 3000', 'Döner Chef Pro', 'Gyro Spit', 'Vertical Broiler', 'AutoRotisserie 5000', 'KebabTech Turbo', 'Pro Grill Master', 'Doner King', 'Spitfire Grill']
grades_inf_contraintes = ['Affilié', 'Symphatisant', 'Adhérent']
grades_inf_contraintes = ['Affilié', 'Symphatisant', 'Adhérent']
grades_sup_contraintes = ['Chevalier', 'Dame', 'Grand Chevalier', 'Haute Dame', 'Commandeur', 'Grande Croix']
rang_contraintes = ['Novice', 'Compagnon']
titre_contraintes = ['Philanthrope', 'Protecteur', 'Honorable']
dignite_contraintes = ['Maître', 'Grand Chancelier', 'Grand Maître']
nom_aliments_contraintes = ['Pomme', 'Carotte', 'Salade', 'Tomate', 'Oignon']
nom_sauce = ['Samourai', 'Blanche', 'algérienne', 'MaxiGras', 'HuileDeMoteur']
nom_legume = ['Salade', 'Tomate', 'Oignon', 'Concombre', 'Chou', 'Poivron', 'Cornichon']
nom_ingredient = ['Tomate', 'Oignon', 'Ail', 'Carotte', 'Pomme de terre', 'Courgette', 'Aubergine', 'Poivron', 'Champignon']
nom_modele = ['KebabMaster Pro', 'Tornado Grill 3000', 'DönerChef Auto', 'SpitRoast X1', 'GyroStar Plus', 'KebabTech Vert', 'ProRotisserie 5000']
lst=[]
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
    for i in range(1,10)
    ]
    
lst = [[i["CodePerso"],i["NomTenrac"]] for i in extension_tenrac]

print(lst)

for i in range(1,10) :
    extension_aliment = {
        "idA : ": i,
        "nomAliment": fake.random_element(elements=nom_aliments_contraintes),
        }
    #print(extension_aliment)
    
for i in range(1,10) :
    extension_sauce = {
        "idS : ": i,
        "nomSauce : " : fake.random_element(elements=nom_sauce)
        }
    #print(extension_sauce)

for i in range(1,10) :
    extension_ingredient = {
        "idI : ": i,
        "nomIngredient : " : fake.random_element(elements=nom_ingredient)
        }
    #print(extension_ingredient)
    
for i in range(1,10) :
    extension_modele = {
        "idMo : ": i,
        "nomModele : " : fake.random_element(elements=nom_modele)
        }
    #print(extension_modele)
    
for i in range(1,10) :
    extension_titre = {
        "idT : ": i,
        "nomTitre : " : fake.random_element(elements=titre_contraintes)
        }
    #print(extension_titre)

for i in range(1,10) :
    extension_dignite = {
        "idD : ": i,
        "nomDignite : " : fake.random_element(elements=dignite_contraintes)
        }
    #print(extension_dignite)

for i in range(1,10) :
    extension_rang = {
        "idRa : ": i,
        "nomRang : " : fake.random_element(elements=rang_contraintes)
        }
    #print(extension_rang)    

for i in range(1,10) :
    extension_legume = {
        "idL : ": i,
        "nomLegume : " : fake.random_element(elements=nom_legume)
        }
    #print(extension_legume)   

for i in range(1,10) :
    extension_organisation = {
        "idO : ": i
        }
    #print(extension_organisation)  

for i in range(1,10) :
    extension_organisme = {
        "idOR : ": i,
        "numeroSiret" : fake.unique.random_int(1000, 9999)
        #raisonSociale  Faut faire deux listes de nom et essayer de les assembler en combinaison random pour simuler des noms d'entreprise
        }
    #print(extension_organisme)

for i in range(1,10) :
    extension_grade = {
        "idG : ": i,
        }
    #print(extension_grade)

for i in range(1,10) :
    extension_pasTresHautGradee = {
        "idG : ": i,
        "nomDeGrade : " :fake.random_element(elements=grades_inf_contraintes)
        }
    #print(extension_pasTresHautGradee)

for i in range(1,10) :
    extension_tresHautGradee = {
        "idG : ": i,
        "nomDeGrade : " :fake.random_element(elements=grades_sup_contraintes)
        # FOREIGN KEY(idG) REFERENCES Grade(idG)
        }
    #print(extension_tresHautGradee)

for i in range(1,10) :
    extension_nomMachine = {
        "idNM : ": i,
        "nomMachine : " :fake.random_element(elements=nom_machine)
        }
    #print(extension_nomMachine)

for i in range(1,10) :
    extension_typeEntretien = {
        "idE : ": i,
        "typeEntretien : " :fake.random_element(elements=nom_entretien)
        }
    #print(extension_typeEntretien)

for i in range(1,10) :
    extension_ordre = {
        "idO : ": i,
        "typeEntretien : " :fake.random_element(elements=nom_ordre),
        "Territoire : ": fake.random_element(elements=nom_territoire)
        # FOREIGN KEY(idO) REFERENCES Organisation(idO)
        }
    #print(extension_ordre)

for i in range(1,10) :
    extension_plat = {
        "idP : ": i,
        "nomPlat : " :fake.random_element(elements=nom_ordre)
        # FOREIGN KEY(idL) REFERENCES Legume(idL)
        }
    #print(extension_plat)
    
for i in range(1,10) :
    extension_adressePartenaire = {
        "idA : ": i,
        "adressePart : " :fake.address("|n",", ")
        # FOREIGN KEY(idO) REFERENCES Ordre(idO)
        }
    #print(extension_adressePartenaire)

for i in range(1,10) :
    extension_club = {
        "idO_1 : ": i,
        "nomClub : " :fake.random_element(elements=nom_club)
        # FOREIGN KEY(idO) REFERENCES Ordre(idO)
        }
    #print(extension_club)

for i in range(1,10) :
    extension_machine = {
        "idM : ": i,
        # FOREIGN KEY(idNM) REFERENCES NomMachine(idNM)
        #  FOREIGN KEY(idMo) REFERENCES Modele(idMo)
        }
    #print(extension_machine)

for i in range(1,10) :
    extension_repas = {
        "idR : ": i,
        "intitule : ": fake.random_element(elements=nom_repas)
        # FOREIGN KEY(idNM) REFERENCES NomMachine(idNM)
        #  FOREIGN KEY(idMo) REFERENCES Modele(idMo)
        }
    #print(extension_repas)

for i in range(1,10) :
    extension_compose = {
        "idP : ": i
        # FOREIGN KEY(idP) REFERENCES Plat(idP),
        # FOREIGN KEY(idR) REFERENCES Repas(idR)
        }
    #print(extension_compose)

for i in range(1,10) :
    extension_constitue = {
        #PRIMARY KEY(idP, idA),
         #FOREIGN KEY(idP) REFERENCES Plat(idP),
        #FOREIGN KEY(idA) REFERENCES Aliment(idA)
        }
    #print(extension_constitue)

for i in range(1,10) :
    extension_est_constitue = {
        #PRIMARY KEY(idS, idI)
        # FOREIGN KEY(idP) REFERENCES Plat(idP),
        # FOREIGN KEY(idR) REFERENCES Repas(idR)
        }
    #print(extension_est_constitue)

for i in range(1,10) :
    extension_contient = {
        #PRIMARY KEY(idP, idS),
        #FOREIGN KEY(idP) REFERENCES Plat(idP),
        #FOREIGN KEY(idS) REFERENCES Sauce(idS)
        }
    #print(extension_contient)

for i in range(1,10) :
    extension_necessite = {
         #PRIMARY KEY(idMo, idNM, idE),
         #FOREIGN KEY(idMo) REFERENCES Modele(idMo),
         #FOREIGN KEY(idNM) REFERENCES NomMachine(idNM),
         #FOREIGN KEY(idE) REFERENCES TypeEntretien(idE)
        }
    #print(extension_necessite)

for i in range(1,10) :
    extension_tenrac = {
        "idT : ": i,
        "nomTenrac : ": fake.name(),
        "courrier : ": fake.free_email(),
        "telephone : ": fake.phone_number(),
        "adressePostal : ": fake.address("|n",", ")
        #idG NUMBER(6, 1) NOT NULL,
        #idT_1 NUMBER(6, 1),
        #idD NUMBER(6, 1),
        #idRa NUMBER(6, 1),
         #PRIMARY KEY(idO, idOr, idT),
         #FOREIGN KEY(idO) REFERENCES Organisation(idO),
         #FOREIGN KEY(idOr) REFERENCES Organisme(idOr),
         #FOREIGN KEY(idG) REFERENCES Grade(idG),
         #FOREIGN KEY(idT_1) REFERENCES Titre(idT),
         #FOREIGN KEY(idD) REFERENCES Dignite(idD),
         #FOREIGN KEY(idRa) REFERENCES Rang(idRa)
        }
    #print(extension_tenrac)

for i in range(1,10) :
    extension_reunion = {
         "idR : ": i,
         "date_ : ": fake.date(),
         "nomReunion : ": fake.random_element(elements=nom_reunion)
         #idO NUMBER(6, 1) NOT NULL,
         #idOr NUMBER(6, 1) NOT NULL,
         #idT NUMBER(6, 1) NOT NULL,
         #idA NUMBER(6, 1) NOT NULL,
         #PRIMARY KEY(idR, date_),
         #FOREIGN KEY(idO, idOr, idT) REFERENCES Tenrac(idO, idOr, idT),
         #FOREIGN KEY(idA) REFERENCES AdressePartenaire(idA)
        }
    #print(extension_reunion)

for i in range(1,10) :
    extension_assiste = {
         #idO NUMBER(6, 1),
   #idOr NUMBER(6, 1),
   #idT NUMBER(6, 1),
   #idR NUMBER(6, 1),
   #date_ DATE,
   #PRIMARY KEY(idO, idOr, idT, idR, date_),
   #FOREIGN KEY(idO, idOr, idT) REFERENCES Tenrac(idO, idOr, idT),
   #FOREIGN KEY(idR, date_) REFERENCES Reunion(idR, date_)
        }
    #print(extension_assiste)

for i in range(1,10) :
    extension_organise = {
         #PRIMARY KEY(idMo, idNM, idE),
         #FOREIGN KEY(idMo) REFERENCES Modele(idMo),
         #FOREIGN KEY(idNM) REFERENCES NomMachine(idNM),
         #FOREIGN KEY(idE) REFERENCES TypeEntretien(idE)
        }
    #print(extension_organise)

for i in range(1,10) :
    extension_evite = {
         #PRIMARY KEY(idMo, idNM, idE),
         #FOREIGN KEY(idMo) REFERENCES Modele(idMo),
         #FOREIGN KEY(idNM) REFERENCES NomMachine(idNM),
         #FOREIGN KEY(idE) REFERENCES TypeEntretien(idE)
        }
    #print(extension_organise)

