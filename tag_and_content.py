import json
from theguardian import theguardian_tag
from theguardian import theguardian_content
from colorama import Fore, Style
import time

def fetch_and_display_content():

    headers = {
        "q": "technology",
        "section": "technology",
        "show-references": "all",
    }
    tag = theguardian_tag.Tag(api='1d961fa1-1d54-4c23-8ee3-b1a1ee231243', **headers)

   
    tag_content = tag.get_content_response()
    results = tag.get_results(tag_content)

    
    if results:
        first_tag_apiUrl = results[0]["apiUrl"]
        content = theguardian_content.Content(api='Your-API_KEY', url=first_tag_apiUrl)
        content_response = content.get_content_response()

        if content_response:
            
            response_data = content_response.get('response', {})
            results_data = response_data.get('results', [])

            
            for result in results_data:
                print('-'*10)
                print(f"{Fore.GREEN}Title:{Style.RESET_ALL} {result.get('webTitle')}")
                print(f"{Fore.BLUE}Publication Date:{Style.RESET_ALL} {result.get('webPublicationDate')}")
                print(f"{Fore.YELLOW}URL:{Style.RESET_ALL} {result.get('webUrl')}")
                print()
                print('-'*10)

           
            time.sleep(3600)
        else:
            print("Content response is empty or None.")
    else:
        print("No results found.")

def main():
    while True:
        fetch_and_display_content()

if __name__ == "__main__":
    main()
