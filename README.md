# SlackSendImage
東京の気圧を[気象庁](https://www.jma.go.jp/jp/amedas_h/today-44132.html)のページから取得して、過去12時間の気圧のグラフを作成したうえで `Slack` に通知する。

```
python=3.8
```

```
pip install beautifulsoup4
pip install requests
pip install numpy
pip install matplotlib
pip install python-dotenv
pip install gspread
pip install oauth2client
```
`token` は `slack` `google api` ともに取得して `json` をカレントディレクトリに配置（これはゆくゆく変えたい）

```sh
python app.py
```
`#imgs` というチャンネルにデフォルトで投稿される

```sh
python app.py random
```
こう指定すると `random` チャンネルに投稿される。
引数を指定するとデバックモードのつもりで、スプレッドシートを分けることができる。
