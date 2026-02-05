import csv

import os
import json
import requests
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

def buscar():
    searchterm = str(input("\n Introdueix la paraula clau a buscar...\n"))
    api_url = 'https://api.spoonacular.com/recipes/complexSearch'
    api_key = 'e951ca95e5db481588ad68a3cf9457cd'

    # -- Codi corregit gràcies a Gemini AI --
    params = {
        'apiKey': api_key,
        'query': searchterm,
        'number': 10       # -- Límit de resultats --
    }

    try:
        req = requests.get(api_url, params=params)
        
        if req.status_code == 200:
            print("\nConnexió realitzada amb èxit. \n")
            data = req.json() 
            
            print("\n-- Llista de Receptes --\n")
            counter = int(0)
            for recipe in data['results']:
                counter = counter + 1
                print(f"{counter}. {recipe['title']}")
            selectrecipe = int(input("\nSeleccione el numero de recepta...\n"))
            params = {
                'apiKey' : api_key,
                'query': searchterm,
                'number' : 1
            }
            req = requests.get(api_url, params=params)
            for recipe in data['results']:
                print(recipe[]) # -- Corregir busqueda individual --
            

        else:
            print(f"\nError en la connexió. Status Code: {req.status_code}")
            print(req.text)

    except Exception as errcon:
        print(f"Error en la connexió, codi d'error: {errcon}")





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

    if select == 3:
        buscar()

    if select == 4:
        menu = False
        print("\n Eixint del programa... Gràcies.\n")