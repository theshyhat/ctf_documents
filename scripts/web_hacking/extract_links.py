'''
This script goes through a webpage file and extracts
any links from it, then prints out the names of the links.
'''

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

base_url = input("Please input the base URL of the website: ")

def extract_links(file_path):
  try:
    # read the content of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read()
    # prase HTML content using BeatifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # find all anchor tags
    links = soup.find_all('a')
    # extract href from anchor tags
    extracted_links = [urljoin(base_url, link.get('href')) for link in links if link.get('href')]
    # print extracted links
    if extracted_links:
      print("Extracted links:")
      for link in extracted_links:
        print(link)
    else:
      print("No links found in the file.")

  except FileNotFoundError:
    print(f"File not found: {file_path}")
  except Exception as e:
    print(f"An error occured: {e}")

if __name__ == "__main__":
  # check if a file path was provided as an argument
  if len(sys.argv) != 2:
    print("Usage: python extract_links.py <path_to_html_file>")
  else:
    # get file path from command line argument
    file_path = sys.argv[1]
    extract_links(file_path)
