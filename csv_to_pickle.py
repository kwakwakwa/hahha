import csv
import pickle


class mod:
    def __init__(list):
        list.Comment = Comment
        list.Polarity = Polarity


    def __str__(list):
        return "{}{}".format(list.Comment, list.Polarity)

    def __iter__(list):
        return iter([list.mod])


a_list = []

with open("mod.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        a_list.append([   row[0], row[1] ]) 

with open('2.pickle', 'wb') as output_file:
    pickle.dump(a_list, output_file)
    output_file.close()
    
with open('2.pickle', 'rb') as file:
    a_dict1 =pickle.load(file)

print(a_dict1)