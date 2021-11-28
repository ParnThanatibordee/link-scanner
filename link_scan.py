from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


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


if __name__ == "__main__":
    print(get_links('https://cpske.github.io/ISP/'))
    print(is_valid_url("https://cpske.github.io/ISP/"))
    print(is_valid_url("https://kucafe.com/search?q=coffee"))
    print(is_valid_url("#prices"))
    print(is_valid_url("abcd"))
