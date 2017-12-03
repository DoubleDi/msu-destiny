# -*- coding: utf-8 -*-
import os
import django
import imghdr
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re
from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author

s = 0
def parse(list, paste):
    # print(list)
    # f.add(list)
    for i in list:
        path = paste + "/" + i
        if os.path.isfile(path) and imghdr.what(path) != None:
            parse_photo(path)

        elif os.path.isdir(path):
            parse(os.listdir(path), path)

    return

def parse_photo(path):
    photo = path[len("media/"):]
    # print(path)
    path_sorted = path[:path.rfind(".jpg")] + "_sorted.txt"
    path1 = path[:path.rfind(".jpg")] + ".txt"
    # print(path)
    if os.path.isfile(path1) == True:
        with open(path1, 'r') as f:
            text = f.read()
        date = get_date(path1)
        # photo = path[len("media/"):path.rfind(".txt")] + ".jpg"
        # substr = path[path.rfind("/") + 1 : path.rfind(".txt")]
        with open(path_sorted, 'r') as f:
            all = f.readlines()
        # print(photo)
        substr = all[1][:-1]
        place = all[3][:-1]
        author1 = all[0][3:-1]
        # print(date)
        # if len(substr) > len("Геологическая разведка в районе действующего рудни"):
        #     print(substr)
        if "Верхнемеловой палеоландшафт с хищными и травоядным" in substr:
            substr = "Верхнемеловой палеоландшафт с хищными и травоядным"
        elif "Геологическая разведка в районе действующего рудни" in substr:
            substr = "Геологическая разведка в районе действующего рудни"
        elif "Палеоландшафт ледникового периода с мамонтами(Сиби" in substr:
            substr = "Палеоландшафт ледникового периода с мамонтами(Сиби"
        elif "Разработка огнеупорных плит Часов-Ярского месторож" in substr:
            substr = "Разработка огнеупорных плит Часов-Ярского месторож"
        elif "Люди нижнего палеолита на фоне ландшафта того врем" in substr:
            substr = "Люди нижнего палеолита на фоне ландшафта того врем"
        elif "Ландшафт Айлайской долины в эпоху древнего оледене" in substr:
            substr = "Ландшафт Айлайской долины в эпоху древнего оледене"
        elif "Вход в большие камеры Ленинабадского рудника Кан-и" in substr:
            substr = "Вход в большие камеры Ленинабадского рудника Кан-и"
        elif "Выступление Калинина на заседании ученого совета м" in substr:
            substr = "Выступление Калинина на заседании ученого совета м"
        elif "Н.И.Лобачевский читает лекцию в Казанском Универси" in substr:
            substr = "Н.И.Лобачевский читает лекцию в Казанском Универси"
        elif "Н.Е.Жуковский демонстрирует опыты на аэродинамичес" in substr:
            substr = "Н.Е.Жуковский демонстрирует опыты на аэродинамичес"
        elif "Перемычка главного котлована на строительстве Куйб" in substr:
            substr = "Перемычка главного котлована на строительстве Куйб"
        elif "Подписание соцдоговора бригадой нефтяников мастера" in substr:
            substr = "Подписание соцдоговора бригадой нефтяников мастера"
        elif "Мореный ландшафт в северной части Московской облас" in substr:
            substr = "Мореный ландшафт в северной части Московской облас"
        elif "Известковая корка на прибрежных скалах на озере Се" in substr:
            substr = "Известковая корка на прибрежных скалах на озере Се"
        elif "Озеро Миассово на южном Урале.Ильменский заповедни" in substr:
            substr = "Озеро Миассово на южном Урале.Ильменский заповедни"
        elif "Ленин выступает перед рабочими на Дворцовой площад" in substr:
            substr = "Ленин выступает перед рабочими на Дворцовой площад"
        elif "Ф.А.Бредихин среди астрономов Московской обсервато" in substr:
            substr = "Ф.А.Бредихин среди астрономов Московской обсервато"
        # print(substr)
        # print(place)
        # check = Place.objects.get(name__contains=place)
        # # print(author1)
        # author = Author.objects.filter(name=author1)
        # author = author[0]
        # item = DestinyObject.objects.filter(name = substr, place = check, author = author)
        # # print(item[0])
        # item = item[0]
        # PhotoItem.objects.create(
        #     photo=photo,
        #     # предварительно на сервер в папочку media надо залить фотки и в photo надо записать путь относительно папочки media
        #     info=text,  # просто весь текст который мы печатали
        #     photo_item=item,  # обьект культурного достояния
        #     # или photo_item = DestinyObject.objects.get(id = id),
        #     date=date  # год в формате строки например 1964
        # )
        # print(photo, substr, date)
    else:
        print(photo)
        name = path[path.rfind("/") + 1:path.rfind(".jpg")]
        place = path[len("media/"):]
        place = place[:place.find("/")]
        print(name)
        print(place)
        print()
        if "Инвентиризационый список художественных произведен" in name:
            name = "Инвентиризационый список художественных произведен"
        # DestinyObject.objects.filter(name = name, author=Author.objects.get(name ="Неизвестный автор"), object_type=ObjectType.objects.get(name__contains="Картина"), place=Place.objects.get(name__contains = place)).delete()
        # DestinyObject.objects.create(
        #     name=name,  # Название картины
        #     author=Author.objects.get(name ="Неизвестный автор"),  # Автор - надо достать обьект автора из базы по имени
        #     # "name__contains" проверяет на подстроку( чтобы точно найти).
        #     # Важно что get должен вернуть 1 обьект иначе он упадет исключением для нескольких есть filter
        #     object_type=ObjectType.objects.get(name__contains="Картина"),
        #     date="",
        #     place=Place.objects.get(name__contains = place)
        # )
        # PhotoItem.objects.create(
        #     photo=photo,
        #     # предварительно на сервер в папочку media надо залить фотки и в photo надо записать путь относительно папочки media
        #     info="",  # просто весь текст который мы печатали
        #     photo_item=DestinyObject.objects.get(name = name, author=Author.objects.get(name ="Неизвестный автор"), object_type=ObjectType.objects.get(name__contains="Картина"), place=Place.objects.get(name__contains = place)),  # обьект культурного достояния
        #     # или photo_item = DestinyObject.objects.get(id = id),
        #     date=""  # год в формате строки например 1964
        # )
    return


def get_date(path):
    with open(path, 'r') as f:
        all = f.readlines()
    date = ""
    for i in all:

        b = re.findall('(\d+)', i)
        if b:
            for j in b:
                if len(j) == 4 and j[0] == '1' and  j[1] == '9'  and len(b) == 1 and i.find("к.") == -1 and i.find("ком.") == -1 and i.find("№") == -1:
                    date = j
                n = i.find(j + "г.")
                if n != -1:
                    if len(j) != 4:
                        date = "19" + j
                    else:
                        date = j
    return date

base = "media"
dir = os.listdir(base)
parse(dir, base)
# PhotoItem.objects.all().delete()
# PhotoItem.objects.all().delete()