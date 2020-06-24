from flask import Flask

app = Flask(__name__)

@app.route('/polls', methods=['GET'])
def get_all_polls():
  return 'get all polls'

if __name__ == '__main__':
    app.run()