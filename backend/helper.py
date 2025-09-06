
import re


def extract_yt_term(command):
    # Try to match 'play <song> on youtube'
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        return match.group(1)
    # Try to match 'play <song>'
    pattern2 = r'play\s+(.*)'
    match2 = re.search(pattern2, command, re.IGNORECASE)
    if match2:
        return match2.group(1)
    return None


def remove_words(input_string, words_to_remove): 
    words = input_string.split()
 
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
 
    result_string = ' '.join(filtered_words)

    return result_string

