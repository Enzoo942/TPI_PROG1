lista_paises :list= [{"nombre":"Argentina",
                      "superficie":5000000,
                      "poblacion":5000000,
                      "continente":"America"},
                    {"nombre":"España",
                      "superficie":4000000,
                      "poblacion":2300000,
                      "continente":"Europa"},
                    {"nombre":"Rusia",
                      "superficie":56000000,
                      "poblacion":99000000,
                      "continente":"Asia"},
                    {"nombre":"Brasil",
                      "superficie":3500000,
                      "poblacion":2100000,
                      "continente":"America"}]
def validar_string(text:str)->str:
    while not text.isalpha():
        text = input("Error, ingresar solamente letras: ").strip().capitalize()
    return text

def validar_entero(num:str)->int:
    while not num.isdigit():
        num = input("Error, ingresar solo numero entero positivo: ").strip()
    return int(num)

def validar_pais_existente(lista:list, buscar:str)->bool:
    for p in lista:
        if buscar == p["nombre"]:
            return True
    return False

def agregar_pais(pais:str) -> dict:
    superficie = input("Ingrese la superficie del pais: ").strip()
    superficie = validar_entero(superficie)

    poblacion = input("Ingrese la poblacion país: ").strip()
    poblacion = validar_entero(poblacion)

    continente = input("Ingrese el continente del pais: ").strip().capitalize()
    continente = validar_string(continente)
    return {"nombre":pais, "superficie":superficie, "poblacion":poblacion, "continente":continente}



if __name__=="__main__":
    parar = False
    while not parar:
        opcion = input("1- Agregar pais \n2- Contar paises \n3- Salir \nSeleccionar opción: ")
        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del país: ").strip().capitalize()
                nombre = validar_string(nombre)
                if validar_pais_existente(lista_paises, nombre):
                    print("Error: País existente")
                    continue
                lista_paises.append(agregar_pais(nombre))
            case "2":
                for pais in lista_paises:
                    print(f"""========================
País: {pais["nombre"]}
Superficie: {pais["superficie"]}
Población: {pais["poblacion"]}
Continente: {pais["continente"]}""")
            case "3":
                parar = True
            case _:
                print("Error: opción inválida")