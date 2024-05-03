from pymongo import MongoClient
import pprint
import re

client = MongoClient("mongodb://localhost:27017/")

db = client["chinook"]

customers_collection = db["customers"]

''''# Print top 1 (topmost) document
doc1 = customers_collection.find_one()
print(doc1)
'''

''''# Print all documents
for doc in customers_collection.find():
    print(doc)
'''

'''Print all documents LastName and FirstName only
for doc in customers_collection.find({}, {"_id": 0,"LastName": 1, "FirstName": 1}):
    print(doc)
'''

'''Print all documents with lastname that starts with "G"'''

rgx = re.compile('^Go.*?$', re.IGNORECASE)

doc_num = 0

for doc in customers_collection.find({"LastName": rgx}):
    doc_num += 1
    pprint.pprint(doc)
    print()

print('No. of documents in customers collection with LastName starting with "G": ', str(doc_num))

client.close()