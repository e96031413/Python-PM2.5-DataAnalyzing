=== Run information ===

Scheme:       weka.classifiers.functions.SMOreg -C 1.0 -N 0 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.001 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007"
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

SMOreg

weights (not support vectors):
 +       0.0924 * (normalized) SO2
 +       0.218  * (normalized) CO
 -       0.025  * (normalized) CO2
 +       0.2525 * (normalized) O3
 -       0.0751 * (normalized) Nox
 -       0.0408 * (normalized) NO
 -       0.1004 * (normalized) NO2
 +       0.0592 * (normalized) THC
 +       0.3898 * (normalized) NMHC
 -       0.1403 * (normalized) CH4
 -       0.148  * (normalized) WindSpeed
 -       0.215  * (normalized) TEMP
 -       0.1073 * (normalized) Humidity
 +       0.3865



Number of kernel evaluations: 3240 (95.964% cached)

Time taken to build model: 0.03 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.8566
Mean absolute error                      2.0882
Root mean squared error                  3.2051
Relative absolute error                 42.1868 %
Root relative squared error             51.7484 %
Total Number of Instances               80     

