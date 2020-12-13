print ("hello and welcome to our rock paper scissors game")                    #welcome the players
print ("are you ready to play")
print ("Let's go!!!")
print ("your choices are rock, paper or scissors")
choices=['rock', 'paper', 'scissors']






def checkcorrectchoice():                                                      #check for errors
    if player1.isdigit() and player2.isdigit():
        print ("your choices are wrong please try again")
    
    else:
        player1 or player2!=choices[0] or choices[1] or choices[2]
        print ("invalid choice")
        return player1
print ("hello and welcome to our rock paper scissors game")                    #welcome the players
print ("are you ready to play")
print ("Let's go!!!")
print ("your choices are rock, paper or scissors")
choices=['rock', 'paper', 'scissors']






def checkcorrectchoice():                                                      #check for errors
    if player1.isdigit() and player2.isdigit():
        print ("your choices are wrong please try again")
    
    else:
        player1 or player2!=choices[0] or choices[1] or choices[2]
        print ("invalid choice")
        return player1

checkcorrectchoice()
for i in range(1,3):    
    player = True
    while player==True:
         player1 = (str(input("please insert your choice:")))            
         player2 = (str(input("please insert your choice:")))
         if player1==choices[0]:
           if player2==choices[1]:
             print ("congratullations player2 you have won")                        #checking for someone's win
           elif player2==choices[2]:
             print ("congratullations player1 you have won")
         elif player2==choices[1]:
            print ("the match is tie")
         elif player1==choices[1]:
             if player2==choices[0]:
               print ("congratullations player1 you have won")
             elif player2==choices[2]:
                print ("congratullations player2 you have won")
             elif player2==choices[1]:
                print ("the match is tie")
         elif player1==choices[2]:
           if player2==choices[0]:
              print ("congratullations player2 you have won")
           elif player2==choices[1]:
              print ("congratullations player1 you have won")
           elif player2==choices[2]:
              print ("the match is tie")




checkcorrectchoice()
player = True
while player==True:
    player1 = (input("please insert your choice:"))            
    player2 = (input("please insert your choice:"))
    if player1==choices[0]:
       if player2==choices[1]:
           print ("congratullations player2 you have won")                        #checking for someone's win
       elif player2==choices[2]:
            print ("congratullations player1 you have won")
       elif player2==choices[1]:
            print ("the match is tie")
    elif player1==choices[1]:
         if player2==choices[0]:
            print ("congratullations player1 you have won")
         elif player2==choices[2]:
              print ("congratullations player2 you have won")
         elif player2==choices[1]:
              print ("the match is tie")
    elif player1==choices[2]:
         if player2==choices[0]:
            print ("congratullations player2 you have won")
         elif player2==choices[1]:
            print ("congratullations player1 you have won")
         elif player2==choices[2]:
              print ("the match is tie")



































        
