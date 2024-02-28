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


if __name__ == "__main__":
    url = input('Enter a URL: ')
    headers = get_headers_from_url(url)

    if headers:
        for header, value in headers.items():
            print(f"{header}: {value}")
    else:
        print("Failed to retrieve HTML headers from the specified URL.")
