# Problem Set 4A
# Name: Harshit Agarwal
# Collaborators:
# Time Spent: 1 hour

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    list = []
    if len(sequence) == 1:
        list = [sequence]
    else:
        for element in get_permutations(sequence[1:len(sequence)]):
            for i in range (0, len(sequence) ):
                new_word = element[0:i] + sequence[0] + element[i: len(element)]
                if new_word not in list:
                    list.append(new_word)
    return list


if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
   print len(get_permutations('harshit'))


