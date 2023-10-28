import streamlit as st
import random
import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

related_words = ['computer', 'mathematical', 'mathematics', 'math', 'physics', 'quantum physics', 'programming']

adjectives = []
for syn in wordnet.all_synsets(wordnet.ADJ):
    for word in related_words:
        if word in syn.definition():
            for lemma in syn.lemmas():
                if 4 <= len(lemma.name()) <= 8:
                    adjectives.append(lemma.name())

nouns = []
for syn in wordnet.all_synsets(wordnet.NOUN):
    for lemma in syn.lemmas():
        if 4 <= len(lemma.name()) < 6:
            nouns.append(lemma.name())

def generate_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective.capitalize()}_{noun.capitalize()}"

def main():
    st.title('Name Generator')
    st.markdown(
        """
        <style>
        .stButton button {
            background-color: pink;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button('Generate Docker Username'):
        docker_name = generate_name()
        st.write(f'Your name is: {docker_name}')

if __name__ == '__main__':
    main()

