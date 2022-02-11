import dashtable
from art import logo, empty, user, computer
from rich.console import Console
from time import sleep
from random import choice

console = Console()

game_board = {
    'a1': empty, 'b1': empty, 'c1': empty,
    'a2': empty, 'b2': empty, 'c2': empty,
    'a3': empty, 'b3': empty, 'c3': empty
}


def print_board(board):  # printing table in CLI
    game_table = [
        [' ', "A", "B", "C"],
        [1, board['a1'], board['b1'], board['c1']],  # a1, b1, c1
        [2, board['a2'], board['b2'], board['c2']],  # a2, b2, c2
        [3, board['a3'], board['b3'], board['c3']],  # a3, b3, c3
    ]

    console.print(logo, style='bold red', justify='center')
    console.print(dashtable.data2rst(game_table, center_cells=True, center_headers=True), justify='center')


def compare(board, usr):  # compare tow player
    if list(board.values())[:3].count(usr) == 3:
        return usr
    elif list(board.values())[3:6].count(usr) == 3:
        return usr
    elif list(board.values())[6:9].count(usr) == 3:
        return usr
    elif list(board.values())[::3].count(usr) == 3:
        return usr
    elif list(board.values())[1::3].count(usr) == 3:
        return usr
    elif list(board.values())[2::3].count(usr) == 3:
        return usr
    elif list(board.values())[::4].count(usr) == 3:
        return usr
    elif list(board.values())[2:7:2].count(usr) == 3:
        return usr
    elif list(board.values()).count(empty) == 0:
        return 'DRAW'
    else:
        return False


def ai_player(board):
    for player in [computer, user]:
        game_table = [
            board['a1'], board['b1'], board['c1'],  # a1, b1, c1
            board['a2'], board['b2'], board['c2'],  # a2, b2, c2
            board['a3'], board['b3'], board['c3'],  # a3, b3, c3
        ]

        if game_table[:3].count(empty) == 1 and game_table[:3].count(player) == 2:
            i = game_table[:3].index(empty)
            find_index = list(board.keys())[:3]
            return find_index[i]
        elif game_table[3:6].count(empty) == 1 and game_table[3:6].count(player) == 2:
            i = game_table[3:6].index(empty)
            find_index = list(board.keys())[3:6]
            return find_index[i]
        elif game_table[6:9].count(empty) == 1 and game_table[6:9].count(player) == 2:
            i = game_table[6:9].index(empty)
            find_index = list(board.keys())[6:9]
            return find_index[i]
        elif game_table[::3].count(empty) == 1 and game_table[::3].count(player) == 2:
            i = game_table[::3].index(empty)
            find_index = list(board.keys())[::3]
            return find_index[i]
        elif game_table[1::3].count(empty) == 1 and game_table[1::3].count(player) == 2:
            i = game_table[1::3].index(empty)
            find_index = list(board.keys())[1::3]
            return find_index[i]
        elif game_table[2::3].count(empty) == 1 and game_table[2::3].count(player) == 2:
            i = game_table[2::3].index(empty)
            find_index = list(board.keys())[2::3]
            return find_index[i]
        elif game_table[::4].count(empty) == 1 and game_table[::4].count(player) == 2:
            i = game_table[::4].index(empty)
            find_index = list(board.keys())[::4]
            return find_index[i]
        elif game_table[2:7:2].count(empty) == 1 and game_table[2:7:2].count(player) == 2:
            i = game_table[2:7:2].index(empty)
            find_index = list(board.keys())[2:7:2]
            return find_index[i]
    else:
        empty_cells = list(filter(lambda x: x[1] == empty, list(board.items())))
        random_empty_choice = choice(empty_cells)
        return random_empty_choice[0]


def play_game():
    print_board(game_board)
    console.print('\n If you want to play a game just choose a cell', style='blue', justify='center')

    should_continue_game = True
    while should_continue_game:
        for player, symbol in enumerate([user, computer], start=1):

            if symbol == user:

                choose = True
                while choose:
                    user_choice = console.input(f'\n [yellow]Player({player})[/yellow]: [red]USER[/red]>>> Enter your choice (e.g. a1 or c3): ')

                    if user_choice in game_board:
                        if game_board[user_choice] == empty:
                            game_board[user_choice] = symbol
                            choose = False
                        else:
                            console.print('\nThis cell is taken , try again', style='red', justify='center')
                    else:
                        console.print('\nINVALID, THIS CELL IS 404 - try again', style='red', justify='center')
            else:
                console.print(f'\n [yellow]Player({player})[/yellow]: [red]COMPUTER[/red]>>>')
                sleep(3)
                user_choice = ai_player(game_board)
                game_board[user_choice] = symbol

            result = compare(game_board, symbol)
            if result in [user, computer]:
                should_continue_game = False
                print_board(game_board)

                if symbol == computer:
                    name = 'COMPUTER - "O"'
                else:
                    name = 'USER - "X"'

                console.print(f'\n{name}', style='red', justify='center')
                console.print(f'\nPlayer [red]{player}[/red] is the WINNER!', style='underline yellow', justify='center')
                break
            elif result == 'DRAW':
                should_continue_game = False
                print_board(game_board)
                console.print("\n>>> It's 'DRAW!!' <<<", style='red', justify='center')
                break
            print_board(game_board)


if __name__ == '__main__':
    play_game()
