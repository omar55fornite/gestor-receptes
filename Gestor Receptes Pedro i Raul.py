import csv
import os
import json
directory = os.path.dirname(os.path.realpath(__file__))
    

def afegir(): # -- Funció per afegir receptes noves --
    print("\nAfegir receptes...\n")
    
    name = str(input("\nAnomene el fitxer en el que vulgues guardar la recepta, sense incloure la extensió.\n"))
    end = str(input("\nEscriva la extensió sense punt, solament les lletres...\n"))
    if end == "csv":
        with open(f"{directory}/Receptes/{name}.csv", 'a', newline="", encoding="utf-8") as ftxcsv:
            writer = csv.writer(ftxcsv)
            content = str("")
            print("\nEscriva la seua recepta a continuació... Escriva 'fin' al acavar.\n")
            
            while content != "fin":
                content = str(input())

                writer.writerow([f"{content}"])

            print("\nRecepta guardada correctament.\n")
    if end == "txt":
        with open(f"{directory}/Receptes/{name}.txt", 'a') as ftxtxt:
            
            content = str("")
            print("\nEscriva la seua recepta a continuació... Escriva 'fin' al acavar.\n")
            
            while content != "fin":
                content = str(input())

                ftxtxt.write(f"{content}\n")

            print("\nRecepta guardada correctament.\n")

    if end == "json":
        with open(f"{directory}/Receptes/{name}.json", 'a', newline="", encoding="utf-8") as ftxjson:
            
            content = str("")
            print("\nEscriva la seua recepta a continuació... Escriva 'fin' al acavar.\n")
            
            while content != "fin":
                content = str(input())
                
                contentforwrite =  {"": f"{content}"}

                json.dump(contentforwrite, ftxjson, indent=4)

            print("\nRecepta guardada correctament.\n")

def llegir():  # -- Funcions bàsiques de lectura dels arxius. Error en .json --
    print("\nLlegir receptes...\n") # Acabar funció llegir
    nameinput = str(input("\nEscriva el nom amb extensió d'arxiu de la recepta que vol llegir.\n"))
    check = bool(False)
    extension = str()
    for i in range(0, len(nameinput)):
        if nameinput[i] == ".":
            check = True
        if check == True:
            extension = extension + nameinput[i]
    print(f"\nBuscant l'arxiu {nameinput}...\n")
    try:
        if extension == ".json":
            with open (f"{directory}/Receptes/{nameinput}" , 'r', encoding='utf-8') as arxjson:
                reader = json.load(arxjson)
                print(reader[""])
        elif extension == ".csv":
            with open (f"{directory}/Receptes/{nameinput}", 'r', encoding='utf-8') as arxcsv:
                reader = csv.reader(arxcsv)
                for row in reader:
                    print(row)
        elif extension == ".txt":
            with open (f"{directory}/Receptes/{nameinput}") as arxtxt:
                print(arxtxt.read())
        else:
            print("\nExtensió invàlida...\n")
    except Exception as erread:
        print(f"Error en la lectura... ERROR CODE: {erread}")




# -- Cos principal del codi --

menu = bool(True)

while menu == True:
    try:
        checkpath = os.path.exists(f"{directory}/Receptes")
        if checkpath == False:
            print("\nCreant carpeta 'Receptes'...\n")
            os.mkdir(f"{directory}/Receptes")

    except Exception as errdir:
        print(f"Error de directori. Tracte de solucionar-lo manualment. ERROR CODE: {errdir} ")

    print("\n--GESTOR DE RECEPTES--\n\n 1. Afegir Recepta 2. LLegir Receptes 3. Consultar en Web 4. Eixir del programa")
    select = int(input("\nSeleccione una opció i polse [ENTER]\n"))

    if select == 1:
        afegir()

    if select == 2:
        llegir()

    if select == 4:
        menu = False
        print("\n Eixint del programa... Gràcies.\n")