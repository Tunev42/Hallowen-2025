while True:
    print("Привет мой друг куда сегодня пойдём?")
    print("Введите 'дом ведьмы' или 'в заброшку'?")
    hallowen = input()
    if hallowen == "в заброшку":
        print("эх к сожелению там сегодня охраник '\n' "
              "дежурит не получиться может пойдём в дом ведьмы? (введите дом ведьмы)"'\n')
        if hallowen == "дом ведьмы":
            print("Ты зашол в дом ведьмы но за тобой закрылась'\n'"
              " дверь и твой друг остался на улице '\n'"
              "чтобы выбраться из дома вам нужно '\n'"
              "найти 4 компонента (яд змеи лапка летучей мыши'\n'"
              "глаз дракона и слеза кота) для зелья они находять в доме найдите их '\n'"
              "чтобы снять чары с дома и выйти из него'\n'")
            print("Куда ты хочешь пойти в зал или в коридор")
            break
    elif hallowen == "дом ведьмы":
        print("Ты зашол в дом ведьмы но за тобой закрылась'\n'"
              " дверь и твой друг остался на улице '\n'"
              "чтобы выбраться из дома вам нужно '\n'"
              "найти 4 компонента (яд змеи лапка летучей мыши'\n'"
              " глаз дракона и слеза кота) для зелья они находять в доме найдите их '\n'"
              "чтобы снять чары с дома и выйти из него'\n'")
        print("Куда ты хочешь пойти в зал или в коридор")
        break
    else:
        print("Введите ('в заброшку' или 'дом ведьмы')")
        continue
hallowen2 = input()
print("Куда ты хочешь пойти в зал или в коридор")
if hallowen2 == "зал":
        print("Вы пришли в зал осмотритесь")
        print("Вы что нибудь нашли?")
        quest1 = input()
        print("Вы нашли что-то?('да' или 'нет')")
        if quest1 == "да":
            print("Хм оно находиться у вороны в клетке'\n'"
                  "вам нужено как то его отвлечь'\n'"
                  "я думую тебе нужено корм для птиц'\n'"
                  "сделай это задание чтобы получить корм для птиц'\n'")
            print("Держи справочник слов:"
                  "bat pumpkin zombie hunted house ghost witch'\n'"
                  " skeleton monster potion skull werewolf'\n'"
                  "I am going to 1)... and I see a 2)... .'\n'"
                  "When I am sleeping, 3)... was fly in front of my windows. '\n'"
                  "My mom cuts face on 4)... .'\n'"
                  "When I am walking I see 5)... and 6)... and 7)... and 8)... .'\n'"
                  "When I am going to bed my brother scared me with a 9)... .'\n'"
                  "I am walking on the forest and I see 10)... .'\n'"
                  "I spelling 11)... in my room.'\n'"
                  "My family dress costumes 12)... and spook me.'\n'")
            a = input()
            b = input()
            c = input()
            d = input()
            e = input()
            f = input()
            g = input()
            h = input()
            i = input()
            j = input()
            k = input()
            if a and b and c and d and e and f and g and h and i and j and k and l == "hunted house" and "ghost" and "bat" and "pumpkin" and "zombie" and "witch" and "skeleton" and "monster" and "potion" and "skull" and "werewolf":
                print("Молодец вы получили 'Корм для птиц'")
        elif quest1 == "нет":
            print("Посмотрите по внимательней :)")
        else:
            print("Введите с маленькой буквы 'да' или 'нет'")

elif hallowen2 == "коридор":
    print("Вы пришли в коридор осмотритесь")
    print("Вы что нибудь нашли?")
    if quest1 == "да":
            print("Хм оно находить высоко вам нужно решить'\n'"
                  "задание чтобы получить лестницу и достать предмет'\n'")
            print("Держи справочник слов:"
                  "bat pumpkin zombie hunted house ghost witch'\n'"
                  "skeleton monster potion skull werewolf'\n'"
                  "I am going to 1)... and I see a 2)... .'\n'"
                  "When I am sleeping, 3)... was fly in front of my windows. '\n'"
                  "My mom cuts face on 4)... .'\n'"
                  "When I am walking I see 5)... and 6)... and 7)... .'\n'"
                  "When I am going to bed my brother scared me with a 8)... .'\n'"
                  "I am walking on the forest and I see 9)... .'\n'"
                  "I spelling 10)... in my room.'\n'"
                  "My family dress costumes 11)... and spook me.'\n'")
            a = input()
            b = input()
            c = input()
            d = input()
            e = input()
            f = input()
            g = input()
            h = input()
            i = input()
            j = input()
            k = input()
            l = input()
            if a and b and c and d and e and f and g and h and i and j and k and l == "hunted house" and "ghost" and "bat" and "pumpkin" and "zombie" and "witch" and "skeleton" and "monster" and "potion" and "skull" and "werewolf":
                print("Молодец вы получили 'Лестницу'")
    elif quest1 == "нет":
            print("Посмотрите внимательней :)")
    else:
            print("Введите с маленькой буквы 'да' или 'нет'")