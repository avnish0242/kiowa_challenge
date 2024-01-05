import random

class CardGame:
    """
    Class representing a simple card game.

    Attributes:
    - deck (list): A list representing the deck of playing cards.
    - players (list): A list containing the players and their respective hands.

    Methods:
    - initialize_deck(): Initializes the deck of playing cards.
    - deal_cards(): Shuffles the deck and deals three cards to each player.
    - evaluate_hand(hand): Evaluates the type of hand (trail, sequence, pair, high card).
    - compare_hands(hand1, hand2): Compares two hands to determine the winner.
    - play_game(): Orchestrates the entire game, from deck initialization to determining the winner.
    """

    def __init__(self):
        self.deck = []
        self.players = []

    def initialize_deck(self):
        """
        Initializes the deck of playing cards.
        """
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for rank in ranks:
            self.deck.extend([rank] * 4)  # Four cards for each rank

    def deal_cards(self):
        """
        Shuffles the deck and deals three cards to each player.
        """
        random.shuffle(self.deck)
        for _ in range(4):
            hand = [self.deck.pop() for _ in range(3)]
            self.players.append(hand)

    def evaluate_hand(self, hand):
        """
        Evaluates the type of hand.

        Args:
        - hand (list): A list representing a player's hand.

        Returns:
        - tuple: A tuple indicating the type of hand and the highest card value.
        """
        if self._is_trail(hand):
            return "Trail", self._get_numeric_value(hand[0])
        elif self._is_sequence(hand):
            return "Sequence", self._get_numeric_value(hand[2])
        elif self._is_pair(hand):
            return "Pair", self._get_numeric_value(hand[0])
        else:
            return "High Card", self._get_highest_card(hand)

    def compare_hands(self, hand1, hand2):
        """
        Compares two hands to determine the winner.

        Args:
        - hand1 (list): A list representing the first player's hand.
        - hand2 (list): A list representing the second player's hand.

        Returns:
        - bool: True if hand1 wins, False otherwise.

        The comparison is based on the preference order: trail > sequence > pair > highest card.
        If both hands have the same type, the comparison is done by evaluating the highest card among them.

        Note:
        - A trail is a hand with three cards of the same rank.
        - A sequence is a hand with cards in consecutive order.
        - A pair is a hand with two cards of the same rank.

        In case of a tie, the player with the higher card in the relevant category wins.
        """
        type1, value1 = self.evaluate_hand(hand1)
        type2, value2 = self.evaluate_hand(hand2)

        if type1 == type2:
            if value1 != value2:
                return value1 > value2
            else:
                return self._get_highest_card(hand1) > self._get_highest_card(hand2)
        else:
            type_order = {"Trail": 0, "Sequence": 1, "Pair": 2, "High Card": 3}
            return type_order[type1] < type_order[type2]

    def play_game(self):
        """
        Orchestrates the entire game, from deck initialization to determining the winner.

        Returns:
        - dict: A dictionary containing the players, winner details, and hand information.
        """
        self.initialize_deck()
        self.deal_cards()

        winner = None
        winning_hands = []

        for i, player in enumerate(self.players):
            print(f"Player {i + 1} hand: {', '.join(player)}")
            hand_type, _ = self.evaluate_hand(player)
            print(f"Player {i + 1} hand type: {hand_type}")

            if winner is None or self.compare_hands(player, winning_hands[0]):
                winner = i + 1
                winning_hands = [player]
            elif player == winning_hands[0]:
                winning_hands.append(player)

        if len(winning_hands) > 1:
            # Handle ties by comparing the highest cards among tied hands
            winning_hands.sort(key=lambda hand: self._get_highest_card(hand), reverse=True)
            winner = self.players.index(winning_hands[0]) + 1

        return {
            'players': [', '.join(player) for player in self.players],
            'winner': {
                'player_number': winner,
                'hand': ', '.join(winning_hands[0]),
                'hand_type': self.evaluate_hand(winning_hands[0])[0]
            }
        }

    # Private methods

    def _get_numeric_value(self, card):
        """
        Gets the numeric value of a card.

        Args:
        - card (str): The card rank.

        Returns:
        - int: The numeric value of the card.
        """
        rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return rank_values[card] if card in rank_values else int(card)

    def _get_highest_card(self, hand):
        """
        Gets the highest numeric value card in a hand.

        Args:
        - hand (list): A list representing a player's hand.

        Returns:
        - int: The numeric value of the highest card in the hand.
        """
        return max(self._get_numeric_value(card) for card in hand)

    def _is_trail(self, hand):
        """
        Checks if a hand is a trail.

        Args:
        - hand (list): A list representing a player's hand.

        Returns:
        - bool: True if the hand is a trail, False otherwise.
        """
        return hand[0] == hand[1] == hand[2]

    def _is_sequence(self, hand):
        """
        Checks if a hand is a sequence.

        Args:
        - hand (list): A list representing a player's hand.

        Returns:
        - bool: True if the hand is a sequence, False otherwise.
        """
        return sorted([self._get_numeric_value(card) for card in hand]) in [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14]]

    def _is_pair(self, hand):
        """
        Checks if a hand is a pair.

        Args:
        - hand (list): A list representing a player's hand.

        Returns:
        - bool: True if the hand is a pair, False otherwise.
        """
        return hand[0] == hand[1] or hand[1] == hand[2] or hand[0] == hand[2]


if __name__ == "__main__":
    game = CardGame()
    game_result = game.play_game()
    print("\nGame Result:")
    print(f"Players: {game_result['players']}")
    print(f"Winner: Player {game_result['winner']['player_number']} with {game_result['winner']['hand']} ({game_result['winner']['hand_type']})")
