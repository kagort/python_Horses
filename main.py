def game():

    money = 100

    print(f"Привет, игрок! У тебя в кармане {money} долларов.")
    list1 = [2, 3, 4, 5, 6, 7, 8, 9]
    a = int(input("Выбери размер ипподрома. (Введи число от 2 до 9): "))
    while a not in list1:
        print("Введи корректный размер!")
        a = int(input("Выбери размер ипподрома. (Введи число от 2 до 9): "))
    print(f"Итак, размер ипподрома - {a}")

    list2 = list(range(111, 1000))
    b = int(input ("Выбери породу лошадей. Введи любое трехзначное число от 111 до 999:___"))
    while b not in list2:
        print ("Не бывает такой породы лошадей! Введи корректное число.")
        b = int(input("Выбери породу лошадей. Введи любое трехзначное число от 111 до 999:___"))
    print(f"О! Отличный выбор! Ты будешь смотреть скачки породы {b}")

    c = int(input("Осталось выбрать номер лошади и сумму ставки!"
                  "В забеге участвует 10 лошадок. Введи номер лошади, на которую  ты будешь ставить (от 0 до 9):_"))
    list3 = [0,1,2,3,4,5,6,7,8,9]
    while c not in list3:
        print ("Выбери правильный номер!")
        c = int(input ("Введи номер лошади, на которую  ты будешь ставить (от 0 до 9):_"))
    print(f"Прекрасно! Ты выбрал лошадь под номером {c}")
    d = int(input("Введи сумму твоей ставки:_"))
    while d > money:
        print("Боюсь, ты хочешь нас обмануть. Введи корректную сумму!")
        d = int(input("Введи сумму твоей ставки:_"))
    print("Старт дан!")

    print("Вот как красиво скачут лошади!")
    print(a**b)
    track = str(a**b)

    print("Количество цифр в этом прекрасном числе равно", len(track))

    one = (1, int(str(track).count('1')))
    print(F'Лошадь под №{one[0]} получила', int(str(track).count('1')),"баллов.")
    two = (2, str(track).count('2'))
    print(f'Лошадь под №{two[0]} получила', int(str(track).count('2')),"баллов.")
    three = (3, int(str(track).count('3')))
    print(f'Лошадь под №{three[0]} получила', int(str(track).count('3')),"баллов.")
    four = (4, int(str(track).count('4')))
    print(f'Лошадь под №{four[0]} получила', int(str(track).count('4')),"баллов.")
    five = (5, int(str(track).count('5')))
    print(f'Лошадь под №{five[0]} получила', int(str(track).count('5')),"баллов.")
    six = (6, int(str(track).count('6')))
    print(f'Лошадь под №{six[0]} получила', int(str(track).count('6')),"баллов.")
    seven = (7, int(str(track).count('7')))
    print(f'Лошадь под №{seven[0]} получила', int(str(track).count('7')),"баллов.")
    eight = (8, int(str(track).count('8')))
    print(f'Лошадь под №{eight[0]} получила', int(str(track).count('8')),"баллов.")
    nine = (9,  int(str(track).count('9')))
    print(f'Лошадь под № {nine[0]} получила', int(str(track).count('9')),"баллов.")
    zero = (0, int(str(track.count('0'))))
    print(f'Лошадь под №{zero[0]} получила', int(str(track).count('0')),"баллов.")

    horse_numbers = (one[0], two[0], three[0], four[0], five[0], six[0], seven[0], eight[0], nine[0], zero[0])
    horse_list = (one, two, three, four, five, six, seven, eight, nine, zero)
    horse_notes =  (one[1], two[1], three[1], four[1], five[1], six[1], seven[1], eight[1], nine[1], zero[1])

    for tuple in horse_list:
        if c == tuple[0]:
            e = (tuple[1])
    print(f"Твоя лощадь под №{c} набрала {e} баллов!")
    h = sorted(horse_notes, reverse=True)[:3]
    print(f"Баллы победилей: {h}")

    if e == h[0] or e==h[1] or e==h[2]:
        print ("Твоя лошадь вошла тройку лидеров. Ты выиграл!")

    if e==h[0] and h[0]>h[1]:
        winnings = (money-d) + d*10
        print(f"Ты получил {d*10} долларов. Теперь у тебя в кармане {winnings} долларов.")
    elif e==h[0] and h[0]==h[1]:
        winnings = (money-d) + d * 7
        print(f"Ты получил {d * 7} долларов. Теперь у тебя в кармане {winnings} долларов.")
    elif e==h[1] and h[1]!= h[0]:
        winnings = (money-d) + d * 5
        print(f"Ты получил {d * 5} долларов. Теперь у тебя в кармане {winnings} долларов.")
    elif e==h[2]:
        winnings = (money-d) * 3
        print(f"Ты получил {d * 3} долларов. Теперь у тебя в кармане {winnings} долларов.")
    else:
        winnings = money - d
        print(f"Увы, ты проиграл! Теперь у тебя в кармане {winnings} долларов.")
game()
while True:
    flag = input('Сыграем ещё раз? [да/нет]: ')

    if flag == 'да':
        game()
    else:
        break






