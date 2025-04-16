import json
import os

JSON_DIR = 'json'
RAW_DIR = 'raw'


def read_json(json_file_path: str) -> dict:
    with open(json_file_path, 'r') as f:
        return json.load(f)


def extract_domains(rule_data: dict) -> list[str]:
    domains = []

    for rule in rule_data.get('rules', []):
        if 'domain' in rule:
            domains.extend(rule['domain'])

        if 'domain_suffix' in rule:
            domains.extend(rule['domain_suffix'])

    return sorted(set(domains))


def save_txt(file_path: str, domains: list[str]) -> None:
    with open(file_path, 'w') as f:
        for domain in domains:
            f.write(f'{domain}\n')


def process_json_files() -> None:
    json_files = [f for f in os.listdir(JSON_DIR) if f.endswith('.json')]

    for json_file in json_files:
        if json_file == 'discord-full.json':  # Since it's in a discord-domains.json
            continue

        json_path = os.path.join(JSON_DIR, json_file)
        txt_filename = os.path.basename(json_file).replace('.json', '.txt')
        txt_path = os.path.join(RAW_DIR, txt_filename)

        rule_data = read_json(json_path)

        domains = extract_domains(rule_data)

        if domains:
            save_txt(txt_path, domains)
            print(f'Processed {json_file} → {txt_filename} ({len(domains)} domains)')
            continue

        print(f'Skipped {json_file} - no domains found')


def main() -> None:
    process_json_files()


if __name__ == '__main__':
    main()
