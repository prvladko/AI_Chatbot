BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', "Здравствуйте", "Хай!"],
            'responses': ['Прив!', 'Хеллоу', 'Как жизнь?']
        },
        'bye': {
            'examples': ['Пока!', 'До свидания!', 'Увидимся!!'],
            'responses': ['Чао!', 'Будь здоров', 'Сайонара']
    }
}

def get_intent(text):
    for intent in BOT_CONFIG['intents']:
        print(intent)

get_intent('')