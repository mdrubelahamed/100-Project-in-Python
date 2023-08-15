# Calculating avarage height of people
# heights = [189,221,345]

# take all height input
heights_input = input("Tell me friends seperared by comma(,) ")
heights_str_list = heights_input.split(",")

# make str value -- int value, and append to heights list
heights = []

for height in heights_str_list:
    heights.append(int(height))
    
combined_height = 0
length_of_list = 0
for height in heights:
    combined_height += height
    length_of_list += 1

avg_height = round(combined_height / length_of_list)
print(f"Rounded avarage height of your friends  {avg_height}")
