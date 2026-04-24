logistica = {
    "Norte": [],
    "Centro": [],
    "Sur": []
}
print("--- Registro de Paquetes ---")
for sector in logistica:
    paquete = input(f"Ingrese paquete para el sector {sector}: ")
    logistica[sector].append(paquete)
    print("\n--- Iniciando Despacho de Rutas ---")
clave_acceso = "AERYS2026"

for sector, paquetes in logistica.items():
    print(f"\nSector actual: {sector}")

   
    if sector == "Centro":
        print("Zona Restringida. Verificando credenciales...")

     
        intento = ""
        while intento != clave_acceso:
            intento = input("Escriba clave de repartidor para abrir portón: ")
            if intento != clave_acceso:
                print("Acceso denegado. Intente otra vez.")

        print("Acceso concedido al Casco Histórico.")

    for p in paquetes:
        print(f"Entregando paquete: {p}")

print("\n--- Misión cumplida: Camión vacío ---")