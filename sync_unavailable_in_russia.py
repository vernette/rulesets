import json

import requests

NO_RUSSIA_HOSTS_URL: str = (
    "https://raw.githubusercontent.com/dartraiden/no-russia-hosts/master/hosts.txt"
)

JSON_DIR: str = "json"
JSON_FILE_PATH: str = f"{JSON_DIR}/unavailable-in-russia.json"

EXCLUDED_DOMAINS: set[str] = {
    "tiktok.com",
    "tiktokv.com",
    "ttwstatic.com",
    "docker.io",
    "google.com",
    "googleapis.com",
    "github.com",
    "githubcopilot.com",
    "githubusercontent.com",
    "epicgames.com",
    "microsoft.com",
    "imgur.com",
    "spotify.com",
    "apple.com",
}

MERGED_SERVICE_FILES: list[str] = [
    f"{JSON_DIR}/claude.json",
    f"{JSON_DIR}/openai.json",
    f"{JSON_DIR}/gemini.json",
    f"{JSON_DIR}/grok.json",
    f"{JSON_DIR}/netflix.json",
]


def read_json(json_file: str) -> dict:
    with open(json_file, "r") as f:
        return json.load(f)


def save_json(json_file: str, data: dict) -> None:
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)


def get_no_russia_hosts(url: str) -> set[str]:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    lines = (line.strip() for line in response.text.splitlines())
    return {line for line in lines if line and "#" not in line}


def get_service_domains(json_files: list[str]) -> set[str]:
    domains: set[str] = set()
    for json_file in json_files:
        rules = read_json(json_file)["rules"][0]
        domains |= set(rules.get("domain_suffix", []))
        domains |= set(rules.get("domain", []))
    return domains


def is_domain_or_parent_exists(domain: str, existing_domains: set[str]) -> bool:
    if domain in existing_domains:
        return True

    for existing_domain in existing_domains:
        if domain.endswith("." + existing_domain):
            return True

    return False


def filter_new_domains(
    candidates: set[str], existing: set[str], excluded: set[str] = frozenset()
) -> set[str]:
    return {
        domain
        for domain in candidates
        if domain not in excluded and not is_domain_or_parent_exists(domain, existing)
    }


def update_domain_suffix_list(data: dict, new_domain_suffixes: set[str]) -> None:
    domain_suffix_list: list[str] = data["rules"][0]["domain_suffix"]
    domain_suffix_list.extend(new_domain_suffixes)
    domain_suffix_list.sort()


def sync_domains(json_file: str, no_russia_hosts: set[str]) -> None:
    json_domains: set[str] = get_service_domains([json_file])
    new_from_dartraiden: set[str] = filter_new_domains(
        no_russia_hosts,
        json_domains,
        EXCLUDED_DOMAINS,
    )

    service_domains: set[str] = get_service_domains(MERGED_SERVICE_FILES)
    new_from_services: set[str] = filter_new_domains(
        service_domains,
        json_domains,
    )

    all_new: set[str] = new_from_dartraiden | new_from_services

    if not all_new:
        print("No new domains found")
        return

    data: dict = read_json(json_file)
    update_domain_suffix_list(data, all_new)
    save_json(json_file, data)

    if new_from_dartraiden:
        print(
            f"Added {len(new_from_dartraiden)} domains from dartraiden/no-russia-hosts"
        )

    if new_from_services:
        print(f"Added {len(new_from_services)} domains from service files")


def main() -> None:
    no_russia_hosts: set[str] = get_no_russia_hosts(NO_RUSSIA_HOSTS_URL)
    sync_domains(JSON_FILE_PATH, no_russia_hosts)


if __name__ == "__main__":
    main()
