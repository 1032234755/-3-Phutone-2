
import numpy as np
from scipy.integrate import quad

# ������� ��� ��������������
def integrand(x):
    return np.exp(-2 * x) * np.sin(6 * x)

# �������������� � ������� quad (���������� ������������ �������)
integral_value, error = quad(integrand, 0, np.inf)

print(f"�������� ��������� = {integral_value:.10f}, ������ ������ = {error:.10e}")
