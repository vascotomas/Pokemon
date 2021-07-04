import pickle,random
class Pokemon:
    def __init__(self):
        self.nombre = ""
        self.ataque = 0
        self.vida = 100
        self.clase = ""
        self.victorias = 0

    def inicializacion(self):
        self.nombre = input("INGRESE EL NOMBRE: ").capitalize()
        self.ataque = int(input("INGRESE EL ATAQUE: "))
        self.clase = input("INGRESE LA CLASE:\nAgua(a): \nFuego(f) \nTierra(t) \nElectricidad(e) \n>>>").lower()
        # Fuego,Agua,Tierra,Electricidad

    def saludar(self):
        if self.clase == "f":
            self.clase = "Fuego"
        elif self.clase == "a":
            self.clase = "Agua"
        elif self.clase == "t":
            self.clase = "Tierra"
        elif self.clase == "e":
            self.clase = "Electricidad"

        print(f"NOMBRE: {self.nombre} - ATAQUE: {self.ataque} - CLASE: {self.clase} - VIDA: {self.vida}")

    def gano(self):
        print(f"{self.nombre} GANO ESTA BATALLA :D !!!")

def guardar(pindex):
    pokemon_obj = open("pokemon_obj", "wb")  # GUARDAMOS ARCHIVO
    pickle.dump(pindex, pokemon_obj)
    pokemon_obj.close()

def crear(pindex):
    while True:
        pok_crear = Pokemon()
        pok_crear.inicializacion()
        pindex.append(pok_crear)
        guardar(pindex)

        select = input("(1) SEGUIR CREANDO (2) TERMINAR PROCESO: ")
        if select == "2":
           # print("\n" * 80)

            return pindex

def listar(pindex):
    print("##################################")
    print("Listado de Pokemones")
    print("##################################")
    totalpk = len(pindex)

    for i in range(totalpk):
        pindex[i].saludar()
        print("NUMERO DE POKEMON:", i + 1)
        print("\n--------------------\n")


def cargadoPok():
    archivoPokemon = open("pokemon_obj", "ab+")
    archivoPokemon.seek(0)

    try:

        pokemon_index_archivo = pickle.load(archivoPokemon)
        print(f"{len(pokemon_index_archivo)} Pokemones cargados exitosamente")

    except EOFError:
        print("No se han cargado Pokemones previos")

    finally:
        archivoPokemon.close()
        del archivoPokemon
        return pokemon_index_archivo

def tirar_dado(num):
    return random.randint(1, num)

def potenciacion(p1, p2):  # AGREGAR MAS POTENCIACIONES ENTRE CLASES
    if p1.clase == "a" and p2.clase == "f":  # agua vs fuego
        potenciacion_p1 = (p1.ataque * 15) / 100
        potenciacion_p2 = 0
        return potenciacion_p1, potenciacion_p2
    elif p2.clase == "a" and p1.clase == "f":
        potenciacion_p2 = (p2.ataque * 15) / 100
        potenciacion_p1 = 0
        return potenciacion_p1, potenciacion_p2
    if p1.clase == "e" and p2.clase == "a":  # electricidad vs agua
        potenciacion_p1 = (p1.ataque * 15) / 100
        potenciacion_p2 = 0
        return potenciacion_p1, potenciacion_p2
    elif p2.clase == "a" and p1.clase == "e":
        potenciacion_p2 = (p2.ataque * 15) / 100
        potenciacion_p1 = 0
        return potenciacion_p1, potenciacion_p2
    else:
        potenciacion_p1 = 0
        potenciacion_p2 = 0
        return potenciacion_p1,potenciacion_p2

def lucha(pturno, p1, p2):
    pot_p1, pot_p2 = potenciacion(p1, p2)

    while p1.vida > 0 and p2.vida > 0:

        if pturno == 1:
            p2.vida = p2.vida - (p1.ataque + pot_p1)
            pturno = 2
            print(f"{p1.nombre} ataca, {p2.nombre} ahora tiene {p2.vida:.2f}")
            print("##### PROXIMA RONDA #####\n")
        else:
            p1.vida = p1.vida - (p2.ataque + pot_p2)
            pturno = 1
            print(f"{p2.nombre} ataca, {p1.nombre} ahora tiene {p1.vida:.2f}")
            print("##### PROXIMA RONDA #####\n")

    if p1.vida <= 0:
        p1.vida = 100
        p2.vida = 100
        p2.gano()
        print("\n" * 10)

    else:
        p1.vida = 100
        p2.vida = 100
        p1.gano()
        print("\n" * 10)