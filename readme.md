# Data Representation - Attention is All You Need

## The Attention Pattern Introduced

The attention pattern aligns closely with data representation models. It represents and processes data based on dyanmic efficiency. In a nutshell, the Attention pattern allows a system to dynamically focus on and priortize certain components / inputs over others, based on context-specific objectives, which improves effectiveness in decisoin-making.

[![Watch the video](https://img.youtube.com/vi/eMlx5fFNoYc/0.jpg)](https://youtu.be/eMlx5fFNoYc?si=37fwBZykRBDZImwZ&t=269)

https://youtu.be/eMlx5fFNoYc?si=37fwBZykRBDZImwZ&t=269 [![YouTube Video Views](https://img.shields.io/youtube/views/eMlx5fFNoYc?style=social)](https://www.youtube.com/watch?v=eMlx5fFNoYc)

## Rationale
In many deep learning systems, especially those with large amounts of data and many components, it is inefficient to treat all input parameters equally. Some inputs may rather be more relevant and important to the current context or task. \
The attention design pattern addresses this by providing a mechanism to evaluate and weight inputs dynamically, and so ensuring the most relevant information has the most significant influence on the output.

## Problems It Solves
1. When the relevance of input data is dependent of the context.
2. There is a time when we need to aggregate multiple inputs, but we want to prioritize some of them over others.
3. In a real-time system which requires adjustments of the current focus based on changing conditions.

## Industry Applications
1. NLP: ChatGPT o1-preview uses this design pattern as its learning architecture.
2. Recommendation System: This kind of system priortizes user preferences based on context or recent behaviours (like Chrome's Cookies, etc.).
3. Sensor Data Fusion: In robotics, there may be a bunch of sensors gathering data. Aggregating sensor inputs, and give more weight to the reliable sensors based on environmental conditions such as air dynamics, pressure differential, etc. 
<br></br>
<br></br>
![Description of UML Diagram](./assets/Chat.png)

## The UML
![Description of UML Diagram](./assets/UML.png)

## The Toy Example
The toy example is an implementation of the UML. There are three main traditional design patterns used for aggregating the design intents for the Attention pattern, in which the pattern itself encapsulates and realizes a modern approach to the Attention mechanism. The mechanism is a well-known research done by Google in the academic paper "Attention is All You Need". [https://arxiv.org/pdf/1706.03762]

## The Sophisticated Example
* Note: you will need to download this model for this example to work: \
https://www.kaggle.com/datasets/watts2/glove6b50dtxt?resource=download \
put it in the directory of ~/PracticalExample/

### 1. Problem Statement
Understanding the context-specific importance of words within a sentence is vital in natural language processing (NLP) and machine learning applications. Traditional models often assign equal weight to all words or use fixed weighting schemes, which can lead to inefficiencies and inaccuracies, especially when processing nuanced or context-dependent language. The key challenge is to dynamically identify which words are most relevant in a given context and adjust their influence accordingly. This dynamic relevance assessment is essential for tasks like text summarization, machine translation, and sentiment analysis, where the semantic relationships between words and their contexts significantly affect performance.

### 2. Solving the Problem Using the Attention Pattern
To solve this problem, we implemented the Attention Design Pattern, which enables the system to dynamically focus on and prioritize words based on their relevance to a specific context. By integrating pre-trained GloVe word embeddings, each word is represented as a numerical vector capturing its semantic meaning. An attention mechanism calculates weights for each word by computing the cosine similarity between the word's embedding and the context embedding (the average of embeddings for context words). This allows the model to assign higher importance to words that are more semantically related to the context, enhancing the performance of tasks like text summarization, machine translation, and sentiment analysis. Additionally, we utilized design patterns such as Strategy, Observer, and Decorator to ensure the system is modular, flexible, and maintainable.

### 3. Codebase Design Explained
Every .py file is well-documented and should be self-explanatory. Please refer to the files individually for modular explanations.

## References (Hyperlink-only)
- https://arxiv.org/abs/1706.03762
- https://www.envisioning.io/vocab/attention-pattern
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7996841/
- https://www.researchgate.net/publication/383607494_Attention-Based_Method_for_Design_Pattern_Detection