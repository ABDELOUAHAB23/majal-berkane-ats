from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/candidates')
def get_candidates():
    # Logic to fetch candidates from your database
    candidates = [{"name": "John Doe", "position": "Developer"}]  # This should be replaced with real data fetching logic
    return jsonify(candidates)

if __name__ == '__main__':
    app.run(port=8506)
