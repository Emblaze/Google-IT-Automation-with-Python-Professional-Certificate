
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~“—'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    
    """Initialising variables"""
    wordDict = {}
    words = []
    # """Checking length of file_contents"""
    # print("File contents len=", len(file_contents))
    def word_cleaner(word):
        """Helper function to clean words from non-alpha characters"""
        #cleaned_word = "".join(char for char in word if char.isalpha() or char not in punctuations)
        #print("Word to inspect: " + word)
        cleaned_word = ""
        for char in word:
            # print(char)
            if char.isalpha() or char not in punctuations:
                cleaned_word += "".join(char)
        #     elif char in punctuations:
        #         print(char + " is in punctuations, ignoring")
        #     elif char.isalpha() == False:
        #         print(char + " is not alpha")
        # print("Returning: " + cleaned_word.lower())
        return cleaned_word.lower()

    """Splitting the text in words with punctation and other characters"""
    file_contents_splitted = file_contents.split(" ")
    # print(file_contents_splitted, type(file_contents_splitted))
    
    """Checking words for non-alphabetical characters"""
    #print("Parsing raw text and linting non-alpha chars")
    for word in file_contents_splitted:
        #print("Calling word_cleaner with word: " + word)
        word_cleaner(word)
        if word not in uninteresting_words:
            words.append(word_cleaner(word))
        
    # print(str(len(words)) + " words added to words list" )

    """Building dictionnary from the word list"""
    # print("Building dictionnary")
    for cleaned_word in words:
        if cleaned_word not in wordDict.keys():
            wordDict[cleaned_word] = 1
        else:
            wordDict[cleaned_word] += 1
    print(wordDict)
    return wordDict

    #wordcloud
    # cloud = wordcloud.WordCloud()
    # cloud.generate_from_frequencies()
    # return cloud.to_array()

fichier = open("The_Prince.txt", newline=None, encoding="utf8")
file_contents = fichier.read()
fichier.close()
#print(file_contents)
calculate_frequencies(file_contents)
