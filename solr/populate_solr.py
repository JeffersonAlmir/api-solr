import requests
from database import db
from models.Ocupacao import Ocupacao
def populateSolar():
    solr_url = "http://solr:8983/solr/ocupacoes/update?commit=true"
    try:
        stmt = db.select(Ocupacao)
        resultados = db.session.execute(stmt).scalars().all()    

        documentos_solr = []
        for row in resultados:
            documentos_solr.append({
                "codigo": row.codigo,  
                "titulo": row.titulo   
            })  

        response = requests.post(solr_url, json=documentos_solr)

        if response.status_code == 200:
            return {
                "status": "sucesso",
                "mensagem": f"{len(documentos_solr)} registros indexados no Solr!",
                "solr_time": response.json().get("responseHeader", {}).get("QTime", 0)
            }
        else:
            return {
                "status": "erro",
                "solr_status": response.status_code,
                "solr_response": response.text
            }, 500

    except Exception as e:
        return {"error": f"Erro interno: {str(e)}"}, 500