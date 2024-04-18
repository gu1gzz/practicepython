class Player:
    def __init__(self,name):
        self.name = name
    
    def player_command(self):
        print("enter rock or paper or scissors: ")
        command = input()
        while (command != 'rock') and (command != 'paper') and (command != 'scissors'):
            print("Error, please enter rock or paper or scissors: ")
            command = input()
        return command
                
def who_whin(command1, command2, name1, name2):
    if command1 == command2:
        print("It's a DRAW ")
    elif command1 == "rock" and command2 == "scissors":
        print(f"{name1} wins")
    elif command1 == "scissors" and command2 == "rock":
        print(f"{name2} wins")
    elif command1 == "scissors" and command2 == "paper":
        print(f"{name1} wins")
    elif command1 == "paper" and command2 == "scissors":
        print(f"{name2} wins")
    elif command1 == "paper" and command2 == "rock":
        print(f"{name1} wins")
    elif command1 == "rock" and command2 == "paper":
        print(f"{name2} wins")

def main():
    print("Playing Rock-Paper-Scissors")
    player_1_name = input("Player One enter your name:")
    player_2_name = input("PLayer Two enter your name:")
    player1 = Player(player_1_name)
    player2 = Player(player_2_name)
    playing = True
    while playing == True:
        player_1_command = player1.player_command()
        player_2_command = player2.player_command()
        who_whin(player_1_command,player_2_command, player1.name, player2.name)
        replay = input("Do you want replay ? Y/N ")
        if replay == "N":
            playing = False
            
if __name__ == "__main__":
    main()