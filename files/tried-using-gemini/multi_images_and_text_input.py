import google.generativeai as genai
from PIL import Image

# 複数画像とテキストを与えた出力を見てみる
gemini_pro_vision = genai.GenerativeModel(
    "gemini-pro-vision"  # 画像を入力するので gemini-pro-vision を指定
)
text = "After describing the two images, list the common features of the two images."
images = [
    Image.open("images/tried-using-gemini/sensoji.jpg"),
    Image.open("images/tried-using-gemini/skytree.jpg"),
]
response = gemini_pro_vision.generate_content(
    [text, *images]  # 配列に複数画像とテキストを含めればOK
)
print(response.text)
