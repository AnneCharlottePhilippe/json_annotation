# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:12:56 2021

@author: Administrateur
"""

import json
import cv2
import csv 
import numpy as np


##############
path_csv = "C:/Users/Administrateur/Documents/CODES/json_annot/csv_simpliCREVETTES.csv"
out_pref_annot = "C:/Users/Administrateur/Documents/CODES/json_annot/annotation_crevettes/"
path_img = "C:/Users/Administrateur/Documents/DATA/mission_crevettes/"
##############

out_pref_annot = out_pref_annot + "an_"
S = 200     # thumnail size


# to save arrays in json
class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)



csv_file = open(path_csv,"r")
csv_reader = csv.reader(csv_file, delimiter=',')    #DictReader (if column names)
temp = 0
for row in csv_reader:
    print("doing annot " + str(temp))
    img_name = path_img + row[0]
    x = np.floor(float(row[2]))
    y = np.floor(float(row[1]))
    # read reference image
    img = cv2.imread(img_name)
    x_img, y_img, z_img = img.shape
    # thumbnail generation
    l_x = range(max(0,abs(int(x)-S)),min(int(x)+S,int(x_img)))
    l_y = range(max(0,abs(int(y)-S)),min(int(y)+S,int(y_img)))
    vign = np.zeros((len(l_x),len(l_y),3), dtype = np.uint8)
    for i in range(len(l_x)):
        for j in range(len(l_y)):
            vign[i, j, :] = img[l_x[i],l_y[j],:]
    ## visualisation et sauvegarde 
    #plt.figure(figsize=(len(l_x),len(l_y)))
    #plt.imshow(vign,  interpolation='nearest')
    #plt.title("annotations de " + row[0], y=1.02, fontsize=12)
    #plt.imsave(path+"imagette_"+str(temp)+".png",vign)

            
    # json 
    annotation = {"vign":vign, 
              "annot_data":{
                  "center": np.array([int(x),int(y)]),
                  "level":2},
              "taxinomy_data":{
                  "current_name":row[3],
                  "url":"http..",
                  "worms":"https://"},
              "reference_data":{
                  "ref_img":row[0],
                  "localisation":""
                  }
              }
    
    temp = temp + 1
    
    # save json
    dumped = json.dumps(annotation, cls=NumpyEncoder)
    with open(out_pref_annot + str(temp) + ".json", "w") as file:
        json.dump(dumped, file)
    
   
    
csv_file.close()
