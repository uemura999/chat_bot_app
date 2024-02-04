from flask import Flask, request, render_template
from openai import OpenAI
import os

# 環境変数からAPIキーを取得して設定
os.environ["OPENAI_API_KEY"] = "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"

# OpenAIクライアントの初期化
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = get_openai_response(user_input)
        return render_template('index.html', user_input=user_input, bot_response=response)
    return render_template('index.html', user_input='', bot_response='')

def get_openai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Error: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
