# Day 26 //Project 26

---
---
### What?
-  Topic  --> **List and Dictionary Comprehension**
- Project --> 

-
- List comprehesion SOP 
1. new_list = [new_item for item in list]
2. new_list = [new_item for item in list if test]

// Use list comprehension to project 24 to reduce lines

- Dictionary comprehesion SOP 
1. new_dict = {new_key:new_value for item in list}
2. new_dict = {new_key:new_value for (key,value) in dict.items()}
3. new_dict = {new_key:new_value for (key,value) in dict.items() if test}


## What I learn so far

- List Comprehesion
    - how to use list comprehension
    - how to use if statement in list comprehension
    - how to use function in list comprehension like `string.upper()`
    - find even numbers
    - use of range in list comprehension
    - how to get square number from number

- Dictionary Comprehension
    - new_dict = {new_key:new_value for item in list}
    - how to find how many time a letter occurs in a string (count)
    - i use the same count func in to create a nested dict
    - generate random score for particular student
    - how to use key,value pair in dictionary comprehension
    - how to find each word length from a sentece (ex: text = "The quick brown fox jumps over the lazy dog")
    - using `dictionary.items()` how to find key,value
    - how to read data in padnas library
    - pandas loop through row by row (`dataframe.iterrows()`) - for ex (df.iterrows())
        - 1
        ```
        for (index, row) in student_data_frame.iterrows():
        if row.score >= 90:
            print(row.student)
        ```
        - 2
        ```
        # **Find the student with the highest score in a DataFrame of student scores***
        max_score = -1
        hig_score_std = []
        for index,row in df.iterrows():
            if row.score > max_score:
                max_score = row.score
                hig_score_std = [row.student]
            elif row.score == max_score:
                hig_score_std.append(row.student)
        print(hig_score_std)
        ```

        - ** In the 2nd code there is very interseting concept i learn which is how to create a single element list which is super cool
- Final Project
    - nato phonetich_alphabate letter
    - I learn how to create a dictionary from csv file using .iterrows()
        ```
        nato_dict = {row.letter: row.code for index,row in data.iterrows()}
        # print(nato_dict)
        ```
    - how to create an output list through phonetic_dict
        ```
        user_word = input("Enter a word: ").upper()
        output_list = [nato_dict[letter] for letter in user_word]
        print(output_list)
        ```
---
---