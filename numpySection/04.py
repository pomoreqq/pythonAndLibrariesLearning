import numpy as np

# response_times = np.array([5, 12, 3, 18, 6, 9, 20, 2])

# meanResponse = np.mean(response_times)

# lenOfFasterResponses = len(response_times[response_times < meanResponse])

# indicesOfSlowResponses = np.where(response_times > 10)


eur_rates = np.array([4.50, 4.48, 4.52, 4.55, 4.60, 4.58])

diffs = np.diff(eur_rates)
maxChange = np.max(np.abs(np.diff(eur_rates)))
diffCount = np.sum(diffs < 0)

maxChangeAmplitude = np.abs(np.max(eur_rates) -  np.min(eur_rates))



order_sizes = np.array([3, 0, 1, 4, 6, 2, 0, 5])

lenOfZero = len(order_sizes[order_sizes == 0])

indicesOfNotZero = np.where(order_sizes > 0)
notZero = order_sizes[indicesOfNotZero]
meanOfNotZero = np.mean(notZero)

moreThanMeanWithNoZero = notZero[notZero > meanOfNotZero]