import os
import time

from dotenv import load_dotenv

from github import Github
from github import Auth
import pandas as pd
from tqdm import tqdm

def get_csharp_percent(languages):
    if 'C#' in languages:
        return languages['C#'] / sum(languages.values())
    else:
        return 0
    
def get_commit_count(repo):
    return repo.get_commits().totalCount

if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("GH_ACCESS_TOKEN"))
    github = Github(auth=Auth.Token(os.getenv("GH_ACCESS_TOKEN")))
    github.per_page = 100
    qualifiers = {
        'forks':'>9',
        'stars':'>9',
        'language':'C#',
        'archived':'false',
        'created':'>2020-10-20',
        'size':'>10000'
    }
    repos = github.search_repositories(' '.join([f'{k}:{v}' for k, v in qualifiers.items()]))
    assert repos.totalCount > 0
    repo_info = {
        'name': [],
        'html_url': [],
        'git_url': [],
        'forks': [],
        'stars': [],
        'language': [],
        'size': [],
        'csharp_percent': [],
        'csharp_lines': [],
        'commit_count': [],
        'default_branch': []
    }
    try:
        for batch in tqdm(range(20)):
            for rep in repos.get_page(batch):
                repo_info['name'].append(rep.full_name)
                repo_info['html_url'].append(rep.html_url)
                repo_info['git_url'].append(rep.git_url)
                repo_info['forks'].append(rep.forks_count)
                repo_info['stars'].append(rep.stargazers_count)
                repo_info['language'].append(rep.language)
                repo_info['size'].append(rep.size)
                languages = rep.get_languages()
                repo_info['csharp_percent'].append(get_csharp_percent(languages))
                repo_info['csharp_lines'].append(languages.get('C#', 0))
                repo_info['commit_count'].append(get_commit_count(rep))
                repo_info['default_branch'].append(rep.default_branch)
            if github.get_rate_limit().core.remaining < 10:
                delay = github.get_rate_limit().core.reset - time.time()
                print(f'Waiting {delay} seconds for rate limit reset')
                time.sleep(delay)
            if github.get_rate_limit().search.remaining < 10:
                delay = github.get_rate_limit().search.reset - time.time()
                print(f'Waiting {delay} seconds for rate limit reset')
                time.sleep(delay)
    except Exception as e:
        print(e)

    repo_table = pd.DataFrame(repo_info)
    repo_table.to_csv('repo_table.csv', index=False)

    # render table to html and save
    repo_table_html = repo_table.to_html()
    with open('repo_table.html', 'w') as f:
        f.write(repo_table_html)

    print(repo_table)
    print('Done!')
