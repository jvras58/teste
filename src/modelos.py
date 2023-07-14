from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship,backref
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Numeric, String, Table
from typing import List
import sqlalchemy as sa

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "tbl_usuarios"

    id                = Column(Integer,primary_key=True)
    artigospublicados = relationship("ArtigoPublicado", back_populates="usuario")
    
class ArtigoPublicado(Base):
    __tablename__ = "tbl_artigospublicados"

    id =         Column(Integer, primary_key=True)
    
    usuario_id = Column(Integer, ForeignKey('tbl_usuarios.id'))
    
    usuario = relationship(  "Usuario", back_populates="artigospublicados")
    
    titulopesquisa =     Column(String, nullable=False)
    


