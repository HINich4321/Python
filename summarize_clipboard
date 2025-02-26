from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import pyperclip

def main():
    clipboard_content = pyperclip.paste()

    speech = ''.join(clipboard_content)
    speech = speech.replace(')mowing', 'knowing')
    speech = re.sub('\\s+', ' ', speech)
    speech_edit = re.sub('[^a-zA-Z]', ' ', speech)
    speech_edit = re.sub('\\s+', ' ', speech_edit)

    while True:
        max_words = input("Enter max words per sentence for summary: ")
        num_sents = input("Enter number of sentences for summary: ")
        if max_words.isdigit() and num_sents.isdigit():
            break
        else:
            print("\nInput must be in whole numbers.\n")

    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentences(speech, word_freq, max_words)

    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSummary:")
    for i in summary:
        print(i[0])

def remove_stop_words(speed_edit):
    stop_words = set(stopwords.words('english'))
    speed_edit_no_stop = ''
    for word in nltk.word_tokenize(speed_edit):
        if word.lower() not in stop_words:
            speed_edit_no_stop += word + ' '
    return speed_edit_no_stop

def get_word_freq(speech_edit_no_stop):
    word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
    return word_freq

def score_sentences(speech, word_freq, max_words):
    sent_scores = dict()
    sentences = nltk.sent_tokenize(speech)
    for sent in sentences:
        sent_scores[sent] = 0
        words = nltk.word_tokenize(sent.lower())
        sent_word_count = len(words)
        if sent_word_count <= int(max_words):
            for word in words:
                if word in word_freq.keys():
                    sent_scores[sent] += word_freq[word]
            sent_scores[sent] = sent_scores[sent] / sent_word_count
    return sent_scores

if __name__ == '__main__':
    main()
