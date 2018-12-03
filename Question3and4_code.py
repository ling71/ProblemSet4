#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, MetaData, ForeignKey
import csv

# Create a sql database for rainfall data
engine = create_engine('sqlite:///rainfall.sqlite')

metadata = MetaData()

# Make Annual_rainfall table
try:
    Annual_rainfall = Table ('Annual_rainfall', metadata, autoload = True)
except:
    Annual_rainfall = Table ('Annual_rainfall', metadata,
                Column('Year', Integer, primary_key = True),
                Column('Annual', Float)
                )

# Make Monthly_rainfall table
try:
    Monthly_rainfall = Table ('Monthly_rainfall', metadata, autoload = True)
except:
    Monthly_rainfall = Table ('Monthly_rainfall', metadata,
                Column('Year', Integer, ForeignKey("Annual_rainfall.Year")),
                Column('Jan', Float),
                Column('Feb', Float),
                Column('Mar', Float),
                Column('Apr', Float),
                Column('May', Float),
                Column('Jun', Float),
                Column('Jul', Float),
                Column('Aug', Float),
                Column('Sep', Float),
                Column('Oct', Float),
                Column('Nov', Float),
                Column('Dec', Float)
                )

metadata.create_all(engine)

conn = engine.connect()

rainfall = open("Gainesville-rainfall.csv")

reader = csv.DictReader(rainfall)

# Load data to Annual_rainfall table
for Line in reader:
    ins1 = Annual_rainfall.insert().values(Year = (Line['Year']),
                            Annual = (Line['Annual']),
                                       )

    result1 = conn.execute(ins1)

# Load data to monthly_rainfall table
    ins2 = Monthly_rainfall.insert().values(Year = (Line['Year']),
                                        Jan = (Line['Jan']),
                                        Feb = (Line['Feb']),
                                        Mar = (Line['Mar']),
                                        Apr = (Line['Apr']),
                                        May = (Line['May']),
                                        Jun = (Line['Jun']),
                                        Jul = (Line['Jul']),
                                        Aug = (Line['Aug']),
                                        Sep = (Line['Sep']),
                                        Oct = (Line['Oct']),
                                        Nov = (Line['Nov']),
                                        Dec = (Line['Dec'])
                                            )
    result2 = conn.execute(ins2)

