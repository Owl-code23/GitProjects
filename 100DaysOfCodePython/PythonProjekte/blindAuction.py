from arts.blind_action_art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
participant = {}
repeat = True

print(logo)

def compare_bids(dict_bids):
    winner = ""
    max_value = 0

    for key in dict_bids:
        if dict_bids[key] > max_value:
            max_value = dict_bids[key]
            winner = key

    print(f"The winner is {winner} with a bid of {dict_bids[winner]}")

while repeat:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    participant[name] = bid
    want_to_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if want_to_continue == 'no':
        repeat = False
        compare_bids(participant)
    else:
        print("\n" * 100)
