from dataclasses import dataclass
from collections import defaultdict
from heapq import heappush, heappop

@dataclass
class LionDescription:
    name: str
    height: int

@dataclass
class LionSchedule:
    name: str
    enter_time: int
    exit_time: int

class LionCompetition:
    def __init__(self, lions: list[LionDescription], schedule: list[LionSchedule]):
        # self.sizeMap = dict(name: height for name,height in lions}
        self.sizeMap = dict((lion.name, lion.height) for lion in lions)
        self.mine = set()
        
        self.ignoreMap = defaultdict(int)

        self.others = []
        
        self.othersLeft = defaultdict(int) 

        # schedule sorted by time of enter/leaving
        self.schedule = []
        for event in schedule:
            name, enter, exit = event.name, event.enter_time, event.exit_time
            self.schedule.append((name, enter, "enter"))
            self.schedule.append((name, exit, "exit"))
            self.ignoreMap[(self.sizeMap[name], enter, "enter")] += 1
            self.ignoreMap[(self.sizeMap[name], exit, "exit")] += 1

        self.schedule.sort(key = lambda t: t[1])
        # schedule index
        self.si = 0

    def lion_entered(self, current_time: int, height: int):
        key = (height, current_time, "enter")
        if self.ignoreMap[key] > 0:
            self.ignoreMap[key] -= 1
        else:
            heappush(self.others, -height)

    def lion_left(self, current_time: int, height: int):
        key = (height, current_time, "exit")
        if self.ignoreMap[key] > 0:
            self.ignoreMap[key] -= 1
        else:
            self.othersLeft[height] += 1

    def get_biggest_lions(self):
        print('-'*50, time)
        while self.si < len(self.schedule) and self.schedule[self.si][1] <= time:
            name, _, type = self.schedule[self.si]
            if type == "enter":
                self.mine.add((name, self.sizeMap[name]))
            else:
                self.mine.remove((name, self.sizeMap[name]))
            self.si += 1

        # flush the heap of other elephants to find the 
        # one who is the tallest and still present
        while self.others:
            cur = abs(self.others[0])
            if self.othersLeft[cur] > 0:
                heappop(self.others)
                self.othersLeft[cur] -= 1
            else:
                break

        tallestRival = abs(self.others[0])
        candidates = [name for name,height in self.mine if height >= tallestRival]
        candidates.sort()
        return candidates

if __name__ == "__main__":
    import sys
    
    read_line = lambda: sys.stdin.readline().split()
    
    descriptions: list[LionDescription] = [] 
    lion_schedule: list[LionSchedule] = []
    
    parse = True
    while parse:
        line = read_line()
        if line[0] == 'definition': 
            name  = line[1]
            size = int(line[2])
            description = LionDescription(name, size)
            descriptions.append(description)
        elif line[0] == 'schedule':
            name = line[1]
            enter_time = int(line[2])
            exit_time = int(line[3])
            schedule_entry = LionSchedule(name, enter_time, exit_time)
            lion_schedule.append(schedule_entry)
        elif line[0] == 'start':
            parse = False
        else:
            raise Exception('invalid input')
        
    lion_competition = LionCompetition(descriptions, lion_schedule)
    parse = True
    
    while parse:
        line = read_line()
        time = int(line[0])
        if line[1] == 'enter':
            size= int(line[2])
            lion_competition.lion_entered(time, size)
        elif line[1] == 'exit':
            size = int(line[2])
            lion_competition.lion_left(time, size)
        elif line[1] == 'inspect': 
            biggest_lions = lion_competition.get_biggest_lions()
            print(len(biggest_lions), end='')
            for lion in biggest_lions:
                print(" "+ lion, end='')
            print()
        elif line[1] == 'end':
            parse = False
        else:
            raise Exception('invalid input')

'''
definition marry 300 
definition rob 250 
schedule marry 10 15
schedule rob 13 20
start
8 enter 200
10 enter 310
10 enter 300
11 inspect
13 enter 250
13 exit 310
13 inspect
15 exit 300
16 inspect
16 exit 200
20 exit 250
21 end
'''