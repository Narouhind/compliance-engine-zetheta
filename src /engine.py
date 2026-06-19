import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, List

# Setup professional logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ZeThetaEngine")

class ComplianceEngine:
    """Core engine for multi-jurisdictional compliance analysis."""
    
    REGULATORY_FRAMEWORKS = {
        "UE_AML": {"limit": 10000, "description": "European AML Directive"},
        "USA_AML": {"limit": 15000, "description": "USA PATRIOT Act"}
    }

    def __init__(self, log_file: str = "audit_log.jsonl"):
        self.log_path = os.path.join(os.path.dirname(__file__), log_file)

    def _write_to_audit(self, report: Dict[str, Any]) -> None:
        """Appends compliance decision to the immutable audit log."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            **report
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def analyze_transaction(self, transaction: Dict[str, Any], framework: str = "UE_AML") -> Dict[str, Any]:
        """Analyzes transaction amount against framework-specific limits."""
        if framework not in self.REGULATORY_FRAMEWORKS:
            raise ValueError(f"Framework '{framework}' is not supported.")

        limit = self.REGULATORY_FRAMEWORKS[framework]["limit"]
        amount = transaction.get("amount", 0)
        
        status = "FLAGGED" if amount > limit else "PASSED"
        report = {
            "rule_id": f"AML-01-{framework}",
            "status": status,
            "message": f"Transaction {transaction.get('transaction_id')} {status.lower()} under {framework}."
        }
        
        self._write_to_audit(report)
        return report
