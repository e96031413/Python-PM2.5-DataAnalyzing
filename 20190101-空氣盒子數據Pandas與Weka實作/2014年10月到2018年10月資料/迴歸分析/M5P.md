=== Run information ===

Scheme:       weka.classifiers.trees.M5P -M 4.0
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

M5 pruned model tree:
(using smoothed linear models)

NMHC <= 0.209 : 
|   CO <= 0.405 : 
|   |   SO2 <= 2.65 : LM1 (11/26.503%)
|   |   SO2 >  2.65 : LM2 (13/28.48%)
|   CO >  0.405 : LM3 (34/34.978%)
NMHC >  0.209 : LM4 (22/53.848%)

LM num: 1
PM25 = 
       2.7509 * SO2 
       + 8.0071 * CO 
       - 0.033 * CO2 
       + 0.2156 * O3 
       - 0.1232 * Nox 
       - 0.1063 * NO 
       + 13.0087 * NMHC 
       - 2.7474 * CH4 
       + 1.8054 * WindSpeed 
       - 0.2508 * TEMP 
       + 21.678

LM num: 2
PM25 = 
       2.6346 * SO2 
       + 8.492 * CO 
       - 0.0307 * CO2 
       + 0.1723 * O3 
       - 0.1232 * Nox 
       - 0.1063 * NO 
       + 13.0087 * NMHC 
       - 2.7474 * CH4 
       + 3.0871 * WindSpeed 
       - 0.2438 * TEMP 
       + 20.4065

LM num: 3
PM25 = 
       0.9767 * SO2 
       + 26.3486 * CO 
       + 0.3695 * O3 
       - 0.0981 * Nox 
       - 0.1063 * NO 
       + 13.0087 * NMHC 
       - 2.7474 * CH4 
       - 0.1317 * TEMP 
       + 1.3021

LM num: 4
PM25 = 
       7.1546 * SO2 
       + 9.3346 * CO 
       + 0.1454 * O3 
       - 0.2097 * NO 
       - 16.8862 * THC 
       + 77.184 * NMHC 
       - 5.4205 * CH4 
       - 0.1061 * TEMP 
       + 27.2498

Number of Rules : 4

Time taken to build model: 0.11 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.9212
Mean absolute error                      1.7976
Root mean squared error                  2.4361
Relative absolute error                 36.3156 %
Root relative squared error             39.3325 %
Total Number of Instances               80     