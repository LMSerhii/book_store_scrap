from pymongo import MongoClient
from random import randint


def connect_to_testdb():
    uri = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.2"

    with MongoClient(uri) as client:
        db = client.testdb
        coll = db.users

        # coll.insert_one(
        #     {
        #         "_id": 1,
        #         "user": "serhii",
        #         "password": "".join([str(randint(0, 9)) for i in range(11)]),
        #         "status": False,
        #         "balance": 0
        #     }
        # )
        # print("Insert one collection completed")

        # data = [
        #     {
        #         "_id": 2,
        #         "user": "Jack",
        #         "password": "".join([str(randint(0, 9)) for i in range(11)]),
        #         "status": False,
        #         "balance": 0
        #     },
        #     {
        #         "_id": 3,
        #         "user": "Jimm",
        #         "password": "".join([str(randint(0, 9)) for i in range(11)]),
        #         "status": False,
        #         "balance": 0
        #     }
        # ]
        # coll.insert_many(data)
        # print("Insert many collections completed")

        # coll.update_one(
        #     {"user": "serhii"}, {"$inc": {"balance": +100}}
        # )
        #

        print("-" * 30)
        for row in coll.find():
            print(row)
        print("-" * 30)

        for row in coll.find({}, {"_id": 0, "user": 1, "status": 1, "balance": 1}):
            print(row)
        print("-" * 30)

        query = {"balance": 0}
        for row in coll.find(query, {"_id": 0, "user": 1, "status": 1, "balance": 1}):
            print(row)
        print("-" * 30)

        print(coll.find_one({'_id': 1}))
        print("-" * 30)

        print("Successfully connect")


def main():
    connect_to_testdb()


if __name__ == '__main__':
    main()