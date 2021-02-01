#!/bin/bash

#株価の予測プログラムを正常に起動するために必要なパッケージに更新を加えるプログラム
./python.sh

#pip list -o アップデート必要なパッケージリスト
#pip list -u 最新状況のパッケージのみを表示
#pip install -U <package-name> パッケージのアップデート
## https://qiita.com/HyunwookPark/items/242a8ceea656416b6da8 ##pipコマンドに関する内容記載
## https://basicincome30.com/python-install-mac ##

#一時的に動作を止める
echo "3秒間動作を止めます。"
sleep 3

#chromedriverのバージョンを確認する
pip show chromedriver-binary

#jupyter noteで作成したpythonファイルをpythonコマンドで実行できる状態へ
jupyter nbconvert --to script stockmodel.ipynb