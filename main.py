#Beginning of HW5

#Grab 20 text instances in 20 .txt files

class Document:

    unique_words = {}

    def tokenize(text):
        words = text.split(" ",".")
        for word in words:
            if word not in unique_words:
                insert = {word:1}
                unique_words.update(insert)
            else:
                unique_words.update([word:1+=])

def save_dictionary(dict,pathname):
    write_file = open("dictionary.txt","w")
    for pair in dict:
        write_file.write(pair + "\t")


#produce TF and IDF stats
def vectorize(path):

