import random

N1 = [[1, 1] for j in range(11)]
N2 = [[1, 1] for j in range(11)]
N1_W = 0
N2_W = 0
g_or_n = "n"
ex = 0
position_player = -1
to_end = 100
while ex == 0:
    stones = 11
    print(to_end)

    if g_or_n == "n":

        N1_moves = [-1 for j in range(11)]
        N2_moves = [-1 for j in range(11)]
        who_walk = -1
        while True:
            if who_walk < 0:
                step = random.randint(1, N1[stones - 1][0] + N1[stones - 1][1])
                if step > N1[stones - 1][0]:
                    N1_moves[stones - 1] = 1
                    stones -= 2
                else:
                    N1_moves[stones - 1] = 0
                    stones -= 1
            else:
                step = random.randint(1, N2[stones - 1][0] + N2[stones - 1][1])
                if step > N2[stones - 1][0]:
                    N2_moves[stones - 1] = 1
                    stones -= 2
                else:
                    N2_moves[stones - 1] = 0
                    stones -= 1

            if stones <= 0:
                if who_walk < 0:

                    N1_W += 1
                    for i in range(11):
                        if N1_moves[i] != -1:
                            N1[i][N1_moves[i]] += 1
                    for i in range(11):
                        if N2_moves[i] != -1:
                            N2[i][N2_moves[i]] -= 1
                            if N2[i][N2_moves[i]] <= 0:
                                N2[i][N2_moves[i]] = 1
                else:
                    N2_W += 1
                    for i in range(11):
                        if N2_moves[i] != -1:
                            N2[i][N2_moves[i]] += 1
                    for i in range(11):
                        if N1_moves[i] != -1:
                            N1[i][N1_moves[i]] -= 1
                            if N1[i][N1_moves[i]] <= 0:
                                N1[i][N1_moves[i]] = 1
                break
            who_walk *= -1
        print(N1_W, N2_W, (N1_W+1)/(N2_W+1+N1_W)*100)
        to_end -= 1
        if to_end <= 0:
            print("прошло 100 игр, для продолжения обучения введите n, а для игры введите g")
            
            g_or_n = input()
            to_end = 100
    else:
        print("Выберети 1 или 2 вы будете ходить")
        position_player = int(input())
        if position_player == 1:
            who_walk = -1
            while True:
                if who_walk < 0:
                    print("Осталось", stones, "камней")
                    print("Ваш ход! Возьмите 1 или 2 камня.")
                    stones -= int(input())
                else:
                    print("Осталось", stones, "камней")
                    print("Ход нейросети")
                    step = random.randint(1, N2[stones - 1][0] + N2[stones - 1][1])
                    if step > N2[stones - 1][0]:
                        print("Нейросеть взяла 2 камня")
                        N2_moves[stones - 1] = 1
                        stones -= 2
                    else:
                        print("Нейросеть взяла 1 камень")
                        N2_moves[stones - 1] = 0
                        stones -= 1

                if stones <= 0:
                    if who_walk < 0:
                        print("Вы победили!")

                    else:
                        print("Вы проиграли!")
                    break
                who_walk *= -1
            print("продолжения обучения введите n, а для игры введите g")
            g_or_n = input()
        else:
            who_walk = -1
            while True:
                if who_walk > 0:
                    print("Осталось", stones, "камней")
                    print("Ваш ход! Возьмите 1 или 2 камня.")
                    stones -= int(input())
                else:
                    step = random.randint(1, N1[stones - 1][0] + N1[stones - 1][1])
                    if step > N1[stones - 1][0]:
                        N1_moves[stones - 1] = 1
                        stones -= 2
                    else:
                        N1_moves[stones - 1] = 0
                        stones -= 1

                if stones <= 0:
                    if who_walk > 0:
                        print("Вы победили!")

                    else:
                        print("Вы проиграли!")
                    break
                who_walk *= -1
            print("продолжения обучения введите n, а для игры введите g")
            g_or_n = input()
