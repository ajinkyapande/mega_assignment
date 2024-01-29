import requests
from bs4 import BeautifulSoup
import os



if __name__ == "__main__":
    mega_download_links = get_mega_download_links()

    if mega_download_links:
        print("Testing Mega Desktop App download links:")
        test_download_links(mega_download_links)
    else:
        print("No Mega Desktop App download links found.")
