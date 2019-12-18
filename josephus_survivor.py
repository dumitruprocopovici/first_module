def josephus_survivor(number_of_players, coeficient):
    if coeficient > 1:
        change = 0
        new_list = []
        list_of_players = list(range(1, number_of_players+1))
        while len(list_of_players) > 1:
            for i in list_of_players:
                change += 1
                if change == coeficient:
                    change = 0
                    new_list.append(i)
            for i in new_list[::-1]:
                list_of_players.remove(i)
            new_list = []
        return int(list_of_players[0])
    else:
        return number_of_players


print(josephus_survivor(7, 3))
