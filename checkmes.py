def check(vk, text, textl, userid, ranid):

    data = []
    with open("jokeses.txt", encoding = 'utf-8') as jokes:  # открываем файл в кодировке utf-8
        data = jokes.readlines()                            # заполяем список построчно 

    for i in range(len(data)):                  # убираем
        if '\n' in data[i]:                     # ненужное
            data[i] = data[i].replace('\n', '') # \n

    joke = []
    anwer = []
    temp = []

    for i in range(len(data)):
        temp.append(data[i].split('=='))    # разделяем список на ДО == и ПОСЛЕ ==
        joke.append(temp[i][0])             # список слов, на которую надо дать рифму
        anwer.append(temp[i][1:])           # список рифм на слово

    if textl == 1:  # всего одно слово
        for element in text.split(' '): # это одно слово в список
            for i in range(len(data)):
                if joke[i].casefold()==element.casefold():  # проверяем, есть ли в списке joke слово из списка text

                    numj = i

                    vk.messages.send(       # отправляем
                    user_id=userid,         # подколку
                    random_id=ranid,        # на
                    message=anwer[numj]     # слово
                    )
