from scanner import scan_terraform
from report import generate_report
from output import write_report

if __name__ == "__main__":
    results = scan_terraform("data")
    report_text = generate_report(results, "policies/nist_controls.yaml")

    print(report_text)

    out_file = write_report(report_text, "reports")
    print(f"\nSaved report to: {out_file}")
