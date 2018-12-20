=== Run information ===

Scheme:       weka.classifiers.functions.SMOreg -C 1.0 -N 0 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.001 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007"
Relation:     PM25¸ê®Æ-weka.filters.AllFilter-weka.filters.unsupervised.attribute.Remove-R4-weka.filters.AllFilter-weka.filters.AllFilter-weka.filters.AllFilter-weka.filters.AllFilter-weka.filters.AllFilter
Instances:    12
Attributes:   15
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
              WIND_SPEED
              TEMP
              RAIN
              PH_RAIN
              Humidity
Test mode:    evaluate on training data

=== Classifier model (full training set) ===

SMOreg

weights (not support vectors):
 -       0.042  * (normalized) SO2
 +       0.2576 * (normalized) CO
 +       0.0391 * (normalized) O3
 +       0.1815 * (normalized) Nox
 -       0.046  * (normalized) NO
 +       0.1968 * (normalized) NO2
 +       0.0894 * (normalized) THC
 +       0.1215 * (normalized) NMHC
 +       0.0526 * (normalized) CH4
 -       0.0972 * (normalized) WIND_SPEED
 +       0.0247 * (normalized) TEMP
 -       0.1791 * (normalized) RAIN
 +       0.0397 * (normalized) PH_RAIN
 -       0.0513 * (normalized) Humidity
 +       0.2135



Number of kernel evaluations: 78 (99.072% cached)

Time taken to build model: 0.01 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.9987
Mean absolute error                      0.3024
Root mean squared error                  0.7372
Relative absolute error                  2.8058 %
Root relative squared error              6.1241 %
Total Number of Instances               12     

