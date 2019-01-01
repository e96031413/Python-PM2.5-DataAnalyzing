=== Run information ===

Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4
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


Linear Regression Model

PM25 =

     -0.559  * SO2 +
     -7.6585 * CO +
      0.2562 * O3 +
     -0.7258 * NO +
      0.8893 * NO2 +
     32.5635 * NMHC +
     16.7113 * CH4 +
      2.0159 * WindSpeed +
     -1.2569 * TEMP +
     -0.1646 * Humidity +
     14.5208

Time taken to build model: 0 seconds

=== Cross-validation ===
=== Summary ===

Correlation coefficient                  0.9487
Mean absolute error                      2.9764
Root mean squared error                  3.8746
Relative absolute error                 27.214  %
Root relative squared error             31.478  %
Total Number of Instances              401     

