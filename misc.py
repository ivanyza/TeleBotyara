import pickle as pk

with open('token.pk', 'rb') as file:
    TOKEN = pk.load(file)

WELCOME = "Дарова чукча!\n" \
          "Так, у нас короче тут анонимный чат лучше чем у\n" \
          "Варгасова пишется за рекордное время.\n" \
          "Юзни комманду '/new' для создания нового диалога"

ALREADY_WELCOME = "Эй, чукча!\n" \
                  "Ты как бы уже стартовал так что не трахай мне мозги,\n" \
                  "поспокойнее будь и юзай '/new'. Если собеседник начнет\n" \
                  "тебя так же задалбливать, как и ты меня успел задолбать," \
                  "\nчто маловероятно, но возможно, пиши /stop"

PRE_DISENGAGED = "Пользователь по ту сторону трубки отключился."
DISENGAGED_PROMPTS = [
    'Ха, Чукча, кажись тебя кинули! \nОтшили всмысле! Лох, короче.\n'
    'Ну, с кем не бывает.',
    'Чукча, тут гудки из трубки кажись, ты чего, опять людей пугаешь своими манерами?\n'
    'Слава богу я ботяра, будь я человеком меня бы от тебя тошнило.',
    'Разговорчивость не твой конек, да, Чукча?',
    'Тебя послали? Не обижайся, для тебя не впервой.'
]
POST_DISENGAGE = "Можешь начать новую сессию если захочешь.\n" \
                 "Команду для этого думаю помнишь."

PRE_DISENGAGE = "Вы отключились от пользователся по ту сторону трубки"
DISENGAGE_PROMPTS = [
    'Надеюсь ты теперь чувствуешь себя отвратительно.\n'
    'Наверняка они хотели почитать твои тупые сообщения еще пару минут, Чукча.',
    'Боже мой, наконец-то ты закончил этот ужас. Больше никому не пиши,\n'
    'я вырублюсь нахер от этого кринжа.',
]

FOUND = 'Очуметь, Чукча, я конечно верил в тебя, но не настолько! Ты нашел с кем поболтать! Боже, храни его нервы.'
STOP_SEARCH = 'Жалко мне тебя, никто с Чукчей говорить не хочет. Но на то ты и Чукча, собственно.'