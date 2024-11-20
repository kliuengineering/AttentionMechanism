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
from strategy import KeywordMatchingStrategy, LengthBasedStrategy, LengthBasedStrategy, EmbeddingSimilarityStrategy
from attention_calculator import AttentionCalculator
from aggregator import WeightedAggregator


def main():
    # Define context
    context = "Professor Miguel Watler is awesome"
    
    # Create words (input components)
    words = [Word("teacher"), Word("rocket"), Word("great"), Word("class"), Word("student"), Word("presentation")]
    
    # Define attention calculator with the EmbeddingSimilarityStrategy
    strategy = EmbeddingSimilarityStrategy()
    attention_calculator = AttentionCalculator(strategy)
    
    # Create aggregator
    aggregator = WeightedAggregator(words, attention_calculator, context)
    
    # prints the context
    print(f'Context of the conversation: "{context}." \n')

    # Initial aggregation
    aggregator.aggregate()
    
    # Change a word to trigger observer
    change = "college"
    print(f'Changed an input to "{change}"')
    words[0].text = change
  
    
    # Re-aggregate after changing a word
    # aggregator.aggregate()
    
    # Optionally, switch to another strategy
    # new_strategy = LengthBasedStrategy()
    # attention_calculator.set_strategy(new_strategy)
    # aggregator.aggregate()


if __name__ == "__main__":
    main()
