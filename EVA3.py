from DAO import DAO
from os import system

dao = DAO()

def menu():
    system('cls')
    print('---- MENU POKEDEX MONGODB ----')
    print('1.- REGISTRAR POKÉMON')
    print('2.- MODIFICAR POKÉMON')
    print('3.- ELIMINAR POKÉMON')
    print('4.- LISTAR POKÉMONS')
    print('5.- BUSCAR POKÉMON X NOMBRE (EXACTA)')
    print('6.- BUSCAR POKÉMON X NOMBRE (COMIENCE)')
    print('7.- BUSCAR POKÉMON X NOMBRE (CONTIENE)')
    print('8.- BUSCAR POKÉMON X NOMBRE (TERMINE)')
    print('9.- BUSCAR X ESTADÍSTICA Y RANGO (ENTRE DOS VALORES)')
    print('10.- BUSCAR X ESTADÍSTICA Y CONDICIÓN (MAYOR / MENOR / IGUAL)')
    print('11.- SALIR')
    
    try:
        op = int(input('INGRESE OPCIÓN: '))
        assert 1 <= op <= 11, "Opción fuera de rango."
    except (ValueError, AssertionError):
        print('¡Error en la opción ingresada!')
        system('pause')
        return menu()

    if op == 1: registrar()
    elif op == 2: modificar()
    elif op == 3: eliminar()
    elif op == 4: listar()
    elif op == 5: buscarExacta()
    elif op == 6: buscarComience()
    elif op == 7: buscarContiene()
    elif op == 8: buscarTermine()
    elif op == 9: buscarPorEstadisticaRango()
    elif op == 10: buscarPorEstadisticaCondicion()
    elif op == 11: salir()

def seleccionar_atributo():
    print('Seleccione la estadística:')
    print('1.- Vida (HP)\n2.- Ataque (ATK)\n3.- Defensa (DEF)\n4.- Velocidad (SPD)')
    while True:
        try:
            op_stat = int(input('Ingrese opción (1-4): '))
            assert 1 <= op_stat <= 4
            return ["Vida", "Ataque", "Defensa", "Velocidad"][op_stat - 1]
        except (ValueError, AssertionError):
            print("¡Error! Ingrese una opción válida (1-4).")

def registrar():
    system('cls')
    print('--- REGISTRO DE POKÉMON ---')
    
    while True:
        try:
            id = input('INGRESE NÚMERO POKEDEX (ID): ').strip()
            assert id, "El ID no puede estar vacío."
            nom = input('INGRESE NOMBRE: ').strip()
            assert nom, "El nombre no puede estar vacío."
            tipo = input('INGRESE TIPO (ej: Fuego): ').strip()
            assert tipo, "El tipo no puede estar vacío."
            break
        except AssertionError as e:
            print(f"¡Error! {e}")
            
    print('\n-- REGISTRO DE HABILIDAD --')
    while True:
        try:
            hab_nombre = input('Nombre de la Habilidad: ').strip()
            assert hab_nombre, "La habilidad no puede estar vacía."
            hab_tipo = input('¿Es Oculta? (Si/No): ').strip().upper()
            assert hab_tipo in ['SI', 'S', 'NO', 'N'], "Debe responder SI o NO."
            hab_tipo = "Si" if hab_tipo in ['SI', 'S'] else "No"
            break
        except AssertionError as e:
            print(f"¡Error! {e}")
            
    print('\n-- REGISTRO DE ESTADÍSTICAS BASE --')
    while True:
        try:
            stat_hp = int(input('Puntos de Vida (HP): '))
            stat_atk = int(input('Puntos de Ataque (ATK): '))
            stat_def = int(input('Puntos de Defensa (DEF): '))
            stat_spd = int(input('Puntos de Velocidad (SPD): '))
            assert stat_hp >= 0 and stat_atk >= 0 and stat_def >= 0 and stat_spd >= 0, "No se permiten valores negativos."
            break
        except ValueError:
            print("¡Error! Ingrese solo números enteros para las estadísticas.")
        except AssertionError as e:
            print(f"¡Error! {e}")
            
    datos = {
        '_id': id, 'nombre': nom, 'tipo': tipo,
        'habilidades': [{"nombre_hab": hab_nombre, "tipo_hab": hab_tipo}],
        'estadisticas': [
            {"stat_name": "Vida", "valor": stat_hp},
            {"stat_name": "Ataque", "valor": stat_atk},
            {"stat_name": "Defensa", "valor": stat_def},
            {"stat_name": "Velocidad", "valor": stat_spd}
        ]
    }
    r = dao.registrar(datos)
    print(f"\nPokémon registrado correctamente con la ID: {r}")
    system('pause')
    menu()
    
