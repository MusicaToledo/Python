# lo dejo vacio para poder llenarlo como quiera
paq= {
    "norte":[], 
    "centro":[],
    "sur":[]
}
print("      INGRESO DE PAQUETES        ")
for zona in paq:
    ingreso=input(f" ingresa el paquete para la zona de entrega {zona} :")
    paq[zona].append(ingreso)
print("      INICIANDO DESPACHO        ")

clave= "123"

for zona,lista in paq.items():
    print(f"zona:{zona}")
    if zona == "centro":
        print("Zona restringida VERIFICANDO CREDENCIALES")
        while True:
            intento = input("Escriba clave de repartidor: ")
            if intento == clave:
                print("Clave correcta")
                break
    else:
        print("Clave incorrecta")
    for paquete in lista:
        print(f"Entregado :{paquete}")
print("\n--- Misión cumplida: Camión vacío ---")