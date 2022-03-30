import requests
import sys
import selenium
import urllib
from urllib.parse import urlparse

roster_id = "何とかしてroster_idを取得する"#これができると動的なページのスクレイピングが可能となる。
task_id = "何とかしてtask_idを取得する"#これができると動的なページのスクレイピングが可能となる。
request = requests.get("https://lome.ft-cons.co.jp/ctrl/roster?action=view&roster_id={}&task_id={}".format(roster_id,task_id))

int(urlparse('https://teratail.com/questions/23283').path.split('/')[2])

#あとは勤務表に伴う