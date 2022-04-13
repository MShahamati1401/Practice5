import random

player_1 = {
    "name": " ",
    "color": " ",
    "rows": " ",
    "cols": " ",
    "symbol": "X"
}
player_2 = {
    "name": " ",
    "color": " ",
    "rows": " ",
    "cols": " ",
"symbol": "O"
}
list_players = [player_1, player_2]
list_colors = ["\33[92m", "\33[93m", "\33[94m", "\33[91m"]
list_rows_cols = ["1", "2", "3"]
list_game = [
                ["_", "_", "_"],
                ["_", "_", "_"],
                ["_", "_", "_"],
            ]
def check_status(list_game, name, symbol):
    status_1 = True
    status_2 = True
    status_3 = True
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                if list_game[i][j] != symbol:
                    status_1 = False
            if list_game[i][j] != symbol:
                status_2 = False
            if list_game[j][i] != symbol:
                status_3 = False
        if status_2 or status_3:
            print(f"WINNER {name}")
            return True
        status_2 = True
        status_3 = True
    if status_1:
        print(f"WINNER {name}")
        return True
    len_list = 3
    status_4 = True
    for b in range(0, 3):
        len_list -= 1
        if list_game[b][len_list] != symbol:
            status_4 = False
    if status_4:
        print(f"WINNER {name}")
        return True
    return False

def check_list(list_final):
    check_list = False
    for ro in range(3):
        for col in range(3):
            if list_final[ro][col] == "_":
                check_list = True
                return True
            else:
                check_list = False
    return check_list

print("1- One Player")
print("2- Two Player")
print("Inter Green Colors Code: 3 ")
print("Inter Yellow Colors Code: 4 ")
print("Inter Blue Colors Code: 5 ")
print("Inter Red Colors Code: 6 ")
while True:
    num_team = int(input("Select Numbers Team: "))
    if 1 <= num_team <= 2:
        for i in range(num_team):
            list_players[i]["name"] = input(f"Please Inter Name Player{i + 1}: ")
            while True:
                color_code = int(input(f"Please Inter Colors Code Player{i + 1}: "))
                if 3 <= color_code <= 6:
                    list_players[i]["color"] = list_colors[color_code - 3]
                    if list_players[0]["color"] != list_players[1]["color"]:
                        pass
                    else:
                        continue
                    break
                else:
                    print("Invalid Colors Code, Try again")
                    continue
        if num_team == 1:
            list_players[1]["name"] = "Computer"
            list_players[1]["color"] = random.choice(list_colors)
        break
end_game = False
while True:
    for i in range(num_team):
        if check_list(list_game) != True:
            print(f"Game Equal")
            exit()
        print(f"Start Player{i + 1}: ")
        while True:
            rows = int(input(f"Please Inter rows Player{i + 1}: "))
            cols = int(input(f"Please Inter cols Player{i + 1}: "))
            if 1 <= rows <= 3 and 1 <= cols <= 3 and list_game[rows - 1][cols - 1] == "_":
                list_game[rows - 1][cols - 1] = list_players[i]["symbol"]
                if check_status(list_game, list_players[i]["name"], list_players[i]["symbol"]):
                    end_game = True
                # Show List_Game
                for i in range(3):
                    for j in range(3):
                        if list_game[i][j] == "X":
                            print(list_players[0]["color"] + list_game[i][j] + "\033[5m", end="\t")
                        if list_game[i][j] == "O":
                            print(list_players[1]["color"] + list_game[i][j] + "\033[5m", end="\t")
                        if list_game[i][j] == "_":
                            print("\033[5m" + list_game[i][j] + "\033[5m", end="\t")
                    print("\n")
                if end_game:
                    exit()
                break
            else:
                print("Invalid rows and cols OR used rows and cols, Please try again")
                continue

    if num_team == 1:
        if check_list(list_game) != True:
            print(f"Game Equal")
            exit()
        print("Start Computer")
        while True:
            rows = random.randint(0, 2)
            cols = random.randint(0, 2)
            if list_game[rows][cols] == "_":
                list_game[rows][cols] = list_players[1]["symbol"]
                # Show List_Game
                for i in range(3):
                    for j in range(3):
                        if list_game[i][j] == "X":
                            print(list_players[0]["color"] + list_game[i][j] + "\033[5m", end="\t")
                        if list_game[i][j] == "O":
                            print(list_players[1]["color"] + list_game[i][j] + "\033[5m", end="\t")
                        if list_game[i][j] == "_":
                            print("\033[5m" + list_game[i][j] + "\033[5m", end="\t")
                    print("\n")
                break
            else:
                continue
        if check_status(list_game, list_players[1]["name"], list_players[1]["symbol"]):
            exit()