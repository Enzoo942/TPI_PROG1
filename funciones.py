#La bilbioteca questionary permite realizar un menu mas interactivo y facil de leer
from questionary import select, Style

#rapidfuzz permite la busqueda de nombres por parcialidad
from rapidfuzz import fuzz

#rich permite poner color a la consola y la variablle console permite usar Console de forma mas sencilla
from rich.console import Console
console = Console()

def main() -> str:
    #La siguiente variable define el estilo de cada elemento que querramos editar
    #por ejemplo, dentro de Style hay que dar una lista de tuplas con el formato
    #(elemento, color y estilo) aunque el estilo es opcional
    estilo_menu = Style([
        ("qmark", "fg:#9dafe4 bold"),
        ("question", "fg:#9dafe4 bold"),
        ("pointer", "fg:#6cbfa6"),
        ("highlighted", "fg:#6cbfa6 italic"),
        ("text", "fg:#a8b8d1")])
    #select permite realizar un menu que se controla con las flechas del teclado
    option= select("¿Que vamos a hacer hoy?" ,choices=[
        "1- Agregar País",
        "2- Actualizar poblacion y superficie",
        "3- Buscar país por nombre",
        "4- Filtrar paises",
        "5- Ordenar paises",
        "6- Ver estadisticas",
        "7- Salir"
        ], style= estilo_menu).ask()
    return option

def validar_string(text:str)->str:
    while not text.isalpha():
        text = console.input("[bold red]Error, ingresar solamente letras:[/bold red] ").strip().capitalize()
    return text

def validar_entero(num:str)->int:
    while not num.isdigit():
        num = console.input("[bold red]Error, ingresar solo numero entero positivo:[/bold red] ").strip()
    return int(num)

def validar_pais_existente(lista:list, buscar:str)->bool:
    for p in lista:
        #fuzz.partialratio devuelve un numero flotante que indica el porcentaje de igualdad
        #entre la variable buscar y la clave p["nombre"]
        if fuzz.partial_ratio(buscar, p["nombre"]) >= 75:
            #coloco 75 porque por ejemplo Roma tiene 4 letras, y con solo fallar una, daria 75%
            return True
    raise NameError

def agregar_pais(pais:str) -> dict:
    superficie = console.input("[i cyan]Ingrese la superficie del pais:[/i cyan] ").strip()
    superficie = validar_entero(superficie)

    poblacion = console.input("[i cyan]Ingrese la poblacion país:[/i cyan] ").strip()
    poblacion = validar_entero(poblacion)

    continente = console.input("[i cyan]Ingrese el continente del pais:[/i cyan] ").strip().capitalize()
    continente = validar_string(continente)
    return {"nombre":pais, "superficie":superficie, "poblacion":poblacion, "continente":continente}

def buscar_pais(lista:list, pais:str) -> dict:
    for i in lista:
        if fuzz.partial_ratio(i["nombre"], pais) >= 75:
            return i
    raise NameError

def actualizar_pais (lista:list, pais:str) -> None:
    pais = buscar_pais(lista, pais)
    superficie_nueva = validar_entero(console.input("[i cyan]Ingrese la nueva superficie del pais:[i cyan] "))
    poblacion_nueva = validar_entero(console.input("[i cyan]Ingrese la nueva población del pais:[i cyan] "))
    pais["superficie"] = superficie_nueva
    pais["poblacion"] = poblacion_nueva

def menu_filtrar_paises() -> str:
    estilo_menu = Style([
        ("qmark", "fg:#421341 bold"),
        ("question", "fg:#421341 bold"),
        ("pointer", "fg:#3F709D"),
        ("highlighted", "fg:#3F709D italic"),
        ("text", "fg:#421341")])

    opcion = select("Desea filtrar paises por:", choices=[
        "> Continente", 
        "> Poblacion",
        "> Superficie"
    ], style= estilo_menu).ask()
    return opcion

def paises_por_continente (lista:list) -> dict:
    paises = dict()
    for pais in lista:
        if pais["continente"] not in paises:
            paises[pais["continente"]] = [pais["nombre"]]
        else:
            paises[pais["continente"]].append(pais["nombre"])
    return paises

if __name__=="__main__":
    print(agregar_pais("Europa"))
    main()