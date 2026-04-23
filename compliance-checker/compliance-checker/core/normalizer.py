def normalize(findings):
    normalized = []

    for f in findings:

        source = f.get("source", "windows" if "type" in f else "lynis")
        raw = f.get("raw") or f.get("text") or str(f)

        # =====================
        # WINDOWS
        # =====================
        if "type" in f:
            severity_map = {
                "critical": "high",
                "warning": "medium",
                "suggestion": "low"
            }

            normalized.append({
                "id": "WIN_" + str(abs(hash(raw))),
                "description": raw,
                "severity": severity_map.get(f.get("type"), "low"),
                "source": "windows"
            })

        # =====================
        # LYNIS (Linux)
        # =====================
        elif source == "lynis":
            text = raw.lower()

            if any(x in text for x in ["critical", "cve", "vulnerability", "exploit", "failed"]):
                severity = "high"
            elif "warning" in text or "suggestion" in text:
                severity = "medium"
            else:
                severity = "low"

            normalized.append({
                "id": "LYNIS_" + str(abs(hash(raw))),
                "description": raw,
                "severity": severity,
                "source": "lynis"
            })

    return normalized