#Beginning of HW5

#Grab 20 text instances in 20 .txt files

class Document:
    @staticmethod
    def tokenize(text):
        unique_words = {}
        text.strip(";\".,/()[]!@#$%^&*()_`~:")
        words = text.upper().split()
        #print(words)
        for word in words:
            if word not in unique_words:
                new_word = {word:1}
                unique_words.update(new_word)
            else:
                unique_words[word] += 1
        return(unique_words)


def save_dictionary(dict,pathname):
    write_file = open(pathname,"w")
    for pair in dict:
        write_file.write(pair + "\t"+ str(dict.get(pair)) + "\n")

#produce TF and IDF stats
def vectorize(pathname):
    DF_dictionary = {}
    doc = Document()
    r = open(pathname,"r")
    words = r.read()
    DF_dictionary.update(doc.tokenize(words))
    save_dictionary(DF_dictionary,"tf_DOCID.txt")
    for word in DF_dictionary:
        if word not in DF_dictionary:
            DF_dictionary.update({word:1})
        elif word is DF_dictionary:
            DF_dictionary[word] += 1
    save_dictionary(DF_dictionary,"df.txt")


vectorize("input_text.txt")
print('''Done.
Check both text documents
to make sure that the correct
results are going into the files.''')