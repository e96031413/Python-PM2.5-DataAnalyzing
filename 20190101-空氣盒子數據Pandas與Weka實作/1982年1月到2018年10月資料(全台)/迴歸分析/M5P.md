=== Run information ===

Scheme:       weka.classifiers.trees.M5P -M 4.0
Relation:     1982-2018
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

M5 pruned model tree:
(using smoothed linear models)

NMHC <= 0.209 : LM1 (58/37.885%)
NMHC >  0.209 : LM2 (22/53.848%)

LM num: 1
PM25 = 
       2.2648 * SO2+ 30.7844 * CO+ 0.2013 * O3- 0.3204 * Nox- 0.106 * NO+ 13.1344 * NMHC-2.5891 * CH4- 0.308 * TEMP+ 9.446

LM num: 2
PM25 = 
       7.1509 * SO2+ 9.1064 * CO+ 0.1448 * O3- 0.2092 * NO- 16.8862 * THC+ 77.4321 * NMHC- 5.1083 * CH4-
       0.1052 * TEMP+ 26.7523

Number of Rules : 2

Time taken to build model: 0.03 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.9058
Mean absolute error                      2.0226
Root mean squared error                  2.6394
Relative absolute error                 40.8598 %
Root relative squared error             42.616  %
Total Number of Instances               80     

