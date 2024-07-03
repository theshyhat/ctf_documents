'''
This script uses the Python requests module to make a web request to a specific webpage and writes its contents to a file on the host machine.
'''
import requests

url = input("Input the desired URL: ")
output_file = 'webpage_fetch.html'

def fetch_webpage(url, output_file):
  try:
    # send GET request to desired URL
    response = requests.get(url)
    # raise an exception if the request was unsuccessful
    response.raise_for_status()
    #write the content of the response to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
      file.write(response.text)
    print(f"Webpage content successfully recorded in {output_file}")
  except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")

fetch_webpage(url, output_file)
