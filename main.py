"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra,rb = foo(x-1), foo(x-2)
        return ra + rb




def longest_run(mylist, key):
    k = 0
    runlist = []
    for i in mylist:
        if [i] ==0:
            runlist.append(0)
        elif i == key:
            runlist.append(k)
        elif i != key:
            k += 1

            runlist.append(k)
            k +=1

    x = 1
    countlist = []
    counter = 0

    for x in range (k):
        counter = 0
        for j in runlist:
            if j == x:
                counter +=1
                countlist.append(counter)

    return int(max(countlist))


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):

    if len(mylist)<= 1:
        return mylist.count(key)
    else:
        l,r = mylist[:len(mylist)//2], mylist[len(mylist)//2:]
        lrun,rrun = longest_run_recursive(l,key), longest_run_recursive(r,key)
    left_end_run = 0
    if l and l[-1] == key:
        left_end_run = 1
        i = len(l) - 2
        while i >= 0 and l[i] == key:
            left_end_run += 1
            i -= 1

    right_start_run = 0
    if r and r[0] == key:

        right_start_run = 1
        i = 1
        while i < len(r) and r[i] == key:
            right_start_run += 1
            i += 1

    if left_end_run and right_start_run:
        cross_run = left_end_run + right_start_run
    else:
        cross_run = 0
    all_runs = [lrun, rrun, cross_run]

    return max(all_runs)


test_list = [2,12,12,8,12,12,12,0,12,1]
key = 12
print(longest_run_recursive(test_list,key))


