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
        tfidf = {}
        for word in doc.split():
            tfidf[word] = term_frequencies[i][word] * idf[word]
        tfidf_scores.append(tfidf)

    return tfidf_scores

def rank_pages(tfidf_scores, keyword):
    
    scores = {}
    for i, tfidf in enumerate(tfidf_scores):
        if keyword in tfidf:
            scores[i] = tfidf[keyword]

    
    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs


with open('input_file.txt', 'r') as file:
    content = file.read()
pages = content.split('\n\n')


tfidf_scores = calculate_tf_idf(pages)


keyword = input("Enter a keyword: ")


ranked_pages = rank_pages(tfidf_scores, keyword)


print("Ranked Pages:")
for page, score in ranked_pages:
    print(f"Page {page + 1}: {score}")
