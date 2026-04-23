def calculate_score(mapped):
    """
    Calcula una puntuación de cumplimiento basada en severidad
    y volumen de hallazgos. Compatible con Linux (Lynis) y Windows (Event Log).
    """

    if not mapped:
        return 100

    score = 100

    # =========================
    # 1. Penalización por severidad
    # =========================
    for m in mapped:
        severity = (m.get("severity") or "low").lower()

        if severity == "high":
            score -= 10   # impacto fuerte pero controlado
        elif severity == "medium":
            score -= 4    # impacto medio realista
        elif severity == "low":
            score -= 0.3  # impacto mínimo (ruido controlado)
        else:
            score -= 0.2  # fallback seguro

    # =========================
    # 2. Penalización por volumen (solo relevante)
    # =========================
    total = len(mapped)

    if total > 150:
        score -= 10
    elif total > 100:
        score -= 7
    elif total > 60:
        score -= 4
    elif total > 30:
        score -= 2

    # =========================
    # 3. Normalización final
    # =========================
    if score > 100:
        score = 100
    if score < 0:
        score = 0

    return round(score, 2)