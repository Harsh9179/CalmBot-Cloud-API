from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# ✅ Your OpenAI API Key (I will show you how to get it later)
openai.api_key = "XXXXXXXXXXXX"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user input from Android
        user_input = request.json.get('inputs')

        # Call OpenAI API (ChatGPT)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a mental health assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the AI response
        ai_message = response.choices[0].message['content']

        # Send the response to Android
        return jsonify({"generatedText": ai_message})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
