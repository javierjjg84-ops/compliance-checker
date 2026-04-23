def parse_lynis(file_path):
    findings = []

    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            line = line.strip().lower()

            if "warning" in line:
                findings.append({"type": "warning", "text": line})

            elif "suggestion" in line:
                findings.append({"type": "suggestion", "text": line})

            elif "vulnerability" in line or "cve" in line:
                findings.append({"type": "critical", "text": line})

            elif "hardening index" in line:
                findings.append({"type": "score", "text": line})

    return findings
