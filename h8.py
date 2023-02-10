
# отримувати відсоток, та кількість використаної оперативної
# пам'яті в даний момент часу.

import psutil

print(f"Використання оперативної пам'яті:")
print(f"{psutil.virtual_memory()[2]}%\n"
      f"{round(psutil.virtual_memory()[3]/1000000000, 3)} ГБ")

