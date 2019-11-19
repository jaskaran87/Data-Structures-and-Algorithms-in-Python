import memory_profiler as mem_profile

import random
import time

names = ['Kiran','King','John','Corey']
majors = ['Math','Comps','Science']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    results = []
    for i in  range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(majors)
                  }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(majors)
                  }
        yield person

# t1 = time.clock()
# people = people_list(100000)
# t2 = time.clock()

# Memory (Before): [12.203125]Mb
# Memory (After): [44.5703125]Mb
# Start time: 0.073347 
# End time: 0.241673

#  -----------------------------------------------------------------

t1 = time.clock()
people = people_generator(100000)
t2 = time.clock()

# Memory (Before): [12.27734375]Mb
# Memory (After): [12.27734375]Mb
# Start time: 0.07458 
# End time: 0.074584



print ( 'Memory (After): {}Mb'.format(mem_profile.memory_usage()))
print ('Start time: {} '.format(t1))
print ('End time: {}'.format(t2))