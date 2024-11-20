"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About strategy.py:
    Defines the Strategy interfaces and concrete strategy implementations. 
    It includes the AttentionStrategy abstract class and concrete 
    strategies like KeywordMatchingStrategy and LengthBasedStrategy for 
    calculating attention weights.

    strategy C and D are added for this more sophisticated example.
    cosine similarity is used for the embeddings.
    so the attention weighting is based off the cosine similarities.
    context embedding is computed by averaging the embeddings of the context words.
    zero vector is also handled properly here.
"""

from abc import ABC, abstractmethod
from word import Word
import numpy as np


# << interface >> Strategy
class AttentionStrategy(ABC):
    @abstractmethod
    def calculate_weight(self, word:Word, context:str) -> float:
        pass


# Concrete strategy A
class KeywordMatchingStrategy(AttentionStrategy):
    def calculate_weight(self, word, context):
        return 1.0 if word.text.lower() in context.lower().split() else 0.1
    

# Concrete strategy B
class LengthBasedStrategy(AttentionStrategy):
    def calculate_weight(self, word, context):
        return len(word.text) / max( len(w) for w in context.split() )
    

# Concrete strategy C
class LengthBasedStrategy(AttentionStrategy):
    def calculate_weight(self, word: Word, context: str) -> float:
        return len(word.text) / max(len(w) for w in context.split())
    

# Concrete strategy D -> the real deal
class EmbeddingSimilarityStrategy(AttentionStrategy):
    def calculate_weight(self, word: Word, context: str) -> float:
        # Generate context embedding by averaging embeddings of context words
        context_words = context.split()
        context_embeddings = []
        for ctx_word in context_words:
            temp_word = Word(ctx_word)
            context_embeddings.append(temp_word.embedding)
        context_vector = np.mean(context_embeddings, axis=0)
        
        # Handle the case where the context vector is zero
        if np.linalg.norm(context_vector) == 0 or np.linalg.norm(word.embedding) == 0:
            return 0.0
        
        # Calculates cosine similarity between word embedding and our context vector
        similarity = self.cosine_similarity(word.embedding, context_vector)
        return similarity

    def cosine_similarity(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        norm_a = np.linalg.norm(vec1)
        norm_b = np.linalg.norm(vec2)
        return dot_product / (norm_a * norm_b)