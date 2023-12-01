import errno
import os
import stat
import time

from dotenv import load_dotenv
import shutil

import pandas as pd
from tqdm import tqdm

def save_table(repo_table):
    repo_table.to_csv('repo_table_filtered.csv', index=False)
    repo_table_html = repo_table.to_html()
    with open('repo_table.html', 'w') as f:
        f.write(repo_table_html)


if __name__ == '__main__':
    load_dotenv()
    repo_table = pd.read_csv('repo_table_filtered.csv', dtype={'repo_path': str, 'status': str, 'time_taken': int})
    root_dir = os.path.join(os.getcwd(), f'{os.getenv("REPO_DIR")}')

    # filter repos
    repo_table = repo_table[repo_table['csharp_percent'] > 0.6]
    repo_table = repo_table[repo_table['commit_count'] > 10]
    repo_table = repo_table.drop_duplicates(subset=['name'])

    # sort by size
    repo_table = repo_table.sort_values(by=['size'], ascending=False)

    if 'repo_path' not in repo_table.columns:
        repo_table['repo_path'] = None
    if 'status' not in repo_table.columns:
        repo_table['status'] = None
    if 'time_taken' not in repo_table.columns:
        repo_table['time_taken'] = 0

    is_null = repo_table['repo_path'].isnull()

    save_table(repo_table)

    # set timeout
    os.system('git config --global http.lowSpeedLimit 1000000000')
    os.system('git config --global http.lowSpeedTime 800')

    # clone repos
    for idx, repo in tqdm(repo_table.iterrows(), total=len(repo_table)):
        if not is_null[idx]:
            print(f'Skipping {repo["name"]}!')
            continue

        full_name = repo['name'].replace('/', '_')
        repo_path = os.path.join(root_dir, full_name)

        if os.path.exists(repo_path):
            os.system(f'rm -rf {repo_path}')

        start = time.time()
        try:
            if not os.path.exists(repo_path):
                os.makedirs(repo_path)
            status = os.system(f'git clone --depth 1 --single-branch --branch {repo["default_branch"]} {repo["html_url"]} {repo_path}')
            if status != 0:
                raise Exception(f'Failed to clone {repo["name"]}!')
            repo_table.at[idx, 'repo_path'] = repo_path
            print(f'Cloned {repo["name"]} to {repo_path}!')

            status = os.system(f'rm -rf {repo_path}/.git')
            if status != 0:
                print(f'Failed to remove .git folder from {repo_path}!')
                repo_table.at[idx, 'status'] = f'.git removal failed'

            save_table(repo_table)
        except Exception as e:
            print(e)
            repo_table.at[idx, 'status'] = f'failed: {e}'
        finally:
            end = time.time()
            time_seconds = int(end - start)
            repo_table.at[idx, 'time_taken'] = time_seconds

            save_table(repo_table)
            continue

    print(repo_table)
    save_table(repo_table)
    print(repo_table.info())
