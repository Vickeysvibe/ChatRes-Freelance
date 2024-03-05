from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

dataset = {
    "What is your name?": "My name is VIBE.",
    "What can you do?": "I can respond to your questions immediately and perform many tasks.",
    "How are you?": "I'm just a computer program, so I don't have feelings, but thank you for asking!",
    "What is the capital of France?": "The capital of France is Paris.",
    "What is the weather like today?": "I'm sorry, I cannot provide real-time information.",
    "How old are you?": "I am a program, so I don't have an age in the way humans do.",
    "What is square root of 25?": "The Square root of 25 is 5.",
    "What is the boiling point of water in Celsius?" : "The boiling point of water in Celsius is 100 degrees.",
    "How many continents are there?": "There are seven continents : Africa, Antarctica, Asia, Europe, North America, South America, and Australia.",
    "How many pounds are in a ounce?" : "There are 16 ounces in a pound."
}


# Function to find the most relevant question in the dataset
def find_most_relevant_question(user_question, dataset):
    max_score = 0
    most_relevant_question = None
    for question in dataset:
        score = similarity_score(user_question, question)
        if score > max_score:
            max_score = score
            most_relevant_question = question
    return most_relevant_question

# Function to calculate similarity score between questions
def similarity_score(str1, str2):
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split())
    return len(words1.intersection(words2))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_pdf', methods=['POST'])
def search_pdf():
    user_question = request.form['userInput']
    most_relevant_question = find_most_relevant_question(user_question, dataset)
    if user_question.lower() == "exit":
        return jsonify({'message': "Thank you"})
    elif most_relevant_question:
        bot_message = dataset.get(most_relevant_question, "Sorry, I couldn't find a relevant answer.")
        return jsonify({'message': bot_message})
    else:
        return jsonify({'message': "Sorry, I couldn't find a relevant answer."})

if __name__ == '__main__':
    app.run(debug=True)
