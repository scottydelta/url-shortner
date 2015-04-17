import re, string, random, requests

def get_page_title(url):
    regex = re.compile('<title>(.*?)</title>', re.IGNORECASE | re.DOTALL)
    try:
        page_content = requests.get(url).text
        title = regex.search(page_content).group(1)
        return title
    except requests.RequestException:
        return ""

def generate_random_string(size=10):
    return ''.join(random.choice(string.hexdigits) for _ in xrange(size))

