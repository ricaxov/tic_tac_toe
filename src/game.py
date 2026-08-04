from dataclasses import dataclass

"""
2 ^ pos 

1 2 3
4 5 6
7 8 9

  01   23   45
  67   89 1011
1213 1415 1617

00 -> unmarked
01 -> X
10 -> O
11 -> used for anding with whole bitmask

0000
"""

@dataclass
class Board: 
  bitmask: int = 0

  def cell_state(self, cell_idx):
    state = (self.bitmask >> (cell_idx * 2)) & 0b11

    return (" ", "X", "O")[state]
    
  def print_board(self):
    print(f" {self.cell_state(0)} | {self.cell_state(1)} | {self.cell_state(2)} ")
    print("---+---+---")
    print(f" {self.cell_state(3)} | {self.cell_state(4)} | {self.cell_state(5)} ")
    print("---+---+---")
    print(f" {self.cell_state(6)} | {self.cell_state(7)} | {self.cell_state(8)} ")

    
  # printar board na tela
  # update board baseado na jogada feita (da pessoa / bot)
  # board checka quem venceu 
  # check if input is valid 

  # fazer no Game (game tem uma class board dentro dele)
  # args: dificuldade do bot + turno de quem

  # receber input (pessoa) => clickavel/setinhas piscar 
  # fazer minimax (jogada do bot)

  # runner eh a main 

B = Board(2)
B.print_board()