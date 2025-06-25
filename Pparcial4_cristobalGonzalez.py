sg = 1

compradores = {
    "concepcion": [],
    "muelleBaron": [],
    "muelleVergara": []
}
compradores["Puentealto"] = {} 
stock ={
    "Conce" :500,
    "Puentealto" :1300,
    "muelleBaron" :100,
    "muelleVergara" :50
}


def entrada_conce():
    nombre = input("Nombre del Comprador: ")
    if nombre in compradores["concepcion"]:
        print("El nombre del comprador ya a sido registrado")
        return

    codigo = input("Codigo de Confirmacion: ")
    if len(codigo) >= 6 and  any(c.isupper() for c in codigo) and any(c.isdigit() for c in codigo) and " "not in codigo:
        compradores["concepcion"].append(nombre)
        stock["Conce"] -= 1
        print(f"Entrada registrada stock restante: {stock['Conce']}")
    else:
        print("Codigo Invalido")
        return

def entrada_puentealto():
    nombre = input("Ingrese nombre del comprador: ")
    try:
        cantidad = int(input("Ingrese cantidad de entradas (máx 3 en total): "))
    except:
        print("Cantidad inválida.")
        return
    if cantidad < 1:
        print("Debe ingresar al menos una entrada.")
        return

    entradas_previas = compradores["Puentealto"].get(nombre, 0)
    if entradas_previas + cantidad > 3:
        print(f"{nombre} ya ha comprado {entradas_previas} entradas. No puede exceder 3 en total.")
        return
    if cantidad > stock["Puentealto"]:
        print("No hay suficientes entradas disponibles.")
        return

    compradores["Puentealto"][nombre] = entradas_previas + cantidad
    stock["Puentealto"] -= cantidad
    print(f"Entrada registrada stock restante: {stock['Puentealto']}")

def entrada_BaronValparaiso():
    nombre = input("Ingrese nombre del comprador: ")
    if nombre in compradores["muelleBaron"]:
        print("El nombre ya ha sido registrado.")
        return
    codigo = input("Ingrese código de confirmación: ")
    if codigo == "G":
        compradores["muelleBaron"].append(nombre)
        stock["muelleBaron"] -= 1
        print(f"Entrada registrada stock restante: {stock['muelleBaron']}")
    else:
        print("Código inválido.")
        return


def entrada_VergaraViña():
    nombre = input("Ingrese nombre del comprador: ")
    if nombre in compradores["muelleVergara"]:
        print("El nombre ya ha sido registrado.")
        return

    codigo = input("ingrese tipo de entrada('Sun'o'Ni'):")
    if codigo == "Sun" or codigo == "Ni":
        compradores["muelleVergara"].append(nombre)
        stock["muelleVergara"] -= 1
        print(f"Entrada registrada stock restante: {stock['muelleVergara']}")

def cerrar_programa():
    print("Programa Terminado....")
    sg = 0

while sg == 1:
    print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("1.- Comprar entrada a “los Fortificados” en Concepción.")
    print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
    print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
    print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
    print("5.- Salir.")
    op = int(input("Seleccione una opcion: "))
    if op == 1:
        entrada_conce()
    elif op == 2:
        entrada_puentealto()
    elif op == 3:
        entrada_BaronValparaiso()
    elif op == 4:
        entrada_VergaraViña()
    elif op == 5:
        cerrar_programa()


    


