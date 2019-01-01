=== Run information ===

Scheme:       weka.classifiers.functions.SMOreg -C 1.0 -N 0 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.001 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007"
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

SMOreg

weights (not support vectors):
 0.1053 * (normalized) SO2 + 0.1935 * (normalized) CO -0.0262 * (normalized) CO2 + 0.1893 * (normalized) O3 -  0.0549 * (normalized) Nox - 0.1136 * (normalized) NO - 0.0147 * (normalized) NO2 +0.0531 * (normalized) THC + 0.4411 * (normalized) NMHC -0.1154 * (normalized) CH4 -0.0531 * (normalized) WindSpeed - 0.2153 * (normalized) TEMP - 0.1232 * (normalized) Humidity + 0.3323



Number of kernel evaluations: 3240 (96.939% cached)

Time taken to build model: 0.02 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.8564
Mean absolute error                      2.1585
Root mean squared error                  3.206 
Relative absolute error                 43.6062 %
Root relative squared error             51.7629 %
Total Number of Instances               80     

