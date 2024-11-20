"""
Authours: 
    - Jasleen Kaur
    - Kevin Liu
    - Ma Toan Bach
"""
"""
About embeddings.py:
    Here we apply Singleton pattern to make sure only 1 instance of
    the model is ever mounted.
    
    1. we load up the model;
    2. get_embedding retrieves the actual embedding vector for a word
    3. if word is not found -> returns 0 vector
"""

import numpy as np

# Singleton Pattern here
class Embeddings:
    _instance = None 

    def __new__(cls, embedding_file):
        if cls._instance is None:
            cls._instance = super(Embeddings, cls).__new__(cls)
            cls._instance._initialized = False

        # Singleton in action -> makes Watler proud
        return cls._instance

    def __init__(self, embedding_file):
        if self._initialized:
            return
        self.embedding_index = self.load_embeddings(embedding_file)
        self._initialized = True

    def load_embeddings(self, embedding_file):
        embeddings_index = {}
        print(f"Loading embeddings from {embedding_file}...")

        # fopen here
        with open(embedding_file, 'r', encoding='utf8') as f:
            for line in f:
                # values == tensor
                values = line.strip().split()
                if len(values) > 2:  # Ensure the line contains data
                    word = values[0]
                    # actual embeddings here
                    coefs = np.asarray(values[1:], dtype='float32')
                    embeddings_index[word] = coefs

        print(f"Loaded {len(embeddings_index)} word vectors. \n")
        return embeddings_index

    def get_embedding(self, word):
        embedding = self.embedding_index.get(word.lower())
        if embedding is not None:
            return embedding
        else:
            # Handle out-of-vocabulary words by returning a zero vector
            return np.zeros(50, dtype='float32')  # we use 50-d model here
