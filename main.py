import requests, vk_api, checkmes, captcha_h, user_vk
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

#captcha_h.captcha_handler(captcha)

session = requests.Session()

vk_session = user_vk.vk_session     # в user_vk.py ввести данные страницы
vk_session.auth(token_only=True)    # вход и только по токену

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

print("I'm in.")    # зашел
    
for event in longpoll.listen(): # постоянная проверка диалога на наличие новых сообщений
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:    # если НОВОЕ СООБ и МНЕ и ТЕКСТ
        print('id{}: "{}"'.format(event.user_id, event.text), end=' ')  # в консоль выводим ID и текст отправителя сообщения
        
        text = str(event.text)                  # текст в строку
        textl = len(text.split(' '))            # количество слов (через пробел)
        userid = '{}'.format(event.user_id)     # юсер id
        ranid = get_random_id()                 # случайный id сообщений

        checkmes.check(vk, text, textl, userid, ranid) # тут def check --> checkmes.py

        print(' ') # чтобы в консоли текст шёл вниз, а не в строчку
