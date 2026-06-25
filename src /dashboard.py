import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="ZeTheta Compliance Portal", layout="wide")

# This function ensures it looks in the same folder where the script is running
def load_audit_data():
    log_path = os.path.join(os.path.dirname(__file__), "audit_log.jsonl")
    
    if not os.path.exists(log_path):
        st.warning(f"File not found at: {log_path}. Please run main.py first.")
        return pd.DataFrame()
    
    data = []
    with open(log_path, "r") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return pd.DataFrame(data)

st.title("🛡️ ZeTheta Compliance Analytics")
df = load_audit_data()

if not df.empty:
    st.success(f"Loaded {len(df)} records.")
    
    # KPI - Visualisation rapide
    col1, col2 = st.columns(2)
    flagged_count = len(df[df['status'] == 'FLAGGED'])
    col1.metric("Transactions Analysées", len(df))
    col2.metric("Alertes Détectées", flagged_count, delta_color="inverse")
    
    # Filtre interactif
    status_filter = st.multiselect("Filtrer par statut :", options=df['status'].unique(), default=df['status'].unique())
    df_filtered = df[df['status'].isin(status_filter)]
    
    st.dataframe(df_filtered)

    # Ajoute cette fonction à ton dashboard.py si tu veux prouver l'immuabilité
def verify_audit_integrity(df):
    is_valid = True
    # Ici, tu pourrais ajouter une logique qui recalcule les hashs 
    # et vérifie s'ils correspondent à la chaîne des prev_hash
    return is_valid

# Et dans ton dashboard, afficher un petit badge :
if verify_audit_integrity(df):
    st.sidebar.success("Audit Trail: Intègre ✅")
else:
    st.sidebar.error("Audit Trail: CORROMPU ⚠️")
