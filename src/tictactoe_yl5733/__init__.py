# read version from installed package
from importlib.metadata import version
__version__ = version("tictactoe_yl5733")

from .tictactoe_yl5733 import initialize_board, make_move, check_winner, reset_game
__all__ = ["initialize_board", 
           "make_move", 
           "check_winner", 
           "reset_game"]
