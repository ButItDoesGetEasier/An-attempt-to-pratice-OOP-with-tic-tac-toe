import random


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def get_turn(self):
        while True:
            choice = input("Enter space to mark(1-9): ")
            if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("Invalid input")
            else:
                return int(choice)-1


class Computer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.available_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def get_turn(self):
        return random.choice(self.available_spaces)


class Board:
    def __init__(self):
        self.board = ["_", "_", "_", "_", "_", "_", " ", " ", " "]
        self.occupied_spaces = []

    def print_board(self):
        print(
            f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        print(
            f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print(
            f"{self.board[6]}|{self.board[7]}|{self.board[8]}")

    def update_board(self, player, move):
        self.board[move] = f"{player.symbol}"

    def check_board(self, player):
        if all((self.board[0] == player.symbol, self.board[1] == player.symbol, self.board[2] == player.symbol)) or all((self.board[3] == player.symbol, self.board[4] == player.symbol, self.board[5] == player.symbol)) or all((self.board[6] == player.symbol, self.board[7] == player.symbol, self.board[8] == player.symbol)) or all((self.board[0] == player.symbol, self.board[3] == player.symbol, self.board[6] == player.symbol)) or all((self.board[1] == player.symbol, self.board[4] == player.symbol, self.board[7] == player.symbol)) or all((self.board[2] == player.symbol, self.board[5] == player.symbol, self.board[8] == player.symbol)) or all((self.board[0] == player.symbol, self.board[4] == player.symbol, self.board[8] == player.symbol)) or all((self.board[2] == player.symbol, self.board[4] == player.symbol, self.board[6] == player.symbol)):
            return True


def menu():
    print("Welcome to Tic-Tac-Toe!")
    print("[a] Player VS Player")
    print("[b] Player VS Computer")
    print("[c] Show Info")
    print("[d] Quit")
    choice = input("Enter choice: ").lower()
    return choice


def instructions():
    print("1|2|3\n4|5|6\n7|8|9")
    print("Refer to the diagram above when entering your moves\nCreator: Beam\nDate Finished: October 31, 2021\n")


def check_if_occupied(player, board):
    while True:
        opt = player.get_turn()
        if opt in board.occupied_spaces:
            print("Space is already occupied!")
        else:
            return opt


def post_game(p1, p2, mode):
    print("[1] Play again")
    print("[2] Show win-loss record")
    print("[3] Go back to menu")
    opt = ''
    while opt not in ("1", "2", "3"):
        opt = input("Enter choice: ")
        if opt == '1':
            print()
            mode(p1, p2)
        elif opt == '2':
            print(f'{p1.name}: {p1.wins}\n{p2.name}: {p2.wins}')
            post_game(p1, p2, mode)
        elif opt == '3':
            print()
        else:
            print("Invalid input")


def pvp(p1, p2):
    new_board = Board()

    has_p1_won = False
    has_p2_won = False

    while not has_p1_won and not has_p2_won and not len(new_board.occupied_spaces) == 9:
        new_board.print_board()
        print("Player 1's Turn:")
        p1_move = check_if_occupied(p1, new_board)
        new_board.occupied_spaces.append(p1_move)
        new_board.update_board(p1, p1_move)
        has_p1_won = new_board.check_board(p1)

        if has_p1_won:
            break

        elif len(new_board.occupied_spaces) == 9:
            break

        new_board.print_board()
        print("Player 2's Turn:")
        p2_move = check_if_occupied(p2, new_board)
        new_board.occupied_spaces.append(p2_move)
        new_board.update_board(p2, p2_move)
        has_p2_won = new_board.check_board(p2)

    if has_p1_won:
        p1.wins += 1
        print("Player 1 won!")

    elif has_p2_won:
        p2.wins += 1
        print("Player 2 won!")

    elif len(new_board.occupied_spaces) == 9:
        print("It is a tie!")

    new_board.print_board()
    post_game(p1, p2, pvp)


def pvc(p1, comp):
    new_board = Board()

    has_p1_won = False
    has_comp_won = False

    while not has_p1_won and not has_comp_won and not len(new_board.occupied_spaces) == 9:
        new_board.print_board()
        print("Your Turn:")
        p1_move = check_if_occupied(p1, new_board)
        new_board.occupied_spaces.append(p1_move)
        comp.available_spaces.remove(p1_move)
        new_board.update_board(p1, p1_move)
        has_p1_won = new_board.check_board(p1)

        if has_p1_won:
            break

        elif len(new_board.occupied_spaces) == 9:
            break

        comp_move = comp.get_turn()
        new_board.occupied_spaces.append(comp_move)
        comp.available_spaces.remove(comp_move)
        new_board.update_board(comp, comp_move)
        print("The computer has cast its move")
        has_comp_won = new_board.check_board(comp)

    if has_p1_won:
        p1.wins += 1
        print("You won!")

    elif has_comp_won:
        comp.wins += 1
        print("The computer won!")

    elif len(new_board.occupied_spaces) == 9:
        print("It is a tie!")

    new_board.print_board()
    comp.available_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    post_game(p1, comp, pvc)


opt = ''
while opt != 'd':
    opt = menu()

    if opt == 'a':
        p1_symbol = random.choice(["X", "O"])
        p2_symbol = "X" if p1_symbol == "O" else "O"

        p1 = Player("Player 1", p1_symbol)
        p2 = Player("Player 2", p2_symbol)

        pvp(p1, p2)
    elif opt == 'b':
        p1_symbol = random.choice(["X", "O"])
        comp_symbol = "X" if p1_symbol == "O" else "O"

        p1 = Player("Player", p1_symbol)
        comp = Computer("Computer", comp_symbol)

        pvc(p1, comp)
    elif opt == 'c':
        instructions()
    elif opt == 'd':
        print("See you again!")
    else:
        print("Invalid input")
