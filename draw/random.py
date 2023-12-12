# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.integrate import solve_ivp

# plt.style.use("seaborn-poster")

# # %matplotlib inline

# F = lambda t,s: np.cos(t)

# t_eval = np.arange(1, np.pi, 1.1)

# sol = solve_ivp(F, [1, np.pi], [1], t_eval=t_eval)

# plt.figure(figsize= (12,4))
# plt.subplot(121)
# plt.plot(sol.t, sol.y[1])
# plt.xlabel('t')
# plt.ylabel('S(t) - sin(t)')
# plt.tight_layout()
# plt.show()


# # import this

# x = "WHAT IS A 401(K)?"
# y = x.capitalize()
# print(y)

from tkinter import *

root = Tk()
root.minsize(width=500, height=500)

w = Canvas(root, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()