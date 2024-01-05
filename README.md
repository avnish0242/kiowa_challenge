# Kiowa Backend Coding Challenge: Simple Card Game

## Problem Statement:

The festive season is here, and we want to create a simple card game of chance that people can enjoy, even when inebriated. The rules of the game involve dealing cards to players and determining the winner based on specific combinations and hierarchy.

## Game Rules:

- Use a regular deck of playing cards, excluding the Joker.
- Each participant receives precisely three cards.
- The 'A' is given a numeral worth of 1.
- In a face-off situation, 'A' trumps all other cards. The hierarchy from highest to lowest is as follows: A > K > Q > J > 10...2.
- Victory conditions include a trail, sequence, pair, or the highest card in the absence of the former.

## Implementation Design:

### CLI-Based Implementation:

#### Structure:
- The code is organized into a class `CardGame` to encapsulate the logic of the card game.
- Methods like `initialize_deck`, `deal_cards`, `evaluate_hand`, `compare_hands`, and `play_game` are defined to handle different aspects of the game.

#### Execution:
- The `play_game` method orchestrates the entire game, initializing the deck, dealing cards, evaluating each player's hand, and determining the winner.
- The winner information is then printed to the console.

### API-Based Implementation:

#### Framework:
- Flask is used to create a simple API with a single endpoint `/play_game`.
- The `CardGame` class is reused from the CLI-based implementation to handle the game logic.

#### API Endpoint:
- The `/play_game` endpoint returns the game result in JSON format.

### Interview Discussion Points:

#### Design Choices:

- **Choosing a Class-Based Structure:**
  - Encapsulating the game's logic within a class-based structure for modularity and organization.
- **Flask for API-Based Implementation:**
  - Using Flask for the API due to its simplicity and suitability for lightweight API development.

#### Readability and Simplicity:

- **Emphasizing Simplicity and Readability:**
  - Prioritizing simplicity and readability for better code maintainability.
- **Modular Functions or Methods:**
  - Dividing logic into modular functions or methods within the `CardGame` class for improved readability and maintainability.

### CLI-Based Approach:

#### Structure:
- A CLI-based script is implemented for running the card game simulation directly in the console.

#### Execution:
- Run the script to observe the game outcome in the console.

### Game Logic Understanding:

- **Explaining Game Rules:**
  - Implementing game rules such as evaluating hand types and determining winners based on hierarchy.
- **Use of Data Structures and Algorithms:**
  - Using basic data structures and algorithms to evaluate and compare hands.

#### Code Reusability:

- **Reusing the CardGame Class:**
  - Reusing the `CardGame` class between CLI and API implementations for code reusability.
- **Promoting Code Reusability and Maintainability:**
  - Centralizing game logic to promote code reusability and maintainability.

#### Testing and Debugging:

- **Importance of Testing:**
  - Emphasizing the importance of testing, especially in scenarios involving randomness like card shuffling.
- **Approach to Testing and Debugging:**
  - Utilizing unit tests, integration tests, and debugging practices for a reliable codebase.

#### Scalability (for API):

- **Addressing Scalability Concerns:**
  - Discussing potential scalability concerns in the API implementation.
- **Extending for More Players or Features:**
  - Explaining how the code could be extended to handle more players or additional features.

#### API Documentation:

- **Documenting the API:**
  - Highlighting the importance of clear and concise API documentation.
- **Importance of Clear and Concise Documentation:**
  - Discussing the significance of well-documented APIs for a positive developer experience.

#### Handling Edge Cases:

- **Addressing Edge Cases:**
  - Handling edge cases, such as ties, by comparing the highest card in tied hands.
- **Extending for Additional Game Rules or Features:**
  - Discussing how the code can be extended to handle new game rules or features.

## Usage:

- For CLI: Run the script and observe the game outcome in the console.
- For API: Make a GET request to `http://127.0.0.1:5000/play_game` (when running locally) to get the game result in JSON format.

## Conclusion:

This implementation showcases a well-structured and readable solution for a simple card game, demonstrating considerations for code reusability, testing, scalability, and documentation.

Feel free to reach out for any clarifications or additional information.


## Steps to Run:
- **For CLI:**
    Open a terminal.
    Navigate to the directory containing the CLI script.
    Run the script with the following command:
    bash
    Copy code
    python your_cli_script.py

- **For Flask API:**
    Install Flask (if not already installed) using:
    pip install flask

    Open a terminal.

    Navigate to the directory containing the Flask script.

    Run the Flask app with the following command:
        python your_flask_script.py

    Open another terminal or use a tool like curl or Postman to make a GET request to:
        http://127.0.0.1:5000/play_game
