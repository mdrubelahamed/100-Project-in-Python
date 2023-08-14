## mark a particular spot

# define rows
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Which locker do you want your treasure to be safe? ")

horizontal = int(position[0]) - 1 # horizontal == coloum
vertical = int(position[1]) - 1   # vertical == row

map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")