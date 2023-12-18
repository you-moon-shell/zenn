import google.generativeai as genai
from PIL import Image

# 画像とテキストを与えた出力を見てみる
gemini_pro_vision = genai.GenerativeModel(
    "gemini-pro-vision"  # 画像を入力するので gemini-pro-vision を指定
)
text = "Explain the nutritional value of the foods in the following image in a tabular format."
image = Image.open("images/tried-using-gemini/breakfast.jpg")
response = gemini_pro_vision.generate_content(
    [text, image]  # 配列に画像とテキストを含めればOK
)
print(response.text)
