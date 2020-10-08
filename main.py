from pdfkit import from_url  # from_url()
from bs4 import BeautifulSoup  # BeautifulSoup
from requests import get  # get()

def get_site_index_urls() -> list:
    """
        Description: For fetching https://www.learncpp.com site index urls and return it.
        Parameters: None
        Return type: list
    """
    r = get(
        "https://www.learncpp.com")  # sending GET request to https://www.learncpp.com
    # Make instance of BeautifulSoup
    soup = BeautifulSoup(r.content, "html.parser")
    urls = []  # For learncpp.com contents urls list, This will be returned

    for i in soup.find_all('tr'):  # Fetch all <tr>
        link = i.find('a', href=True)  # Finding all <a> that have a href
        if link is None:
            continue  # If it was an empty list
        urls.append(link['href'])  # Append an thing that it find in the list

    urls.pop(0)  # Because for some reason the first url that it find is '/'
    return urls  # return urls


def site_index_print_urls(raw_urls: list) -> list:
    """
        Description: For content's print urls.
        Parameters: raw_urls: list
        Return type: list
    """
    print_urls = [] # The list that raw_urls will append to it. This will be returned
    for url in raw_urls:
        print_urls.append(url + "print/") # Adding "print/" for having printable url
    return print_urls # Returning them


if __name__ == "__main__":
    site_index_urls = get_site_index_urls()  # site index urls
    site_index_print_urls = site_index_print_urls(site_index_urls)  # For content's print urls