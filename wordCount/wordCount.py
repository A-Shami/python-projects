from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Word Count App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            
            h1 {
                color: #333;
                text-align: center;
                margin-top: 20px;
            }
            
            form {
                text-align: center;
                margin-top: 20px;
            }
            
            textarea {
                width: 400px;
                height: 200px;
                padding: 10px;
                border: 1px solid #ddd;
                resize: none;
            }
            
            input[type="submit"] {
                padding: 5px 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            
            .result {
                margin-top: 20px;
                padding: 10px;
                background-color: #fff;
                border: 1px solid #ddd;
                
                            }
            
            .result p {
                margin: 5px;
                
            }
        </style>
    </head>
    <body>
        <h1>Word Count App</h1>
        <form action="/wordcount" method="post">
            <textarea name="text" rows="10" cols="50"></textarea><br>
            <input type="submit" value="Count">
        </form>
        {% if count %}
            <div class="result">
                <p>Total words: {{ count }}</p>
                <p>Text entered:</p>
                <p>{{ text }}</p>
            </div>
        {% endif %}
    </body>
    </html>
    ''')

@app.route('/wordcount', methods=['POST'])
def wordcount():
    text = request.form['text']
    word_list = text.split()
    count = len(word_list)
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Word Count App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            
            h1 {
                color: #333;
                text-align: center;
                margin-top: 20px;
            }
            
            form {
                text-align: center;
                margin-top: 20px;
            }
            
            textarea {
                width: 400px;
                height: 200px;
                padding: 10px;
                border: 1px solid #ddd;
                resize: none;
            }
            
            input[type="submit"] {
                padding: 5px 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            
            .result {
                margin-top: 20px;
                padding: 10px;
                background-color: #fff;
                border: 1px solid #ddd
                
 }
            
            .result p {
                margin: 5px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Word Count App</h1>
        <form action="/wordcount" method="post">
            <textarea name="text" rows="10" cols="50">{{ text }}</textarea><br>
            <input type="submit" value="Count">
        </form>
        <div class="result">
            <p>Total words: {{ count }}</p>
            <p>Text entered:</p>
            <p>{{ text }}</p>
        </div>
    </body>
    </html>
    ''', count=count, text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')