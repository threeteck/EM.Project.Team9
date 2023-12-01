# Main Task

This README provides detailed descriptions of each file in the `MainTask` folder of our software project repository. This folder contains the core scripts and results of our study, focusing on identifying a minimal subset of metrics that explain the “structure” of a software repository.

## Files in this Folder

### `main_task.ipynb`

- **Description**: A Jupyter notebook that applies dimensionality reduction techniques to the collected metrics. The algorithms applied are PSO and GA, and cost function being optimized are Sammon's error function and Kruskal's stress function. More details about exact formulas, algorithms and etc. can be found in the report. Each algorithm is highly optimized and uses parallization on 8 cores for maximum performance.
This notebook also contains a detailed analysis of the results, constructing different plots and tables. The notebook is highly documented, so make sure to look into it.
- **Dependencies**: Requires Jupyter Notebook and Python libraries such as Pandas, Numpy, Scikit-learn.
- **Usage**: Run this notebook to perform dimensionality reduction on the collected metrics. Note, that execution may require a lot of time depending on the machine resources.

### `main_task_utils.py`

- **Description**: A Python utility file containing functions and classes used across inside `main_task.ipynb`. Mainly needed for parallization.
- **Dependencies**: Requires Python and any specific libraries used within the functions (e.g., Pandas, Numpy).
- **Usage**: Should not be used directly, only needed for `main_task.ipynb`.

### `class_metrics_results.csv`

- **Description**: This CSV file contains the results of the optimization of error functions using two different algorithms for each repository and for each number of metrics in the minimal subset $k$. It also contains the array of numbers of the optimal subset. These number, ranging from 0 to 1, represent the rank of a metric. To get the best subset of metrics for a given repository, $k$, error function being optimized and optimization algorithm, you need to get the indicies of top-k values from this array and select the corresponding metrics from `final_metrics_table.csv` at the same indicies after filtering for `Category == 'Class'`.
- **Usage**: Used for reviewing and further analysis of the results of finding the minimal subset of class-level metrics.

### `method_metrics_results.csv`

- **Description**: Similar to `class_metrics_results.csv`, this CSV file presents the results of the optimization procedures, but for method-level metrics.
- **Usage**: Used for reviewing and further analysis of the results of finding the minimal subset of class-level metrics.

### `final_metrics_table.csv`

- **Description**: A CSV file containing the final set of metrics, it abbreviations, full names and descriptions, which were parsed from the documents.
- **Usage**: Acts as a reference for interpreting results in both `class_metrics_results.csv` and `method_metrics_results.csv`. Essential for any user attempting to understand or replicate the study's findings.

## General Usage Notes

- Ensure that all dependencies are installed and accessible before running any scripts or notebooks.
- Familiarize yourself with the `final_metrics_table.csv` for understanding the metrics analyzed in this study.
- The `main_task_utils.py` should be kept in the same directory and `__init__.py` file should be created.