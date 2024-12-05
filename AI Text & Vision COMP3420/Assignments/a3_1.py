import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('universal_tagset')
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import collections
import pandas as pd

# Task 1 (5 marks)
def topN_pos(csv_file_path, N):
    """
    Extracts the top N most frequent nouns from the 'qtext' column of the CSV file,
    ensuring that only unique questions are considered.

    Args:
    csv_file_path (str): Path to the CSV file.
    N (int): Number of top nouns to return.

    Returns:
    list: A list of tuples with the top N nouns and their frequencies.
    """

    # Step 1: Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Step 2: Remove duplicate questions by considering only unique values in the 'qtext' column
    df_unique = df.drop_duplicates(subset=['qtext'])

    # Step 3: Concatenate all the unique questions into one big text string
    all_text = ' '.join(df_unique['qtext'].values)

    # Step 4: Tokenize the concatenated text into individual sentences
    sentences = sent_tokenize(all_text)

    # Step 5: Tokenize each sentence into individual words
    word_tokens = [word_tokenize(sentence) for sentence in sentences]

    # Step 6: Tag each word with its part of speech using NLTK's pos_tag_sents for multiple sentences
    pos_tags = nltk.pos_tag_sents(word_tokens, tagset='universal')

    # Step 7: Filter out only the nouns (POS tag 'NOUN') from the tagged words
    nouns = [word for sentence in pos_tags for word, pos in sentence if pos == 'NOUN']

    # Step 8: Count the frequency of each noun
    noun_freq = collections.Counter(nouns)

    # Step 9: Return the top N most frequent nouns in descending order
    return noun_freq.most_common(N)

# Task 2 (5 marks)
def topN_2grams(csv_file_path, N):
    """
    Returns two lists of the top N most frequent 2-grams: one with lowercase tokens
    and one with original (non-lowercased) tokens, along with their normalized frequency.

    Args:
    csv_file_path (str): Path to the CSV file.
    N (int): Number of top 2-grams to return.

    Returns:
    tuple: Two lists of tuples containing the top N 2-grams and their normalized frequency,
           one for lowercase and one for original tokens, each rounded to 4 decimal places.

    """

    # Step 1: Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Step 2: Drop duplicate questions based on the 'qtext' column to keep only unique ones
    df_unique = df.drop_duplicates(subset=['qtext'])

    # Step 3: Concatenate all unique questions into one large text block for analysis
    all_text = ' '.join(df_unique['qtext'].values)

    # Step 4: Tokenize the entire text block into sentences
    sentences = sent_tokenize(all_text)

    # Step 5: Tokenize each sentence into words (preserving original casing)
    word_tokens_original = [word_tokenize(sentence) for sentence in sentences]

    # Step 6: Tokenize each sentence into words (lowercased)
    word_tokens_lower = [word_tokenize(sentence.lower()) for sentence in sentences]

    # Step 7: Generate 2-grams manually from original tokens
    bigrams_original = []
    for sentence in word_tokens_original:
        for i in range(len(sentence) - 1):
            bigram = (sentence[i], sentence[i + 1])
            bigrams_original.append(bigram)

    # Step 8: Generate 2-grams manually from lowercased tokens
    bigrams_lower = []
    for sentence in word_tokens_lower:
        for i in range(len(sentence) - 1):
            bigram = (sentence[i], sentence[i + 1])
            bigrams_lower.append(bigram)

    # Step 9: Count the frequency of each bigram
    bigram_freq_original = collections.Counter(bigrams_original)
    bigram_freq_lower = collections.Counter(bigrams_lower)

    # Step 10: Calculate the total number of bigrams for normalization
    total_bigrams_original = sum(bigram_freq_original.values())
    total_bigrams_lower = sum(bigram_freq_lower.values())

    # Step 11: Normalize the frequency of each bigram by dividing by the total, rounding to 4 decimal places
    normalized_bigrams_original = [(bigram, round(count / total_bigrams_original, 4)) for bigram, count in bigram_freq_original.most_common(N)]
    normalized_bigrams_lower = [(bigram, round(count / total_bigrams_lower, 4)) for bigram, count in bigram_freq_lower.most_common(N)]

    # Step 12: Return both the top N bigrams with original and lowercase tokens
    return normalized_bigrams_lower, normalized_bigrams_original





