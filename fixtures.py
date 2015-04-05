import pymongo
from pymongo import MongoClient
from faker import Factory
fake = Factory.create('ru_RU')

dataset1 = []
dataset2 = []

for _ in range(0,150):
  dataset1.append(
    {"name": fake.color_name()}
  )
  dataset2.append(
    {"name": fake.name()}
  )

client = MongoClient('localhost', 27017)

db = client['boojom']
db.tags.insert(dataset1)
db.objects.insert(dataset2)