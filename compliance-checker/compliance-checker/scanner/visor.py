import subprocess


def run_event_audit(output_file):
    """
    Ejecuta auditoría de eventos en Windows y guarda salida en la ruta indicada.
    """

    command = f"""
    Get-WinEvent -FilterHashtable @{{
        LogName = 'System','Application'
        Level = 2
        StartTime = (Get-Date).AddDays(-7)
    }} |
    Select-Object TimeCreated, LogName, Id, LevelDisplayName, ProviderName, MachineName, Message |
    Sort-Object TimeCreated -Descending |
    Out-File "{output_file}"
    """

    print("[*] Iniciando auditoría de eventos de Windows...")

    status = subprocess.call([
        "powershell",
        "-Command",
        command
    ])

    if status == 0:
        print("[OK] Auditoría completada correctamente.")
        return True
    else:
        print("[!] Error en auditoría.")
        return False


def parse_visor(file_path):
    """
    Parser simple de salida de eventos.
    """

    findings = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip().lower()

            if not line:
                continue

            findings.append({
                "type": "event",
                "text": line
            })

    return findings