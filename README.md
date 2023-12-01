# EM.Project.Team9

## Project Overview
This repository hosts the resources and results of a project for Emperical Methods Course by Team 9, aimed at identifying a minimal subset of metrics that explain the “structure” of a software repository. The study involves collecting metrics from various repositories, conducting data analysis, applying dimensionality reduction techniques, and performing hypothesis tests to validate the results.

## Repository Structure

### CollectedMetrics
Contains CSV files for each of 118 software repositories, with metrics data at class and method levels. Metrics include 40 class-level and 14 method-level metrics. For more details, see the `CollectedMetrics` [README](./CollectedMetrics/README.md).

### DataCollection
Includes scripts for data retrieval and analysis notebooks, along with the resulting data tables. Scripts include repository searching and cloning, .NET version verification, and metrics collection. For more information, refer to the `DataCollection` [README](./DataCollection/README.md).

### MainTask
Contains the core scripts and results of the study, focusing on the application of dimensionality reduction techniques to the collected metrics. Files include Jupyter notebooks, utility scripts, and CSV files with the results. Detailed explanations are available in the `MainTask` [README](./MainTask/README.md).

### HypothesisTests
Hosts the results of various hypothesis tests conducted on the collected metrics at both class and method levels. It includes CSV files with the test results and a Jupyter notebook for conducting the tests. For a detailed description, see the `HypothesisTests` [README](./HypothesisTests/README.md).

## Replicating the Study's Results

1. **Set up the Environment**: 
   - Install Python and necessary libraries as mentioned in the dependencies of each script.
   - Install Jupyter Notebook for running the `.ipynb` files.
   - Ensure that the appropriate .NET SDK versions are installed for SourceMeter tool compatibility (more details are provided in `DataCollection` [README](./DataCollection/README.md)).
   - Download and install SourceMeter.

2. **Data Collection**:
   - Ensure that the `.env` file is configured correctly for each script.
   - Run the scripts in the `DataCollection` folder in the following order: `search_repositories.py`, `clone_repositories.py`, `verify_dotnet_version.py`, `collect_metrics.ipynb`, and `analyse_metrics.ipynb`.

3. **Main Task**:
   - Execute `main_task.ipynb` in the `MainTask` folder for dimensionality reduction analysis.

4. **Hypothesis Testing**:
   - Open and run `hypothesis_tests.ipynb` in the `HypothesisTests` folder to replicate the hypothesis tests.

5. **Review Results**:
   - Examine the CSV files in `MainTask` and `HypothesisTests` as well as `main_task.ipynb` and `hypothesis_tests.ipynb` notebooks for analysis results and hypothesis test outcomes.
   - Refer to the project report, `EM_2023_Project_Team09.pdf`, for detailed methodologies, explanations, and interpretations of the results.

## Additional Notes
- Ensure all dependencies are installed and accessible before running any scripts or notebooks.
- Read the descriptions in each folder's README for specific details on files and their usage.
- The process may require significant computational resources, especially for scripts in the `MainTask` folder.