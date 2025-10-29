from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# 1️⃣ Cria a conexão com o banco SQLite
db = create_engine("sqlite:///banco.db")


# 2️⃣ Cria a base para os modelos
Base = declarative_base()


# 4️⃣ Cria as tabelas no banco
Session= sessionmaker(bind=db)
Base.metadata.create_all(db)
