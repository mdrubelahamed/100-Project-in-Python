import os
# [os.makedirs(f"day{i}", exist_ok=True) or open(f"day{i}/README.md", "a").close() for i in range(6, 101)]
# [os.rename(f"day{i}", f"day {i}") for i in range(6, 101)]

import shutil; [shutil.rmtree(f"day {i}") for i in range(6, 101)]


