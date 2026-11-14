import funciones as f
#La libreria rich permite agregar color y estilo a la consola
from rich.console import Console
console = Console()

lista_paises :list= f.leer_csv()

if __name__=="__main__":
    parar = False
    while not parar:
        opcion = f.main()#Devuelve un texto donde el primer caracter es un numero

        #opcion[0] hace referencia al primer caracter de la variable
        #ya que cada opcion de main() tiene como primer caracter un numero del 1 al 7
        if opcion[0] == "1":
            #[i cyan] define donde se comienza a pintar el texto y [/i cyan] define donde se terminan de pintar
            #Todo texto que este por fuera aparece normal, a menos que se defina un color por defecto con "style="
            nombre = console.input("[i cyan]Ingrese el nombre del país:[/i cyan] ").strip().capitalize()
            nombre = f.validar_string(nombre)
            try:
                #Aca se valida que el país no exista para saber si seguir o volver al inicio indicando que el pais ya existe
                if f.validar_pais_existente(lista_paises, nombre):
                    #Si el país existe, devolvemos al inicio
                    console.print("[bold red]Error: País existente[bold red]")
                    f.limpiar_consola()
            except NameError:
                #Si la funcion lanza error, significa que el pais no existe por lo que la logica de la opcion esta bien
                lista_paises.append(f.agregar_pais(nombre))
                console.print("¡País agregado exitosamente!", style="bold green")
                f.actualizar_csv(lista_paises)
                f.limpiar_consola() 

        elif opcion[0] == "2":
            pais = console.input("[i cyan]Ingrese el pais:[/i cyan]: ").capitalize().strip()
            #Aca es al reves, si la funcion validar_pais_existente lanza error, significa que no hay pais
            #al cual actualizarle datos
            try:
                if f.validar_pais_existente(lista_paises, pais):
                    f.actualizar_pais(lista_paises, pais)
                    f.limpiar_consola()
            except NameError:
                console.print("Error: País inexistente", style= "bold red")
                f.limpiar_consola()
            else:
                f.actualizar_csv(lista_paises)

        elif opcion[0] == "3":
            pais_buscar = console.input("[i cyan]Ingrese el pais a buscar:[/i cyan] ").strip().capitalize()
            try:
                pais = f.buscar_pais(lista_paises, pais_buscar)
                console.print(f"""
[i cyan]Nombre:[/i cyan] {pais["nombre"]}
[i cyan]Poblacion:[/i cyan] {pais["poblacion"]}
[i cyan]Superficie:[/i cyan] {pais["superficie"]}
[i cyan]Continente:[/i cyan] {pais["continente"]}
""", style= "bold magenta")
                f.limpiar_consola()
#Todo lo que esta por dentro de los corchetes [i cyan]-[/i cyan] estaran pintados de cian, y los 
#que esten por fuera de los corchetes, aparecen pintados ya que "style=" agrega color a todo texto
#que este por fuera de esos corchetes
            except NameError:
                console.print("Error: País inexistente", style= "bold red")
                f.limpiar_consola()
    
        elif opcion[0] == "4":
            opcion = f.menu_filtrar_paises()
            if opcion == "> Continente":
                paises = f.paises_por_continente(lista_paises)
                #k es la clave del diccionario y v es el valor, en este caso una lista
                for k, v in paises.items():
                    console.print(f"{k}:", style="bold magenta")
                    #Como "v" es una lista, la recorremos para imprimir sus valores
                    for i in range(len(v)):
                        console.print(f" > {v[i]}", style="i cyan")
                f.limpiar_consola()

            elif opcion == "> Poblacion":
                paises = f.paises_por_pob_o_sup(lista_paises, "poblacion")
                for k, v in paises.items():
                    console.print(f"{k}:", style="bold magenta")
                    for i in range(len(v)):
                        console.print(f" > {v[i]}", style="i cyan")
                f.limpiar_consola()
            else:
                paises = f.paises_por_pob_o_sup(lista_paises, "superficie")
                for k, v in paises.items():
                    console.print(f"{k}:", style="bold magenta")
                    for i in range(len(v)):
                        console.print(f" > {v[i]}", style="i cyan")
                f.limpiar_consola()

        elif opcion[0] == "5":
            pass
        elif opcion[0] == "6":
            pass
        elif opcion[0] == "7":
            parar = True