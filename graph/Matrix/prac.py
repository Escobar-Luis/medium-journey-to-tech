# You are given list of sessions details


# Each session is of the format <user_id, session_first_seen_time, session_last_seen_time>


# You can be asked the following question multiple times with different parameters: Given a user_id, start_time and end_time, find out how long was the user logged in, without overlaps or gaps


# Write a program to do the above assuming that all of the data can be stored on a single machine.



sessionDetails = [

    {"user": "u1", "startTime": 100, "endTime": 200},

    {"user": "u2", "startTime": 200, "endTime": 300},

    {"user": "u1", "startTime": 300, "endTime": 600}, # 200

    {"user": "u2", "startTime": 400, "endTime": 600},

    {"user": "u1", "startTime": 500, "endTime": 700}, # 100

    {"user": "u1", "startTime": 800, "endTime": 1000} # 100
    
    # {"user": "u1", "startTime": 1200, "endTime": 1400}

];


def totalLoginTime(user, queryStartTime, queryEndTime):

    # Fill in to determine how long the user was logged in between start time and end time

    # Make sure any overlapping times between sessions only counts once

    ans=0
    tmp=queryStartTime
    for session in sessionDetails:
        if session['user']==user:
            if session['endTime'] >= queryStartTime and session['startTime'] <= queryEndTime:
                x= min(session['endTime'], queryEndTime)
                y=max(session['startTime'],tmp) 
                ans += x- y
                tmp=x
    return ans
totalLoginTime("u1", 400, 900)
    


# print(totalLoginTime("u1", 400, 900)) # answer should be 400