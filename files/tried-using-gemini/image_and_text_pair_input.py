import google.generativeai as genai
from PIL import Image

# 画像と説明ペアで与えた出力を見てみる
gemini_pro_vision = genai.GenerativeModel(
    "gemini-pro-vision"  # 画像を入力するので gemini-pro-vision を指定
)
response = gemini_pro_vision.generate_content(
    [
        Image.open("images/tried-using-gemini/sensoji.jpg"),
        "浅草寺：東京/台東区 (623年)",
        Image.open("images/tried-using-gemini/skytree.jpg"),
        "スカイツリー：東京/墨田区 (2012年)",
        Image.open("images/tried-using-gemini/tokyotower.jpg"),
    ]  # 配列に 画像->説明->画像->説明->画像 の順に渡す
)
print(response.text)
