from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.modelos import Usuario,ArtigoPublicado




database_user="postgres"
database_senha="postgres"
database_port="5439"
database_banco="Teste"



def getURLLOCAL() -> str:
        return f"""postgresql+psycopg2://{database_user}:{database_senha}@localhost:{database_port}/{database_banco}"""



session = Session(bind=create_engine(getURLLOCAL(), echo= False))  

if __name__ == "__main__":
    
    pesquisador = session.query(Usuario).get(1235) 
    # pesquisador = Usuario(
    #     id = 2
    # )
    
    artigo = ArtigoPublicado(
        id = 7, 
        titulopesquisa = "seila"
    ) 
    
    print(pesquisador)

#    pesquisador.artigospublicados.append(artigo)
    
    
#    session.merge(pesquisador)
#    session.commit()
#    session.close()