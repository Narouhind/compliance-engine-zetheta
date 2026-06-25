import os
import json
import logging
from datetime import datetime
from typing import Dict, Any
from graph_manager import GraphManager
from compliance_utils import check_watchlist
import hashlib

# Configuration du rôle (Global pour le test)
current_user_role = "COMPLIANCE_OFFICER"

def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user_role != required_role:
                raise PermissionError(f"Accès refusé : Rôle {required_role} requis.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

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
        self.graph = GraphManager(
            "neo4j+s://aff5afc9.databases.neo4j.io", 
            "neo4j", 
            "FM3pyZpl3JL63MEqVeLSOC0MqrRHtOuJtBwr_sYrVQE"
        )

    def _write_to_audit(self, report: Dict[str, Any]) -> None:
        prev_hash = "0"
        if os.path.exists(self.log_path):
            with open(self.log_path, "r") as f:
                lines = f.readlines()
                if lines:
                    last_entry = json.loads(lines[-1])
                    prev_hash = last_entry.get("hash", "0")

        data_string = json.dumps(report, sort_keys=True)
        current_hash = hashlib.sha256((data_string + prev_hash).encode()).hexdigest()
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            **report,
            "prev_hash": prev_hash,
            "hash": current_hash
        }
        
        with open(self.log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    @require_role("COMPLIANCE_OFFICER")
    def analyze_transaction(self, transaction: Dict[str, Any], client_id: str, client_name: str, framework: str = "UE_AML") -> Dict[str, Any]:
        sanctions_list = ["John Smith", "Alpha Corp", "Beta Trading"]
        
        # 1. Vérification des sanctions (Fuzzy Matching)
        is_blacklisted, score = check_watchlist(client_name, sanctions_list)
        
        # 2. Logique de seuil
        limit = self.REGULATORY_FRAMEWORKS[framework]["limit"]
        amount = transaction.get("amount", 0)
        
        status = "FLAGGED" if (amount > limit or is_blacklisted) else "PASSED"
        
        report = {
            "rule_id": f"AML-01-{framework}",
            "status": status,
            "message": f"Transaction {transaction.get('transaction_id')} {status.lower()} under {framework}."
        }
        
        # LOGIQUE D'AUDIT ET GRAPH
        self._write_to_audit(report)
        self.graph.log_transaction(client_id, transaction.get('transaction_id'), amount, status)
        
        return report
