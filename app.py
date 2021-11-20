from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

url = 'https://ai-mentalhealth-bot.azurewebsites.net/qnamaker/knowledgebases/c47db293-13b8-4143-a272-9ffa1473cfd5/generateAnswer'
end_point = 'c786c561-4636-4597-bb00-a23b3d010054'

headers = {
    'Authorization': 'EndpointKey ' + str(end_point).strip(),
    'Content-type': 'application/json',
}


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/ask/<text>")
def ask(text):
    data = """{'question':'""" + text + """'}"""
    response = requests.post(
        str(url).strip(),
        headers=headers, data=data)
    information = json.loads(response.text)
    return information['answers'][0]['answer']
