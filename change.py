import piexif
from PIL import Image
import json
import os
import time,datetime
import random
IMAGE_PATH="./img"
def get_random_time(begin_time,end_time):
    return random.randint(begin_time,end_time)

def get_rand_true_false():
   return random.randint(0,1) == 1


image_list = os.listdir(IMAGE_PATH)
data_obj = json.load(open("./config.json"));
start_time =int(time.mktime(time.strptime(data_obj['begin_date'],"%Y-%m-%d")))
end_time =int(time.mktime(time.strptime(data_obj['end_date'],"%Y-%m-%d")))+86400
time_st = start_time
for image in image_list:
    last_time_stamp=None
    local_time = time.strftime("%Y-%m-%d",time.localtime(time_st))
    if get_rand_true_false():
        start_no_rest_time = local_time+" "+data_obj['time_line_start'];
        start_no_rest_stamp = int(time.mktime(time.strptime(start_no_rest_time,"%Y-%m-%d %H:%M:%S")))
        end_no_rest_time = local_time + " "+data_obj['rest_time_begin']
        end_no_rest_stamp =int(time.mktime(time.strptime(end_no_rest_time,"%Y-%m-%d %H:%M:%S")))
        last_time_stamp = random.randint(start_no_rest_stamp,end_no_rest_stamp);
    else:
        start_aft_rest_time = local_time+" "+data_obj['rest_time_end'];
        start_aft_rest_stamp = int(time.mktime(time.strptime(start_aft_rest_time,"%Y-%m-%d %H:%M:%S")))
        end_aft_rest_time = local_time + " "+data_obj['time_line_end']
        end_aft_rest_stamp = int(time.mktime(time.strptime(end_aft_rest_time,"%Y-%m-%d %H:%M:%S")))
        last_time_stamp = random.randint(start_aft_rest_stamp,end_aft_rest_stamp)
    data_link = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(last_time_stamp))
    data_image_time = time.strftime("%Y:%m:%d %H:%M:%S",time.localtime(last_time_stamp))

    print(data_image_time)
    print(data_link)
    img = Image.open("./img/"+image)
    exif = piexif.load(img.info['exif'])
    exif['Exif'][36867]=data_image_time.encode()
    exif['Exif'][36868]=data_image_time.encode()
    img.save('res/'+data_link+'.jpg',exif=piexif.dump(exif))
    time_st = time_st+86400
    if time_st >= end_time:
        time_st = start_time
    
    
