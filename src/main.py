from scanner import scan_terraform
from report import generate_report

if __name__ == "__main__":
    results = scan_terraform("data")
    print(generate_report(results))
