# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:35:08 2021

@author: Administrateur

Script qui crée le fichier csv simplifié à partir des sorties Biigle-Ifremer
"""

import os.path
import csv 

##############
path_csv = "C:/Users/Administrateur/Documents/CODES/json_annot/10-pl07.csv"
path_csv_new = "C:/Users/Administrateur/Documents/CODES/json_annot/csv_simpliPL07.csv"
path_img = "Y:/images/Kanadeep/PL07_final/"
##############


null_string = 'NULL'       # to check null object


csv_file = open(path_csv,"r")
csv_reader = csv.DictReader(csv_file, delimiter=',')
csv_out = open(path_csv_new, 'w', newline='')
csv_writer = csv.writer(csv_out, delimiter=',')
for row in csv_reader:
    # fields of interest for the simplified csv
    img_filename = row['filename'] 
    pos = row['points']
    pos = pos.split(',')
    posx = pos[0][1:]   # pour enlever "[" du début du split
    posy = pos[1]
    current_name = row['label_name']
    if os.path.exists(path_img+img_filename) and posx!=null_string and posy!=null_string :
        csv_writer.writerow([img_filename,posx,posy,current_name])
    
csv_file.close()
csv_out.close()



