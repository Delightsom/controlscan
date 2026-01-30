# controlscan
Compliance-as-Code engine that maps Terraform infrastructure to NIST 800-53 and FedRAMP controls and generates automated gap reports.
## Quick Start

Run ControlScan locally:

```bash
python src/main.py

## What ControlScan Does

ControlScan scans Terraform infrastructure code and automatically maps detected security controls to NIST 800-53 and FedRAMP requirements.

Current automated checks include:

- Encryption at rest (SC-13, SC-28)
- Audit logging and record generation (AU-2, AU-12)

Results are produced as both terminal output and audit-ready Markdown reports.

---

## Why This Matters

Modern security programs rely on Compliance-as-Code to:

- Reduce manual audit effort  
- Enforce security controls continuously  
- Generate real-time compliance evidence  

ControlScan demonstrates how regulatory controls can be transformed into automated, repeatable workflows.

---

## Roadmap

Planned enhancements:

- Risk scoring (High/Medium/Low findings)  
- IAM least privilege detection  
- Network security control mapping  
- CI/CD pipeline automation  
- POA&M auto-generation  

