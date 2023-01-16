import pymongo
from pymongo import MongoClient
from random import randint, choice

from config import user, password

try:
    uri = f"mongodb+srv://{user}:{password}@cluster0.lmgyayr.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.users
    db_test = client.testdata
    coll = db.user
    coll_test = db_test.users

    # for i in range(1, 1001):
    #     coll.insert_one(
    #         {
    #             "_id": i,
    #             "user": f"user_{i}",
    #             "password": "".join([str(randint(1, 9)) for num in range(8)]),
    #             "status": True if i % 2 == 0 else False
    #         }
    #     )

    # users = ['Anna', 'Denis', 'Carrol', 'March', 'Homer', 'Bart', 'Maggy']
    # status = [True, False]
    # data = [
    #     {
    #         "_id": 11,
    #         "user": choice(users),
    #         "password": "".join([str(randint(1, 9)) for num in range(8)]),
    #         "status": choice(status)
    #     },
    #     {
    #         "_id": 12,
    #         "user": choice(users),
    #         "password": "".join([str(randint(1, 9)) for num in range(8)]),
    #         "status": choice(status)
    #     },
    #     {
    #         "_id": 13,
    #         "user": choice(users),
    #         "password": "".join([str(randint(1, 9)) for num in range(8)]),
    #         "status": choice(status)
    #     }
    # ]
    # coll.insert_many(data)

    # rows = coll.find()
    # for row in rows:
    #     print(row)

    # rows = coll.find().sort("status", -1)
    # for row in rows:
    #     print(row)

    # rows = coll.find().limit(3)
    # for row in rows:
    #     print(row)

    # rows = coll.find({}, {"_id": 0, "user": 1, "password": 1})
    # for row in rows:
    #     for k, v in row.items():
    #         print(f"{k}: {v}")
    #     print("-" * 10)

    # query = {"status": True}
    # rows = coll.find(query, {"_id": 0, "user": 1, "password": 1})
    # for row in rows:
    #     print(row)

    # query = {"user": {"$regex": "user*"}}
    # rows = coll.find(query, {"_id": 0, "user": 1, "password": 1})
    # for row in rows:
    #     print(row)

    # # возвращает то что начинается на букву и ниже по алфавиту
    # query = {"user": {"$gt": "W"}}
    # rows = coll.find(query, {"_id": 0, "user": 1, "password": 1})
    # for row in rows:
    #     print(row)

    # query = {"user": "Anna"}
    # rows = coll.find_one(query)
    # print(rows)

    # rows = coll.find()
    # for row in rows:
    #     coll.update_one(row, {"$set": {"balance": 0}})

    # rows = coll.find()
    # for row in rows:
    #     print(row)

    # rows = coll.find({"status": True})
    # for row in rows:
    #     coll.update_one(row, {"$inc": {"balance": +500}})

    # rows = coll.find()
    # for row in rows:
    #     print(row)

    # current = {"user": {"$regex": "Hom"}}
    # new_data = {
    #     "$inc": {"balance": +300},
    #     "$set": {"status": True}
    # }
    # coll.update_one(current, new_data)

    # current = {"_id": 12}
    # new_data = {"$set": {"list": ['first', 'second', 'third', 'fourth']}}
    # coll.update_one(current, new_data)

    # # удаляет последний элемент в списке, 1 это True
    # current = {"_id": 12}
    # new_data = {"$pop": {"list": 1}}
    # coll.update_one(current, new_data)

    # current = {"_id": 12}
    # new_data = {"$pull": {"list": "first"}}
    # coll.update_one(current, new_data)

    # current = {"status": False}
    # new_data = {"$inc": {"balance": -100}}
    # coll.update_many(current, new_data)

    # rows = coll.find().sort("status")
    # for row in rows:
    #     print(row)

    # all things
    # print(coll.count_documents({}))

    # count with filter
    # print(coll.count_documents({"user": "Anna"}))

    # count with regex
    # query = {"user": {"$regex": "user*"}}
    # print(coll.count_documents(query))

    # print(client.list_database_names())

    # res = client.list_databases()
    # for i in res:
    #     print(i)

    # print(db.list_collection_names())
    # print(db_test.list_collection_names())

    # coll_test.drop()

    # coll.delete_one({"_id": 11})

    # query = {"password": {"$regex": "8*"}}
    # result = coll.delete_many(query)
    # print(f"deleted: {result.deleted_count}")

    # result = coll.delete_many({})
    # print(f"deleted: {result.deleted_count}")

    # res = coll.find()
    # for row in res:
    #     print(row)

    # index
    # --------------------------------------------------------
    coll.create_index([("user", pymongo.DESCENDING)])
    print(coll.index_information())

    # --------------------------------------------------------

    print('-' * 30)
    print("Successfully connect".center(30))
    print('-' * 30)
except Exception as _ex:
    print(_ex)
finally:
    client.close()
