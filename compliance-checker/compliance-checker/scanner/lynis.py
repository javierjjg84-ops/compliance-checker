import os

def run_lynis():
    # Asegurar que la carpeta output existe donde se ejecuta el script
    if not os.path.exists("output"):
        os.makedirs("output")

    # --quick: No hace pausas entre secciones
    # --pentest: Modo no interactivo (evita que se quede bloqueado esperando un 'Enter')
    command = "sudo lynis audit system --quick --pentest --no-colors > output/lynis.dat 2>/dev/null"

    print("[*] Iniciando escaneo real de Lynis (modo automatizado)...")
    
    # Ejecutamos y capturamos el resultado
    status = os.system(command)
    
    if status == 0:
        print("[OK] Escaneo completado exitosamente.")
    else:
        print("[!] El escaneo fue interrumpido o tuvo errores.")

if __name__ == "__main__":
    run_lynis()
