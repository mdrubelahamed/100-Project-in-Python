# For loops, range and Code Blocks
### day5 notes

## For loop


### Proj 
Here I learn a important lessson of using for loop and one another thing   
How to take number input as a string, then split those number in one by one value   
then, create an another list    
lastly, append those values one as an int, using for loop
```
heights_input = input("Tell me friends seperared by comma(,) ")
heights_str_list = heights_input.split(",")

# make str --> int, and append to heights list
heights = []

for height in heights_str_list:
    heights.append(int(height))
```

### project highest score lowest score
```
lowest_score = student_score[0]
for score in student_score:
    if score < lowest_score:
        lowest_score = score
print(f"The lowest Score in the class is: {lowest_score}")
```