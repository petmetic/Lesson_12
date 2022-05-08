from functions_guess_game import play_game, get_top_scores

while True:
    selection = input("Would you like t A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + "attempts, date:" + score_dict.get("date"))
    else:
        break