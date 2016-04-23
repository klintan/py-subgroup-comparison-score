import pandas as pd
import scipy.stats

class SubgroupEvaluationComparisons():

    """
     This module aims to implement the evaluation comparisons for subgroups in the paper "Subgroup identification for treatment selection in biomarker adaptive design"
     The comparisons compare the different subgroups and treatments. 5 different comparisons are made:
     1. control vs treatment in all patients
        test if treatment is effective in all patients
     2. control vs treatment in subgroup
        test if treatment is effective in subgroup
     3. control vs treatment in parent group
        test if treatment is effective in parent group (this comparison is generally statistically insignificant)
     4. parent vs subgroup in treatment arm
        test if treatment effect differ between subgroup and parent group (may be associated witg a baseline difference in the control arm, comparison 5)
     5. parent vs subgroup in control arm
        commonly used in assesment of prognostic biomarkers


     These are compared using a regular P-value test for significance. Alpha-significance needs to account for multiple testing, but is otherwise considered 0.05. This can be customized.

    Inputs :
    y         = full pandas dataset y values
    subgroup     = split subgroup pandas dataframe
    parentgroup     = split parentgroup pandasdataframe


    Outputs :


    Attributes:
        score: The computed score
    """

    def __init__(self, dataset=None):
        """Initialize evaluation comparisons"""
        self.dataset = dataset

    def compare(self, dataset, subgroup, parentgroup):
        '''
        '''

        # 1. control vs treatment in all patients
        #create a mask for treatment and control in all patients
        trt1_all = dataset['trt'] == 1
        trt0_all = dataset['trt'] == 0
        print "Comparison 1"
        print "Treatment all patients", dataset[trt1_all]['y'].mean()
        print "Control all patients", dataset[trt0_all]['y'].mean()
        zstats, pvalue_one = scipy.stats.ttest_ind(dataset[trt1_all]['y'], dataset[trt0_all]['y'])
        print pvalue_one
        print "\n"

        # 2. control vs treatment in subgroup
        #create a mask for treatment and control in subgroup
        trt1_subgroup = subgroup['trt'] == 1
        trt0_subgroup = subgroup['trt'] == 0
        print "Comparison 2"
        print "Treatment subgroup", subgroup[trt1_subgroup]['y'].mean()
        print "Control subgroup", subgroup[trt0_subgroup]['y'].mean()
        zstats, pvalue_two = scipy.stats.ttest_ind(subgroup[trt1_subgroup]['y'], subgroup[trt0_subgroup]['y'])
        print pvalue_two
        print "\n"

        # 3. control vs treatment in parentgroup
        #create a mask for treatment and control in parent group
        trt1_parent = parentgroup['trt'] == 1
        trt0_parent= parentgroup['trt'] == 0
        print "Comparison 3"
        print "Treatment parent", parentgroup[trt1_parent]['y'].mean()
        print "Control parent", parentgroup[trt0_parent]['y'].mean()
        zstats, pvalue_three = scipy.stats.ttest_ind(parentgroup[trt1_parent]['y'], parentgroup[trt0_parent]['y'])
        print pvalue_three
        print "\n"

        # 4. parent vs subgroup in treatment arm
        print "Comparison 4"
        print "Treatment subgroup", subgroup[trt1_subgroup]['y'].mean()
        print "Treatment parent", parentgroup[trt1_parent]['y'].mean()
        zstats, pvalue_four = scipy.stats.ttest_ind(subgroup[trt1_subgroup]['y'], parentgroup[trt1_parent]['y'])
        print pvalue_four
        print "\n"

        # 5. parent vs subgroup in control arm
        print "Comparison 5"
        print "Control subgroup", subgroup[trt0_subgroup]['y'].mean()
        print "Control parent", parentgroup[trt0_parent]['y'].mean()
        zstats, pvalue_five = scipy.stats.ttest_ind(subgroup[trt0_subgroup]['y'], parentgroup[trt0_parent]['y'])
        print pvalue_five
        return pvalue_one, pvalue_two, pvalue_three, pvalue_four, pvalue_five

