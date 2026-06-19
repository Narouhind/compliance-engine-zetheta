# compliance-engine-zetheta
# compliance-engine-zetheta
# Compliance Rule Engine - ZeTheta Project

## Description
This project is an automated compliance monitoring system designed to analyze financial transactions against Anti-Money Laundering (AML) rules. It generates an immutable, timestamped audit trail for regulatory compliance.

## Project Structure
- `src/main.py`: Main orchestration script.
- `src/engine.py`: Compliance logic engine containing AML rules.
- `src/config.json`: Configuration file for system thresholds (AML-01, AML-02).
- `.gitignore`: Security configuration to protect sensitive audit logs and local environment files.

## Prerequisites
- Python 3.14 or higher.
- No external heavy dependencies are required; the system uses standard libraries (`os`, `json`, `datetime`).

## Usage
1. Ensure the configuration file `src/config.json` is present.

ZeTheta RegTech Engine - Compliance ProjectThe ZeTheta engine is a software solution designed to automate regulatory 
compliance monitoring (RegTech) and ensure the traceability of financial transactions.  System ArchitectureEngine (engine.py): Core logic enabling multi-framework analysis of transactions.  Audit Trail (audit_log.jsonl): Immutable log recording every compliance audit decision.  Dashboard (dashboard.py): Interactive user interface developed with Streamlit for visualizing and filtering compliance alerts.  Key FeaturesFeatureDescriptionMulti-Framework AnalysisDynamic support for EU and USA standards with adjustable thresholds.  TraceabilityAutomatic logging of all compliance decisions.  Real-time MonitoringInteractive dashboard allowing filtering of suspicious transactions.  User GuideInstall dependencies: pip install streamlit pandas  Run the dashboard: streamlit run dashboard.py  Visualization: Access the results in your browser at the local address indicated in the terminal.  Compliance Test Results Summary (from ZeTheta_Compliance_Report.pdf)  EU_AML (12k€): FLAGGED – Exceeds EU threshold.  USA_AML (12k€): PASSED – Compliant with USA standards.  Conclusion: The ZeTheta system has proven its ability to manage divergent regulations dynamically, ensuring precise compliance according to the jurisdiction. 
2. Run the system from the project root:
```bash
   python src/main.py
## Documentation
You can find the detailed technical design document for this project here:
[Technical Design Document](docs/Regulatory_Compliance_Engine_Technical_Report.pdf)


