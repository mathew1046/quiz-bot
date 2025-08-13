from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def safe_json_loads(s):
    """
    Parses normal JSON or JSONP strings like 'callbackName({...})' or 'json[{}]'.
    """
    # Remove JSONP function/variable wrapper using regex
    match = re.search(r'(\{.*\}|\[.*\])', s, re.DOTALL)
    if not match:
        raise ValueError("No valid JSON object or array found")
    
    json_str = match.group(1)
    return json.loads(json_str)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_questions():
    data = request.json
    syllabus_text = data.get('syllabus', '')

    if not syllabus_text:
        return jsonify({"error": "No syllabus provided"}), 400

    prompt = f"""
    Based on the following syllabus, create 5 multiple choice questions.
    Provide them in valid JSON format with 'question', 'options', and 'answer' fields.

    Syllabus:
    {syllabus_text}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    try:
        generated_text = response.text
    except AttributeError:
        generated_text = response.candidates[0].content.parts[0].text

    # Parse the JSON string into Python objects before sending
    try:
        questions = safe_json_loads(generated_text)
        print("Generated Questions:", questions)
    except json.JSONDecodeError:
        return jsonify({"error": "Model output was not valid JSON"}), 500

    return jsonify({"questions": questions})


if __name__ == '__main__':
    app.run(debug=True)
