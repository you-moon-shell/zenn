---
title: "Gemini API 触ってみる"
emoji: "😇"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["Gemini", "Google", "Python", "GenerativeAI", "Multimodal"]
published: false
publication_name: open8
---

株式会社オープンエイトで今年 9 月からエンジニアをしている山田 Y です！

# 動機

弊社では動画編集クラウドと銘打って[VideoBrain](https://video-b.com/)というサービスを展開しています。
動画を中心に扱っているサービスなので、マルチモーダルに強みのある(らしい) Gemini はチェックしておこうと思いました。
Google が公開した Gemini の紹介動画が以下になります。(結構編集の力を借りているようですが、、、)

https://youtu.be/UIZAiXYceBI

# とりあえず動かしてみる

https://ai.google.dev/tutorials/python_quickstart

↑ を参考にまずは動かせるところまで確認しようと思います。(Jupyter は利用しない方針で環境構築します。)
Python を使って Gemini API 経由で生成結果を取得します！

## 実行環境

- OS: macOS Ventura 13.6.2
- Chip: Apple M1 Pro
- Python: 3.12.0

## 準備

以下のコマンドを実行し必要なライブラリをインストールします。

```
pip install google-generativeai pillow
```

[Setup your API key](https://ai.google.dev/tutorials/python_quickstart#setup_your_api_key) を参考に `GOOGLE_API_KEY` を取得し環境変数にセットします。

```
export GOOGLE_API_KEY=<your_api_key>
```

## 動作確認

以下のコードを実行してみます！

https://github.com/you-moon-shell/zenn/blob/5cc9ae48076b05ba348b561035df334b0384efdc/files/tried-using-gemini/operation_confirmation.py

こんな感じの結果が返ってくれば動作確認完了です。

```
The meaning of life is a multifaceted concept that has been pondered by philosophers, theologians, and individuals throughout history. While there is no definitive or universally agreed-upon answer, here are some commonly discussed perspectives on the meaning of life:

1. **Purpose and Fulfillment:** Some believe that the meaning of life lies in finding and fulfilling one's unique purpose or potential. This could involve setting personal goals, pursuing passions, making a positive contribution to society, or finding a sense of accomplishment and fulfillment in various aspects of life.

<中略>

Ultimately, the meaning of life is a personal and subjective quest that each individual must explore and define for themselves. There is no right or wrong answer, and different perspectives can coexist and hold validity for different individuals and cultures.
```

# いろいろ試してみる

https://ai.google.dev/docs/multimodal_concepts

https://developers.googleblog.com/2023/12/how-its-made-gemini-multimodal-prompting.html
