from TikTokApi import TikTokApi
import json
import csv 
# `msToken` is an optional parameter, pass it once requests are not working
api = TikTokApi()

'''
for video in api.trending.videos(get_all=True):
    print(video.as_dict)

user_data = api.user(username='therock').info()
print(user_data, "end of user_data\n")


user = api.user(username='Coopkhans')
for video in user.liked():
    print("hashtags: ", video.hashtags)

video_bytes = api.video(id='7041997751718137094').bytes()

# Saving The Video
with open('saved_video.mp4', 'wb') as output:
    output.write(video_bytes)


with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
'''
users = []
search = api.search.users('tiktok', count=50)

for s in search:
    users.append(s)


#tik_id = api.user('tiktok')['userInfo']['user']['id']
#suggested = api.getSuggestedUsersbyID(count=30, startingId=tik_id)

# LAST WORKING VERSION
'''
data = {}
for u in users:
    user = u
    liked = u.liked()
    data[user.username] = liked

print("length: ", len(data))
print(type(data))
x = list(data.keys())[0]

print(data[x])

for l in data[x]:
    print(l)
'''

# User data is a list of two objects: user object, followed by an iterator of liked videos.
# ex. [ [user, liked videos], [user, liked videos], [user, liked videos], ... ]

user_details = ['user', 'liked_videos']
f = open('users.csv' , 'w', encoding="utf-8") 
write_users = csv.writer(f) 
write_users.writerow(user_details) 

video_details = ["video"]
f_2 = open('videos.csv', 'w')
write_videos = csv.writer(f_2) 
write_videos.writerow(video_details) 


user_data = []
u_counter = 0
for u in users:
    try:
        user = u
        liked = u.liked() # casting generator (iterator type) to list
        #if (len(liked) > 0 and liked[0] != "User's likes are most likely private"):
        #for l in liked:
        #    if (l != "User's likes are most likely private"):
        l = []
        
        for vid in liked:
            l.append(vid)
        if (len(l) == 0):
            continue
        u_counter +=1
        user_data.append([user.as_dict ,l])
        write_users.writerow([user.as_dict ,l])
    finally:
        #print(str(u_counter) + " first it is what it is")
        pass
#write_users.writerows(user_data)
print("length: ", len(user_data))
print(type(user_data))

videos_data = []

#for l in user_data[0][1]:
#    print(l)
vid_counter = 0
for user in user_data:
    liked = user[1]
    if (len(liked) == 0):
        continue
    for video in liked:
        try:
            if(video.id.isnumeric()):
                vid = api.video(id=video.id)
                write_videos.writerow(vid.id)
                videos_data.append(vid.id)
                vid_counter += 1

            # Bytes of the TikTok video
            video_data = vid.bytes()
            outFileName="C:\\Users\\u1369704\\Downloads\\TikTok-Api-5.1.2\\TikTok-Api-5.1.2\\examples\\vidoes\\" +video.id + ".mp4"
            outFile=open(outFileName, "wb")
            outFile.write(video_data)
            outFile.close()
            #with open( "videos\\" +video.id + ".mp4", "wb") as out_file:
            #    out_file.write(video_data)
        finally:
            print(str(vid_counter) + ' Second wellll it isss what it issss')


f.close()
f_2.close()