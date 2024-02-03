import random
def roll_dice():
    return random.randint(1, 6)
def play_dice_game(player_1, player_2):
    player_1_score = 0
    player_2_score = 0
    for round_number in range(1,6):  
        dice1_result = roll_dice()
        dice2_result = roll_dice()
        player_1_score += dice1_result
        player_2_score += dice2_result
        print(f"Round: {round_number} - {player_1} rolled {dice1_result}, {player_2} rolled {dice2_result}")
    print("\nGame Results:")
    print(f"{player_1}'s Total Score: {player_1_score}")
    print(f"{player_2}'s Total Score: {player_2_score}")
    if player_1_score > player_2_score:
        print(f"{player_1} wins!")
    elif player_1_score < player_2_score:
        print(f"{player_2} wins!")
    else:
        print("It's a tie!")
player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")
play_dice_game(player1_name, player2_name)
