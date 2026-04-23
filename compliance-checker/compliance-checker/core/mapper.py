import json
import os

def map_controls(findings):
    controls_path = os.path.join("data", "controls.json")

    if not os.path.exists(controls_path):
        return []

    with open(controls_path, "r", encoding="utf-8") as f:
        controls = json.load(f)

    mapped = []

    for fnd in findings:

        # FIX CLAVE: aceptar todos los formatos posibles
        desc = (
            fnd.get("description") or
            fnd.get("raw") or
            fnd.get("text") or
            ""
        ).lower()

        matched = False

        for key, meta in controls.items():
            keywords = meta.get("keywords", [])

            if any(kw.lower() in desc for kw in keywords):
                mapped.append({
                    "id": fnd.get("id", "N/A"),
                    "title": meta.get("title", "Sin título"),
                    "description": desc,
                    "iso": meta.get("references", {}).get("iso27001", "N/A"),
                    "ens": meta.get("references", {}).get("ens", "N/A"),
                    "severity": meta.get("severity", "low")
                })
                matched = True
                break

        #fallback para no perder información
        if not matched:
            mapped.append({
                "id": fnd.get("id", "N/A"),
                "title": "Sin clasificar",
                "description": desc,
                "iso": "N/A",
                "ens": "N/A",
                "severity": fnd.get("severity", "low")
            })

    return mapped