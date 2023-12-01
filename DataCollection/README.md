# Data Collection

This README provides detailed descriptions of each file in the `DataCollection` folder of our software project repository. This folder includes scripts for data retrieval, analysis notebooks, and the resulting data tables.

## Files in this Folder

### `search_repositories.py`

- **Description**: Python script for searching and filtering GitHub repositories based on specific criteria. The exact criteria are specified in the report.
- **Dependencies**: Requires Python's `requests` module and GitHub API tokens. Github API token should be specified in the `.env` file inside the folder with the key `GH_ACCESS_TOKEN`.
- **Usage**: Used to create a list of repositories that meet the study's criteria. Outputs `repo_table.csv`.

### `clone_repositories.py`

- **Description**: A Python script for cloning and filtering repositories from GitHub. The script uses bash to call `git clone` with several optimizations to clone only the code itself on the last commit inside the default branch. The cloning process has a timeout of 800 seconds, so that repositories with a lot of large blobs are skipped. Additionally, `repo_table_filtered.csv` is updated after each successful or unsuccessful cloning, which allows the script to continue from the last point after unexpected interuption, without the need to start from the scratch. Notably, this is one of the longest steps in the project, requiering almost 12 hours to complete.
- **Dependencies**: Requires Git.
- **Usage**: Used to clone the repositories listed in `repo_table.csv`. Modify the script to specify the destination folder for cloned repositories. The destintaion folder should be specified in the `.env` file inside the folder with the key `REPO_DIR`. Outputs `repo_table_filtered.csv`.

### `verify_dotnet_version.py`

- **Description**: A Python script to check the .NET version used in the repositories. It does so by finding all .csproj C# project definition files, parsing them and aggregating the results across the whole repository (as there can be multiple .csproj files inside one repostory). After the results are aquired, they are saved in the `repo_table_filtered_cloned.csv`, which is a copy of previous table, but with a new column `dotnet_versions`. Again, this table is save sequentially, after each step, so the script has the ability to continue from the last point after interuption. It also logs the process in the log file, specified by `LOG_FILE_PATH` env variable.
- **Dependencies**: Requires Python and access to the cloned repositories.
- **Usage**: Run this script to ensure that the repositories are compatible with the .NET version used in this study. The log file path should be specified in the `.env` file inside the folder with the key `LOG_FILE_PATH`. Outputs `repo_table_filtered_cloned.csv`.

Continuing from your examples, here are the detailed descriptions for the remaining files in the `DataCollection` folder:

### `collect_metrics.ipynb`

- **Description**: This script is responsible for extracting various metrics from the cloned repositories using SourceMeter. It analyzes each repository and extracts metrics like code churn, complexity, and lines of code, among others. The extracted metrics are categorized into two CSV files: one for class-level metrics and another for method-level metrics. The process is logged, and the script has the capability to resume from the last processed repository in case of an interruption. It analyses each repository cloned by `clone_repositories.py` and tries to collect metrics from it using SourceMeter. If it is unsuccessful or a timeout is reached, it skips this repository.
- **Dependencies**: Requires SourceMeter installed and as many different version of [.NET SDKs](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks) as possible, including out of support versions. The more different versions are installed, the higher will be the success rate, because SourceMeter tool needs to build a C# solution before it can analyze it, so you would need an appropriate version of .NET SDK, corresponding to the repository you are analyzing, however, as we need to analyze a lot of different repositories, it is helpful to install all .NET SDK versions simultaniously before starting this file. Note, that there are a lot of repositories in github, that uses .NET Framework versions, so make sure to install them too, however, this means, that the process of metric collection should be performed on Windows PC, as .NET Framework supports only Windows OS. Also, the SourceMeter itself requires .NET Core 3.1.
- **Usage**: Run this script to generate metrics data from each repository. The output CSV files are saved in the `CollectedMetrics` folder. Ensure that the cloned repositories are available and specify the path to `AnalyzerCSharp.exe` inside the installed SourceMeter folder in the `.env` file with the key `SOURCE_METER_PATH` (i.e. `"D:\\SourceMeter-10.2.0-x64-Windows\\CSharp\\AnalyzerCSharp.exe"`).

### `analyse_metrics.ipynb`

- **Description**: A Jupyter notebook used for the initial analysis of the collected metrics. It includes various data visualization and statistical analysis methods to understand the underlying patterns and trends in the data, such as correlation analysis.
- **Dependencies**: Requires Jupyter Notebook and Python libraries such as Pandas, Numpy, Matplotlib and Seaborn.
- **Usage**: Open this notebook in a Jupyter environment to perform the analysis. The notebook assumes that the metrics CSV files are available in the specified directory.

### `final_metrics_table.csv`

- **Description**: A CSV file containing the final set of metrics, it abbreviations, full names and descriptions, which were parsed from the documents.
- **Usage**: This file is used for selecting a relevant subset of metrics as well as mapping the abbreviations, which are used as column names in `CollectedMetrics` files, to their full names and descriptions.

### `repo_table.csv`

- **Description**: CSV file containing a list of GitHub repositories initially identified for the study. This table includes repository names, URLs, and other relevant metadata.
- **Usage**: Serves as the base data for repository selection and cloning processes. It is the starting point for the data collection phase. Used as an input for the `clone_repositories.py` script. It contains the repositories that meet the specific criteria for cloning.

### `repo_table_filtered.csv`

- **Description**: CSV file containing a filtered list of repositories based on defined criteria from the initial list. This table is an outcome of the cloning and filtering process applied to the `repo_table.csv`.
- **Usage**: Used as an input for the `verify_dotnet_version.py`.

### `repo_table_filtered_cloned.csv`

- **Description**: An updated version of `repo_table_filtered.csv`, this CSV file lists the repositories that have been successfully cloned and verified for .NET version compatibility. Each entry includes the repository details and the result of the cloning and .NET version verification process.
- **Usage**: Acts as a record of the cloning process and is used in `collect_metrics.ipynb`.

## General Usage Notes

- Ensure all dependencies are installed before running any scripts, especially .NET SDK versions, as they are needed for SourceMeter tool to work properly.
- Scripts should be run in the order they are listed for a smooth data collection process.
- Adjust the scripts if necessary to fit your specific environment or requirements.