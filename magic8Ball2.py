import random

answers = ['It is certain', 'It is decidedly so', 'Yes', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very Doubtful']

answers.insert(3, 'Are you crazy?!')

print(answers)
print(random.choice(answers))