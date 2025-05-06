# # import turtle
# from turtle import Turtle, Screen
# import prettytable
from prettytable import PrettyTable

# bob = Turtle()
# print(bob)
# bob.shape("turtle")
# bob.color("red")
# bob.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
pokemon = ['Pikachu','Squirtle', 'Chamander']
pokemon_type = ['Eletric', 'Water', 'Fire']
table.add_column('Pokemon Name', pokemon)
table.add_column('Type', pokemon_type)
table.align = 'l'
print(table)