def modificar():
    system('cls')
    print('---- MODIFICAR POKÉMON ----')
    while True:
        try:
            id = input('INGRESE ID DEL POKÉMON A MODIFICAR: ').strip()
            assert id, "El ID no puede estar vacío."
            nom = input('INGRESE NUEVO NOMBRE: ').strip()
            assert nom, "El nombre no puede estar vacío."
            tipo = input('INGRESE NUEVO TIPO: ').strip()
            assert tipo, "El tipo no puede estar vacío."
            break
        except AssertionError as e:
            print(f"¡Error! {e}")
    
    print('\n-- ACTUALIZAR HABILIDAD --')
    while True:
        try:
            hab_nombre = input('Nuevo Nombre de Habilidad: ').strip()
            assert hab_nombre, "La habilidad no puede estar vacía."
            hab_tipo = input('¿Es Oculta? (Si/No): ').strip().upper()
            assert hab_tipo in ['SI', 'S', 'NO', 'N'], "Debe responder SI o NO."
            hab_tipo = "Si" if hab_tipo in ['SI', 'S'] else "No"
            break
        except AssertionError as e:
            print(f"¡Error! {e}")
    
    print('\n-- ACTUALIZAR ESTADÍSTICAS --')
    while True:
        try:
            stat_hp = int(input('Nuevo valor de Vida (HP): '))
            stat_atk = int(input('Nuevo valor de Ataque (ATK): '))
            stat_def = int(input('Nuevo valor de Defensa (DEF): '))
            stat_spd = int(input('Nuevo valor de Velocidad (SPD): '))
            assert stat_hp >= 0 and stat_atk >= 0 and stat_def >= 0 and stat_spd >= 0, "No se permiten valores negativos."
            break
        except ValueError:
            print("¡Error! Ingrese solo números enteros para las estadísticas.")
        except AssertionError as e:
            print(f"¡Error! {e}")
            
    datos = {
        'nombre': nom, 'tipo': tipo,
        'habilidades': [{"nombre_hab": hab_nombre, "tipo_hab": hab_tipo}],
        'estadisticas': [
            {"stat_name": "Vida", "valor": stat_hp},
            {"stat_name": "Ataque", "valor": stat_atk},
            {"stat_name": "Defensa", "valor": stat_def},
            {"stat_name": "Velocidad", "valor": stat_spd}
        ]
    }
    r = dao.modificar(id, datos)
    print("\n¡POKÉMON MODIFICADO!" if r == 1 else "\n¡ERROR O SIN CAMBIOS AL MODIFICAR!")
    system('pause')
    menu()
    
def eliminar():
    system('cls')
    print('---- ELIMINAR POKÉMON ----')
    id = input('INGRESE ID DEL POKÉMON: ').strip()
    r = dao.eliminar(id)
    print("¡POKÉMON ELIMINADO!" if r == 1 else "¡ERROR AL ELIMINAR!")
    system('pause')
    menu()
    
def mostrar_formato_pokemon(listado):
    cantidad = 0
    for doc in listado:
        cantidad += 1
        print(f"ID POKEDEX: {doc['_id']} | NOMBRE: {doc['nombre']} | TIPO: {doc['tipo']}")
        print("HABILIDADES:")
        for hab in doc.get('habilidades', []):
            print(f"  - {hab['nombre_hab']} (Oculta: {hab['tipo_hab']})")
        print("ESTADÍSTICAS BASE:")
        stats = [f"{st['stat_name']}: {st['valor']}" for st in doc.get('estadisticas', [])]
        print(f"  { ' | '.join(stats) }")
        print('-----------------------------------------------------------------')
    if cantidad == 0: print("No se encontraron registros.")

def listar():
    system('cls')
    print('---- LISTADO GENERAL DE LA POKEDEX ----')
    mostrar_formato_pokemon(dao.listar({}))
    system('pause')
    menu()
    
def buscarExacta():
    system('cls')
    nom = input('INGRESE NOMBRE (EXACTA): ').strip()
    mostrar_formato_pokemon(dao.listar({"nombre": {"$regex": f"^{nom}$", "$options": 'i'}}))
    system('pause')
    menu()
    
def buscarComience():
    system('cls')
    nom = input('INGRESE NOMBRE (COMIENCE): ').strip()
    mostrar_formato_pokemon(dao.listar({"nombre": {"$regex": f"^{nom}", "$options": 'i'}}))
    system('pause')
    menu()

def buscarContiene():
    system('cls')
    nom = input('INGRESE NOMBRE (CONTIENE): ').strip()
    mostrar_formato_pokemon(dao.listar({"nombre": {"$regex": f"{nom}", "$options": 'i'}}))
    system('pause')
    menu()
    
def buscarTermine():
    system('cls')
    nom = input('INGRESE NOMBRE (TERMINE): ').strip()
    mostrar_formato_pokemon(dao.listar({"nombre": {"$regex": f"{nom}$", "$options": 'i'}}))
    system('pause')
    menu()
    
def buscarPorEstadisticaRango():
    system('cls')
    print('---- BUSCAR POKÉMON POR ESTADÍSTICA Y RANGO ----')
    stat_nombre = seleccionar_atributo()
    print(f'\n--- Buscando por {stat_nombre} ---')
    while True:
        try:
            val_min = int(input('Ingrese el valor MÍNIMO: '))
            val_max = int(input('Ingrese el valor MÁXIMO: '))
            assert val_min <= val_max, "El mínimo no puede ser mayor que el máximo."
            break
        except ValueError: print("¡Error! Ingrese números válidos.")
        except AssertionError as e: print(f"¡Error! {e}")
        
    condicion = {"estadisticas": {"$elemMatch": {"stat_name": stat_nombre, "valor": {"$gte": val_min, "$lte": val_max}}}}
    mostrar_formato_pokemon(dao.listar(condicion))
    system('pause')
    menu()

def buscarPorEstadisticaCondicion():
    system('cls')
    print('---- BUSCAR POKÉMON POR ESTADÍSTICA Y CONDICIÓN ----')
    stat_nombre = seleccionar_atributo()
    print('\n1.- (>=) | 2.- (<=) | 3.- (=)')
    while True:
        try:
            op_comp = int(input('Ingrese opción (1-3): '))
            assert 1 <= op_comp <= 3
            valor = int(input(f'Ingrese el valor para {stat_nombre}: '))
            break
        except (ValueError, AssertionError): print("¡Error! Entrada inválida.")
        
    operador = ["$gte", "$lte", "$eq"][op_comp - 1]
    condicion = {"estadisticas": {"$elemMatch": {"stat_name": stat_nombre, "valor": {operador: valor}}}}
    mostrar_formato_pokemon(dao.listar(condicion))
    system('pause')
    menu()
    
def salir():
    dao.cerrarConexion()
    print('¡Adios Entrenador!')
    
menu()