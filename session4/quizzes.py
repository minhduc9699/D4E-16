from pymongo import MongoClient

client = MongoClient()
database = client.get_database('D4E16')
quiz_collection = database.get_collection('quizzes')
result_collection = database.get_collection('results')

register = input('enter your nickname: ')
quizzes = quiz_collection.find()
total_quiz = quiz_collection.count()
count = 0
for quiz in quizzes:
    print(quiz['question'])
    choices = quiz['choices']
    for i in range(len(choices)):
        print(f'{i+1}. {choices[i]}')
    user_choice = int(input('Enter your choice ')) - 1
    if user_choice == quiz['rightChoice']:
        count += 1
    else:
        print('buồn quá')

score = count / total_quiz * 100
result_data = {
    'username': register,
    'score': score
}
result_collection.insert_one(result_data)
