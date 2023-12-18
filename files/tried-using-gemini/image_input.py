import google.generativeai as genai
from PIL import Image

# 画像だけ与えて推論してもらう
gemini_pro_vision = genai.GenerativeModel(
    "gemini-pro-vision"  # 画像を入力するので gemini-pro-vision を指定
)
image = Image.open("images/tried-using-gemini/breakfast.jpg")
response = gemini_pro_vision.generate_content([image])
print(response.text)
