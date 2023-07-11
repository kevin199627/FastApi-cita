from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Date, Time, CHAR
from config.db import engine, meta_data

citas = Table("citas", meta_data,
              Column("id",Integer, primary_key=True),
              Column("fecha", Date, nullable=False),
              Column("hora", Time, nullable=False),
              Column("estado", CHAR, nullable=False))


meta_data.create_all(engine)