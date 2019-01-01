=== Run information ===

Scheme:       weka.classifiers.trees.M5P -M 4.0
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
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

M5 pruned model tree:
(using smoothed linear models)

TEMP <= 27.905 : 
|   TEMP <= 25.29 : 
|   |   NMHC <= 0.19 : LM1 (41/32.513%)
|   |   NMHC >  0.19 : LM2 (92/28.194%)
|   TEMP >  25.29 : LM3 (77/27.483%)
TEMP >  27.905 : 
|   O3 <= 25.6 : LM4 (105/19.315%)
|   O3 >  25.6 : LM5 (86/25.199%)

LM num: 1
PM25 = 
       -2.6845 * SO2 
       + 18.3794 * CO 
       + 0.0409 * O3 
       + 0.4027 * Nox 
       - 0.3489 * NO 
       + 0.2208 * NO2 
       + 18.3256 * THC 
       + 14.7424 * NMHC 
       + 2.1709 * CH4 
       + 1.298 * WindSpeed 
       - 0.1256 * TEMP 
       - 0.3165 * Humidity 
       + 1.5285

LM num: 2
PM25 = 
       -0.307 * SO2 
       - 3.5132 * CO 
       + 0.0409 * O3 
       - 0.2182 * NO 
       + 0.296 * NO2 
       + 1.3192 * THC 
       + 8.9908 * NMHC 
       + 2.1709 * CH4 
       + 1.298 * WindSpeed 
       - 0.0528 * TEMP 
       - 0.0838 * Humidity 
       + 31.9873

LM num: 3
PM25 = 
       -0.2261 * SO2 
       + 6.0771 * CO 
       + 0.2569 * O3 
       + 0.3797 * Nox 
       - 0.1202 * NO 
       + 0.0988 * NO2 
       + 21.1361 * THC 
       + 4.3036 * NMHC 
       + 2.1709 * CH4 
       + 6.599 * WindSpeed 
       - 0.8863 * TEMP 
       - 0.0838 * Humidity 
       - 22.6008

LM num: 4
PM25 = 
       -0.0407 * SO2 
       - 12.7195 * CO 
       + 0.0555 * O3 
       - 1.3445 * NO 
       + 0.4684 * NO2 
       + 0.1609 * THC 
       + 20.3628 * NMHC 
       + 11.9558 * CH4 
       + 3.0954 * WindSpeed 
       + 0.1468 * TEMP 
       - 0.1681 * Humidity 
       - 1.4847

LM num: 5
PM25 = 
       -0.0407 * SO2 
       - 11.8582 * CO 
       + 0.3403 * O3 
       - 1.4731 * NO 
       + 0.6312 * NO2 
       + 16.5824 * THC 
       + 5.602 * CH4 
       + 3.4488 * WindSpeed 
       + 0.1468 * TEMP 
       - 0.0915 * Humidity 
       - 33.1762

Number of Rules : 5

Time taken to build model: 0.22 seconds

=== Cross-validation ===
=== Summary ===

Correlation coefficient                  0.4001
Mean absolute error                     14.5561
Root mean squared error                 24.0148
Relative absolute error                133.0901 %
Root relative squared error            195.1034 %
Total Number of Instances              401     

