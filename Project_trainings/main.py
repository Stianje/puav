import cv2
import glob
import os
#0 213 1038 241 1072 10000 1 0 0 "Biker"
agent = ["Bicyclist", "Pedestrian", "Skateboarder", "Cart", "Car", "Bus", "Biker"]
path = "C://Users//Stian//ikt213g22h//assignments//solutions//projectv2//data//annotations_fixed"

video_name = "quad3"

def findDiffernce(xmin, xmax):
    return xmax - xmin

def annotation(name):
    file_path = "data/videos/"+ name +".mov" # change to your own video path
    vid = cv2.VideoCapture(file_path)
    height_picture = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width_picture = vid.get(cv2.CAP_PROP_FRAME_WIDTH)


    num_lines = sum(1 for line in open('data/annotations/%s.txt' %name))
    with open('data/annotations/%s.txt' %name, 'r') as file:
        for lines in file:
            first_line = file.readline()
            first_line.strip()
            first_line = first_line.split(" ")
            if first_line[6] == "0" and first_line[7] == "0":
                width = findDiffernce(int(first_line[1]), int(first_line[3])) / width_picture
                height = findDiffernce(int(first_line[2]), int(first_line[4])) / height_picture

                center_x = ((findDiffernce(int(first_line[1]), int(first_line[3])) / 2) + int(first_line[1])) / width_picture
                center_y = ((findDiffernce(int(first_line[2]), int(first_line[4])) / 2) + int(first_line[2])) / height_picture

                agent_id = first_line[9][1:-2]

                if agent_id in agent:
                    agent_id_index = agent.index(agent_id)

                new_string = str(agent_id_index) + " " + str(center_x) + " " + str(center_y) + " " + str(width) + " " + str(height)

                with open('data/annotations_fixed/%s%s.txt' % (name, first_line[5]), 'a') as file2:
                    print(first_line[5])
                    file2.write(new_string + "\n")
                    file2.close()

def video_to_frames(name):
    vidcap = cv2.VideoCapture('data/videos/%s.mov' %name)
    success, image = vidcap.read()
    count = 0

    list = []

    for (root, dirs, file) in os.walk(path):
        for f in file:
            if '.txt' in f:
                list.append(f)
    print(list)
    while success:
        print(name + str(count) + ".txt")
        if name + str(count) + ".txt" in list:
            cv2.imwrite('data/annotations_fixed/%s%d.jpg' % (name, count), image)  # save frame as JPEG file
        success, image = vidcap.read()
        count += 1


annotation(video_name)
video_to_frames(video_name)