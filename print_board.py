# print_board.py
def print_board(board):
    """현재 스도쿠 보드를 보기 쉽게 출력합니다."""
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()