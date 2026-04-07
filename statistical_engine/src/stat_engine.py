import math
from typing import List, Union


class StatEngine:
    def __init__(self, data: Union[List, tuple]):
        if not data:
            raise ValueError("Dataset cannot be empty.")

        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("No valid numeric data found.")

    def _clean_data(self, data):
        cleaned = []
        for item in data:
            if isinstance(item, (int, float)):
                cleaned.append(float(item))
            else:
                raise TypeError(f"Invalid data type detected: {item}")
        return cleaned

    # -------------------------
    # CENTRAL TENDENCY
    # -------------------------

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]

        if max_freq == 1:
            return "No mode (all values are unique)"

        return modes

    # -------------------------
    # DISPERSION
    # -------------------------

    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean = self.get_mean()

        if is_sample:
            if n < 2:
                raise ValueError("Sample variance requires at least 2 data points.")
            denominator = n - 1
        else:
            denominator = n

        variance = sum((x - mean) ** 2 for x in self.data) / denominator
        return variance

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # -------------------------
    # OUTLIERS
    # -------------------------

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        return [
            x for x in self.data
            if abs(x - mean) > threshold * std
        ]