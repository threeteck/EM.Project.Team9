# Hypothesis Tests

This README provides detailed descriptions of each file in the `HypothesisTests` folder of our software project repository. This folder contains the results of various hypothesis tests conducted on the collected metrics, focusing on class and method level metrics.

## Files in this Folder

### `class_level_hyp1_results.csv`

- **Description**: This CSV file contains the results of the first hypothesis test conducted at the class level. The first hypothesis tests whether the distributions of error functions for class and method level metrics are similar when optimized using Particle Swarm Optimization (PSO) and Genetic Algorithm (GA), by employing the Mann-Whitney U test to compare the distributions of Sammon’s error and Kruskal’s stress at
each k value for both class and method level metric. Details of the hypothesis, including its formulation and statistical methods used, are explained in the project report.
- **Usage**: Review this file to understand the outcomes of the class-level hypothesis test, including statistical significance.

### `class_level_validation_results.csv`

- **Description**: This file presents the results of the second hypothesis test, which was aimed at testing, wheter the found optimal subset of metrics on train set is as efficient on validation set. It includes details such as p-values and means of errors for each algorithm on validation set using class-level metrics.
- **Usage**: Use this file to assess the validity of the class-level metrics used in the study.

### `hypothesis_tests.ipynb`

- **Description**: A Jupyter notebook containing the code used for running the hypothesis tests on both class and method level metrics.
- **Dependencies**: Requires Jupyter Notebook and Python libraries such as Pandas, numpy and SciPy.
- **Usage**: Run this notebook to replicate the hypothesis testing process or to modify the tests for further analysis.

### `method_level_hyp1_results.csv`

- **Description**: Similar to `class_level_hyp1_results.csv`, but focuses on the method-level metrics. This CSV file contains the results of the first hypothesis test conducted at the method level.
- **Usage**: Review to understand the outcomes of the method-level hypothesis test.

### `method_level_validation_results.csv`

- **Description**: This file contains the results of second hypothesis test for method-level metrics.
- **Usage**: Use to assess the validity of the method-level metrics.

## General Usage Notes

- The Jupyter notebook (`hypothesis_tests.ipynb`) can be modified and rerun to test different hypotheses or to apply different statistical methods.
- Ensure that the necessary Python libraries are installed before running the notebook.
- The results in the CSV files should be cross-referenced with the project report for comprehensive understanding and context.