import os
import xml.etree.ElementTree as ET

import dotenv
import pandas as pd
from glob import glob
from tqdm import tqdm

def save_table(repo_table):
    repo_table.to_csv('repo_table_filtered_cloned.csv', index=False)
    repo_table_html = repo_table.to_html()
    with open('repo_table.html', 'w') as f:
        f.write(repo_table_html)


def log(message, log_file):
    with open(log_file, 'a+') as f:
        f.write(message + '\n')

def get_logger(log_file):
    if os.path.exists(log_file):
        os.remove(log_file)
    def logger(*message):
        log(' '.join([str(m) for m in message]), log_file)
    return logger


if __name__ == "__main__":
    dotenv.load_dotenv()
    log_file_path = os.getenv('LOG_FILE_PATH')
    logger = get_logger(log_file_path)
    df = pd.read_csv('repo_table_filtered_cloned.csv', dtype={'repo_path': str, 'status': str, 'time_taken': int, 'dotnet_versions': str})
    is_dotnet_null = df['dotnet_versions'].isnull()
    is_repo_null = df['repo_path'].isnull()
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        if is_repo_null[idx] or not is_dotnet_null[idx]:
            logger(f'Skipping {row["name"]}!')
            continue
        glob_path = glob(f'{row["repo_path"]}/**/*.csproj', recursive=True)
        versions = {}
        try:
            if len(glob_path) > 0:
                logger(row['name'])
                for csproj_path in glob_path:
                    tree = ET.parse(csproj_path)
                    root = tree.getroot()
                    property_groups = [child for child in root if child.tag.endswith('PropertyGroup')]
                    dotnet_runtime = None
                    dotnet_version = None
                    for property_group in property_groups:
                        for child in property_group:
                            if child.tag.endswith('TargetFramework') or child.tag.endswith('TargetFrameworks'):
                                if child.text is not None:
                                    dotnet_version = child.text
                                    if child.text.startswith('netcoreapp'):
                                        dotnet_runtime = 'core'
                                    elif child.text.startswith('net'):
                                        dotnet_runtime = 'core'
                                    elif child.text.startswith('netstandard'):
                                        dotnet_runtime = 'standard'
                                    else:
                                        dotnet_runtime = 'unknown'
                                    logger(' '*3, '-', child.tag, child.text, dotnet_runtime, dotnet_version)
                                    break
                            elif child.tag.endswith('TargetFrameworkVersion'):
                                if child.text is not None:
                                    dotnet_version = child.text
                                    dotnet_runtime = 'framework'
                                    logger(' '*3, '-', child.tag, child.text, dotnet_runtime, dotnet_version)
                                    break
                    if dotnet_runtime is not None and dotnet_version is not None:
                        version = f'{dotnet_runtime}/{dotnet_version}'
                        if version in versions:
                            versions[version] += 1
                        else:
                            versions[version] = 1
        except Exception as e:
            logger(' '*3, '-', e)
        if versions is not None and len(versions) != 0:
            df.at[idx, 'dotnet_versions'] = ';'.join(versions.keys())
        save_table(df)

    save_table(df)

