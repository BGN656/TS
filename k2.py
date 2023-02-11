# %%
import numpy as np
from matplotlib import pyplot as plt

# %%
x = np.arange(1, 10, 0.1)
y1 = np.log(x)
y2 = 2**x


# %%
plt.figure()
plt.plot(x, y1, "black", label="Ускорение", ls="-.")
plt.plot(x, y2, "black", label="2-й график", marker="^")
plt.xlim(left=2, right=6)
plt.ylim(bottom=1, top=100)
plt.yscale("log")
plt.xlabel("Время, с")
plt.ylabel(r"Ускорение, $м/с^2$")
plt.title("2 графика", fontsize=30)
plt.legend()
plt.grid()
plt.savefig("grafics.svg")

# %%
x = np.arange(1, 10, 0.1)
y1 = np.log(x)
y2 = 2**x

# Create two subplots and unpack the output array immediately
fig, axes = plt.subplots(2, 2, sharey=True)

axes[0][0].plot(x, y1)
axes[0][0].set_title("Логарифм")
axes[0][0].set_xlabel("Время")
axes[0][0].set_ylabel(r"Ускорение, $м/с^2$")

axes[1][1].scatter(x, y2)
fig.suptitle("Общий заголовок", fontsize=25)
fig.tight_layout()


# %%
