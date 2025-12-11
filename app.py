from database import db
from application import app, api

from solr.config_solr import configSolar
from solr.populate_solr import populateSolar
from models.Ocupacao import Ocupacao
from resources.OcupacoesResource import OcupacoesResource, OcupacoesResourcePostgres


api.add_resource(OcupacoesResource,"/ocupacoes")
api.add_resource(OcupacoesResourcePostgres,"/ocupacoespostgres")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
   
    with app.app_context():
        
        db.create_all() 
        print("Configurando Solr...")
        configSolar()
        print("Populando Solr...")
        resultado = populateSolar()
        print(f"Resultado População: {resultado}")

    app.run(host='0.0.0.0', debug=True)