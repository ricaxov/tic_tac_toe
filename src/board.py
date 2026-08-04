from dataclasses import dataclass

"""
2 ^ pos

1 2 3
4 5 6
7 8 9

  01   23   45
  67   89 1011
1213 1415 1617

00 -> unmarked (0)
01 -> X (1)
10 -> O (2)
11 -> used for anding with whole bitmask (3)

1100
--11
"""

@dataclass
class Board: 
  bitmask: int = 0

  # def get_mask_per_idx

  # turn bit on
  # turn bit off 
  # helper functions ^^^

  def cell_state(self, cell_idx: int):
    state = (self.bitmask >> (cell_idx * 2)) & 0b11

    return (" ", "X", "O")[state]


  def update_cell(self, cell_idx: int, new_cell: str):
    if cell_idx not in range(9) or new_cell not in (" ", "X", "O"):
        return False

    val = {" ": 0b00, "X": 0b01, "O": 0b10}[new_cell]
    self.bitmask &= ~(0b11 << (cell_idx * 2))
    self.bitmask |= (0b11 << (cell_idx * 2))

    return True
  
  def check_winner(self):
      # 01   23   45
      #   67   89 1011
      # 1213 1415 1617

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

resp = B.update_cell(1, "X")
print(resp)
B.print_board()

B.update_cell(0, "O")
B.print_board()

print("asd")

A = Board(1)
A.print_board()