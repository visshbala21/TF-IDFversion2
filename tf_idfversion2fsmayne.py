import math
from collections import Counter

def calculate_tf_idf(documents):
    term_frequencies = []
    for doc in documents:
        word_counts = Counter(doc.split())
        total_words = len(doc.split())
        tf = {word: count / total_words for word, count in word_counts.items()}
        term_frequencies.append(tf)

    document_count = len(documents)
    idf = {}
    for doc in documents:
        words = set(doc.split())
        for word in words:
            if word in idf:
                idf[word] += 1
            else:
                idf[word] = 1

    idf = {word: math.log(document_count / freq) for word, freq in idf.items()}

    tfidf_scores = []
    for i, doc in enumerate(documents):
        tfidf = sum(term_frequencies[i][word] * idf[word] for word in doc.split())
        tfidf_scores.append(tfidf)

    return tfidf_scores

def rank_pages(tfidf_scores):
    sorted_docs = sorted(enumerate(tfidf_scores), key=lambda x: x[1], reverse=True)
    return sorted_docs

# Read input from a file
with open('input_file.txt', 'r') as file:
    content = file.read()
    pages = content.split('\n\n')

# Calculate TF-IDF scores for the pages
tfidf_scores = calculate_tf_idf(pages)

# Rank the pages based on the TF-IDF scores
ranked_pages = rank_pages(tfidf_scores)

# Print the ranked pages
print("Ranked Pages:")
for page, score in ranked_pages:
    print(f"Page {page + 1}: {score}")
