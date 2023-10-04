import requests


def check_url(url: str) -> bool:
    response = requests.get(url)
    if 200 <= response.status_code <= 299:
        return True
    return False


if __name__ == "__main__":
    url = "http://wmii.uwm.edu.pl/"
    print(check_url(url))
