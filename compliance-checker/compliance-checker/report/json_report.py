def generate_json(score, data):
    import json

    with open("output/report.json", "w") as f:
        json.dump({
            "score": score,
            "findings": data
        }, f, indent=4)
