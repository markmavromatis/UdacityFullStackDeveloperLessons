import urllib

FILE_NAME="movie_quotes.txt"
def read_text():
    f = open(FILE_NAME, 'r')
#    print f
    file_text = f.read()
    print file_text
    f.close()
    check_profanity(file_text)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()
