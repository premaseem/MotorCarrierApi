
from pymongo import MongoClient

class MotorCarrierCenus(object):
  source_db = MongoClient('mongodb://localhost:27017/smsdbRecent').get_default_database()['MotorCarrier']
  destination_db = MongoClient('mongodb://localhost:27017/smsdb').get_default_database()['MotorCarrier']

  print("source count "+ str(source_db.count()))

  records = source_db.find()
  for new_doc in records:
    usdot = new_doc['DOT_NUMBER']
    del new_doc["_id"]
    retrieved_doc = destination_db.find_one({"DOT_NUMBER": usdot})
    if retrieved_doc is not None:
      retrieved_doc.update(new_doc)
      destination_db.save(retrieved_doc)
    else:
      destination_db.save(new_doc)

  print("destination count" + str(destination_db.count()))
