import requests  # Import library

def get_html_from_url(url: str) -> str:
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve HTML. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    

def get_headers_from_url(url: str) -> dict:
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.headers
        else:
            print(f"Failed to retrieve headers. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


def get_web_server(url: str) -> str:
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.headers.get('Server', 'Unknown')
        else:
            print(f"Failed to retrieve web server. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    

def get_cookies(url: str) -> list:
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.cookies
        else:
            print(f"Failed to retrieve cookies. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    url = input('Enter a URL: ')

    if web_server := get_web_server(url):
        print(f'Web server: {web_server}')

    if cookies := get_cookies_from_url(url):
        print('Cookies:')
        for cookie in cookies:
            print(f'\tName: {cookie.name}')
            print(f'\tExpires: {cookie.expires}\n')

