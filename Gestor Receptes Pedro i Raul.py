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

def llegir():
    print("\nW.I.P...\n") # Acabar funció llegir


# -- Cos principal del codi --

try:
    checkpath = os.path.exists(f"{directory}/Receptes")
    if checkpath == False:
        print("\nCreant carpeta 'Receptes'...\n")
        os.mkdir(f"{directory}/Receptes")

except Exception as errdir:
    print(f"Error de directori. Tracte de solucionar-lo manualment. ERROR CODE: {errdir} ")

print("\n--GESTOR DE RECEPTES--\n\n 1. Afegir Recepta 2. LLegir Receptes 3. Consultar en Web")
select = int(input("\nSeleccione una opció i polse [ENTER]\n"))

if select == 1:
    afegir()

if select == 2:
    llegir()