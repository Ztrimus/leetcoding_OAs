'''
-----------------------------------------------------------------------
File: q2_medial_analysis.py
Creation Time: Nov 7th 2023 3:30 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''

import pandas as pd
from scipy import stats


def perform_tests(data):
    # Initialize dictionaries to store results for different tests
    mann_whitney_results = {}
    ttest_results = {}
    chi_square_results = {}
    shapiro_wilk_results = {}

    # Extract the 'death' column as a categorical variable
    death = data['death']

    # Iterate through all columns in the DataFrame
    for column in data.columns:
        if column != 'death':
            variable = data[column]
            if variable.dtype == 'int64':
                # Categorical variable, perform Chi-squared test
                contingency_table = pd.crosstab(death, variable)
                chi2, p, _, _ = stats.chi2_contingency(contingency_table)
                chi_square_results[column] = round(p, 4)
            else:
                # Numerical variable, perform Shapiro-Wilk test for both death categories
                death_0 = variable[death == 0]
                death_1 = variable[death == 1]
                p_0 = stats.shapiro(death_0)[1]
                p_1 = stats.shapiro(death_1)[1]
                shapiro_wilk_results[column] = (round(p_0, 4), round(p_1, 4))

                if p_0 > 0.05 and p_1 > 0.05:
                    # If both samples have a normal distribution, perform unpaired t-test
                    t_stat, p_ttest = stats.ttest_ind(death_0, death_1, equal_var=False)
                    ttest_results[column] = round(p_ttest, 4)
                else:
                    # Otherwise, perform Mann-Whitney U test
                    u_stat, p_mann_whitney = stats.mannwhitneyu(death_0, death_1)
                    mann_whitney_results[column] = round(p_mann_whitney, 4)

    # Create the final dictionary with results
    result_dict = {
        'mann_whitney': [(var, p) for var, p in mann_whitney_results.items()],
        'ttest': [(var, p) for var, p in ttest_results.items()],
        'chi_square': [(var, p) for var, p in chi_square_results.items()],
        'shapiro_wilk': [(var, p_values) for var, p_values in shapiro_wilk_results.items()]
    }

    return result_dict