# Task 3 (5 marks)
def sim_tfidf(csv_file_path):
    """
    Calculate the proportion of questions that can be accurately answered using the tf-idf feature.
    
    Args:
    csv_file_path (str): Path to the CSV file.
    
    Returns:
    float: Proportion of questions accurately answered using tf-idf (rounded to 2 decimal places).
    """
    
    # Step 1: Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Step 2: Remove duplicate rows to ensure unique question-answer-label triplets
    df_unique = df.drop_duplicates()
    
    # Step 3: Get all unique questions and answers
    unique_questions = df_unique['qtext'].unique()
    unique_answers = df_unique['atext'].unique()
    
    # Step 4: Create a TfidfVectorizer with stop words removed
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Step 5: Fit the TF-IDF vectorizer on all unique questions and answers
    all_text = np.concatenate((unique_questions, unique_answers))
    vectorizer.fit(all_text)
    
    # Step 6: Group the DataFrame by 'qtext' to get candidate answers for each question
    grouped = df_unique.groupby('qtext')
    
    correct_count = 0  # Initialize count of correct answers
    num_questions = len(grouped)  # Total number of unique questions
    
    # Step 7: Iterate over each question and its group of candidate answers
    for question, group in grouped:
        # Extract candidate answers and their labels for this question
        candidate_answers = group['atext'].values
        labels = group['label'].values
        
        # Transform the question and candidate answers into TF-IDF vectors
        question_tfidf = vectorizer.transform([question])
        answers_tfidf = vectorizer.transform(candidate_answers)
        
        # Compute cosine similarities between the question and each candidate answer
        # Using matrix multiplication for efficiency
        similarity_scores = question_tfidf.dot(answers_tfidf.T).toarray().flatten()
        
        # Find the index of the candidate answer with the highest similarity
        top_answer_idx = np.argmax(similarity_scores)
        
        # Check if the label of the top candidate answer is 1 (correct)
        if labels[top_answer_idx] == 1:
            correct_count += 1  # Increment the correct count
    
    # Step 8: Calculate the proportion of questions accurately answered
    proportion = correct_count / num_questions
    
    # Step 9: Round the proportion to 2 decimal places and return
    return round(proportion, 2)



# DO NOT MODIFY THE CODE BELOW
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    print(topN_pos('train.csv', 3))
    print("------------------------")
    print(topN_2grams('train.csv', 3))
    print("------------------------")
    print(sim_tfidf('train.csv'))


"""
Use of AI Generators in this Assignment

Throughout the development of this assignment, I utilized AI tools to assist in resolving various challenges and ensuring the accuracy of my work.
Specifically, I used OpenAI's ChatGPT and Microsoft's Copilot to address issues such as syntax errors, runtime errors, and conceptual questions regarding the functionality of my code.

For example, I encountered syntax and logic errors while implementing certain tasks, and in response, I used AI tools to troubleshoot. I would input error messages from my terminal or paste the entire code snippet into GPT, asking for fixes.
In addition, I sought explanations for unclear outputs and feedback to guide my corrections. Prompts like "fix this error" or "explain step-by-step what this code does" helped me understand the issues more clearly and identify areas requiring improvement.

The comments in my code were also enhanced by GPT, which assisted in breaking down and explaining each step in a structured manner. 
his provided clarity for understanding how each part of the code worked.

It is essential to highlight that the AI tools primarily supported my debugging and comprehension process, similar to how one might use a search engine or community forums for help.
The conceptual understanding and code implementation remain my own work. Modifications based on AI-generated suggestions included fixing syntax issues, adjusting incorrect logic, resolving indentation problems, and ensuring accurate output alignment.

In summary:
- What part of your code is based on the output of such tools: Comments explaining step-by-step processes were generated by AI, and AI-assisted troubleshooting was used to resolve syntax and logic errors.
- What tools you used: OpenAI's ChatGPT and Microsoft's Copilot.
- What prompts you used to generate the code or text: I sent error messages, pasted the code, and requested fixes or explanations. I also asked the AI to review the code and provide feedback on issues such as indentation, logic, or incorrect outputs.
- What modifications you made to the generated code or text: Based on the AI’s feedback, I fixed syntax errors, corrected outputs, and resolved indentation issues, among other code adjustments.

It is s important to note that, although AI tools were used to assist with debugging and understanding, all code design, model development, and conceptual solutions presented are my own.

"""
