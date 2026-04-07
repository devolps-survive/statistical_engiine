from typing import List, Union
import math

Number = Union[int, float]


class StatEngine:
    def __init__(self, data: Union[List, tuple]):
        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("Dataset is empty after cleaning.")

    def _clean_data(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")

        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(float(x))
            elif isinstance(x, str):
                try:
                    cleaned.append(float(x))
                except ValueError:
                    raise TypeError(f"Invalid value: {x}")
            else:
                raise TypeError(f"Unsupported type: {type(x)}")

        return cleaned

    # ---------------- CENTRAL TENDENCY ---------------- #

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        freq = {}
        for val in self.data:
            freq[val] = freq.get(val, 0) + 1

        max_count = max(freq.values())

        if max_count == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in freq.items() if v == max_count]
        return modes

    # ---------------- DISPERSION ---------------- #

    def get_variance(self, is_sample: bool = True) -> float:
        n = len(self.data)
        if n < 2 and is_sample:
            raise ValueError("Sample variance requires at least 2 data points.")

        mean = self.get_mean()

        squared_diffs = [(x - mean) ** 2 for x in self.data]
        divisor = (n - 1) if is_sample else n

        return sum(squared_diffs) / divisor

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        return math.sqrt(self.get_variance(is_sample))

    # ---------------- OUTLIERS ---------------- #

    def get_outliers(self, threshold: float = 2):
        mean = self.get_mean()
        std = self.get_standard_deviation(is_sample=True)

        if std == 0:
            return []

        outliers = [
            x for x in self.data
            if abs(x - mean) > threshold * std
        ]

        return outliers
