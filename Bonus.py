import statistics

age = [36.36
,47.02
,54.15
,39.67
,40.31
,34.86
,22.14
,59.12
,58.18
,29.73
,42.5
,22.21
,45.45
,21.1
,59.47
,50.97
,47.23
,24.66
,58.08
,49.85
,22.64
,23.77
,44.72
,37.27
,59.42
,28.02
,27.59
,48.09
,42.39
,53.68
,36.24
,36.14
,23.92
,26.24
,24.02
,49.69
,48.49
,33.89
,43.63
,55.97
,55.14
,35.02
,32.58
,38.65
,52.99
,33.73
,27.73
,56.38
,23.73
,21.3
,28.76
,28.23
,58.15
,34.75
,56.66
,26.25
,24.61
,59.27
,56.27
,21.93
,56.53
,47.78
,32.75
,22.72
,25.93
,57.37
,32.08
,52.51
,30.9
,34.87
,43.59
,54.16
,25.1
,31.29
,58.43
,25.96
,32.29
,26.35
,50.05
,41.19
,48.79
,25.98
,32.77
,33.55
,24.01
,42.79
,42.21
,50.7
,35.91
,37.62
,37.84
,39.77
,37.57
,56
,39.43
,22.82
,32.61
,52.66
,29.6
,38.38
]

print("Standard Deviation in age of the employees of the organization = " + str(statistics.stdev(age)))
print("Variance in age of the employees of the organization = " + str(statistics.variance(age)))