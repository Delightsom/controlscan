def generate_report(results: dict) -> str:
    lines = ["Compliance Report", "----------------"]
    for check, passed in results.items():
        status = "PASS" if passed else "FAIL"
        lines.append(f"{check}: {status}")
    return "\n".join(lines)
