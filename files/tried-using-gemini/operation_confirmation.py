import google.generativeai as genai

# 環境変数に GOOGLE_API_KEY が設定されていれば不要
# GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)

# テキストのみ処理可能
gemini_pro = genai.GenerativeModel("gemini-pro")
prompt = "What is the meaning of life?"
response = gemini_pro.generate_content(prompt)
print(response.text)
