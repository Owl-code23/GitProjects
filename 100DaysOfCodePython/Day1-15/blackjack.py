import random
from arts_and_data.blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw(deck):
    """Adds a card from cards to the list
     and also turn 11 into 1 if the list has a score over 21"""
    deck.append(random.choice(cards))
    while sum(deck) > 21:
        if 11 in deck:
            y = deck.index(11)
            deck[y] = 1
        else:
            return

def output_final_scores(player, computer):
    """Outputs player's and computer's final scores"""
    print(f"   Your final hand: {player}, final score: {sum(player)}")
    print(f"   Computer's final hand: {computer}, final score: {sum(computer)}")


def output_result(player, computer):
    """Outputs the end result"""
    if sum(computer) > 21:
        print("Opponent went over. You win \N{grinning face}")
    elif sum(player) == sum(computer):
        print("Draw \N{upside-down face}")
    elif sum(player) > sum(computer):
        print("You win \N{grinning face with smiling eyes}")
    elif sum(player) < sum(computer):
        print("You lose 😤")


def blackjack():
    """A Game of Blackjack"""
    print(logo)
    player_cards = []
    computer_cards = []

    for _ in range(2):
        draw(player_cards)
        draw(computer_cards)

    if sum(computer_cards) == 21:
        output_final_scores(player_cards, computer_cards)
        print("Opponent wins with a Blackjack \N{loudly crying face}")
        return
    elif sum(player_cards) == 21:
        output_final_scores(player_cards, computer_cards)
        print("Win with a Blackjack \N{smiling face with sunglasses}")
        return

    wants_to_draw = True
    while wants_to_draw:
        print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        card_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if card_or_pass == 'y':
            draw(player_cards)
            if sum(player_cards) > 21:
                output_final_scores(player_cards, computer_cards)
                print("You went over. You lose \N{loudly crying face}")
                return
        else:
            wants_to_draw = False

    while sum(computer_cards) <= 16:
        draw(computer_cards)

    output_final_scores(player_cards, computer_cards)
    output_result(player_cards, computer_cards)


wants_to_play = True

while wants_to_play:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice == "y":
        print("\n" * 20)
        blackjack()
    else:
        wants_to_play = False
