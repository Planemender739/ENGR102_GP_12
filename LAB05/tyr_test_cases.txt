# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Lane Mack, Thomas Tang, Ashrith Talluri
# Section: Engr 102-511
# Assignment: Lab Topic 5 Team
# Date: 22 September 2025
#
#tyr_test_cases.txt


##### FAIL CASES #####

#sex:male age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:
#sex:female age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:


#AGE EDGE CASES
#sex:M age:19 cho:150 smo:N hdl:60 sbp:100 med:N out:
#sex:M age:80 cho:105 smo:N hdl:60 sbp:100 med:N out:
sex:M age:20 cho:150 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:79 cho:105 smo:N hdl:60 sbp:100 med:N out:10
#sex:M age:0 cho:105 smo:N hdl:60 sbp:100 med:N out:
#sex:M age:-40 cho:105 smo:N hdl:60 sbp:100 med:N out:

#CHOLESTEROL EDGE CASES
#sex:M age:21 cho:-10 smo:N hdl:60 sbp:100 med:N out:
sex:M age:21 cho:160 smo:N hdl:60 sbp:100 med:N out:<1
#sex:M age:21 cho:0 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:21 cho:280 smo:N hdl:60 sbp:100 med:N out:1

#SMOKER EDGE CASES
#sex:M age:21 cho:105 smo:no hdl:60 sbp:100 med:N out:
#sex:M age:21 cho:105 smo:yes hdl:60 sbp:100 med:N out:

#HDL EDGE CASES
#sex:M age:21 cho:105 smo:N hdl:-10 sbp:100 med:N out:
sex:M age:21 cho:105 smo:N hdl:40 sbp:100 med:N out:<1
sex:M age:21 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:21 cho:105 smo:N hdl:70 sbp:100 med:N out:<1

#SBP EDGE CASES
#sex:M age:21 cho:105 smo:N hdl:60 sbp:-10 med:N out:

#MEDICATION EDGE CASES
#sex:M age:21 cho:105 smo:N hdl:60 sbp:100 med:no out:
#sex:M age:21 cho:105 smo:N hdl:60 sbp:100 med:yes out:
#### END FAIL CASES ####



#### SEX TESTING ####
sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1


#### AGE TESTING ####
sex:M age:21 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:36 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:46 cho:105 smo:N hdl:60 sbp:100 med:N out:1
sex:M age:51 cho:105 smo:N hdl:60 sbp:100 med:N out:2
sex:M age:56 cho:105 smo:N hdl:60 sbp:100 med:N out:3
sex:M age:61 cho:105 smo:N hdl:60 sbp:100 med:N out:5
sex:M age:66 cho:105 smo:N hdl:60 sbp:100 med:N out:6
sex:M age:71 cho:105 smo:N hdl:60 sbp:100 med:N out:8
sex:M age:77 cho:105 smo:N hdl:60 sbp:100 med:N out:10





#Random leftover cases from looking at stuff that could be missing. Possible overlap with previous tests

sex:M age:41 cho:250 smo:N hdl:65 sbp:111 med:N out:2
sex:M age:46 cho:290 smo:N hdl:65 sbp:111 med:N out:6
sex:M age:51 cho:150 smo:N hdl:65 sbp:110 med:N out:2
sex:M age:51 cho:170 smo:N hdl:65 sbp:110 med:N out:3
sex:M age:51 cho:210 smo:N hdl:65 sbp:110 med:N out:4
sex:M age:51 cho:250 smo:N hdl:65 sbp:110 med:N out:5
sex:M age:56 cho:290 smo:Y hdl:65 sbp:110 med:N out:20
sex:M age:61 cho:150 smo:N hdl:65 sbp:110 med:N out:5
sex:M age:61 cho:170 smo:N hdl:65 sbp:110 med:N out:6
sex:M age:61 cho:210 smo:N hdl:65 sbp:110 med:N out:6
sex:M age:61 cho:250 smo:N hdl:65 sbp:110 med:N out:8
sex:F age:21 cho:290 smo:N hdl:30 sbp:180 med:Y out:2
sex:F age:38 cho:260 smo:N hdl:43 sbp:145 med:N out:1
sex:F age:41 cho:150 smo:N hdl:65 sbp:110 med:N out:<1
sex:F age:41 cho:170 smo:N hdl:65 sbp:110 med:N out:<1
sex:F age:41 cho:210 smo:N hdl:65 sbp:111 med:N out:<1
sex:F age:41 cho:250 smo:N hdl:65 sbp:111 med:N out:<1
sex:F age:46 cho:290 smo:Y hdl:65 sbp:111 med:N out:8
sex:F age:51 cho:150 smo:N hdl:65 sbp:110 med:N out:<1
sex:F age:51 cho:170 smo:N hdl:65 sbp:110 med:N out:<1




