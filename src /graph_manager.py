# src/graph_manager.py
from neo4j import GraphDatabase

class GraphManager:
    """Gère la connexion à la base de données Neo4j pour l'analyse des risques."""
    
    def __init__(self, uri, user, password):
        # Utilisation de 'neo4j+ssc' (Self-Signed Certificate) pour éviter les erreurs SSL
        # lors de la connexion locale. Le driver gère l'encryption automatiquement.
        ssc_uri = uri.replace("neo4j+s://", "neo4j+ssc://")
        
        self.driver = GraphDatabase.driver(
            ssc_uri, 
            auth=(user, password)
        )

    def close(self):
        """Ferme la connexion proprement."""
        self.driver.close()

    def log_transaction(self, client_id, tx_id, amount, status):
        """
        Envoie les données au graphe :
        1. Crée ou met à jour le client.
        2. Crée ou met à jour la transaction.
        3. Crée une relation 'PERFORMED' entre les deux.
        """
        query = """
        MERGE (c:Client {id: $c_id})
        MERGE (t:Transaction {id: $t_id})
        SET t.amount = $amount, 
            t.status = $status, 
            t.timestamp = datetime()
        MERGE (c)-[:PERFORMED]->(t)
        """
        try:
            with self.driver.session() as session:
                session.run(
                    query, 
                    c_id=client_id, 
                    t_id=tx_id, 
                    amount=amount, 
                    status=status
                )
        except Exception as e:
            print(f"Erreur lors de l'envoi vers Neo4j : {e}")

# Exemple de schéma de données généré par ce code :
#
