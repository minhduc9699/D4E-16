quizzes = [ # collection 
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
        'rightChoice': 3
    }
]
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

score = count / len(quizzes) * 100
print(f'Score: {score}%')
