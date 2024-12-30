import random

class RandomizedSet(object):

    def __init__(self):
        self.m = {} #values to indices 
        self.l = []


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.m:
            return False 
        # sets current value as key for its index in list
        self.m[val] = len(self.l)
        self.l.append(val)
        return True 

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.m:
            return False 
        
        # gets index of value to be removed
        index = self.m[val]
        # gets value of last item in list
        lastitem = self.l[-1]
        # makes our dict map last item to our 
        # removed values current index
        self.m[lastitem] = index
        temp = self.l[index]
        # makes value at our removed values index
        # to be last item in list
        self.l[index] = self.l[len(self.l) - 1]
        # sets last value in list to be our removed value
        self.l[len(self.l) - 1] = temp
        # removes from list
        self.l.pop()
        # removes from dict
        del self.m[val]

        
        return True 
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.l)