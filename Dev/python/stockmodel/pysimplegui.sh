PySimpleGUIをインストールする一般的に2つの方法があります。

PyPIからpipでインストールする
PySimpleGUI.pyファイルをダウンロードしてアプリケーションのフォルダに配置します
Pipインストールとアップグレード
現在提案されているpipコマンドを呼び出す方法は、Pythonを使ってモジュールとして実行することです。 以前は、pipまたはpip3コマンドはコマンドライン/シェル上で 直接実行されました。 提案された方法は以下となります。

Windows の初期インストール

python -m pip install PySimpleGUI

Linux および MacOS の初期インストール

python3 -m pip install PySimpleGUI

pipを使用してアップグレードするには、単に2つのパラメータ--upgrade --no-cache-dirを指定するだけです。

Windows のアップグレード

python -m pip install --upgrade --no-cache-dir PySimpleGUI

Linux および MacOS のアップグレード

python3 -m pip install --upgrade --no-cache-dir PySimpleGUI



https://github.com/PySimpleGUI/PySimpleGUI/blob/master/readme.ja.md#pypi-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB

https://github.com/PySimpleGUI/PySimpleGUI/find/master
