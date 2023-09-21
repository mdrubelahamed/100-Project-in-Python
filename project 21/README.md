# PING PONG GAME

## What?
- Create Screen
- Create Paddle in oop
- move the paddle
- Ball bounce it hits the upper and lower side of the screen
- Ball contact with the paddle


## Note How I Am Doing It?
-  Setup a 1000,600 Screen  

-  I Create a "Paddle" With Where I Use "Turtle" As a Super Class 
- Then I Design Two Move_Up And Move_Down Function
`self.shapesize(stretch_wid=5, stretch_len=1)` Here I Strech My Paddle Length Multiply By 5

- Create The Ball?
First I Create a File Called `ball.py` The Inside This I Create a Ball Turtle, And Create a Move Function Which Change The .xcor() And .ycor()
So It'S Looks That The Ball Is Moving
& I Added Also Sleep Time So The Ball Move After a Time Gap

- I Added a Logic Where The Ball Will Bounce If The Ball Hit The Upper or Lower Side Of The Screen(By Reversing The Y-Axis Direction)
```
    def bounce_y(self):
        self.y_move *= -1
```

- Then I Added a Logic Where If The Ball Hits The Paddle'S The Ball Change his Direction In The Opposite Where I Change X-Axis Direction, So The Ball Move To The Opposite Direction
```
    def bounce_x(self):
        self.x_move *= -1
```

- Then I Added Some Logic By Which If The Ball Goes Or Too Far From The Screnn Either Right Side Or Left Side The Ball Will Reset His Position To The Home Position And If **Goes To The Opposite Side Of Paddle**
```
    def reset_postion(self):
        self.home()
        self.x_move *= -1
```
- Also I added two condition where if ball miss the right paddle the point will be goes to the left player and vice-versa