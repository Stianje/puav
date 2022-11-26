import os


Pedestrian_y, Skateboarder_y, Cart_y, Car_y, Bus_y, Biker_y = 0, 0, 0, 0, 0, 0

Pedestrian_a, Skateboarder_a, Cart_a, Car_a, Bus_a, Biker_a = 0, 0, 0, 0, 0, 0

id_List_yolo = [1]

id_List_annotations = [1]



#open textfile 
with open('labels.txt', 'r') as f:
    #read every line and extract the first number
    for line in f:
        id = int(line.split(":")[0])
        if id not in id_List_yolo:
            id_List_yolo.append(id)
            remove_ID = line.split(":")[1]
            retrive_Name = remove_ID.split(",")[0]

            if retrive_Name == "Pedestrian":
                Pedestrian_y += 1
            elif retrive_Name == "Skateboarder":
                Skateboarder_y += 1
            elif retrive_Name == "Cart":
                Cart_y += 1
            elif retrive_Name == "Car":
                Car_y += 1
            elif retrive_Name == "Bus":
                Bus_y += 1
            elif retrive_Name == "Biker":
                Biker_y += 1

print("Pedestrian: ", Pedestrian_y, "Skateboarder:", Skateboarder_y, "Cart:", Cart_y, "Car:", Car_y, "Bus:", Bus_y, "Biker:", Biker_y)



with open('annotations.txt', 'r') as f_a:

    for line_a in f_a:
        id_a = int(line_a.split(" ")[0])
        if id_a not in id_List_annotations:
            id_List_annotations.append(id_a)

            retrive_name_a = line_a.split(" ")[9].strip().replace('"', '')

            if retrive_name_a == "Pedestrian":
                Pedestrian_a += 1
            elif retrive_name_a == "Skateboarder":
                Skateboarder_a += 1
            elif retrive_name_a == "Cart":
                Cart_a += 1
            elif retrive_name_a == "Car":
                Car_a += 1
            elif retrive_name_a == "Bus":
                Bus_a += 1
            elif retrive_name_a == "Biker":
                Biker_a += 1

print("Pedestrian:", Pedestrian_a, "Skateboarder:", Skateboarder_a, "Cart:", Cart_a, "Car:", Car_a, "Bus:", Bus_a, "Biker:", Biker_a)




