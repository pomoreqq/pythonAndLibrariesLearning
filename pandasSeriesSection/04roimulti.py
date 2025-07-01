
import pandas as pd
arrays = [
    [2021, 2021, 2021, 2022, 2022, 2022, 2023, 2023, 2023],
    ['Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3']
]

index = pd.MultiIndex.from_arrays(arrays, names=("year", "quarter"))

kpi = pd.DataFrame({
    'ROI': [0.12, 0.10, 0.15, 0.13, 0.14, 0.11, 0.18, 0.17, 0.16]
}, index=index)


sortedKpi = kpi.sort_index(level=['year', 'quarter'], ascending=[False, True])
roiToNumpy =  sortedKpi['ROI'].to_numpy()
print(sortedKpi)
print(roiToNumpy)