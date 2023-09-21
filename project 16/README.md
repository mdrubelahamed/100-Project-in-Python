## ?review

- Using turtle 

```
# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.color("green")
# timmy.shape("turtle")
# 
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)
```


- How to integreted python packages into project?
Ans: I just install a package in my "100 project in python" folder, 
package name - PrettyTable
version - 0.7.2
```pip install PrettyTable==0.7.2```   

NOTE: I am install this version explicitly 'cause from my learning resource,she install the same version so it would better that i use the same version when i am learning, which makes less confusion


- Use PrettyTable
```
from prettytable import PrettyTable

x = PrettyTable()
x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

print(x)
```

```
# CREATE A TABLE ON YOUR OWN
from prettytable import PrettyTable

# create an object called 'table' from 'PrettyTable' class 
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

# print(table.align)
table.align = "r"


print(table)

```



Q. BUILD A REAL LIFE TABLE FROM THE INTERNET?   
--> 









```
from turtle import Turtle
timmy = Turtle()

timmy.width(5)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.home()
timmy.forward(100)
timmy.right(angle=90)
timmy.forward(100)
timmy.right(angle=90)
timmy.forward(100)
timmy.right(angle=90)
timmy.forward(100)
# timmy.right(angle=90)
```