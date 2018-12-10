
# Ce fichier contient les fonctions nécessaires à la mise en place d'un système d'ordonnancement 
# de textes selon leur degré de similarité.

# SimilarityRanking - Classe implémentant les différentes opérations nécessaire au calcul du niveau de similarité entre différents textes.
#
# Les opérations implémentées sont les suivantes :
#               - conversion d'un texte vers une forme exploitable (en matrice dans notre cas) par un réseau de neurones convolutif (CNN)
#               - "raisonnement" sur les représentations des textes, calcul du niveau de similarité
#
#

# Imports
import tensorflow as tf
from tensorflow import keras

import numpy as np
import bcolz as bz
import pickle


class SimilarityRanking :
    
    #
    vectorsFilesPath = 'C:/Users/AMN14/Documents/ENSIIE/WIA/Projet/wia.projet/Vectors'
    
    # 
    hyperParameters = []
    
    #
    # Constructeur.
    #
    # @Param vectorsFileName - Le nom du fichier contenant les vecteurs pré-calculés à utiliser.
    #
    def __init__(self, vectorsFileName) :
        
        # dictionaire contenant les mots en tant que clés et les vecteurs associés en tant que valeurs
        self.word2vectorDictionary = None
        
        # tableau contenant les mots décrits par des vecteurs
        words = []
        
        # tableau contenant les vecteurs
        vectors = bz.carray(np.zeros(1), rootdir=f'{SimilarityRanking.vectorsFilesPath}\{vectorsFileName}.dat', mode='w')
        
        # dictionnaire contenant l'index du vecteur associé à chaque mot
        words2vectorsIdx = {}
        
        wordIndex = 0
        
        # lecture du fichier de vecteurs
        with open(f'{SimilarityRanking.vectorsFilesPath}\{vectorsFileName}', 'rb') as file:
            for l in file:
                line = l.decode().split()
                word = line[0]
                words.append(word)
                words2vectorsIdx[word] = wordIndex
                wordIndex += 1
                vect = np.array(line[1:]).astype(np.float)
                vectors.append(vect)
            
        vectors = bz.carray(vectors[1:].reshape((400000, 50)), rootdir=f'{SimilarityRanking.vectorsFilesPath}/{vectorsFileName}.dat', mode='w')
        vectors.flush()
        pickle.dump(words, open(f'{SimilarityRanking.vectorsFilesPath}/{vectorsFileName}_words.pkl', 'wb'))
        pickle.dump(words2vectorsIdx, open(f'{SimilarityRanking.vectorsFilesPath}/{vectorsFileName}_idx.pkl', 'wb'))
        
        vectors = bz.open(f'{SimilarityRanking.vectorsFilesPath}/{vectorsFileName}.dat')[:]
        words = pickle.load(open(f'{SimilarityRanking.vectorsFilesPath}/{vectorsFileName}_words.pkl', 'rb'))
        words2vectorsIdx = pickle.load(open(f'{SimilarityRanking.vectorsFilesPath}/{vectorsFileName}_idx.pkl', 'rb'))
        
        self.word2vectorDictionary = {word : vectors[words2vectorsIdx[word]] for word in words}
        
        # La correspondance entre les mots et les vecteurs est maintenant établie
            
    #
    # Méthode convertissant un texte en une matrice. Chaque mot est converti en un vecteur et une phrase est alors la 
    # concaténation de ces vecteurs, on parle de "word Embedding". 
    #
    # On utilisera un modèle de type "word2vec", qui consiste à représenter les mots sous la forme de vecteurs appartenant 
    # à un espace. La "proximité" de deux vecteurs dans cet espace peut par exemple indiquer que ces deux mots ont un sens 
    # proche. Ces représentations vectorielles des mots sont générées par des réseaux de neurones.
    #
    # Il est possible de générer soi-même les vecteurs associés aux mots, ou bien on peut utiliser un jeu de vecteurs pré-entraînés.
    #
    # Dans notre cas, nous utiliserons un jeu de vecteurs pré-entraîné : GloVe
    # Il existe plusieurs fichiers (4) contenant les représentations vectorielles des mots, nous utiliserons le suivant (plus léger) :
    #                   - Wikipedia 2014 + Gigaword 5 (https://nlp.stanford.edu/projects/glove/, archive glove.6B.zip)
    #
    # Ce jeu de vecteurs pré-entraînés contient plusieurs fichiers, contenant eux-mêmes des vecteurs de 50, 100, 200 et 300 dimensions.
    #
    # @param text - le texte a convertir
    #
    def convertTextToMatrix(self, text) :
        txtMatrix = []
        return txtMatrix
        
    #
    # Méthode 
    #
    def learn(self) :
        return