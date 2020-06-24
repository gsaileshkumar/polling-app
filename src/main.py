from flask import Flask, request

app = Flask(__name__)

polls=[]

@app.route('/polls', methods=['GET'])
def get_all_polls():
  return polls

@app.route('/poll', methods=['POST'])
def create_poll():
  return request.get_json()

@app.route('/poll/<id>', methods=['GET'])
def get_poll(id):
  return polls[id]

@app.route('/vote', methods=['POST'])
def vote_poll():
  return request.get_json()

if __name__ == '__main__':
    app.run()