from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def get_links(url: str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    my_options = Options()
    my_options.headless = True

    assert my_options.headless

    # TODO: change path_to_driver to your own path
    path_to_driver = 'C:/Users/parn8/OneDrive/Desktop/chromedriver_win32/chromedriver.exe'  # Your PATH/TO/DRIVER
    browser = webdriver.Chrome(path_to_driver, options=my_options)
    browser.implicitly_wait(10)
    browser.get(url)

    result = []

    all_a_tag = browser.find_elements_by_css_selector('li a')
    for a in all_a_tag:
        clean_tag = a.get_attribute('href').split("#")[0].split("?")[0]
        if not(clean_tag in result) and clean_tag != "":
            result.append(clean_tag)

    return result


if __name__ == "__main__":
    print(get_links('https://cpske.github.io/ISP/'))
