import requests


class HTTP_Helper:

    def get_mega_download_links(self):
        url = "https://mega.nz/desktop"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            download_links = []

            # Find all download links on the page
            for link in soup.find_all('a', {'class': 'btn'}):
                href = link.get('href')
                if href and 'linux' in href.lower():
                    download_links.append(href)

            return download_links
        else:
            print(f"Failed to retrieve page content. Status code: {response.status_code}")
            return []

    def test_download_links(self, download_links):
        for link in download_links:
            try:
                response = requests.get(link, stream=True)
                if response.status_code == 200:
                    print(f"Download link {link} is working.")
                else:
                    print(f"Download link {link} returned status code: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error testing download link {link}: {e}")