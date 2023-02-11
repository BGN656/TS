# %%
import math

import numpy as np
from scipy.integrate import solve_ivp

C_F = 0.47  # шар
G = 9.81  # ускорение свободного падения, м/с^2
MASS = 2
RHO = 4
S = math.pi * 0.1**2 / 4


def gravity_force() -> np.array:
    """Посчитать вектор силы гравитации.

    Returns
    -------
    np.array
        Вектор силы гравитации.
    """
    return np.array([0, 0, -MASS * G])


def aerodynamic_drag_force(velocity: np.array) -> np.array:
    """Посчитать вектор силы аэродинамического сопротивления из вектора скорости.

    Parameters
    ----------
    velocity : np.array
        Вектор скорости.

    Returns
    -------
    np.array
        Вектор силы аэродинамического сопротивления.
    """
    drag_force = -C_F * RHO * velocity * np.linalg.norm(velocity) / 2 * S

    return drag_force


def total_force(velocity: np.array) -> np.array:
    """Посчитать вектор общей силы действующей на тело.

    Parameters
    ----------
    velocity : np.array
        Вектор скорости.

    Returns
    -------
    np.array
        Вектор общей силы.
    """
    force = gravity_force() + aerodynamic_drag_force(velocity)

    return force


def three_dimensional_cannon_with_drag(t: float, y: np.array) -> np.array:
    """Функция вычисляет dy/dt, где y - вектор состояния.

    Parameters
    ----------
    t : float
        время
    y : np.array
        rx, ry, rz, vx, vy, vz

    Returns
    -------
    np.array
        dy/dt = np.array([vx, vy, vz, ax, ay, az])
    """

    acceleration = total_force(velocity=y[3:]) / MASS

    # конвертацию в numpy можно убрать, в любом случае будет осуществлена автоматически
    dy_dt = np.array([*y[3:], *acceleration])

    return dy_dt


def hit_ground_three_dimensional(t: float, y: np.array) -> np.float64:
    """Event-функция, которая выдаёт нуль только при касании земли

    Parameters
    ----------
    t : float
        время
    y : np.array
        rx, ry, rz, vx, vy, vz
    Returns
    -------
    float
        rz = y[2]
    """

    return y[2]


hit_ground_three_dimensional.terminal = True
hit_ground_three_dimensional.direction = -1

# %%
r0 = [0, 0, 0]
v0 = [1, 2, 100]

sol = solve_ivp(
    fun=three_dimensional_cannon_with_drag,
    t_span=[0, 30],
    y0=[*r0, *v0],
    events=hit_ground_three_dimensional,
)


rx, ry, rz, vx, vy, vz = sol.y
t = sol.t
print(f"Касание поверхности земли произошло в {t[-1]} c")
print(f"rx = {rx[-1]:.2f}, ry = {ry[-1]:.2f}, rz = {rz[-1]:.2f}")
print(f"vx = {vx[-1]:.2f}, vy = {vy[-1]:.2f}, vz = {vz[-1]:.2f}")

# %%
