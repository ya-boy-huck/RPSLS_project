#RPSLS

#GAME RULES

#0. Greeting to the Games - Gameboard.py

#1. Display rules (how does the game work/function?) - Gameboard.py

#2. Let user select game mode and number of players - Gameboard. py

#3. Display options to the players 

#4. Pick a gesture from list *

    #5. Second Player/AI picks

#6. Compare gesture

    #7. Same gesture - no winner

    #8. Declare winner of round

    #9. Give winner a point

#10. keep playing rounds until we can "declare winner"

#11. Declare Winner!


#Player - Parent class (inherit)

    #Single Player (Human vs AI) - Child
    #Multiplayer (Human vs Human) - Child

#Gameplay - how the game is played and ran (rules)
#Main.py

#function promptFor(question, valid){
  #let isValid;
  #do{
    #var response = prompt(question).trim();
    #isValid = valid(response);
  #} while(response === ""  ||  isValid === false)
  #return response;
