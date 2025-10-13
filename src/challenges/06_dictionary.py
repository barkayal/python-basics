import pickle


def save_dict(dict_to_save, filename):
    file_path = '../../f.output/'+filename
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(filename):
    file_path = '../../f.output/'+filename
    with open(file_path, 'rb') as file:
        return pickle.load(file)


test_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(test_dict, 'test_dict.pickle')
recovered = load_dict('test_dict.pickle')
print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}