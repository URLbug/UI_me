from sqlalchemy import MetaData
from sqlalchemy import Column, String, Integer, Table


metadata_obj = MetaData()

user = Table(
  "user",
  metadata_obj,
  Column("user_id", Integer, primary_key=True),
  Column("first_name", String(40)),
  Column("last_name", String(50)),
  Column("email", String(100)),
  Column("password", String(500))
)