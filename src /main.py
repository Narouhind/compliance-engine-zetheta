from engine import ComplianceEngine

def run_multi_framework_test(engine, tx, client_id, client_name):
    for fw in ["UE_AML", "USA_AML"]:
        # Ajout du paramètre client_name ici
        res = engine.analyze_transaction(tx, client_id, client_name, framework=fw)
        print(f"[{fw}] Status: {res['status']} | {res['message']}")

if __name__ == "__main__":
    engine = ComplianceEngine()
    tx = {"transaction_id": "TXN-2026-001", "amount": 12000}
    # Test avec un nom qui va matcher ("Jhon Smith" vs "John Smith" dans ta liste)
    run_multi_framework_test(engine, tx, "CLIENT_001", "Jhon Smith")
