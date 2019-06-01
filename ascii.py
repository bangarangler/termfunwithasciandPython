from pyfiglet import figlet_format
from termcolor import colored
from random import choice


def randAscii():
  valid_colors = ('red','green','yellow','blue','magenta','cyan','white')
  words = ('Jon','JP',"Dain",'Node!!!!!','Python!!!','React!!','Code!')
  randm = choice(words)
  randc = choice(valid_colors)

  ascii_art = figlet_format(randm)
  colored_ascii = colored(ascii_art, color=randc)
  print(colored_ascii)

randAscii()



