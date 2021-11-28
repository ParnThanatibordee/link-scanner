from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from typing import List


def get_links(url: str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    my_options = Options()
    my_options.headless = True

    assert my_options.headless

    browser = webdriver.Chrome(options=my_options)
    browser.implicitly_wait(10)
    browser.get(url)

    result = []

    all_a_tag = browser.find_elements_by_css_selector('li a')
    for a in all_a_tag:
        clean_tag = a.get_attribute('href').split("#")[0].split("?")[0]
        if not(clean_tag in result) and clean_tag != "":
            result.append(clean_tag)

    return result


def is_valid_url(url: str):
    """Return True if the URL is OK, False otherwise. Also return False is the URL has invalid syntax."""
    try:
        req = Request(url)
        urlopen(req)
    except ValueError:
        return False
    except HTTPError as error_code:
        if error_code.code == 403:
            return True
        return False
    except URLError:
        return False
    else:
        return True


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    invalid_list = []

    for i in urllist:
        if not(is_valid_url(i)):
            invalid_list.append(i)

    return invalid_list


if __name__ == "__main__":
    print('run...')
    listt = ["https://cpske.github.io/ISP/", "https://kucafe.com/search?q=coffee", "#prices", "abcd"]
    print(invalid_urls(listt))
