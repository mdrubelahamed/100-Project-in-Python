from prettytable import PrettyTable

# create an object called 'table' from 'PrettyTable' class 
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

# print(table.align)
table.align = "l"


print(table)
