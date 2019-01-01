=== Run information ===

Scheme:       weka.classifiers.trees.REPTree -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0
Relation:     KH-1982-2018
Instances:    401
Attributes:   13
              SO2
              CO
              O3
              PM25
              Nox
              NO
              NO2
              THC
              NMHC
              CH4
              WindSpeed
              TEMP
              Humidity
Test mode:    evaluate on training data

=== Classifier model (full training set) ===


REPTree
============

TEMP < 27.88
|   TEMP < 25.29
|   |   NMHC < 0.17
|   |   |   TEMP < 21.81 : 36.17 (4/17.19) [2/7.06]
|   |   |   TEMP >= 21.81 : 27.38 (6/18.58) [2/13.25]
|   |   NMHC >= 0.17 : 39.93 (85/14.34) [34/15.74]
|   TEMP >= 25.29
|   |   CO < 0.34 : 19.8 (8/11.5) [2/122]
|   |   CO >= 0.34
|   |   |   Nox < 26.79
|   |   |   |   CH4 < 1.98
|   |   |   |   |   WindSpeed < 1.79
|   |   |   |   |   |   THC < 2.06 : 21.33 (2/0.25) [1/0.25]
|   |   |   |   |   |   THC >= 2.06
|   |   |   |   |   |   |   SO2 < 5.1 : 25 (5/0.8) [2/1]
|   |   |   |   |   |   |   SO2 >= 5.1 : 23.5 (2/0.25) [0/0]
|   |   |   |   |   WindSpeed >= 1.79 : 27.22 (12/7.24) [6/6.48]
|   |   |   |   CH4 >= 1.98 : 30.85 (17/14.72) [10/17.71]
|   |   |   Nox >= 26.79 : 36.33 (4/2.19) [5/34.66]
TEMP >= 27.88
|   O3 < 28.7
|   |   O3 < 19.15
|   |   |   WindSpeed < 1.06 : 14 (3/8.67) [2/12.5]
|   |   |   WindSpeed >= 1.06
|   |   |   |   NO < 3.08 : 10.57 (3/4.67) [4/12.25]
|   |   |   |   NO >= 3.08 : 8.3 (19/1.94) [8/13.75]
|   |   O3 >= 19.15
|   |   |   THC < 2.01
|   |   |   |   O3 < 26.05
|   |   |   |   |   Humidity < 74.09 : 12.53 (12/1.42) [5/12.65]
|   |   |   |   |   Humidity >= 74.09 : 10.57 (16/4.25) [12/5.25]
|   |   |   |   O3 >= 26.05
|   |   |   |   |   SO2 < 3.6
|   |   |   |   |   |   CO < 0.26 : 13.33 (2/0.25) [1/0.25]
|   |   |   |   |   |   CO >= 0.26 : 12 (3/0) [1/0]
|   |   |   |   |   SO2 >= 3.6 : 15.2 (3/0.89) [2/43.61]
|   |   |   THC >= 2.01 : 14.69 (21/6.9) [14/34.63]
|   O3 >= 28.7
|   |   NO2 < 14.47 : 18.33 (31/10.35) [15/16.6]
|   |   NO2 >= 14.47
|   |   |   TEMP < 28.66 : 25.33 (6/6.47) [3/26.47]
|   |   |   TEMP >= 28.66 : 20.5 (3/2.67) [3/15]

Size of the tree : 43

Time taken to build model: 0.02 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.9587
Mean absolute error                      2.5781
Root mean squared error                  3.483 
Relative absolute error                 23.6516 %
Root relative squared error             28.4262 %
Total Number of Instances              401     

