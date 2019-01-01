=== Run information ===

Scheme:       weka.classifiers.trees.REPTree -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0
Relation:     2014-2018
Instances:    80
Attributes:   14
              SO2
              CO
              CO2
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

NMHC < 0.21
|   O3 < 26.1
|   |   CO < 0.46 : 13.27 (13/3.21) [9/6.78]
|   |   CO >= 0.46 : 16.5 (4/5.25) [4/5.25]
|   O3 >= 26.1 : 17.71 (19/9.32) [9/9.63]
NMHC >= 0.21
|   TEMP < 25.39 : 25.17 (13/9.21) [5/29.36]
|   TEMP >= 25.39 : 32.75 (4/34.69) [0/0]

Size of the tree : 9

Time taken to build model: 0 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.8573
Mean absolute error                      2.5928
Root mean squared error                  3.1885
Relative absolute error                 52.3799 %
Root relative squared error             51.4812 %
Total Number of Instances               80     

