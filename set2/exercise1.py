"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?'] # I think this is creating a set with all of these words

for word in some_words: # I think this one is for making all of these words individually
    print(word) # Print these words one by one

for x in some_words: # I think this is same as before
    print(x) # Print it out

print(some_words) # Print the final result

if len(some_words) > 3: # Set a if means if it does, it will runs. In here it means if there is more than 3 words in some_words, it will run
    print('some_words contains more than 3 words') # Print it out

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
