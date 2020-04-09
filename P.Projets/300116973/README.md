#Explication Jeu tic ta toe# :smile:

:one: :pushpin: Ce programme contient une notion importante de la programmation qui est l'imbrication. le tableau de jeu est une liste des listes. Ici on utilise les boucles qui contiennent des boucles.

:Two: :pushpin: Remarque :le choix de l'identifiant ici sont des commentaire que nous avont mis avant chaque fonction utilisee.

# le tableu de jeu est une grille 3x3 a deux dimension. nous avons representer la grille a l'aide d'une liste de 3 lignes contenant 3 chaines de caracteres. un joueur sera identifier par le "X" et un autre par "0" pour le cercle. au debut du jeu toutes les cases sont vides.
game_board = [ ["", "", "",],
	       ["", "", "",],
	       ["", "", "",]]

# on ferra le tour du jeu qui consiste a faire un cercle faire jouer le joueur des croix, puis faire jouer le joueuer du rond

:three: :pushpin: les tours de jeu son pareils pour les deux joueurs:
 - premierement on affiche le tableau
- apres on regarde si la partir n'est pas terminer s'il nya plus de coup possible
- si la partir n'est pas terminer, demander au joueur courant de faire son choix en lui demandant de choisir une ligne, puis une colonne dans la grille. alors on imprimera jouer courant 1 ou 2

- si le joueur joue sur une case occuper, alors un message apparaitra pour lui dire que la colonne a deja ete occuper choisir une colonne ou une autre ligne.
- affichage du tableau avec la fonction def game_board(game_map...) apres on utilise la condition if et return.
- pour savoir qu'un joueur est gagnant, on regarde si le joueur a les memes nombres de sens des lignes er des colonne : verticalement, horizontallement et diagonalle dans les deux sens. les fonctions suivantes renvoi les resultants dans les sens suivant :

def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and (l)[0] !=0:
            return True
        else:
            return False
        
    #horizontal 
    for row in game :
        print(row) 
        if all_same(row):
            print (f"Player {row[0]} is the winner horizontally!")
            return True
	    
 # :pushpin: on determine aussi les couleurs
 
    #diagonal
    diags =[]
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same (diags):
        print (f"Player {diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for ix in range (len(game)):
        diags.append(game[ix][ix])
    if all_same (diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True

    #vertical
    for col in range (len(game)):
        check = []
    
    for row in game:
        check.append (row[col])
        
    if all_same (check):
        print (f"Player {check[0]} is the winner vertically (|)!")
        return True
    
    return False
    
:four: :pushpin: la fonction suivante determine les joueurs 

play = True
players = [1, 2]
while play:
    
    game_size =int (input ("what size game of tic tac toe?"))
    game = [[0 for i in range (game_size)] for i in range (game_size)]
    
    game_won = False
    game,_ = game_board (game, just_display=True)
    player_choice = itertools.cycle ([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        
        while not played:
            column_choice = int(input ("what column do you want to play? (0, 1, 2): "))
            row_choice = int(input ("what row do you want to play? (0, 1, 2): "))
            game, played = game_board (game, current_player, row_choice, column_choice)

:five: :pushpin: Pour savoir si un joueu est gagnant on teste les lignes et les colonnes et les diagonales du tableau.

# la fonction suivante determine le gagnant et la fin du jeu:

 if win(game):
            game_won = True
            again = input ("the game is over, would you like to play again? (y/n)")
            
            if again.lower() == "y":
                print("restarting")
                
            elif again.lower() == "n":
                print ("byeeeee")
                play = False
            else:
                print ("Not a valid answer, so... c u l8r aligator")
                play = False



