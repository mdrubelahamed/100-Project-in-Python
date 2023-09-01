# CREATE A QUIZ GAME TRUE AND FALSE WITH OBJECT ORIENTED PROGRAMMING

## create my own class


# Constructer
- Initialize at the begining of the clas
```
class Car:
    def __init__(self):
    #Initialize attributes
```


```
# user_1 = User()
# user_1.id = "001"
# user_1.username = "rubel"

# print(user_1)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "rohan"

# user_3 = User()
# user_3.id = "003"
# user_3.username = "robert"
```

```
# print("Every time __init__ will be called when we create an object")
class User:

    def __init__(self, user_id, username):
        """"Every time __init__ will be called when we create an object"""
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "rubel")
user_2 = User("002", "rohan")


user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# print(user_1.username)
# print(user_1.followers)
```