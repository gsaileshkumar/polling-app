from flask import Flask

app = Flask(__name__)

@app.route('/polls', methods=['GET'])
def get_all_polls():
  return 'get all polls'

@app.route('/poll', methods=['POST'])
def create_poll():
  return 'create poll'

@app.route('/poll/<id>', methods=['GET'])
def get_poll(id):
  return 'get poll for id {}'.format(id)

@app.route('/vote', methods=['POST'])
def vote_poll():
  return 'vote a poll'

if __name__ == '__main__':
    app.run()