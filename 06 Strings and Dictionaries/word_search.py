def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    index = []
    
    for i, doc in enumerate(doc_list):
        clean = [word.strip(".,").lower() for word in doc.split()]
        if keyword.lower() in clean:
            index.append(i)

    return index
