'''
-----------------------------------------------------------------------
File: q3.py
Creation Time: Nov 7th 2023 3:23 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.models import Word2Vec
import numpy as np

# You can access all models by uncommenting the following command
# models = {
#            "w2v": Word2Vec.load("models/w2v"),
#            "tfidf": TfidfModel.load("models/tfidf"),
#            "dct": Dictionary.load("models/dct"),
#        }

# You can use this helper function to get tfidf weights for a given
# sentence and for accessed models
def get_tfidf_weights(models, sentence):
    transformed = models["dct"].doc2bow(sentence.split())
    tfidf_dct = {
        models["dct"][key]: value for (key, value) in models["tfidf"][transformed]
    }
    return tfidf_dct

def embed_sentence(models, sentence):
    w2v_model = models['w2v']
    sentence_tokens = sentence.split()
    
    w2v_embeddings = []
    tfidf_weights = get_tfidf_weights(models, sentence)
    
    for word in sentence_tokens:
        if word in w2v_model.wv.vocab:
            w2v_embeddings.append(w2v_model.wv[word])
        else:
            w2v_embeddings.append(np.zeros(w2v_model.vector_size))
    
    w2v_embedding = np.mean(w2v_embeddings, axis=0)
    
    tfidf_embedding = np.zeros(w2v_model.vector_size)
    total_tfidf_weight = 0.0
    
    for i, word in enumerate(sentence_tokens):
        if word in tfidf_weights:
            tfidf_embedding += w2v_embeddings[i] * tfidf_weights[word]
            total_tfidf_weight += tfidf_weights[word]
    
    if total_tfidf_weight > 0:
        tfidf_embedding /= total_tfidf_weight
    
    result = {
        'w2v_embedding': w2v_embedding.tolist(),
        'tfidf_embedding': tfidf_embedding.tolist()
    }
    
    return result

# Example usage:
# models = {
#    'w2v': Word2Vec.load("models/w2v"),
#    'tfidf': TfidfModel.load("models/tfidf"),
#    'dct': Dictionary.load("models/dct")
# }
# sentence = "I have a dream"
# embeddings = embed_sentence(models, sentence)
# print("Word2Vec Embedding:", embeddings['w2v_embedding'])
# print("TFIDF-Weighted Embedding:", embeddings['tfidf_embedding'])