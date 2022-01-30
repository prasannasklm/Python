'''Create a list comprehension by pairing elements in given two lists
    INPUT
        words: list containing the words
        counts: list containing the frequencies of words
    OUTPUT
        combine: list containing the word,count tuple
    Example:
        input:
            words = ["A","B","C","D"]
            counts = [1,2,3,4]
        output:
            [["A",1],["B",2],["C",3],["D",4]]

    Note: Replace the None with output in return statement.'''
words=['a','b','c','d']
counts=[1,2,4,5]
nl=[[words[i],counts[i]] for i in range(len(words))]
print(nl)
