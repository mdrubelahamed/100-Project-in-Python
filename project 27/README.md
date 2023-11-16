# Day 27 //Project 27

------
### What?
-   Topic -> Graphical User Interfaces with Tkinter and Function Arguments
- Project ->

### What I learn so far?
- How to Create a window with the help of tkinter, `tkinter.Tk`
- How to Make the window visible `tkinter.mainloop()`
- how to display label `Lable.Pack()`
- How to change size of window, change text font, side, expanded

### Advance Arguments  
- *args  
 *args stads for unlimited positonal arguments, it's use when you want to pass lots of parameter but don't want specify how many parameter you want pass in a function so there comes *args, * is mandotary and args is variable so you can change it on your own, but it's better to use args. the args variable become a 'tuple'.
to give you an example here it is 
    ```
    def even_num(*args):
        even_list = []
        for n in args:
            if n%2 == 0:
                even_list.append(n)
        return even_list

    print(even_num(1,2,3,4,5,6,7,8,9,10))
    ```

- *kwargs  
*kwargs stands for keyword argument where you can specify as many as you can and it's represent a dictionary where the keytword is the key and the argument is the value. we can create class also by *kw, to give you an example here it is 
    ```
    def calculate(n, **kwargs):
        print(kwargs)
        # print(kwargs["add"])
        # print(kwargs["multiply"])

        for key, value in kwargs.items():
            print(key)
            print(value)
        n += kwargs["add"]
        print(n)
        n *= kwargs["multiply"]
        print(n)


    calculate(5, add=2, multiply=3)
    ```


    ```
    # create a class with kwars from scratch

    class Car:
        def __init__(self, **kw):
            self.make = kw.get("make")
            self.model = kw.get("model")
            self.color = kw.get("color")
            self.speed = kw.get("speed")
        
    my_car = Car(make="Tata", model="Nano", speed=255)
    print(my_car.color)
    ```


---
---