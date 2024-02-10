class game():
    
    def __init__(self,players):
        self.players = players
        
    def first_round(self,my_list,players,highest_card):
        #print("So far so good")
        temp_list = []
        while len(highest_card) < 1 and len(temp_list) < 5:
            for x in players:
                if "ACE \u2660" in players[x]:
                    #print("It works so far")
                    print(x,"has Ace of \u2660")
                    temp_list.append(players[x].pop(players[x].index("ACE \u2660")))
                    highest_card = x
            
            for y in players:
                if y == highest_card:
                    continue
                print()
                print(y,"':",players[y])
                print(y,end=" ")
                player_choice = str(input("Enter your card: "))
                temp = player_choice.split()
                if  temp[1]== "S":
                    temp[1] = "\u2660"
                    #print(" ".join(temp))
                    temp = " ".join(temp)
                    if temp in players[y]:
                        #print("It works")
                        temp_list.append(players[y].pop(players[y].index(temp)))
                    else:
                        print("It's not working")
                        
                if  temp[1]== "C":
                    temp[1] = "\u2663"
                    print(" ".join(temp)) 
                    temp_list.append(players[x].pop(players[y].index(temp)))
                if  temp[1]== "D":
                    temp[1] = "\u2666"
                    print(" ".join(temp))
                    temp_list.append(players[x].pop(players[y].index(temp)))
                if  temp[1]== "H":
                    temp[1] = "\u2665"
                    print(" ".join(temp))
                    temp_list.append(players[x].pop(players[y].index(temp)))
        print("Cards this rounds:",temp_list)
        my_list.append(temp_list)
        self.game_play(my_list,players,highest_card)

    
    def game_play(self, my_list,players,highest_card):
        temp_list = []
        winner = False
        while winner == False:
            print("-------------------------------------------")
            for person in players:
                if person != highest_card:
                    continue
                print()
                print(person,"':",players[person])
                print(person,end=" ")
                player_choice = str(input("Enter your card: "))
                temp = player_choice.split()
                if  temp[1]== "S":
                    temp[1] = "\u2660"
                    #print(" ".join(temp))
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
                if  temp[1]== "C":
                    temp[1] = "\u2663"
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
                if  temp[1]== "D":
                    temp[1] = "\u2666"
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
                if  temp[1]== "H":
                    temp[1] = "\u2665"
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
            
            for human in players:
                if human == highest_card:
                    continue
                print()
                print(human,"':",players[human])
                print(human,end=" ")
                player_choice = str(input("Enter your card: "))
                temp = player_choice.split()
                if  temp[1]== "S":
                    temp[1] = "\u2660"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
                if  temp[1]== "C":
                    temp[1] = "\u2663"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
                if  temp[1]== "D":
                    temp[1] = "\u2666"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
                if  temp[1]== "H":
                    temp[1] = "\u2665"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
            
            my_list.append(temp_list)
            #print("Cards this rounds:",temp_list)
            highest_card = input("Who played the higest card? ")
            self.determine_winner(players)
                      
        

    def determine_winner(self,players):
        for x in players:
            if len(players[x]) < 1:
                return True
        