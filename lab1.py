import requests
from datetime import datetime

def main():
    while True:
        user_url = input("\nEnter the URL: ")
        if user_url == "":
            break
        else:
            if 'https://' in user_url or 'http://' in user_url:
                s = requests.session()
                r = s.get(user_url)
                with requests.get(user_url) as response:
                    print_headers(response)
                    get_software(response)
                    get_cookies(r)
                cont = input("\nSearch another URL? (y/n)\n")
                if cont == "n":
                    break
            else:
                print("This is not a URL, Please type a URL or press enter to stop")

#print headers
def print_headers(response):
    headers = response.headers
    print("\nHeaders:")
    for header, value in headers.items():
        print( header + ": " + value )

def get_software(response):
    if 'Server' in response.headers:
        print("\nServer Software: " + response.headers['Server'])
    else:
        print("\nServer Software: No Server Software found")
        

def get_cookies(response):
    cookies = response.cookies
    if cookies:
        print("\nThis URL uses the following Cookies:")
        for cookie in cookies:
            if isinstance(cookie.expires,int):
                print("\nCookie name: " + cookie.name+ "\nExpiration Date: ",datetime.fromtimestamp(cookie.expires))
            else:
                print("\nCookie name: " + cookie.name+ "\nExpiration Date: ",cookie.expires)
    else:
        print("\nCokkies: No Cookies found\n")


if __name__ == "__main__":
    main()
