from respy.shared import calculate_expected_value_functions
import numpy as np
import pandas as pd

# Set up inputs
wage = np.array([1.46178695e04, 9.70115277e03, 1.00000000e00, 1.00000000e00])
nonpec = np.array([0.0, 0.0, -4000.0, 17750.0])
continuation_values = np.array(
    [359856.6202004, 362415.98557173, 375897.29303581, 353287.24408844]
)
draws = pd.read_pickle("draws.pickle")
delta = 0.95


# Evaluate the integral
res = calculate_expected_value_functions(
    wage, nonpec, continuation_values, draws, delta
)
print(res)
