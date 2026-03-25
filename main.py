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
    f = open('requetes/insertion_donnees' + nom_table + '.txt', 'a')
    for i in donnees :
        sql="INSERT INTO " + nom_table + " VALUES("
        for j in i.values() :
            sql+=str(j)+","
        sql = sql[:-1]
        sql+=")"
        cursor.execute(sql)
        f.write(sql+';\n')
    f.close()
def effacerContenuDuFichier(fiename) :
    file = open('requetes/' + fiename, 'w')
    file.close()
#effacerDonnesTables('Aliment')
#insertionDonneesTables(list_test,'Aliment')
#cursor = connection.cursor()
#effacerContenuDuFichier('insertion_donneesAliment.txt')
#effacerDonnesTables('Aliment')
#print(cursor.execute("SELECT * FROM Aliment").fetchall())

#createToutesLesTables()
#createInsertionFiles()

#connection.commit()
connection.close()
