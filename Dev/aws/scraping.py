#yahooのトピックス一覧抽出
import requests
from bs4 import BeautifulSoup
import urllib

def main():
    load_url = "https://news.yahoo.co.jp/"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    topic = soup.find(class_ = "topics")

    for element in topic.find_all("a"):
        print(element.text)
        print("- - - - - - - - - - - - - - - - - - - - -")

    filename = "yahoo-topix.txt"
    with open(filename, "w") as f:

      #全てのaタグを検索し、リンクを絶対URLで書き出す
      topic = soup.find(class_ = "topics")
      for element in topic.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url , url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
        return element.text
