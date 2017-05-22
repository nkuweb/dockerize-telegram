import requests
from urllib.parse import urlparse


def url(url):

    x = urlparse(url)
    r = requests.get(url)
    status_of_url = True
    if r.status_code == 200 and (x.hostname is not None):
        pass
    else:
        status_of_url = False

    return status_of_url


