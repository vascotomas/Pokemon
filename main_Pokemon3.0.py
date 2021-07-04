from Pokemon3 import  Pokemon as P
from Pokemon3 import  guardar, crear,listar,cargadoPok,tirar_dado,lucha,potenciacion
import pickle, random
p = P ()



pokemon_index_archivo = cargadoPok()

while True:
    print("(1) CREAR POKEMON \n (2) VER INDEX \n (3) A LUCHAR! \n (4) SALIR)")
    s_menu = input(">")

    if s_menu == "1":
        pokemon_index_archivo = crear(pokemon_index_archivo)

    elif s_menu == "2":
        listar(pokemon_index_archivo)
    elif s_menu == "3":
        select1 = int(input("SELECCIONA TU POKEMON: "))
        select2 = int(input("SELECCIONA TU ADVERSARIO: "))

        select1 = pokemon_index_archivo[select1 - 1]
        select2 = pokemon_index_archivo[select2 - 1]

        turno = tirar_dado(2)
        lucha(turno,select1,select2)
    else:
        break

#

#
