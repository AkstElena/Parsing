import json

with open('steam_games.json', 'r', encoding="utf-8") as datafile:
    datastore = json.load(datafile)
    print(len(datastore))

    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(datastore, f, ensure_ascii=False, indent=4)
    list_1 = {}
    list_2 = {}
    list_3 = {}
    list_4 = {}
    list_5 = {}
    for n, details in enumerate(datastore):
        if n < 11000:
            list_1[details] = datastore[details]
        elif n < 23000:
            list_2[details] = datastore[details]
        elif n < 35000:
            list_3[details] = datastore[details]
        elif n < 46000:
            list_4[details] = datastore[details]
        else:
            list_5[details] = datastore[details]

    with open('steam_games_1.json', 'w', encoding='utf-8') as f:
        json.dump(list_1, f, ensure_ascii=False)

    with open('steam_games_2.json', 'w', encoding='utf-8') as f:
        json.dump(list_2, f, ensure_ascii=False)

    with open('steam_games_3.json', 'w', encoding='utf-8') as f:
        json.dump(list_3, f, ensure_ascii=False)

    with open('steam_games_4.json', 'w', encoding='utf-8') as f:
        json.dump(list_4, f, ensure_ascii=False)

    with open('steam_games_5.json', 'w', encoding='utf-8') as f:
        json.dump(list_5, f, ensure_ascii=False)
