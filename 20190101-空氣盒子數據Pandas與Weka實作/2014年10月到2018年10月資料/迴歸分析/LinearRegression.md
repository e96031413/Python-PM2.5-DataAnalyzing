=== Run information ===

Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4
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


Linear Regression Model

PM25 =

      1.7013 * SO2 +
     23.3474 * CO +
      0.33   * O3 +
     -0.4431 * NO +
     58.9062 * NMHC +
    -10.8507 * CH4 +
     -0.2763 * TEMP +
     -0.2159 * Humidity +
     28.5669

Time taken to build model: 0.02 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.8662
Mean absolute error                      2.2954
Root mean squared error                  3.095 
Relative absolute error                 46.3717 %
Root relative squared error             49.9717 %
Total Number of Instances               80     

