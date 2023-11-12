import streamlit as st

def classify_entrepreneur(answers):
    counts = {
        'Builder': answers.count('a'),
        'Opportunist': answers.count('b'),
        'Visionary': answers.count('c'),
        'Thought Leader': answers.count('d'),
        'Empire Builder': answers.count('e'),
        'Socialpreneur': answers.count('f'),
    }
    result = max(counts, key=counts.get)
    return result

def main():
    st.title("Entrepreneur Mindset Classifier")

    language_options = ['English', 'Thai', 'Chinese']
    selected_language = st.selectbox("Select Language", language_options)

    questions = {
        'English': [
            ("When considering a new business idea, what is most important to you?",
             {'a': 'Solving a problem or fulfilling a need',
              'b': 'Being your own boss',
              'c': 'Making a lot of money',
              'd': 'Building something great',
              'e': 'Creating jobs for others',
              'f': 'Disrupting an industry'}),
            ("When considering a new business idea, what is most important to you?",
             {'a': 'Solving a problem or fulfilling a need',
              'b': 'Being your own boss',
              'c': 'Making a lot of money',
              'd': 'Building something great',
              'e': 'Creating jobs for others',
              'f': 'Disrupting an industry'}),
        ],
        'Thai': [
            # Thai questions translation goes here
        ],
        'Chinese': [
            # Chinese questions translation goes here
        ]
    }

    answers = []

    for i, (question, options) in enumerate(questions[selected_language]):
        selected_option = st.radio(f"{i + 1}. {question}", list(options.keys()), format_func=lambda x: options[x])
        answers.append(selected_option)

    if st.button("Classify"):
        result = classify_entrepreneur(answers)
        st.success(f"You have a {result} mindset!")

if __name__ == "__main__":
    main()