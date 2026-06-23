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


print(f"\nNombre del heroe: {opcion1}\n "f"\nTu poder: {opcion2}\n " f"\nCiudad que proteges: {opcion3}\n "
      f"\nBando al que perteneces {opcion4}\n")
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


print(f"\"{opcion1} {final}\" ")

print()

# Day 2 I added Stats and damage calculator

print("[NUEVAS PREGUNTAS DIA 2...]")
print()
ataque_Base = int(input("Ingresa el Ataque Base: " ))
print()
multiplicador_De_Fuerza = float(input("Ingresa el multiplicador de Fuerza: "))
print()
Dano_Total = int(ataque_Base * multiplicador_De_Fuerza)

print("""
=============================================
         FICHA DEL HEROE ACTUALIZADA        
=============================================
""")

print(f"***ESTADISTICAS NUMERICAS***\n ->ATAQUE BASE: {ataque_Base}\n ->MULTIPLICADOR: {multiplicador_De_Fuerza}X\n "
      f"->DANO_TOTAL: {Dano_Total} puntos.\n")
print("===============================================")
