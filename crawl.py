from bs4 import BeautifulSoup
import requests
import json

def main():

    data = open("/home/chanwoo/PycharmProjects/crawler/company_links.csv", "r")
    company_links = []

    for link in data:
        link = link.replace("stock-price-history","roe")
        company_links.append(link)

    print(company_links[0])
    fetch_number(company_links[0])

def fetch_number(url):

    url_data = requests.get(url)
    soup = BeautifulSoup(url_data.content, 'html.parser')
    chart_json = soup.json()
    #main_content = main_content_container.find_all('div', attrs={'class':'main_content'})
    print(chart_json)


if __name__ == '__main__':
    main()