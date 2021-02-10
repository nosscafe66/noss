#!/bin/bash

#株価の予測プログラムを正常に起動するために必要なパッケージに更新を加えるプログラム
./python.sh

#一時的に動作を止める
echo "3秒間動作を止めます。"
sleep 3

#chromedriverのバージョンを確認する
pip show chromedriver-binary

#jupyter noteで作成したpythonファイルをpythonコマンドで実行できる状態へ
jupyter nbconvert --to script stockmodel.ipynb
