from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

consultas = Table("consultas", meta_data,
              Column("id",Integer, primary_key=True),
              Column("diagnostico", String(255), nullable=False))
              
  
meta_data.create_all(engine)