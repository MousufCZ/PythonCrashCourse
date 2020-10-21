def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
        
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        pass

    else:
        # Count the approx number of words in a file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
#count_words(filename)
for filename in filenames:
    count_words(filename)

