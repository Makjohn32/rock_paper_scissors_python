print ("hello and welcome to our rock paper scissors game")                    #welcome the players
print ("are you ready to play")
print ("Let's go!!!")
print ("your choices are rock, paper or scissors")
choices=['rock', 'paper', 'scissors']






def checkcorrectchoice():                                                      #check for errors
   if player1.isdigit() and player2.isdigit():
        print ("your choices are wrong please try again")
    
   elif player1!=choices[0] or player1!=choices[1] or player1!=choices[2]:
      print ("invalid choice")
      return player1
   
   elif player2 != choices[0] or player2 != choices[1] or player2 != choices[2]:
      return player2




player = True
while player:
   for i in range(1,4):
      player1 = (str(input("please insert your choice:")))            
      player2 = (str(input("please insert your choice:")))
      checkcorrectchoice()
      if player1==choices[0]:
         if player2==choices[1]:
            print ("congratullations player2 you have won")                        #checking for someone's win
            break
         elif player2==choices[2]:
            print ("congratullations player1 you have won")
            break
         elif player2==choices[0]:
            print ("the match is tie")
            break
      elif player1==choices[1]:
         if player2==choices[0]:
            print ("congratullations player1 you have won")
            break
         elif player2==choices[2]:
            print ("congratullations player2 you have won")
            break
         elif player2==choices[1]:
            print ("the match is tie")
            break
      elif player1==choices[2]:
         if player2==choices[0]:
            print ("congratullations player2 you have won")
            break
         elif player2==choices[1]:
            print ("congratullations player1 you have won")
            break
         elif player2==choices[2]:
            print ("the match is tie")
            break
   player=False

#testing 








        
