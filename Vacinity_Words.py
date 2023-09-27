import re

def find_similar_words(text, target_word, max_distance=5):
    """
    Find occurrences of similar words within a specified maximum distance
    of a target word in the given text.

    Args:
    - text (str): The input text.
    - target_word (str): The word to search for.
    - max_distance (int): The maximum allowed distance between words.

    Returns:
    - List of tuples: Each tuple contains the similar word, its position, and the count of occurrences.
    """
    # Split the text into words
    words = text.split()

    # Prepare a regular expression pattern to match similar words
    pattern = re.compile(rf"(\w+)?(\s*\w+\s*){{0,{max_distance}}}\b{re.escape(target_word)}\b(\s*\w+\s*){{0,{max_distance}}}(\w+)?", re.IGNORECASE)

    # Search for matches in the text
    matches = re.finditer(pattern, text)

    # Initialize a dictionary to store similar words and their counts
    similar_words = {}

    # Extract and store the similar words and their positions
    for match in matches:
        similar_word = match.group(0).strip()
        if similar_word in similar_words:
            similar_words[similar_word] += 1
        else:
            similar_words[similar_word] = 1

    # Convert the dictionary to a list of tuples
    similar_word_list = [(word, count) for word, count in similar_words.items()]

    return similar_word_list

# Example usage:
text = " India and Pakistan, two neighboring South Asian nations, share a long and intricate history marked by both cooperation and conflict. Following the partition of British India in 1947, India emerged as a secular state, while Pakistan was founded as a Muslim-majority country with East Pakistan (now Bangladesh) and West Pakistan (present-day Pakistan). Tensions primarily revolve around the disputed region of Kashmir, which has been the source of multiple wars and conflicts. Diplomatic relations between the two countries have often been strained due to territorial disputes, nuclear capabilities, and ideological differences. Despite these challenges, cultural and economic ties persist, and international mediation efforts continue to seek a path toward lasting peace. The relationship remains complex, with a mix of cooperation, conflict, and competition, making it a critical and delicate matter in the region."
target_word = "Pakistan"
max_distance = 3

similar_words = find_similar_words(text, target_word, max_distance)
for similar_word, count in similar_words:
    print(f"Similar word: '{similar_word}' (Count: {count})")
