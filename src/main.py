from flask import Flask, request, jsonify

app = Flask(__name__)

polls=[]

@app.route('/polls', methods=['GET'])
def get_all_polls():
  return jsonify(polls)

@app.route('/poll', methods=['POST'])
def create_poll():
  polls.append(request.get_json())
  return jsonify(request.get_json())

@app.route('/poll/<id>', methods=['GET'])
def get_poll(id):
  return jsonify(polls[id])

@app.route('/vote', methods=['POST'])
def vote_poll():
  return jsonify(request.get_json())

if __name__ == '__main__':
    app.run()