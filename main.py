#precisa revisar os comandos e ver se está rodando tudo ainda. 
#CrieumaplicativoCRUDcomFastAPIeSQLAlchemyNesteartigo,fornecereiumguiasimplesediretosobrecomovocêpodeconstruirumaplicativoCRUDcomFastAPIeSQLAlchemy. OaplicativoFastAPIseráexecutadoemumservidorwebStarlette,usaráPydanticparavalidaçãodedadosearmazenarádadosemumbancodedadosSQLite.ObancodedadospadrãoparaesteartigoéSQLite,mascolocareiumaseçãonestetutorialparaorientá-losobrecomoconfigurarumservidorPostgrescomDockereajustarocódigoparafuncionarcomobancodedadosPostgreSQLemexecução.

#https://www.maismulheres.tech/courses/take/bootcamp-back-end-python/pdfs/48348808-desafiofastapi

# from flask import Flask
# from threading import Thread
# app = Flask('')
# @app.route('/')
#     def home():
#     return  "I'm alive"
#     def run():
#     app.run(host='0.0.0.0',port=8080)
# t = Thread(target=run)
# t.start()

from fastapi import FastAPI
app=FastAPI()

@app.get("/api/healthchecker")
def root():
    return{"message":"WelcometoFastAPIwithSQLAlchemy"}