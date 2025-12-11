from flask_restful import Resource 
import requests
from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError

from models.Ocupacao import Ocupacao
from database import db


class OcupacoesResource(Resource):
    def get(self):
        termo = request.args.get("termo")
        solr_url = f"http://solr:8983/solr/ocupacoes/select"
        params = {
            "q": f"titulo:{termo} OR titulo:{termo}~2 OR titulo:{termo}*",
            "rows": 10,
            "wt": "json",
            "fl": "codigo,titulo" 
        }
        
        try:
            response = requests.get(solr_url,params=params)
            return jsonify(response.json())
        except Exception as e:
            return {"error": f"Erro ao conectar no Solr: {str(e)}"}, 500
        
        
    
    def post(self):
        data = request.get_json()
        codigo = data.get("codigo")
        titulo = data.get("titulo")
        try:
            
            ocup = Ocupacao(codigo=codigo, titulo=titulo)
            db.session.add(ocup)
            db.session.commit()

            solr_url = "http://solr:8983/solr/gettingstarted/update?commit=true"
            doc = {"codigo": codigo, "titulo": titulo}
            response = requests.post(solr_url, json=[doc])

            return jsonify({
            "status": "ok",
            "postgres": f"Ocupação {titulo} inserida",
            "solr_response": response.text
            })

        except SQLAlchemyError as e:        
            return {"mensagem": "Problema com o banco de dados."}, 500
        

class OcupacoesResourcePostgres(Resource):
    def get(self):
        try:
            page = request.args.get("page", 1, type=int)
            limit = request.args.get("limit", 10, type=int) 
            
            offset = (page - 1) * limit

            stmt = db.select(Ocupacao).limit(limit).offset(offset)
            results = db.session.execute(stmt).scalars().all()

            lista_ocupacoes = []
            for ocupacao in results:
                lista_ocupacoes.append({
                    "codigo": ocupacao.codigo,
                    "titulo": ocupacao.titulo
                })

            return jsonify({
                "data": lista_ocupacoes,
                "page": page,
                "limit": limit
            })

        except Exception as e:
            return {"error": str(e)}, 500