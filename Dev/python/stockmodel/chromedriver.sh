#!/bin/bash

./python.sh

echo "3秒間動作を止めます。"
sleep 3

#chromedriverのバージョンを確認する
pip show chromedriver-binary

#jupyter noteで作成したpythonファイルをpythonコマンドで実行できる状態へ
jupyter nbconvert --to script stockmodel.ipynb
