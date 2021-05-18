import vk_api
vk_session = vk_api.VkApi(
    login = '89174388525',	# логин ВК
    password = 'Termot228',	# пароль ВК
    token = 'dcd273c3ae6cb14a93cd300a76f11876da2a4b828aa506eb53f2a90836cc52a8de4008b7bf6991f1a200f', # токен с правами на отправку сообщений
    app_id = 2685278,   # app - kate mobile
    #captcha_handler=captcha_handler # капча
    )