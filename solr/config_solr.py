import requests

def configSolar():
    solr_base_url = "http://solr:8983/solr/ocupacoes"
    schema_url = f"{solr_base_url}/schema"

    schema = {
    "add-field": [
        {
            "name": "codigo",
            "type": "pint",
            "stored": True,
            "indexed": True,
            "required": True
        },
        {
            "name": "titulo",
            "type": "text_general",
            "stored": True,
            "indexed": True
        },
    ]
}

    try:
        r = requests.post(schema_url, json=schema)
        print(f"Campos: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Erro ao criar campos: {e}")