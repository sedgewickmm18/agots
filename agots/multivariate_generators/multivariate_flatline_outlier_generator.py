import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateFlatlineOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, factor=8):
        timestamps = timestamps or []
        self.timestamps = timestamps
        self.factor = factor

    def add_outliers(self, timeseries):
        additional_values = np.zeros(timeseries.size)
        for start, end in self.timestamps:
            local_mean = timeseries.iloc[max(0, start - 10):end + 10].mean()
            additional_values[list(range(start, end))] += -timeseries.iloc[start:end] + local_mean
        return additional_values
