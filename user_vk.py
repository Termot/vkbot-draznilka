import vk_api
vk_session = vk_api.VkApi(
    login = '',	# логин ВК
    password = '',	# пароль ВК
    token = '', # токен с правами на отправку сообщений
    app_id = 2685278,   # app - kate mobile
    #captcha_handler=captcha_handler # капча
    )