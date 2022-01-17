game = {
    "top": {'tl': '-', 'tm': '-', 'tr': '-'},
    "middle": {'ml': '-', 'mm':'-', 'mr':'-'},
    "buttom": {'bl': '-', 'bm': '-', 'br': '-'}
}

allowed_input = ['x', 'o']
allowed_combination_x = ('x', 'x', 'x')
allowed_combination_o = ('o', 'o', 'o')
available_positions = ["top-left", "top-middle", "top-right", "middle-left",
 "middle-middle", "middle-right", "buttom-left", "buttom-middle", "buttom-right"]

winner = False
previous_player = None


def check_winner_x():
    #Horizontal Combinations
    if (game['top']['tl'], game['top']['tm'], game['top']['tr']) == allowed_combination_x:
        return "player x wins"
    elif (game['middle']['ml'], game['middle']['mm'], game['middle']['mr']) == allowed_combination_x:
        return "player x wins"
    elif (game['buttom']['bl'], game['buttom']['bm'], game['buttom']['br']) == allowed_combination_x:
        return "player x wins"

    #Vertical combinations
    if (game['top']['tl'], (game['middle']['ml']), game['buttom']['bl']) == allowed_combination_x:
        return "player x wins"
    elif (game['top']['tm'], game['middle']['mm'], game['buttom']['bm']) == allowed_combination_x:
        return "player x wins"
    elif (game['top']['tr'], game['middle']['mr'], game['buttom']['br']) == allowed_combination_x:
        return "player x wins"

    #Diagonal combinations 
    if (game['top']['tl'], game['middle']['mm'], game['buttom']['br']) == allowed_combination_x:
        return "player x wins"
    elif (game['top']['tr'], game['middle']['mm'], game['buttom']['bl']) == allowed_combination_x:
        return "player x wins"


def check_winner_o():
    #Horizontal Combinations
    if (game['top']['tl'], game['top']['tm'], game['top']['tr']) == allowed_combination_o:
        return "player o wins"
    elif (game['middle']['ml'], game['middle']['mm'], game['middle']['mr']) == allowed_combination_o:
        return "player o wins"
    elif (game['buttom']['bl'], game['buttom']['bm'], game['buttom']['br']) == allowed_combination_o:
        return "player o wins"

    #Vertical combinations
    if (game['top']['tl'], (game['middle']['ml']), game['buttom']['bl']) == allowed_combination_o:
        return "player o wins"
    elif (game['top']['tm'], game['middle']['mm'], game['buttom']['bm']) == allowed_combination_o:
        return "player o wins"
    elif (game['top']['tr'], game['middle']['mr'], game['buttom']['br']) == allowed_combination_o:
        return "player o wins"

    #Diagonal combinations 
    if (game['top']['tl'], game['middle']['mm'], game['buttom']['br']) == allowed_combination_o:
        return "player o wins"
    elif (game['top']['tr'], game['middle']['mm'], game['buttom']['bl']) == allowed_combination_o:
        return "player o wins"



while winner != True:
    for v in available_positions:
        print(f"Pick {available_positions.index(v)} to play {v}")

    try:
        position = int(input("enter a number corresponding to the position you'd like to play: "))
    except ValueError as err:
        print('enter a valid number')

    player_input = input("What are you playing X or O:").lower()


    if player_input in allowed_input and available_positions[position] and previous_player != player_input:
        if available_positions[position].startswith('t'):
            game["top"][available_positions[position]] = player_input
            available_positions.remove(available_positions[position])
            previous_player = player_input
            try:
                if check_winner_x().lower() == "player x wins":
                    print(check_winner_x())
                    winner = True
                elif check_winner_o().lower() == "player o wins":
                    print(check_winner_o())
                    winner = True
            except Exception as err:
                pass

        elif available_positions[position].startswith('m'):
            game["middle"][available_positions[position]] = player_input
            available_positions.remove(available_positions[position])

            try:
                if check_winner_x().lower() == "player x wins":
                    print(check_winner_x())
                    winner = True
                elif check_winner_o().lower() == "player o wins":
                    print(check_winner_o())
                    winner = True
            except Exception as err:
                pass       

        else:
            game["buttom"][available_positions[position]] = player_input
            available_positions.remove(available_positions[position])

            try:
                if check_winner_x().lower() == "player x wins":
                    print(check_winner_x())
                    winner = True
                elif check_winner_o().lower() == "player o wins":
                    print(check_winner_o())
                    winner = True
            except Exception as err:
                pass
    else:
        print("invalid input!")
        break
    print(game)
