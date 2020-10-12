from pymongo import MongoClient
from bson import ObjectId

# client = MongoClient('10.1.9.118', 27017)
client = MongoClient()
database = client.get_database('D4E16')
quiz_collection = database.get_collection('quizzes')
data = [  # collection
    {
        'question': 'con chó có mấy chân?',
        'choices': [
            '1 chân',
            '2 chân',
            '9 chân',
            '4 chân',
        ],
        'rightChoice': 3
    },
    {
        'question': 'con thỏ có mấy chân?',
        'choices': [
            '1 chân',
            '2 chân',
            '9 chân',
            '4 chân',
        ],
        'rightChoice': 1
    },
    {
        'question': 'con vịt có mấy chân?',
        'choices': [
            '1 chân',
            '3 chân',
            '9 chân',
            '2 chân',
        ],
        'rightChoice': 1
    }
]
# CREATE
# # quiz_collection.insert_one(data) # data -> dict
quiz_collection.insert_many(data) # data -> list

# READ
# quizzes = quiz_collection.find() # find all
# print(quizzes)
# for quiz in quizzes:
#     print(quiz)
query = {}
update = {
    '$unset': {
        'is_deleted': ''
    }
}
# quiz = list(quiz_collection.find())
# for q in quiz:
#     print(q["rightChoice"])
# quiz = list(quiz_collection.find({'updated': 9999999}))
# print(quiz)
quiz_collection.find_one_and_update(query, update)
# quiz = quiz_collection.find_one(query)
# print(quiz)
# quiz_collection.delete_many(query)
quizzes = quiz_collection.find({'is_deleted': False, 'is_deleted': {'$exists': False}})
for q in quizzes:
    print(q)