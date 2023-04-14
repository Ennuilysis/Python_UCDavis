# Gerrik Labra
from BoardPrinterProject.src import boards_manager, board  # type: ignore
def menuselect(usr_choice: int) -> None:
    global brd_mng
    x = brd_mng.cur_board
    t = [x.Fill_spot, x.Erase_spot, brd_mng.switch_board, brd_mng.create_new_board,brd_mng.program_quit]  # type: ignore
    t[usr_choice]()  # type: ignore


def print_cur_board() -> None:
    global brd_mng
    y = brd_mng.cur_board
    print(y.board_name)  # type: ignore
    cols = y.col  # type: ignore
    col_indeces = "".join(str(list(range(cols))))
    col_indeces = col_indeces.strip(",[]")
    col_indeces = "  " + col_indeces.replace(",", "")
    print(col_indeces)
    for num, row in enumerate(y.board_list):    # type: ignore
        dang = " ".join(row)
        dang = dang.strip(",")
        print(f"{num} {dang}")


brd_mng = boards_manager.Board_manager()
brd_mng.create_new_board(first_run=True)

if __name__ == '__main__':
    while 1:
        print_cur_board()
        menu_prompt = "Select your action from the list below.\n1. Fill Spot\n2. Erase Spot\n3. Switch Board\n4. Create Board\n5. Quit\n"
        print(menu_prompt)
        usr_choice = int(input("Enter the number of the action you would like to do: "))
        menuselect(usr_choice - 1)
