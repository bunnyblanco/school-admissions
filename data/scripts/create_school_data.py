"""Script to generate a table of the schools in the report"""
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Float
import sqlalchemy.ext.declarative
Base = sqlalchemy.ext.declarative.declarative_base()
db = sqlalchemy.create_engine('sqlite:///data/processed_data/db_report.sqlite')

class School(Base):
    __tablename__='school'
    id = Column(Integer, primary_key=True)
    num = Column(Integer)
    type = Column(String)
    name = Column(String(34))
    district = Column(String(34))
    city = Column(String(18))
    county = Column(String(12))
    district_type = Column(String(2))
    district_size = Column(String(2))
    district_type_name = Column(String(12))
    district_size_name = Column(String(7))
    school_type_name = Column(String(12))
    grades = Column(String(32))

Base.metadata.create_all(db)
lhead = Base.metadata.Tables['school'].Columns()
#lhead = {
#        'num',
#        'type',
#        'school',
#        'district',
#        'city',
#        'county',
#        'district_type',
#        'district_size',
#        'district_type_name',
#        'district_size_name',
#        'school_type_name',
#        'grades'
#    }
#
conn = db.connect()

import csv
#import csvkit
"""This doesn't use headers"""

csv_in = open('data/processed_data/rc13.csv', 'r')
reader = csv.reader(f, delimiter=';')
lrecord = {}
lrecords = []
for line in reader:
    lrecord = {
        'num' : line[0],
        'type' : line[1],
        'school' : str.strip(line[2]),
        'district' : str.strip(line[4]),
        'city' : str.strip(line[5]),
        'county' : str.strip(line[6]),
        'district_type' : line[7],
        'district_size' : line[8],
        'district_type_name' : str.strip(line[9]),
        'district_size_name' : str.strip(line[10]),
        'school_type_name' : str.strip(line[11]),
        'grades' : line[12]
    }
    lrecords.append(lrecord)

conn.execute(Base.metadata.tables['school'].insert(), lrecords)
