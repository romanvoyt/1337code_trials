from typing import List
import math
import random

def isValid(s: str) -> bool:
    """
    Check if the given string s is a valid sequence of parentheses.
    """
    stack = []

    def isopen(par: str):
        """
        Check if the given character is an opening parenthesis.
        """
        if par in '([{':
            return True
        else:
            return False

    def match(open_id, close_id):
        """
        Check if the given pair of parentheses match each other.
        """
        opens = '([{'
        closes = ')]}'

        return opens.index(open_id) == closes.index(close_id)

    # Iterate through each character in the string
    for br in s:
        if isopen(br):
            # If it's an opening parenthesis, push to stack
            stack.append(br)
        else:
            # If it's a closing parenthesis, check for matching
            if not stack:
                return False  # No matching opening parenthesis
            top = stack.pop()
            if not match(top, br):
                return False  # Parentheses do not match

    # Return True if no unmatched parentheses remain
    return not stack

class Solution:
    def generateParenthesis(self, n: int) -> List[int]:
        """
        Generate all combinations of n pairs of valid parentheses.
        """
        length = n * 2  # Each valid combination will have 2n characters

        # Calculate the number of possible combinations using binomial coefficient
        combs = math.factorial(length) / (math.factorial(n) * math.factorial(length - n))

        sets = set()  # Use a set to store unique combinations
        counter = 0
        while counter != combs:
            # Generate a random combination of parentheses
            str = ''.join(random.choices('()', k=length))
            print(str)
            if isValid(str):
                # If the generated combination is valid, add to the set
                sets.add(''.join(str))
                counter += 1
        
        # Return the set of valid combinations as a list
        return list(sets)
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
