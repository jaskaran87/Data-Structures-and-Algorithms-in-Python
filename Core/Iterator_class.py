class Test: 
  
    # Cosntructor 
    def __init__(self, start,limit ): 
        self.limit = limit 
        self.x = start

    # Called when iteration is initialized 
    def __iter__(self):
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def next(self): 
        # Store current value ofx 
        x = self.x
        # Stop iteration if limit is reached 
        if x > self.limit:
            raise StopIteration
        # Else increment and return old value
        self.x = x + 1;
        return x

# Prints numbers from 10 to 15 
for i in Test(2,15): 
    print(i)

# Prints nothing 
print('-------')
for i in Test(5,9): 
    print(i) 