from pymongo import MongoClient

client = MongoClient()
database = client.get_database('D4E16')
quiz_collection = database.get_collection('quizzes')

input_question = input('enter question ')
input_choices = input('enter choices ').split(',')
input_right_choices = int(input('which one is right? ')) - 1

quiz_data = {
    'question': input_question,
    'choices': input_choices,
    'rightChoice': input_right_choices
}
print(quiz_data)
quiz_collection.insert_one(quiz_data)