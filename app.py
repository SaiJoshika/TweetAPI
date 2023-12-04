import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load tweet data from the JSON file
with open("100tweets.json", "r", encoding="utf-8") as file:
    tweets_data = json.load(file)

# Step 2: Write a GET endpoint at the base URL
@app.route('/')
def hello_world():
    return 'Hello World!'

# Step 3: Write a new GET endpoint that returns ALL tweets
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    return jsonify(tweets_data)

# Step 4: Modify the above endpoint to filter tweets using a query parameter
@app.route('/tweets_filtered', methods=['GET'])
def get_filtered_tweets():
    query_param = request.args.get('filter_param')
    # Implement filtering logic using query_param
    filtered_tweets = ...
    return jsonify(filtered_tweets)

# Step 5: Write a new GET endpoint for a specific tweet by ID
@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet_by_id(tweet_id):
    try:
        tweet = tweets_data[tweet_id]
        return jsonify(tweet)
    except IndexError:
        return jsonify({"error": "Tweet not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Step 6: Use Try/Except to handle errors and return appropriate HTTP status codes

if __name__ == '__main__':
    # Step 6: Run your API in the command line
    app.run(debug=True)



