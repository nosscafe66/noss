#!/bin/bash
echo "Google chrome driverの自動更新および必要なパッケージの更新実施"
./chromedriver.sh

#一時的に停止
echo "3秒間停止"
sleep 3

#jupyter noteから変換したpythonファイルの実行権限を変更する
chmod 777 stockmodel.py

#株価予測プログラムを動作させる
echo "これより株価の予測プログラムを開始"
python stockmodel.py >> log.txt


echo "株価予測が終了しました。"