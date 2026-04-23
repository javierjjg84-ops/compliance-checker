import os
import platform
import sys

from scanner.lynis import run_lynis
from scanner.visor import run_event_audit
from parser.lynis_parser import parse_lynis
from parser.visor_parser import parse_visor
from core.normalizer import normalize
from core.mapper import map_controls
from core.scorer import calculate_score
from report.json_report import generate_json
from report.pdf_report import generate_pdf


def main():
    print("================================================")
    print("   COMPLIANCE CHECKER - AUDITORÍA DE SEGURIDAD  ")
    print("================================================\n")

    sistema_operativo = platform.system()

    root_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(root_dir, "output")

    os.makedirs(output_dir, exist_ok=True)

    raw_data = []

    # ================= WINDOWS =================
    if sistema_operativo == "Windows":
        print(f"[*] Detectado: {sistema_operativo}")
        print("[*] Iniciando auditoría...")

        path_reporte = os.path.join(output_dir, "auditoria_errores.txt")

        exito = run_event_audit(path_reporte)

        if not exito:
            print("[!] ERROR: auditoría fallida.")
            return

        if os.path.exists(path_reporte):
            raw_data = parse_visor(path_reporte)
        else:
            print(f"[!] No se encontró {path_reporte}")
            return

    # ================= LINUX =================
    elif sistema_operativo == "Linux":
        print(f"[*] Detectado: {sistema_operativo}")
        print("[*] Iniciando Lynis...")

        run_lynis()

        path_reporte = os.path.join(output_dir, "lynis.dat")

        if os.path.exists(path_reporte):
            raw_data = parse_lynis(path_reporte)
        else:
            print(f"[!] No se encontró {path_reporte}")
            return

    else:
        print("[!] Sistema no soportado")
        return

    # ================= PIPELINE =================
    if not raw_data:
        print("[!] Sin datos.")
        return

    print("[*] Normalizando...")

    # 🔥 FIX CLAVE: conservar type + raw correctamente
    normalized = normalize([
        {
            "source": "windows" if sistema_operativo == "Windows" else "lynis",
            "raw": item["text"],
            "type": item.get("type", "suggestion")
        }
        for item in raw_data
    ])

    print("[*] Mapeando controles...")
    mapped = map_controls(normalized)

    print("[*] Calculando score...")
    score = calculate_score(mapped)

    print("[*] Generando reportes...")

    generate_json(score, mapped)
    generate_pdf(score, mapped)

    print("\n[*] AUDITORÍA FINALIZADA")
    print(f"Score: {score}/100")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()