import xlrd

rc13_work = xlrd.open_workbook('data/raw_data/RC13_layout.xlsx')
lsheet = rc13_work.sheets()
rc13 = lsheet[0]

col_index = rc13.col_values(0)
col_name = rc13.col_values(5)

rc13_layout = []
table = 'SCHOOL'
table_id = len(col_index)

for n in range(0, len(col_index)):
    if type(col_index[n])==type(float(0.0)):
        rc13_layout.append({'id' : int(col_index[n]), 'name' : col_name[n], 'type' : 'COLUMN', 'table' : table })
    else:
        table_id = table_id + 1
        if len(col_index[n])<9:
            name = col_index[n]
        else:
            name = col_index[n]
            table = col_index[n]
        rc13_layout.append({'id' : table_id, 'name' : name, 'type' : 'TABLE', 'table' : table })

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
db = sqlalchemy.create_engine('sqlite:///data/processed_data/db_rc13.sqlite')

source = Table('source', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('type', String),
   Column('table', String)
)

metadata.create_all(db)
conn = db.connect()

result = conn.execute(source.insert(), rc13_layout)

