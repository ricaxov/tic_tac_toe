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
"""

@dataclass
class Board: 
  bitmask: int

  # printar board na tela
  # update board baseado na jogada feita (da pessoa / bot)
  # board checka quem venceu 
  # check if input is valid 

  # fazer no Game (game tem uma class board dentro dele)
  # args: dificuldade do bot + turno de quem

  # receber input (pessoa) => clickavel/setinhas piscar 
  # fazer minimax (jogada do bot)

  # runner eh a main 