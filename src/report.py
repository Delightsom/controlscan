import yaml

def load_controls(policy_path: str) -> dict:
    with open(policy_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("controls", {})

def generate_report(results: dict, policy_path: str = "policies/nist_controls.yaml") -> str:
    controls = load_controls(policy_path)

    lines = [
        "ControlScan Report (NIST 800-53 / FedRAMP)",
        "----------------------------------",
    ]

    if not controls:
        lines.append("No controls found in policy file.")
        return "\n".join(lines)

    for control_id, meta in controls.items():
        check = meta.get("check")
        title = meta.get("title", "").strip()
        passed = bool(results.get(check, False))
        status = "PASS" if passed else "FAIL"
        lines.append(f"{control_id} - {title}: {status}")

    return "\n".join(lines)

