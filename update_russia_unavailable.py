import json

import requests


NO_RUSSIA_HOSTS_URL: str = 'https://raw.githubusercontent.com/dartraiden/no-russia-hosts/master/hosts.txt'
JSON_FILE_PATH: str = 'json/unavailable-in-russia.json'
EXCLUDED_DOMAINS: set[str] = {
    'tiktok.com',
    'tiktokv.com',
    'ttwstatic.com',
    'docker.io',
    'google.com',
    'googleapis.com',
    'github.com',
    'githubcopilot.com',
    'githubusercontent.com',
    'netflix.com',
    'fast.com',
    'chatgpt.com',
    'openai.com',
    'oaistatic.com',
    'oaiusercontent.com',
    'epicgames.com',
}


def read_json(json_file: str) -> dict:
    with open(json_file, 'r') as f:
        return json.load(f)


def save_json(json_file: str, data: dict) -> None:
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)


def get_no_russia_hosts(url: str) -> set[str]:
    response = requests.get(url)

    domains: set[str] = {
        line
        for line in response.text.splitlines()
        if line and '#' not in line
    }

    return domains


def get_json_domains(json_file: str) -> set[str]:
    rules: dict = read_json(json_file)['rules'][0]
    return set(rules['domain']) | set(rules['domain_suffix'])


def is_domain_or_parent_exists(domain: str, existing_domains: set[str]) -> bool:
    if domain in existing_domains:
        return True
    
    for existing_domain in existing_domains:
        if existing_domain.endswith('.' + domain):
            return True
            
    return False


def get_new_domain_suffixes(no_russia_hosts: set[str], json_domains: set[str]) -> set[str]:
    return {
        domain for domain in no_russia_hosts
        if domain not in EXCLUDED_DOMAINS
        and not is_domain_or_parent_exists(domain, json_domains)
    }


def update_domain_suffix_list(data: dict, new_domain_suffixes: set[str]) -> None:
    domain_suffix_list: list[str] = data['rules'][0]['domain_suffix']
    domain_suffix_list.extend(new_domain_suffixes)
    domain_suffix_list.sort()


def update_json(json_file: str, no_russia_hosts: set[str]) -> None:
    json_domains: set[str] = get_json_domains(json_file)
    new_domain_suffixes: set[str] = get_new_domain_suffixes(no_russia_hosts, json_domains)

    if not new_domain_suffixes:
        print('No new domains found')
        return

    data: dict = read_json(json_file)
    update_domain_suffix_list(data, new_domain_suffixes)
    save_json(json_file, data)
    print(f'Added {len(new_domain_suffixes)} new domains')


def main() -> None:
    no_russia_hosts: set[str] = get_no_russia_hosts(NO_RUSSIA_HOSTS_URL)
    update_json(JSON_FILE_PATH, no_russia_hosts)


if __name__ == '__main__':
    main()
