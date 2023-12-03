import os

dayno = 29
projno = 29
path = f"./project {projno}"



os.mkdir(path=path)

with open(f"./project {projno}/main.py", mode="w") as f1, open(f"./project {projno}/README.md", mode="w") as f2:
    f1.write("")
    f2.write(f"""# Day {dayno} //Project {projno}

---
---
### What?
-   Topic 
- Project

- What I learn so far?
-

---
---""")

