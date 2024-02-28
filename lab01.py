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


if __name__ == "main":
    url = input('Enter a URL: ')
    html_content = get_html_from_url(url)

    if html_content:
        print(html_content)
    else:
        print("Failed to retrieve HTML from the specified URL.")
