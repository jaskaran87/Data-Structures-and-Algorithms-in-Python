'''
    # Pickle module accepts any Python object and 
    # converts it into a string representation 
    # and dumps it into a file by using dump function, 
    # this process is called pickling. 
    # While the process of retrieving original Python objects 
    # from the stored string representation is called unpickling.

    # Module Interface :

    # dumps ()  This function is called to serialize an object hierarchy.
    # loads ()  This function is called to de-serialize a data stream.
    # For more control over serialization and de-serialization, Pickler or an Unpickler objects are created respectively.
'''

import pickle
#make pickle
example_dict = { 1:"1",2:"2",3:"3",}
pickle_out = open('dict.pickle', "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

#read pickle
pickle_in = open('dict.pickle', "rb")
read_dict = pickle.load(pickle_in)
print(read_dict)