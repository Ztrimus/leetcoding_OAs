'''
File: millennium_q2_popular_song_order.py
Project: Coding
File Created: 1st Oct 2023 3:04 pm, Sunday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
'''

from collections import defaultdict
n = 3
m = 3
song_pre = [[0,1,2], [0,2,1], [1,2,0]]

# n = 5
# m = 4
# song_pre = [[0,1,3,2],[0,2,3,1],[1,0,3,2],[2,1,0,3],[0,3,1,2]]

# n = 4
# m = 3
# song_pre = [[2,0,1], [0,2,1], [0,1,2], [2,1,0]]
# Output = [0, 2, 1]

# def getPopularityOrder(n,m,song_pre):
#     order_dict={}
#     for user in song_pre:
#         for user_pre_song in user:
#             for song in range(m):
#                 if song not in order_dict:
#                     order_dict[song] = [0 for i in range(m)]
#                 if user_pre_song not in order_dict:
#                     order_dict[user_pre_song] = [0 for i in range(m)]
                
#                 if user.index(song) > user.index(user_pre_song) or (user.index(song) == user.index(user_pre_song) and song<user_pre_song):
#                         if song in [0,1]:
#                             pass
#                         order_dict[song][user_pre_song] -=1
#                         order_dict[user_pre_song][song] +=1

#     for key, values in order_dict.items():
#         beats_song = 0
#         for index, value in enumerate(values):
#             if index != key:
#                 if value >=0:
#                     beats_song+=1
#             order_dict[key] = beats_song
    
#     sorted_dict = sorted(order_dict.items(), key=lambda x:x[1], reverse=True)

#     return [i[0] for i in sorted_dict]

def getPopularityOrder(n, m, song_pre):
    order_dict = {}
    for user in song_pre:
        order = {song: i for i, song in enumerate(user)}
        for user_pre_song in user:
            for song in range(m):
                if song not in order_dict:
                    order_dict[song] = [0 for i in range(m)]
                if user_pre_song not in order_dict:
                    order_dict[user_pre_song] = [0 for i in range(m)]
                
                if order[song] > order[user_pre_song] or (order[song] == order[user_pre_song] and song < user_pre_song):
                    order_dict[song][user_pre_song] -= 1
                    order_dict[user_pre_song][song] += 1

    order_beats = {}
    for key, values in order_dict.items():
        beats_song = 0
        for index, value in enumerate(values):
            if index != key and value >= 0:
                beats_song += 1
        order_beats[key] = beats_song
    
    sorted_dict = sorted(order_beats.items(), key=lambda x:x[1], reverse=True)

    return [i[0] for i in sorted_dict]
    

print(getPopularityOrder(n,m,song_pre))