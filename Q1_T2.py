
# Question 1
# Task 3: Programming and Research
    # 3.2: Using the ‘Auto Tokenizer’ function in the ‘Transformers’ library,
    # write a ‘function’ to count unique tokens in the text (.txt) and give the ‘Top 30’ words.

import warnings
from transformers import AutoTokenizer
from collections import Counter
import csv

# Ignore warnings related to clean_up_tokenization_spaces
warnings.filterwarnings("ignore", category=FutureWarning, message=".*clean_up_tokenization_spaces*.")

def count_unique_tokens(text_file, model_name="dmis-lab/biobert-v1.1", max_length=512, chunk_size=1000):
    # Use BioBERT Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize a Counter to count unique tokens
    unique_tokens = Counter()

    # Open the text file and read it in chunks to save memory
    with open(text_file, 'r', encoding='utf-8') as file:
        while True:
            # Read a chunk of lines
            lines = file.readlines(chunk_size)
            if not lines:
                break  # End of file

            # Join lines into a single chunk of text
            text_chunk = ''.join(lines)

            # Tokenize the chunk with truncation enabled
            tokens = tokenizer.tokenize(text_chunk, truncation=True, max_length=max_length)

            # Update the Counter with the token occurrences
            unique_tokens.update(tokens)

    # Get the 30 most common tokens
    top_30_tokens = unique_tokens.most_common(30)

    # Write the results to a CSV file
    output_file = r'top_30_tokens.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Token', 'Count'])
        # Write the 30 most common tokens and their counts
        writer.writerows(top_30_tokens)

    print(f"Top 30 tokens and counts saved to: {output_file}")

# Input file
input_text_file = r'CSV_file.txt'

# Call the function to count tokens and save the result
count_unique_tokens(input_text_file)
