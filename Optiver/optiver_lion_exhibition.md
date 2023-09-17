Lion Exhibition

As a lion trainer, you are taking part in an international lion exhibition. During the event lions from different teams enter and exit the showroom where lion experts can inspect and score them. Lions do not enter the showroom all at once, as that would cause too much commotion. The organizers of the event are letting them in and out based on a predefined schedule. Before the show starts you get access to the schedule for your lions - but not for the others. Nevertheless, during the show, you can observe all lions getting in and out of the room.
Based on your experience, you believe that judges tend to award the biggest lions in the room with the highest scores. Before the final results are out, you want to estimate your chances of winning this competition.

Problem Statement

Complete the following functions:
• The LionCompetition class constructor that accepts lion descriptions and the private schedule of when the lions enter and exit the showroom.
The LionEntered and lionLeft functions that are called whenever a new lion enters or leaves the room.
• The getBiggestLions function that, for the current time, returns a list of our lions in the room that are at
least as big as the biggest lion from competing teams in the room. The presented list has to be sorted
alphabetically.
Function definitions
LionCompetition class constructor parameters:
• Lions-list or elements describing your lions: 
⚫ name-string representing a name of the lion
o. height-height of the lion
schedule- a private schedule of when your lions enter and leave the show room name-string representing a name of the lion
o enterTime number of minutes since the start of the show when the lion will enter the room
• exitTime-number of minutes since the start of the show when the lion will exit the room
lionEntered function parameters:
• currentTime number of minutes since the start of the show
height-height of the lion that entered the room
lionLeft function parameters.
• currentTime - number of minutes since the start of the show
height-height of the lion that left the room

Constraints
. Subsequent invocations of LionLeft and lionEntered functions are always called in order, according to the currentTime parameter.
• The schedule is strictly followed - your lions enter and exit the room exactly at specified times.
• The lion inspection (invocation of the getBiggestLions function) takes place either before or after all lions scheduled to enter or leave the room at a given minute did that - never in between.
• Lion names are unique.
• Times (currentTime, enterTime and exitTime) are always whole numbers (and multiple events can occur at the same time).
• A single lion enters the room only once during the show.

Sample Case
Sample Input For Custom Testing
definition marry 300 definition rob 250 schedule marry 10 15 start
schedule rob 13 20
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

Sample Output
0
2 marry rob
1 rob

Explanation
We have two lions:
• marry with a height of 300cm that enters the show 10 minutes after its start and exits it 15 minutes after its start.
⚫ rob with a height of 250cm that enters the show 13 minutes after its start and exits it 20 minutes after its start.
The show goes as follows:
⚫ 8 minutes after the start of the show a lion with a height of 200cm enters the room - based on the schedule it is not one of ours.
⚫ 10 minutes after the start of the show two lions enter the room: a 310cm one and a 300cm one. The second one is marry.
• We do an inspection, but unfortunately marry is not the biggest lion in the room, so we return an empty
list.
⚫ 13 minutes after the start of the show rob enters the room and the unknown 310cm lion exits it.
• We do an inspection. Both marry and rob are higher than the 200cm height lion that entered the room at the 8th minute of the show, so we return both names.
⚫ 15 minutes after the start of the show marry leaves the room.
• We do an inspection. rob is still the biggest lion in the room.
⚫ 16 and 20 minutes after the start of the show both remaining lions exit the room.


Python code
===========
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
    def __init__(self, lions: list[LionDescription], schedule: list [LionSchedule]):
        # Enter your code here
        pass

if __name__ == "__main__":
    import sys
    
    read_line = lambda: sys.stdin. readline().split()
    
    descriptions: list [LionDescription] = [] 
    lion_schedule: list [LionSchedule] = []
    
    parse = True
    while parse:
        line = read_line()
        if line[0] == 'definition': 
            name  = line [1]
            size = int(line [2])
            description = LionDescription(name, size)
            descriptions.append(description)
        elif line[0] == 'schedule':
            name = line[1]
            enter_time = int(line [2])
            exit_time = int(line [3])
            schedule_entry = LionSchedule (name, enter_time, exit_time)
            lion_schedule.append(schedule_entry)
        elif line[0] == 'start':
            parse = False
        else:
            raise Exception('invalid input')
        
    lion_competition = LionCompetition (descriptions, lion_schedule)
    parse = True
    
    while parse:
        line = read_line()
        time = int(line[0])
        if line[1] == 'enter':
            size= int(line [2])
            lion_competition. lion_entered (time, size)
        elif line[1] == 'exit':
            size = int(line [2])
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