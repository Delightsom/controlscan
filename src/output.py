from pathlib import Path
from datetime import datetime

def write_report(report_text: str, out_dir: str = "reports") -> str:
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = Path(out_dir) / f"controlscan-report-{ts}.md"

    out_path.write_text(report_text, encoding="utf-8")
    return str(out_path)
