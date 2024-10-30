from tictactoe_yl5733 import tictactoe_yl5733

#  Part1: Unit Tests

def test_initialize_board():
  board = initialize_board()
  assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], f"Should be initialized, but got {board}."

def test_make_move_valid():
  # set up a mock board
  board = [['X', ' ', 'X'],
           ['O', ' ', 'O'],
           [' ', 'O', ' ']]

  # test player X
  # check if move can sucessfully execute
  assert make_move(board, 1, 1, 'X') == True, "Player X should be able to move, but failed."
  # check if the board is occupied correctly
  assert board[1][1] == 'X', f"Player X should occupy board[1][1], but got {board[1][1]}."
  
  # reset board and test player O
  board = [['X', ' ', 'X'],
           ['O', ' ', 'O'],
           [' ', 'O', ' ']]
  assert make_move(board, 2, 2, 'O') == True, "Player O should be able to move, but failed."
  assert board[2][2] == 'O', f"Player O should occupy board[2][2], but got {board[2][2]}"

def test_make_move_invalid():
  board = [['X', ' ', 'X'],
           ['O', ' ', 'O'],
           [' ', 'O', ' ']]

  # test player X and O
  assert make_move(board, 0, 0, 'X') == False, f"Player X should not be able to move, but succeeded." 
  assert make_move(board, 0, 0, 'O') == False, f"Player O should not be able to move, but succeeded."


def test_game_integration():

  # 1. Initialize the board and test
  board = initialize_board()
  assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], f"Board should be initialized, but got {board}."

  # 2. Make moves and test each move
  # player X makes first move
  assert make_move(board, 1, 1, 'X') == True, f"Player X should be able to move, but failed."
  assert board[1][1] == 'X', f"Player X should occupy board[1][1], but got {board[1][1]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player O makes first move
  # I assume a setting that player O wants to occupy the center of the board, failed. Then try to move on another location.
  assert make_move(board, 1, 1, 'O') == False, f"Player O should not be able to move on board[1][1], but succeeded."
  assert make_move(board, 0, 0, 'O') == True, f"Player O should be able to move, but failed."
  assert board[0][0] == 'O', f"Player O should occupy board[0][0], but got {board[0][0]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player X makes second move
  assert make_move(board, 1, 0, 'X') == True, f"Player X should be able to move, but failed."
  assert board[1][0] == 'X', f"Player X should occupy board[1][0], but got {board[1][0]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player O makes second move
  assert make_move(board, 1, 2, 'O') == True, f"Player O should be able to move, but failed."
  assert board[1][2] == 'O', f"Player O should occupy board[1][2], but got {board[1][2]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player X makes third move
  assert make_move(board, 0, 1, 'X') == True, f"Player X should be able to move, but failed."
  assert board[0][1] == 'X', f"Player X should occupy board[0][1], but got {board[0][1]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player O makes third move
  assert make_move(board, 2, 1, 'O') == True, f"Player O should be able to move, but failed."
  assert board[2][1] == 'O', f"Player O should occupy board[2][1], but got {board[2][1]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player X makes fourth move
  assert make_move(board, 2, 0, 'X') == True, f"Player X should be able to move, but failed."
  assert board[2][0] == 'X', f"Player X should occupy board[2][0], but got {board[2][0]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player O makes fourth move
  assert make_move(board, 0, 2, 'O') == True, f"Player O should be able to move, but failed."
  assert board[0][2] == 'O', f"Player O should occupy board[0][2], but got {board[0][2]}."
  assert check_winner(board) == None, f"Game should not be over, but got {check_winner(board)}."

  # player X makes fifth move (final move)
  assert make_move(board, 2, 2, 'X') == True, f"Player X should be able to move, but failed."
  assert board[2][2] == 'X', f"Player X should occupy board[2][2], but got {board[2][2]}."

  # 3. Check the final result of the game
  assert check_winner(board) == "Draw", f"Game should be over as a draw, but got {check_winner(board)} as winner."

  # 4. Reset the board and test
  board = reset_game()
  assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], f"Board should be reset, but got {board}."
  
  
  
  # Part 2: Advanced Tests
  
  import pytest
@pytest.fixture
def test_board():
  test_board = [['X', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
  return test_board

# by using fixture, it saves time to reset the board over and over again in @pytest.mark.parametrize decorator
# 1. Empty Board Test
  # since this test checks whether an initialized board is empty,
  # it stands out from other tests, so i re-arrange it here
def test_initialize_board():
  board = initialize_board()
  assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], f"Should be initialized, but got {board}."

@pytest.mark.parametrize(
    "test_type, row, col, player, expected", [
        # 2. Occupied Cell Test
        ("occupied_cell_test", 
         0, 0, 'O', False),
        
        # 3. Valid Move Test
        ("valid_move_test",
         0, 1, 'O', True),
        
        # 4.1 Out-of-Bounds Move Test: Row
        ("out_of_bound_row_test",
         3, 0, 'O', False),
        
        # 4.2 Out-of-Bounds Move Test: Column
        ("out_of_bound_column_test",
         0, 3, 'O', False),
        
        # 4.3 Out-of-Bounds Move Test: Row and Column
        ("out_ot_bound_both_test",
         3, 3, 'O', False),
    ]
)
def test_make_move(test_type, test_board, row, col, player, expected):
  result = make_move(test_board, row, col, player)
  assert result == expected, f"{test_type} move error: Expected result {expected}, but got {result}."

  # then i want to test whether the board occupation is correct
  if result:
    # check situations where result is True. i.e., the move is valid
    assert test_board[row][col] == player, f"{test_type} board error: Expected board[{row}][{col}] to be {player}, but got {test_board[row][col]}."
  else:
    if (0 <= row < len(test_board)) and (0 <= col < len(test_board[0])):
      # check situations where the move is invalid due to cell occupied
      assert test_board[row][col] != player, f"{test_type} board error: Expected board[{row}][{col}] should not be {player}."
    
    else:
      # check situations where
      assert test_board == [['X', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']], f"{test_type} board error: bound change!"

