import os
import re
import requests

# repository used for storing input data for development branches
DOCKERHUB_DATA_REPO = 'dtcenter/metplus-data-dev'

# URL of DockerHub repository
DOCKERHUB_URL = f'https://hub.docker.com/v2/repositories/{DOCKERHUB_DATA_REPO}/tags'


def docker_get_volumes_last_updated(current_branch):
    dockerhub_request = requests.get(DOCKERHUB_URL)
    if dockerhub_request.status_code != 200:
        print(f"Could not find DockerHub URL: {DOCKERHUB_URL}")
        return None

    volumes_last_updated = {}
    attempts = 0
    page = dockerhub_request.json()
    while attempts < 10:
        results = page['results']
        for repo in results:
            repo_name = repo['name']
            if repo_name.split('-')[0] == current_branch:
                volumes_last_updated[repo_name] = repo['last_updated']
        if not page['next']:
            break
        page = requests.get(page['next']).json()
        attempts += 1

    return volumes_last_updated

def get_branch_from_github_ref():
    github_ref = os.environ.get('GITHUB_REF')
    if github_ref is None:
        print("GITHUB_REF is not set")
        return None, None

    # check if it matches branch or tags format
    for ref_type in ['heads', 'tags']:
        regex_pattern = r'refs\/' + ref_type + r'\/(.*)'
        match = re.match(regex_pattern, github_ref)
        if match:
            is_branch = True if ref_type == 'heads' else False
            return match.group(1), is_branch

        print("Could not extract branch/tag name from GITHUB_REF")
        return None, None
