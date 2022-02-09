import dashtable
from art import logo, empty, user, computer
from rich.console import Console

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


def compare(board, choice):  # compare tow player
    if list(board.values())[:3].count(choice) == 3:
        return choice
    elif list(board.values())[3:6].count(choice) == 3:
        return choice
    elif list(board.values())[6:9].count(choice) == 3:
        return choice
    elif list(board.values())[::3].count(choice) == 3:
        return choice
    elif list(board.values())[1::3].count(choice) == 3:
        return choice
    elif list(board.values())[2::3].count(choice) == 3:
        return choice
    elif list(board.values())[::4].count(choice) == 3:
        return choice
    elif list(board.values())[2:7:2].count(choice) == 3:
        return choice
    else:
        return False


def play_game():
    print_board(game_board)
    console.print('\n If you want to play a game just choose a cell', style='blue', justify='center')

    should_continue_game = True
    while should_continue_game:
        for player, symbol in enumerate([user, computer], start=1):
            choose = True
            while choose:
                user_choice = console.input(f'\n [red]Player({player})[/red]: Enter your choice (e.g. a1 or c3): ')
                if user_choice in game_board:
                    if game_board[user_choice] == empty:
                        game_board[user_choice] = symbol
                        choose = False
                    else:
                        console.print('This cell is taken , try again', style='red', justify='center')
                else:
                    console.print('INVALID, THIS CELL IS 404 - try again', style='red', justify='center')

            result = compare(game_board, symbol)
            if result:
                should_continue_game = False
                print_board(game_board)
                console.print(f'{symbol}', style='red', justify='center')
                console.print(f'Player [red]{player}[/red] is WINNER', style='underline yellow', justify='center')
                break
            print_board(game_board)


if __name__ == '__main__':
    play_game()
