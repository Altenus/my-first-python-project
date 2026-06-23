import random
print(r""" 
••      ••  ••••••••••  ••••••••      ••••••    ••••••••••    ••••••••  
••      ••  • ••••••••  • ••••••      ••••••    • ••••••••    ••••••••  
••      ••  ••          ••      ••  ••      ••  ••          ••          
••      ••  ••          ••      ••  ••      ••  ••          ••          
• •••••• •  • ••••••    • ••••••    ••      ••  • ••••••      ••••••    
• •••••• •  • ••••••    • •••• •    ••      ••  • ••••••      ••••••    
••      ••  ••          ••    ••    ••      ••  ••                  ••  
••      ••  ••          ••    ••    ••      ••  ••                  ••  
••      ••  • ••••••••  ••      ••    ••••••    • ••••••••  ••••••••    
••      ••  ••••••••••  ••      ••    ••••••    ••••••••••  ••••••••        
""")

print()

print("Nesesitamos tu ayuda para selecionar nuestro nuevo heroe!!!   ")
print()
opcion1 = input("Nombre del heroe: ").title()
opcion2 = input("Super poder principal: ").title()
opcion3 = input("Ciudad que protege: ").title()
opcion4 = input("Bando al que pertenece: ").title()

almacen1 = [opcion1, opcion2, opcion3, opcion4]


print(f"""
🦸‍Nombre del heroe: {opcion1} 

🧬Tu poder: {opcion2}

🏙️Ciudad que proteges: {opcion3} 

🛡️/😈Bando al que perteneces {opcion4}""")

print()

dato_sorpresa = random.choice(almacen1)
print(f"El sistema ha selecionado tu dato mas importante: {dato_sorpresa}!!")

destino_Heroes = [
      "Muere salvando al mundo y se convierte en un símbolo eterno",
      "Deja las armas y busca una vida pacífica y oculta de la fama",
      "Se aleja del mundo al sentir que su poder es un peligro para otros."
]

destino_Villanos = [
      "El villano queda atrapado repitiendo el mismo evento catastrófico o doloroso por la eternidad ",
                    "Encierro en dimensiones vacías, espejos, lámparas mágicas o el propio subconsciente ",
                    "Pierde todo el poder y terminar en una posición ridícula, como ser el juguete olvidado en un camión de basura "
                    ]
print()

if opcion4== "Heroe":
      final = random.choice(destino_Heroes)
else:
      final =random.choice(destino_Villanos)

print()

# Day 2 I added Stats and damage calculator

print("[NUEVAS PREGUNTAS DIA 2...]")
print()
ataque_Base = int(input("Ingresa el Ataque Base: " ))
print()
multiplicador_De_Fuerza = float(input("Ingresa el multiplicador de Fuerza: "))
print()
Dano_Total = int(ataque_Base * multiplicador_De_Fuerza)

Aumento_De_Poder = 0    # Power Up
Perdida_De_Poder = 0    # Lost Power
print("""
=============================================
         FICHA DEL HEROE ACTUALIZADA        
=============================================
""")

print(f"""***ESTADISTICAS NUMERICAS*** 

->⚔️ATAQUE BASE: {ataque_Base} 

->🚀MULTIPLICADOR: {multiplicador_De_Fuerza}X 

 f"->💥DANO_TOTAL: {Dano_Total} puntos.""")

print("===============================================")

# Added nested interactive menus, dynamic power modifiers, and pre-initialized global variables.⬇️

print("""
====================================
¿ESTAS LISTO PARA TU PRIMERA MISION?
====================================
""")

print("1 Si")
print("2 No")

Decision = int(input("Elige una opcion 1 o 2: " ))
if Decision == 1:
    print("TE TELETRANSPORTASTE A UNA CUEVA")
    print()
    print("\033[1m--- ¡Te encuentras una puerta cerrada! ---\033[1m")
    print()
    print("->1 Asomarse por la puerta ")
    print("->2 Derribar la puerta de una patada ")
    print()
    Decision2 = int(input("""Elige una opcion 1 o 2: """ ))
    if Decision2 == 1:
        print("Entraste en silencio y viste que todos estaban duermiendo ")
        Aumento_De_Poder = Dano_Total * 30
        print(f"🚀 Multiplicaste tu poder :D : {Aumento_De_Poder} puntos totales")
    elif Decision2 == 2:
        print("Despertaste a todos ")
    else:
        print("esta opcion no es valida")

else:
    print("Haz rechazado la Mision perdiste los posibles puntos ")
    perdida_De_Poder = Dano_Total - 200

    print(f"Perdiste Mucho poder por no aceptar la mision :C tu Nuevo Dano total es : {perdida_De_Poder} ")
    print()
    print(type(perdida_De_Poder))

print()


print(f"\"{opcion1} {final}\" ")