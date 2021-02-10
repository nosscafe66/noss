#!/bin/bash

#brewアップデートとpipのアップデート
brew update
brew upgrade
pip install --upgrade pip

#株価予測プログラムに必要なパッケージインストール
pip install chromedriver-binary-auto
pip install webdriver_manager
pip install scipy
pip install pandas
pip install selenium
pip install scikit-learn
pip install matplotlib
pip3 install seaborn

#pyenvのインストールとバージョン確認
brew install pyenv
brew upgrade pyenv
brew install python
pyenv -v
pyenv install --list
echo y | pyenv install 3.8.0
pyenv global 3.8.0


#バージョン確認
pyenv versions
python -V

pip install -r ./requirements.txt
