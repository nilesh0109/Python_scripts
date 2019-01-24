import requests
import re

def is_a_valid_image(url):
    """
        check if the downloaded content is image type
        valid image types are ['png', 'jpg', 'jpeg', 'svg', 'gif', 'tiff', 'icon', 'x-icon']
        input: URL to download
        return boolean
    """
    #Lame, i know. It could be improved with a proper complex Regex, but for simplicity i am just checking the length
    if not url or len(url) < 10:
        return False
    white_list_image_extensions = ['png', 'jpg', 'jpeg', 'svg', 'svg+xml', 'gif', 'tiff', 'icon', 'x-icon']
    is_valid_image = False
    try:
        res = requests.head(url, allow_redirects=True)
        if (res.status_code):
            content_type = res.headers.get('content-type')
            is_valid_image = content_type.split('/')[-1] in white_list_image_extensions
        return is_valid_image

    except requests.exceptions.RequestException as e:
        print(e)


def get_file_name(header_content, url):
    """
        Get filename from content-disposition
        Take the fileName from content-deposition or lastpart from the url
        return fileName or None
    """
    if not header_content:
        return url.split('/')[-1]
    fname = re.findall('filename="(.+)"', header_content)
    if len(fname) == 0:
        return url.split('/')[-1]
    else:
        return fname[0]

def get_url_content(url):
    """
        Read the file from the provided url
    """
    try:
        return requests.get(url, allow_redirects=True)
    except:
        print('Could not open url:', url)
        return None

