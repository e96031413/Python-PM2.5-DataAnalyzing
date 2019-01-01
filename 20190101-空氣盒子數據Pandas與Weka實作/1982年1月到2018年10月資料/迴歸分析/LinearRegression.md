=== Run information ===

Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4
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


Linear Regression Model

PM25 =

      1.7094 * SO2 +
     13.399  * CO +
      0.3164 * O3 +
     -0.4121 * NO +
     68.7883 * NMHC +
     -0.2826 * TEMP +
     -0.2461 * Humidity +
     14.3279

Time taken to build model: 0 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.8626
Mean absolute error                      2.3243
Root mean squared error                  3.1333
Relative absolute error                 46.9556 %
Root relative squared error             50.589  %
Total Number of Instances               80     

