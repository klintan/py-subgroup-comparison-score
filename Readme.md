# Subgroup evaluation comparisons
This module aims to implement the evaluation comparisons for subgroups in the paper "Subgroup identification for treatment selection in biomarker adaptive design".
The comparisons compare the different subgroups and treatments. 5 different comparisons are made:
     1. control vs treatment in all patients
     2. control vs treatment in subgroup
     3. control vs treatment in parent group
     4. parent vs subgroup in treatment arm
     5. parent vs subgroup in control arm

These are compared using a regular P-value test for significance. Alpha-significance needs to account for multiple testing, but is otherwise considered 0.05. This can be customized.

Inputs :
    y         = full pandas dataset y values
    subgroup     = split subgroup pandas dataframe
    parentgroup     = split parentgroup pandasdataframe


Outputs :


Attributes:
    score: The computed score


For any improvements of this module feel free to do a pull request.