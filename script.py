import re

def do_regex(file_contents):
    # we check the type of `file_contents`
    if type(file_contents) != str:
        # returns error message if `file_contents` is not a string
        return 'file_contents is not a string. Exiting...'

    # we compiled the regular expression in `ending_at`
    ending_at = re.compile(r'\w*at\b')

    # all words which match the above pattern are stored in `regexed`
    regexed = re.findall(ending_at, file_contents)

    # the filter function is provided with the above `regexed` variable
    # we have also provided a lambda function which returns True if the length of the word is greater than or equal to 3. False otherwise. The filter function returns an iterator and we'll need to convert it to a list.
    filtered = filter(lambda x: len(x) > 3, regexed)

    # we use list comprehension to return the list made from the above iterator.
    return [i for i in filtered]

def main():
    
    with open('pg25990.txt', 'r') as f:
        # `contents` has all the text inside `pg25990.txt`
        contents = f.read()
    # we called the `do_regex` function with `contents`
    print(do_regex(contents))

main()
