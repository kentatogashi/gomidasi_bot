# 概要

ゴミ出し曜日通知BOT

LINEのMessage APIを通して、曜日ごとのゴミ種別を対象のユーザへ通知する。

# 手順

1. LINE developersにChannel登録する。
2. herokuにLINEのユーザIDを取得するだけのWebHookアプリをデプロイする。Procfileとcallback.pyが該当する。
3. LINE developersのWeb Hook URLにherokuアプリのURLを登録する。
4. LINEアプリで、BOTを友達登録する。
5. 友達登録をトリガーに、WebHook処理が実行されるので、heroku logsで、userIdを確認する。
6. gomidasi_bot.pyのtoにuserIdを書いて、cronに設定する。

# heroku logsの実行例

```
2018-06-17T12:33:08.819016+00:00 app[web.1]: b'{"events":[{"type":"follow","replyToken":"bc4089e698404165bcdbdc698b18b679","source":{"userId":"U2b8b4d33a30df0dd1370fxxxxxxxxx","type":"user"},"timestamp":1529238778994}]}'
```
