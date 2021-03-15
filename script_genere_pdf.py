# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:00:46 2021

@author: Administrateur
"""


import json
import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.backends.backend_pdf import PdfPages


##############
rep_annot = "C:/Users/Administrateur/Documents/CODES/json_annot/annotation_crevettes/"
out_file = rep_annot + "rapport_annotations.pdf"
##############


pref_annot = "an_"
annotCounter = len(glob.glob1(rep_annot,"*.json"))          # compte le nombre d'annotations json dans le repertoire
img_temp = rep_annot + "vignette_temp.png" 



with PdfPages(out_file) as pdf: 
    for an in range(1,annotCounter+1):
        print(an)
        json_dump_file = rep_annot + pref_annot + str(an) + ".json"
        # load dumped json
        with open(json_dump_file, 'r') as f:
            annot_json = json.load(f)
            json_load = json.loads(annot_json)
            # data to write
            vign = np.asarray(json_load["vign"])
            ref_img = json_load["reference_data"]["ref_img"]
            current_name = json_load["taxinomy_data"]["current_name"]
            # thumbnail
            plt.figure(figsize=(3, 3))
            if len(vign)>0:    
                plt.imshow(vign)
            pdf.attach_note("image de référence: " + ref_img)  # you can add a pdf note to
            plt.title(current_name)
            #plt.text(1, 1,  "image de référence: " + ref_img, ha = 'center', va = 'bottom', fontsize = 8)  
            plt.axis('off')
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()
    
    
