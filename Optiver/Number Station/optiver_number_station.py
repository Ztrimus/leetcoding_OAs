# Author: Saurabh Zinjad
# https://leetcode.com/discuss/interview-question/4004051/Online-Assessment-for-Optiver

import sys
popped_element = 0

queue = []

def ProcessSample(seq_id, char):
    addCharOnIndex(seq_id, char)

    if char == '-':
        onMessageComplete()
        

def onMessageComplete():
    global queue
    global popped_element

    mesg = ''
    is_any_place_empty = False

    queue.pop(0)
    popped_element+=1

    while queue[0] != '-':
        if queue[0] == '':
            is_any_place_empty = True
        else:
            if not is_any_place_empty:
                mesg += queue[0]
        
        queue.pop(0)
        popped_element+=1
    
    if mesg != '' and not is_any_place_empty:
        print(f"\n\nComplete Message: {mesg}")
    

def addCharOnIndex(relative_seq_id, char):
    global queue
    global popped_element

    seq_id = relative_seq_id - popped_element

    if seq_id > (len(queue)-1 if len(queue) >= 0 else 0):
        while seq_id > len(queue):
            queue.append('')
        queue.append(char)
    else:
        if seq_id > 0:
            queue[seq_id] = char

for i in sys.stdin:
    if len(i) > 0:
        i_split = i.split()
        if len(i_split) == 2:
            seq_id, char = i_split
            ProcessSample(int(seq_id), char)