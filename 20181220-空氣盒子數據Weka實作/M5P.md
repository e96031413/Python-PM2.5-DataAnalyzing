=== Run information ===

Scheme:       weka.classifiers.trees.M5P -M 4.0
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

M5 pruned model tree:
(using smoothed linear models)
LM1 (12/9.61%)

LM num: 1
PM25 = 
	40.5403 * CO 
	+ 1.2594 * NO2 
	- 16.9834

Number of Rules : 1

Time taken to build model: 0.01 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.9954
Mean absolute error                      0.9368
Root mean squared error                  1.1568
Relative absolute error                  8.692  %
Root relative squared error              9.6101 %
Total Number of Instances               12     