sex:M age:66 cho:290 smo:Y hdl:65 sbp:110 med:N out:16
sex:M age:71 cho:150 smo:N hdl:65 sbp:110 med:N out:8
sex:M age:71 cho:170 smo:N hdl:65 sbp:110 med:N out:8
sex:M age:71 cho:210 smo:N hdl:65 sbp:110 med:N out:8
sex:M age:71 cho:250 smo:N hdl:65 sbp:110 med:N out:10
sex:M age:76 cho:290 smo:Y hdl:65 sbp:110 med:N out:16
sex:M age:61 cho:150 smo:Y hdl:35 sbp:110 med:N out:12
sex:M age:76 cho:290 smo:Y hdl:41 sbp:110 med:N out:25
sex:M age:76 cho:290 smo:Y hdl:10 sbp:170 med:Y out:>30
sex:F age:21 cho:150 smo:Y hdl:65 sbp:110 med:Y out:<1
sex:F age:21 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:36 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:46 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:51 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:56 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:61 cho:105 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:66 cho:105 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:71 cho:105 smo:N hdl:60 sbp:100 med:N out:2
sex:F age:77 cho:105 smo:N hdl:60 sbp:100 med:N out:3


sex:M age:21 cho:150 smo:Y hdl:65 sbp:110 med:Y out:<1
sex:M age:21 cho:150 smo:Y hdl:65 sbp:110 med:N out:<1
sex:M age:21 cho:170 smo:N hdl:65 sbp:121 med:N out:<1
sex:M age:21 cho:170 smo:N hdl:65 sbp:121 med:Y out:<1
sex:M age:21 cho:210 smo:N hdl:65 sbp:131 med:N out:<1
sex:M age:21 cho:210 smo:N hdl:65 sbp:131 med:Y out:<1
sex:M age:21 cho:250 smo:N hdl:65 sbp:141 med:N out:1
sex:M age:21 cho:250 smo:N hdl:65 sbp:141 med:Y out:1
sex:M age:21 cho:290 smo:N hdl:30 sbp:180 med:N out:2
sex:M age:21 cho:290 smo:N hdl:30 sbp:180 med:Y out:3
sex:M age:38 cho:260 smo:N hdl:43 sbp:145 med:N out:3


sex:F age:21 cho:150 smo:Y hdl:65 sbp:110 med:N out:<1
sex:F age:21 cho:170 smo:N hdl:65 sbp:121 med:N out:<1
sex:F age:21 cho:170 smo:N hdl:65 sbp:121 med:Y out:<1
sex:F age:21 cho:210 smo:N hdl:65 sbp:131 med:N out:<1
sex:F age:21 cho:210 smo:N hdl:65 sbp:131 med:Y out:<1
sex:F age:21 cho:250 smo:N hdl:65 sbp:141 med:N out:<1
sex:F age:21 cho:250 smo:N hdl:65 sbp:141 med:Y out:<1
sex:F age:21 cho:290 smo:N hdl:30 sbp:180 med:N out:1

sex:M age:41 cho:150 smo:Y hdl:65 sbp:110 med:N out:1
sex:M age:41 cho:170 smo:N hdl:65 sbp:110 med:N out:1

sex:F age:51 cho:210 smo:N hdl:65 sbp:110 med:N out:1
sex:F age:51 cho:250 smo:N hdl:65 sbp:110 med:N out:1
sex:F age:56 cho:290 smo:Y hdl:65 sbp:110 med:N out:6
sex:F age:61 cho:150 smo:N hdl:65 sbp:110 med:N out:1
sex:F age:61 cho:170 smo:N hdl:65 sbp:110 med:N out:1
sex:F age:61 cho:210 smo:N hdl:65 sbp:110 med:N out:1
sex:F age:61 cho:250 smo:N hdl:65 sbp:110 med:N out:1
sex:F age:66 cho:290 smo:Y hdl:65 sbp:115 med:N out:5
sex:F age:71 cho:150 smo:N hdl:65 sbp:115 med:N out:2
sex:F age:71 cho:170 smo:N hdl:65 sbp:115 med:N out:2
sex:F age:71 cho:210 smo:N hdl:65 sbp:115 med:N out:2
sex:F age:71 cho:250 smo:N hdl:65 sbp:110 med:N out:3
sex:F age:76 cho:290 smo:Y hdl:65 sbp:110 med:N out:6

sex:M age:41 cho:210 smo:N hdl:65 sbp:111 med:N out:1
sex:F age:76 cho:100 smo:N hdl:55 sbp:110 med:N out:4
sex:F age:76 cho:290 smo:Y hdl:45 sbp:110 med:N out:11
sex:F age:76 cho:290 smo:Y hdl:35 sbp:110 med:N out:14
sex:F age:76 cho:290 smo:Y hdl:35 sbp:121 med:N out:17
sex:F age:76 cho:290 smo:Y hdl:35 sbp:131 med:N out:22
sex:F age:76 cho:290 smo:Y hdl:35 sbp:141 med:N out:27
sex:F age:76 cho:290 smo:Y hdl:10 sbp:170 med:Y out:>30