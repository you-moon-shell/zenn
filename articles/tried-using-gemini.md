---
title: "Gemini API 触ってみる"
emoji: "😇"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["Gemini", "Google", "Python", "GenerativeAI", "Multimodal"]
published: true
publication_name: open8
---

株式会社オープンエイトで今年 9 月からエンジニアをしている山田 Y です！

# 動機

弊社では動画編集クラウドと銘打って[VideoBrain](https://video-b.com/)というサービスを展開しています。
動画編集を中心に扱っているサービスなので、マルチモーダルに強みのある(らしい) Gemini はチェックしておこうと思いました。
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

https://github.com/you-moon-shell/zenn/blob/e2a6cd5413854943d87847e3c5cc212d5360de20/files/tried-using-gemini/operation_confirmation.py

こんな感じの結果が返ってくれば動作確認完了です 👌

```
The meaning of life is a multifaceted concept that has been pondered by philosophers, theologians, and individuals throughout history. While there is no definitive or universally agreed-upon answer, here are some commonly discussed perspectives on the meaning of life:

1. **Purpose and Fulfillment:** Some believe that the meaning of life lies in finding and fulfilling one's unique purpose or potential. This could involve setting personal goals, pursuing passions, making a positive contribution to society, or finding a sense of accomplishment and fulfillment in various aspects of life.

<中略>

Ultimately, the meaning of life is a personal and subjective quest that each individual must explore and define for themselves. There is no right or wrong answer, and different perspectives can coexist and hold validity for different individuals and cultures.
```

# いろいろ試してみる

この辺りを参考に Gemini でできることをいくつか試してみようと思います！

https://ai.google.dev/docs/multimodal_concepts

https://developers.googleblog.com/2023/12/how-its-made-gemini-multimodal-prompting.html

## 1. 画像だけ与えて推論してもらう

試しにおいしそうな朝食の画像を与えて、アウトプットを見てみます。

![](/images/tried-using-gemini/breakfast.jpg)
_鎌倉で食べた美味しい朝食_

コードはこちらです。
画像を入力したいのでモデルは `gemini-pro-vision` を指定します。([Generate text from image and text inputs](https://ai.google.dev/tutorials/python_quickstart#generate_text_from_image_and_text_inputs))

https://github.com/you-moon-shell/zenn/blob/e691f5aed726c9d12a45f76f70490eb1ef7204f5/files/tried-using-gemini/image_input.py

```:result
A delicious breakfast of eggs, bacon, toast, and salad.
```

しっかりとおいしい朝食として認識してくれているようですが、ベーコンの下にあるビーフパティには気付いてくれませんでした。

## 2. テキストも一緒に与えて出力をより詳しくする

先ほどの朝食の画像と一緒にテキストを与えて、詳細なアウトプットを得られるか見てみます。
それぞれの食べ物の栄養価を表形式で出力してみようと思います。

https://github.com/you-moon-shell/zenn/blob/b49fd654b23bbcbef739eaa46151b44aba26b9f4/files/tried-using-gemini/image_and_text_input.py

```:result
| Food Item | Calories | Protein (g) | Carbohydrates (g) | Fat (g) |
|---|---|---|---|---|
| Egg | 71 | 6.3 | 0.6 | 4.9 |
| Bacon | 43 | 3.6 | 0 | 3.4 |
| Toast (2 slices) | 142 | 5.2 | 25.5 | 2.3 |
| Salad | 20 | 1.5 | 3.9 | 0.7 |
| Dressing | 50 | 0 | 4 | 5 |

| Total | 326 | 16.6 | 34 | 16.3 |
```

ちゃんと栄養価の出力を表形式で得られました！
ざっくり調べてみたところ栄養価の数値としては、実際とそこまで乖離がないように見えました。(卵、トーストはほぼ完璧でした。)

## 3. 画像を複数与えて共通点を判断してもらう

以下の 2 枚の画像を与えて、それぞれの説明と共通点があるか出力してもらおうと思います。

![](/images/tried-using-gemini/sensoji.jpg =400x)
_浅草寺(夜)_

![](/images/tried-using-gemini/skytree.jpg =400x)
_スカイツリー(夜)_

コードはこちらです。

https://github.com/you-moon-shell/zenn/blob/3bdfe099b3919a37e87722c35540808b5dfb5218/files/tried-using-gemini/multi_images_and_text_input.py

```:result
The two images are both night scenes of Tokyo, Japan.
The first image is of the Sensoji Temple, a Buddhist temple located in Asakusa.
The second image is of the Tokyo Skytree, a communications and observation tower located in Sumida.
Both images feature tall structures that are illuminated at night.
The Sensoji Temple is a five-story pagoda, while the Tokyo Skytree is a 634-meter-tall tower.
Both images also feature people walking around the structures.
The Sensoji Temple is located in a busy shopping area, while the Tokyo Skytree is located in a more modern area. Both images capture the beauty of Tokyo at night.

The common features of the two images are:

1. Both images are night scenes of Tokyo, Japan.
2. Both images feature tall structures that are illuminated at night.
3. Both images feature people walking around the structures.
4. Both images capture the beauty of Tokyo at night.
```

```:result(和訳)
この2つの画像はどちらも東京の夜景である。
1枚目は浅草にある浅草寺。
2つ目の画像は、墨田区にある通信・展望タワー、東京スカイツリー。
どちらの画像も、夜になるとライトアップされる高い建造物が特徴だ。
浅草寺は五重塔で、東京スカイツリーは高さ634メートルのタワーである。
どちらの画像も、建造物の周りを歩く人々も写っている。
浅草寺は繁華街にあり、東京スカイツリーはもっと近代的なエリアにある。
どちらの画像も夜の東京の美しさをとらえている。

2つの画像に共通する特徴は

1. どちらも東京の夜景である。
2. どちらの画像も、夜にライトアップされた高い建造物が特徴である。
3. どちらの画像にも、建造物の周りを歩く人々が写っている。
4. どちらの画像も夜の東京の美しさをとらえている。
```

浅草寺とスカイツリーそれぞれ判別できており、ある程度正しく説明できています。
共通点も 4 つ挙げられ 3 つ目以外は正しい結果となりました！

## 4. 与えた画像・説明に合わせて別の画像に説明を付与する

浅草寺とスカイツリーの説明を「名称：所在地 (竣工年)」といった形で与え、以下の画像の説明を出力できるか見てみようと思います。

![](/images/tried-using-gemini/tokyotower.jpg =400x)
_東京タワー(夜)_

コードはこちらです。

https://github.com/you-moon-shell/zenn/blob/5409e5fbaaf71b8c4f64d15bf09b4be143a34b66/files/tried-using-gemini/image_and_text_pair_input.py

```:result
東京タワー：東京/港区 (1958年)
```

フォーマットも内容も正しい結果となりました！

# まとめ

4 つのケースで現状の Gemini の精度やできることを見てみて、細かい点を見落としたり一部誤った出力となる場合もありましたが、わかりやすい画像や指示でシンプルな出力を求めれば活用できる場面は見出せるように思いました。
今後動画を入力できたり精度や速度の向上が行われると期待しているので、逐次チェックしていきたいです！
