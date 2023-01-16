# Afficher la grille
# Faire la grille
# jouer un coup
#     (vérifier si le coup est possible )
#         (vérifier que la case est vide)
#         (vérifier que la case existe)
# Vérifier si la grille est gagnante ou match nul
# Changer de joueur
# vérifier si grille gagnante ou match nul encore


#Variables globales
import os
grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

joueur_en_cours = "X" #on initialise  le premier joueur avec la valeur "X"
gagnant = None        #on initialise la variable mais nous n'avons pas données  
partie_en_cours = True


#affichage grille

def afficher_grille(grille):
    """_summary_ affiche la grille de départ du jeu du morpion en 3*3 = 9 cases.Chaque case vide est représentée pr le signe "-"

    Args: grille
        grille (_type_): _description_ case remplies par élément de type string
    """
    
    print(grille[0] + " | " + grille[1] + " | " +grille[2] + " | ")
    print("-----------")
    print(grille[3] + " | " + grille[4] + " | " +grille[5] + " | ")
    print("-----------")
    print(grille[6] + " | " + grille[7] + " | " +grille[8] + " | ")
    
    

#jouer un coup

def joueur_coup(grille):
    
    """_summary_: initialise l'entrée que le joueur doit effectuer pour remplir une des cases
    choix entre les nombres situés entre 1 et 9
    on s'assure que le joueur entre une valeur entre 1 et 9 et la case choisie n'est pas déja utilisée donc avec le "-".
    On enregistre le coup du joueur dans grille[coup-1].
    Si cela ne remplie aucune des 2 conditions si dessus alors on prévient le joueur que son choix n'est pas valide.
    

    Args:
        grille (_type_): _description_: entrée de type integer
    """
    
    coup = int(input("Entrer un nombre entre 1 et 9: "))
    if coup >= 1 and coup <= 9 and grille[coup-1] == "-":
        grille[coup-1] = joueur_en_cours
    else:
        print("Action impossible !")
        coup = int(input("Choisisser une autre case ou Entrer un nombre entre 1 et 9 !!! : "))
    # while coup <= 1 or coup >= 9 and grille[coup-1] != "-":
    #     grille[coup-1] = joueur_en_cours
    #     print("Action impossible, rejouer une nouvelle fois !")
    #     coup = int(input("Entrer un nombre entre 1 et 9: "))
    


        
        
#vérifier si la partie est gagnée 

""" on vérifie si les différentes possiblités de victoires sont remplies, en ligne, en colonne, en diagonale.
    """
    
    
def vérification_par_ligne(grille):
    
    """_summary_ on vérifie les différents conditions de victoires sur une ligne en comparant si chaque case est identique et l'une d'elles différentes de la case vide représentée par "-"
    on crée une variable globale.
    on peut indiquer n'importe quel index [0] d'une ligne car toutes les cases sont égales pour la victoire.

    Args:
        grille (_type_): _description_ signe choisit par le joueur "X" ou "O" est un string

    Returns:
        _type_: _description_
    """
    
    global gagnant
    
    
    if grille[0] == grille[1] == grille[2] and grille[1] != "-":
        gagnant = grille[0]     
        return True  
    
   
    elif grille[3] == grille[4] == grille[5] and grille[3] != "-":
        gagnant = grille[3]     
        return True
    
    
    elif grille[6] == grille[7] == grille[8] and grille[7] != "-":
        gagnant = grille[6]     
        return True  
    
     # return True cela va permettre d'arréter la partie car la condition de victoire est remplie.
     
     
     
def vérification_par_colonne(grille):
    
    """_summary_ on vérifie les différents conditions de victoires sur une colonne en comparant si chaque case est identique et l'une d'elles différentes de la case vide représentée par "-"
    on crée une variable globale.
    on peut indiquer n'importe quel index [0] d'une colonne car toutes les cases sont égales pour la victoire.

    Args:
        grille (_type_): _description_ signe choisit par le joueur "X" ou "O" est un string

    Returns:
        _type_: _description_
    """
    
    global gagnant
    
    
    if grille[0] == grille[3] == grille[6] and grille[0] != "-":
        gagnant = grille[0]     
        return True  
    
   
    elif grille[1] == grille[4] == grille[7] and grille[1] != "-":
        gagnant = grille[3]     
        return True
    
    
    elif grille[2] == grille[5] == grille[8] and grille[2] != "-":
        gagnant = grille[6]     
        return True 
    
def vérification_en_diagonale(grille):
    
    global gagnant
   
    if grille[0] == grille[4] == grille[8] and grille[0] != "-":
        gagnant = grille[0]     
        return True  
    
   
    elif grille[2] == grille[4] == grille[6] and grille[2] != "-":
        gagnant = grille[2]     
        return True
    
"""summary_ on vérifie les différents conditions de victoires sur une diagonale en comparant si chaque case est identique et l'une d'elles différentes de la case vide représentée par "-"
    on crée une variable globale.
    on peut indiquer n'importe quel index [] d'une diagonale car toutes les cases sont égales pour la victoire.

    Args:
        grille (_type_): _description_ signe choisit par le joueur "X" ou "O" est un string

    Returns:
        _type_: _description_
"""  

#vérifier si la partie est nulle 

def vérification_partie_nulle(grille):
    
    """summary_ on vérifie que la partie est nulle si le string "-" n'est plus présent sur la grille donc aucun des joueurs ne peut plus entrer un choix, donc la partis s'arrête.
    on crée une variable globale.
    
    Args:
        grille (_type_): _description_ signe  "-" est un string

    Returns:
        _type_: _description_
    """ 
    
    #global partie_en_cours
    partie_en_cours = True
    if "-" not in grille:
        afficher_grille(grille)
        print("la partie est nulle !")
        partie_en_cours = False
        
        
def vérification_de_victoire():
    """_summary_ selon le résultat des différentes conditions précédentes on affiche lequel des joueurs "X" ou "O" gagnent
    """
    global partie_en_cours
    if vérification_par_ligne(grille) or vérification_par_colonne(grille) or vérification_en_diagonale(grille):
        print(f"le gagnant est {gagnant}")
        partie_en_cours = False      
        

# Changer de joueur

def changer_de_joueur(): 
    """_summary_ on vérifie si le joueur actuel utilise le signe "X" ou "O" en le comparant à la valeur initiale "X".
    """
    global joueur_en_cours
    
    if joueur_en_cours == "X":
        joueur_en_cours = "O"
    else:
        joueur_en_cours = "X"          
        
         
             
      
    
    
            
        
while partie_en_cours:
    afficher_grille(grille)
    joueur_coup(grille)
    vérification_de_victoire()
    vérification_partie_nulle(grille)
    changer_de_joueur()        
