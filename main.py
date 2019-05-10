#Beginning of HW5

#Grab 20 text instances in 20 .txt files

class Document:

    unique_words = {}

    def tokenize(text):
        text.strip(";\".,/()[]!@#$%^&*()_")
        words = text.upper().split()
        print(words)
        for word in words:
            if word not in unique_words:
                new_word = {word:1}
                unique_words.update(new_word)
            else:
                unique_words[word] += 1
        print(unique_words)

def save_dictionary(dict,pathname):
    write_file = open("dictionary.txt","w")
    for pair in dict:
        write_file.write(pair + "\t")


#produce TF and IDF stats
def vectorize(path):
    DF_dictionary = {}
    r = open(path,"r")
    words = r.readlines()
    save_dictionary(DF_dictionary,out)
    for word in words:
        for checks in DF_dictionary:
            if word not in DF_dictionary:
                DF_dictionary.update({word:1})
            else if word == checks:
                DF_dictionary[word] += 1
    save_dictionary(DF_dictionary,"DF_Dictionary.txt")

        
