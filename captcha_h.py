def captcha_handler(captcha):
    
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи"""
    
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    
    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)