
import numpy as np
from scipy.integrate import quad

# Функция для интегрирования
def integrand(x):
    return np.exp(-2 * x) * np.sin(6 * x)

# Интегрирование с помощью quad (адаптивное квадратурное правило)
integral_value, error = quad(integrand, 0, np.inf)

print(f"Значение интеграла = {integral_value:.10f}, Оценка ошибки = {error:.10e}")
