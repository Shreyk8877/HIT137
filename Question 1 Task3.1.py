# QUESTION 1:
# Task 3: Programming and Research
    #3.1: Using any in-built library present in Python
    #count and give the "Top 30" most common words

import csv
from collections import Counter
import re

def count_words(CSV_file):
    # Read the text file
    with open(CSV_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Normalize the text by converting it to lowercase and removing punctuation
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    return word_counts

def save_top_words_to_csv(word_counts, output_csv_path, top_n=30):
    # Get the top 'top_n' most common words
    top_words = word_counts.most_common(top_n)
    
    # Write the top words and their counts to a CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Word', 'Count'])  # Header row
        csvwriter.writerows(top_words)

if __name__ == "__main__":
    input_file = 'CSV_file.txt'  # Replace with the path to your text file
    output_csv = 'top_30_common_words.csv'
    
    word_counts = count_words(input_file)
    save_top_words_to_csv(word_counts, output_csv)
    
    print(f'Top 30 words have been saved to {output_csv}')
