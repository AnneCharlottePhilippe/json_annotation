# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:36:13 2021

@author: Administrateur

Script qui crée le fichier csv simplifié à partir des sorties DSS
"""
import os.path
import csv 

##############
path_csv = "C:/Users/Administrateur/Documents/DATA/mission_crevettes.csv"
path_csv_new = "C:/Users/Administrateur/Documents/CODES/json_annot/csv_simpliCREVETTES.csv"
path_img = "C:/Users/Administrateur/Documents/DATA/mission_crevettes/"
##############


null_string = 'NULL'       # to check null object


csv_file = open(path_csv,"r")
csv_reader = csv.DictReader(csv_file, delimiter=',')
csv_out = open(path_csv_new, 'w', newline='')
csv_writer = csv.writer(csv_out, delimiter=',')
for row in csv_reader:
    # fields of interest for the simplified csv
    img_filename = row['name']  
    posx = row['pos1x']
    posy = row['pos1y']
    current_name = row['name_fr']
    if os.path.exists(path_img+img_filename) and posx!=null_string and posy!=null_string :
        csv_writer.writerow([img_filename,posx,posy,current_name])
    
csv_file.close()
csv_out.close()




