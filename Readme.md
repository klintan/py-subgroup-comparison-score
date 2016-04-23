# Subgroup evaluation comparisons
This module aims to implement the evaluation comparisons for subgroups in the paper "Subgroup identification for treatment selection in biomarker adaptive design".
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


For any improvements of this module feel free to do a pull request.