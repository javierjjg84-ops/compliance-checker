def parse_visor(file_path):
    findings = []

    # 🔥 palabras que NO son seguridad (ruido de Windows)
    noise_filters = [
        "windows app runtime",
        "information",
        "eventlog",
        "audit success",
        "operational",
        "service control manager"
    ]

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip().lower()

            # =========================
            # 1. LIMPIEZA BÁSICA
            # =========================
            if not line:
                continue

            if "\x00" in line or "\u0000" in line:
                line = line.replace("\x00", "").replace("\u0000", "").strip()

            if not line:
                continue

            # =========================
            # 2. FILTRO DE RUIDO WINDOWS
            # =========================
            if any(noise in line for noise in noise_filters):
                continue

            # =========================
            # 3. FILTRO DE METADATOS
            # =========================
            if line.startswith("timecreated"):
                continue
            if line.startswith("logname"):
                continue
            if line.startswith("providername"):
                continue
            if line.startswith("machinename"):
                continue
            if line.startswith("message :"):
                continue
            if line.startswith("id"):
                continue

            # =========================
            # 4. CLASIFICACIÓN REALISTA
            # =========================
            if any(x in line for x in ["error", "failed", "critical", "service failed", "denied", "timeout"]):
                ftype = "high"

            elif any(x in line for x in ["warning", "delayed", "slow"]):
                ftype = "medium"

            elif any(x in line for x in ["success", "started", "completed", "running"]):
                ftype = "low"

            else:
                ftype = "low"

            # =========================
            # 5. GUARDAR FINDING
            # =========================
            findings.append({
                "type": ftype,
                "text": line
            })

    return findings