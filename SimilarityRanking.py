
# Ce fichier contient les fonctions nécessaires à la mise en place d'un système d'ordonnancement 
# de textes selon leur degré de similarité.

# SimilarityRanking - Classe implémentant les différentes opérations nécessaire au calcul du niveau de similarité entre différents textes.
#
# Les opérations implémentées sont les suivantes :
#               - conversion d'un texte vers une forme exploitable (en matrice dans notre cas) par un réseau de neurones convolutif (CNN)
#               - "raisonnement" sur les représentations des textes, calcul du niveau de similarité
#
#
class SimilarityRanking :
    
    #
    # Méthode convertissant un texte en une matrice.
    #
    def convertTextToMatrix(self, text) :
        txtMatrix = []
        return txtMatrix
        
    