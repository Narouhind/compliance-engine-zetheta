# Compliance Rule Engine - ZeTheta Project

## 1. Project Overview
ZeTheta is an automated Regulatory Technology (RegTech) solution designed to monitor financial transactions against global Anti-Money Laundering (AML) standards. It ensures high-integrity traceability and provides an immutable audit trail for regulatory compliance.

## 2. System Architecture
- **Engine (`src/engine.py`)**: Core logic enabling multi-framework analysis (EU vs USA standards) with Role-Based Access Control (RBAC) and Fuzzy Matching (via rapidfuzz) for KYC risk detection.
- **Audit Trail (`audit_log.jsonl`)**: Cryptographically secured logs (SHA-256) ensuring compliance decision immutability.
- **Graph Manager (`graph_manager.py`)**: Integration with `Neo4j` for relationship-based fraud detection.
- **Dashboard (`dashboard.py`)**: Interactive interface (Streamlit) for real-time monitoring and filtering.
## 3. Key Features
| Feature | Description |
| :--- | :--- |
| **Multi-Framework Analysis** | Dynamic support for EU/USA standards with adjustable thresholds. |
| **Immutable Audit Trail** | Cryptographic hash chaining (SHA-256) for audit integrity. |
| **Fuzzy Matching KYC** | Intelligent name-matching for watchlist screening. |
| **Neo4j Graph Integration** |Persistent relationship storage for deep-link fraud analysis. |
| **RBAC Security** |Role-Based Access Control to restrict sensitive compliance functions. |
| **Real-time Monitoring** | Streamlit-based dashboard for instant alert visualization. |

## 4.Security & Compliance Design
- **Multi-Framework**: Dynamic support for EU AML (10k€) and USA PATRIOT Act (15k€) standards.

- **Cryptographic Integrity**: By chaining hashes (prev_hash), any unauthorized modification in the audit_log.jsonl is immediately detectable.

- **Access Control**: Python decorators are used to protect critical analytical methods, ensuring only authorized roles (COMPLIANCE_OFFICER) can execute them.

  ## Configuration
Before running the engine, create a `.env` file at the root of the project with your Neo4j Aura credentials:

```bash
NEO4J_URI=your_uri_here
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password
NEO4J_DATABASE=neo4j

## 5. Compliance Results (Performance Summary)
Based on the ZeTheta Compliance Report:
- **EU_AML (12k€)**: **FLAGGED** – Exceeds threshold.
- **USA_AML (12k€)**: **PASSED** – Compliant with USA PATRIOT Act.
- **Conclusion**: The engine effectively manages divergent regulatory requirements in a single execution pipeline.

## 6. Getting Started
### Prerequisites
- Python 3.14+
- `pip install streamlit pandas rapidfuzz neo4j`
- `pip install -r requirements.txt`

### Execution
1. Configure thresholds in `src/config.json`.
2. Run the main engine: `python src/main.py`
3. Launch the dashboard: `streamlit run dashboard.py`

## 6. Documentation
- [Technical Design Document](docs/Regulatory_Compliance_Engine_Technical_Report.pdf)
