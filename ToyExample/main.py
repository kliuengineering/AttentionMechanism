"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About main.py: 
    Serves as the entry point of the program. It sets up the components, 
    initializes the strategies, creates word objects, 
    and directs the interactions between different classes to 
    demonstrate our attention mechanism.
"""


from word import Word
from strategy import KeywordMatchingStrategy, LengthBasedStrategy
from attention_calculator import AttentionCalculator
from aggregator import WeightedAggregator


def main():
    # Define context
    context = "important project deadline"

    # Create words (input components)
    words = [Word("This"), Word("is"), Word("an"), Word("important"), Word("project"), Word("deadline")]

    # Define attention calculator with a strategy
    strategy = KeywordMatchingStrategy()
    attention_calculator = AttentionCalculator(strategy)

    # Create aggregator
    aggregator = WeightedAggregator(words, attention_calculator, context)

    # Change a word to trigger observer
    words[0].text = "Today"

    # Change strategy at runtime
    new_strategy = LengthBasedStrategy()
    attention_calculator.set_strategy(new_strategy)
    aggregator.aggregate()


if __name__ == "__main__":
    main()
