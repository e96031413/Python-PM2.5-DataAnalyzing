=== Run information ===

Scheme:       weka.classifiers.functions.SMOreg -C 1.0 -N 0 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.001 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007"
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

SMOreg

weights (not support vectors):
 (-       0.0614 * (normalized) SO2
 (-       0.0502 * (normalized) CO
 (+       0.2653 * (normalized) O3
 (+       0.1826 * (normalized) Nox
 (-       0.2204 * (normalized) NO
 (+       0.3368 * (normalized) NO2
 (+       0.0981 * (normalized) THC
 (+       0.2463 * (normalized) NMHC
 (+       0.1666 * (normalized) CH4
 (+       0.1282 * (normalized) WindSpeed
 (-       0.3701 * (normalized) TEMP
 (-       0.0989 * (normalized) Humidity
 (+       0.2352



Number of kernel evaluations: 80601 (93.956% cached)

Time taken to build model: 0.05 seconds

=== Cross-validation ===
=== Summary ===

Correlation coefficient                  0.9491
Mean absolute error                      2.9616
Root mean squared error                  3.868 
Relative absolute error                 27.0784 %
Root relative squared error             31.4247 %
Total Number of Instances              401     

