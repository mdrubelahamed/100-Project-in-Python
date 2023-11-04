## day 24    
- what?     
In today's lesson I know about file system, absolute path, relative path, how to read, write, append file, also about .replace(), .strip() and most importantly .readlines()

how .readlines() return a list of every line,
for ex:
```
['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']
```
- .write()      
it generally overwrite on the file content, but if the file not present on the current directory it's create the particular file which is really cool

- project   
with the help of those python features i create many mails where the for every letter the person name will show like - Dear [name], ....<br>
and the file name was `letter_for_{name}.txt` If any one reading this they can find the code on the `project 23/main.py` file, I am writing this so whenever I want to what i did in the particular project I just get the view of what was the project back in the day     
✌🏼Peace

---


### open, read, write files using the "with" keyword
- 1 
```# with open("project 23\myfile.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("project 23\\new_file.txt", mode="w") as file:
#     file.write("This is text file, which is not present in the folder so first it will create the file and the it will write the text which i am providing..")
```
```
# with open(file="project 23\hello.txt", mode="w") as file:
#     file.write("I am writing on a file which is not present in the currrent folder")

```

### Mail Merging

---
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp  
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp     
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp    

---