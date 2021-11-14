#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Split of Francois d'Haène at UTMB 2021
input_data = [
              {"idpt":'0',"kmt":'0,0 km',"kmp":'NaN km',"dt":'0 m',"dp":'NaN m',"p":"","a":'1 037 m',"n":"Chamonix","lon":'6.86875',"lat":'45.9237',"meet":'1',"hp":'Ve. 17:01',"tc":'00:00:00',"clt":'-',"vit":'-km/h'},
              {"idpt":'1',"kmt":'13,8 km',"kmp":'13,8 km',"dt":'838 m',"dp":'838 m',"p":"Chamonix","a":'1 741 m',"n":"Le Delevret","lon":'6.75661',"lat":'45.8792',"meet":'',"hp":'Ve. 18:19',"tc":'01:18:05',"clt":'4',"vit":'10,63km/h'},
              {"idpt":'2',"kmt":'21,6 km',"kmp":'7,8 km',"dt":'926 m',"dp":'88 m',"p":"Le Delevret","a":'829 m',"n":"Saint-Gervais","lon":'6.71135',"lat":'45.8928',"meet":'1',"hp":'Ve. 18:54',"tc":'01:52:49',"clt":'6',"vit":'13,40km/h'},
              {"idpt":'3',"kmt":'31,8 km',"kmp":'10,2 km',"dt":'1 500 m',"dp":'574 m',"p":"Saint-Gervais","a":'1 160 m',"n":"Les Contamines Montjoie","lon":'6.7261',"lat":'45.8221',"meet":'1',"hp":'Ve. 19:52',"tc":'02:50:35',"clt":'4',"vit":'10,59km/h'},
              {"idpt":'4',"kmt":'40,1 km',"kmp":'8,3 km',"dt":'2 067 m',"dp":'567 m',"p":"Les Contamines Montjoie","a":'1 714 m',"n":"La Balme","lon":'6.7107',"lat":'45.7575',"meet":'',"hp":'Ve. 20:48',"tc":'03:47:18',"clt":'2',"vit":'8,81km/h'},
              {"idpt":'5',"kmt":'45,7 km',"kmp":'5,6 km',"dt":'2 859 m',"dp":'792 m',"p":"La Balme","a":'2 456 m',"n":"Refuge de la Croix du Bonhomme","lon":'6.71752',"lat":'45.7221',"meet":'',"hp":'Ve. 21:46',"tc":'04:44:20',"clt":'2',"vit":'5,90km/h'},
              {"idpt":'6',"kmt":'50,8 km',"kmp":'5,0 km',"dt":'2 859 m',"dp":'0 m',"p":"Refuge de la Croix du Bonhomme","a":'1 551 m',"n":"Les Chapieux","lon":'6.73353',"lat":'45.6956',"meet":'1',"hp":'Ve. 22:09',"tc":'05:07:25',"clt":'1',"vit":'13,05km/h'},
              {"idpt":'7',"kmt":'61,4 km',"kmp":'10,6 km',"dt":'3 913 m',"dp":'1 054 m',"p":"Les Chapieux","a":'2 516 m',"n":"Col de la Seigne","lon":'6.80695',"lat":'45.7514',"meet":'',"hp":'Ve. 23:34',"tc":'06:32:44',"clt":'2',"vit":'7,48km/h'},
              {"idpt":'9',"kmt":'68,5 km',"kmp":'7,2 km',"dt":'4 170 m',"dp":'257 m',"p":"Col de la Seigne","a":'1 979 m',"n":"Lac Combal","lon":'6.85574',"lat":'45.7706',"meet":'1',"hp":'Sa. 00:24',"tc":'07:22:26',"clt":'1',"vit":'8,63km/h'},
              {"idpt":'10',"kmt":'72,5 km',"kmp":'4,0 km',"dt":'4 631 m',"dp":'461 m',"p":"Lac Combal","a":'2 434 m',"n":"Arête du Mont-Favre","lon":'6.89007',"lat":'45.7723',"meet":'',"hp":'Sa. 01:02',"tc":'08:01:12',"clt":'2',"vit":'6,18km/h'},
              {"idpt":'11',"kmt":'77,0 km',"kmp":'4,5 km',"dt":'4 648 m',"dp":'17 m',"p":"Arête du Mont-Favre","a":'1 976 m',"n":"Col Checrouit Maison Vieille","lon":'6.93107',"lat":'45.7907',"meet":'1',"hp":'Sa. 01:26',"tc":'08:25:17',"clt":'1',"vit":'11,19km/h'},
              {"idpt":'12',"kmt":'81,4 km',"kmp":'4,4 km',"dt":'4 671 m',"dp":'23 m',"p":"Col Checrouit Maison Vieille","a":'1 192 m',"n":"Courmayeur - Mountain Sport Center Entrée","lon":'6.96486',"lat":'45.7943',"meet":'1',"hp":'Sa. 01:53',"tc":'08:51:32',"clt":'1',"vit":'10,13km/h'},
              {"idpt":'13',"kmt":'81,4 km',"kmp":'0,0 km',"dt":'4 671 m',"dp":'0 m',"p":"Courmayeur - Mountain Sport Center Entrée","a":'1 192 m',"n":"Courmayeur - Mountain Sport Center Sortie","lon":'6.96486',"lat":'45.7943',"meet":'1',"hp":'Sa. 01:58',"tc":'08:56:40',"clt":'1',"vit":'-km/h'},
              {"idpt":'16',"kmt":'86,4 km',"kmp":'4,9 km',"dt":'5 476 m',"dp":'805 m',"p":"Courmayeur - Mountain Sport Center Sortie","a":'1 981 m',"n":"Refuge Bertone","lon":'6.97857',"lat":'45.8091',"meet":'',"hp":'Sa. 02:55',"tc":'09:53:33',"clt":'1',"vit":'5,19km/h'},
              {"idpt":'18',"kmt":'98,9 km',"kmp":'12,5 km',"dt":'5 874 m',"dp":'398 m',"p":"Refuge Bertone","a":'1 800 m',"n":"Arnouvaz","lon":'7.05387',"lat":'45.8713',"meet":'1',"hp":'Sa. 04:27',"tc":'11:25:49',"clt":'1',"vit":'8,14km/h'},
              {"idpt":'20',"kmt":'103,5 km',"kmp":'4,6 km',"dt":'6 619 m',"dp":'745 m',"p":"Arnouvaz","a":'2 529 m',"n":"Grand Col Ferret","lon":'7.07794',"lat":'45.889',"meet":'',"hp":'Sa. 05:20',"tc":'12:19:14',"clt":'1',"vit":'5,20km/h'},
              {"idpt":'23',"kmt":'113,4 km',"kmp":'9,9 km',"dt":'6 683 m',"dp":'64 m',"p":"Grand Col Ferret","a":'1 599 m',"n":"La Fouly","lon":'7.0984',"lat":'45.9358',"meet":'1',"hp":'Sa. 06:21<br/>Sa. 06:21',"tc":'13:19:51',"clt":'1',"vit":'9,82km/h'},
              {"idpt":'26',"kmt":'127,0 km',"kmp":'13,6 km',"dt":'7 230 m',"dp":'547 m',"p":"La Fouly","a":'1 470 m',"n":"Champex-Lac","lon":'7.12229',"lat":'46.0256',"meet":'1',"hp":'Sa. 07:46<br/>Sa. 07:49',"tc":'14:44:56',"clt":'1',"vit":'9,62km/h'},
              {"idpt":'28',"kmt":'138,5 km',"kmp":'11,5 km',"dt":'8 154 m',"dp":'924 m',"p":"Champex-Lac","a":'1 886 m',"n":"La Giète","lon":'7.03407',"lat":'46.0558',"meet":'',"hp":'Sa. 09:21',"tc":'16:20:15',"clt":'1',"vit":'7,52km/h'},
              {"idpt":'30',"kmt":'143,5 km',"kmp":'4,9 km',"dt":'8 286 m',"dp":'132 m',"p":"La Giète","a":'1 305 m',"n":"Trient","lon":'6.99493',"lat":'46.0556',"meet":'1',"hp":'Sa. 09:51<br/>Sa. 09:54',"tc":'16:49:41',"clt":'1',"vit":'10,05km/h'},
              {"idpt":'31',"kmt":'146,8 km',"kmp":'3,3 km',"dt":'8 945 m',"dp":'659 m',"p":"Trient","a":'1 931 m',"n":"Les Tseppes","lon":'6.97961',"lat":'46.0475',"meet":'',"hp":'Sa. 10:34',"tc":'17:32:22',"clt":'1',"vit":'5,00km/h'},
              {"idpt":'32',"kmt":'154,0 km',"kmp":'7,2 km',"dt":'9 100 m',"dp":'155 m',"p":"Les Tseppes","a":'1 292 m',"n":"Vallorcine Entrée","lon":'6.93221',"lat":'46.0323',"meet":'1',"hp":'Sa. 11:22',"tc":'18:21:11',"clt":'1',"vit":'8,90km/h'},
              {"idpt":'33',"kmt":'154,0 km',"kmp":'0,0 km',"dt":'9 100 m',"dp":'0 m',"p":"Vallorcine Entrée","a":'1 292 m',"n":"Vallorcine Sortie","lon":'6.93221',"lat":'46.0323',"meet":'1',"hp":'Sa. 11:24',"tc":'18:22:34',"clt":'1',"vit":'-km/h'},
              {"idpt":'43',"kmt":'161,7 km',"kmp":'7,7 km',"dt":'9 971 m',"dp":'871 m',"p":"Vallorcine Sortie","a":'2 118 m',"n":"La Tête aux vents","lon":'6.90654',"lat":'45.9824',"meet":'',"hp":'Sa. 12:41',"tc":'19:39:48',"clt":'1',"vit":'5,96km/h'},
              {"idpt":'44',"kmt":'165,2 km',"kmp":'3,5 km',"dt":'10 047 m',"dp":'76 m',"p":"La Tête aux vents","a":'1 882 m',"n":"La Flégère","lon":'6.88674',"lat":'45.9607',"meet":'1',"hp":'Sa. 13:06',"tc":'20:05:18',"clt":'1',"vit":'8,21km/h'},
              {"idpt":'142',"kmt":'172,1 km',"kmp":'7,0 km',"dt":'10 055 m',"dp":'8 m',"p":"La Flégère","a":'1 037 m',"n":"Chamonix","lon":'6.86875',"lat":'45.9237',"meet":'1',"hp":'Sa. 13:47',"tc":'20:45:59',"clt":'1',"vit":'10,28km/h'}
          ]

# Split of Aurélien Dunand Pallaz at UTMB 2021
input_data2 = [
              {"idpt":'0',"kmt":'0,0 km',"kmp":'NaN km',"dt":'0 m',"dp":'NaN m',"p":"","a":'1 037 m',"n":"Chamonix","lon":'6.86875',"lat":'45.9237',"meet":'1',"hp":'Ve. 17:01',"tc":'00:00:00',"clt":'-',"vit":'-km/h'},
              {"idpt":'1',"kmt":'13,8 km',"kmp":'13,8 km',"dt":'838 m',"dp":'838 m',"p":"Chamonix","a":'1 741 m',"n":"Le Delevret","lon":'6.75661',"lat":'45.8792',"meet":'',"hp":'Ve. 18:19',"tc":'01:17:59',"clt":'2',"vit":'10,64km/h'},
              {"idpt":'2',"kmt":'21,6 km',"kmp":'7,8 km',"dt":'926 m',"dp":'88 m',"p":"Le Delevret","a":'829 m',"n":"Saint-Gervais","lon":'6.71135',"lat":'45.8928',"meet":'1',"hp":'Ve. 18:54',"tc":'01:53:03',"clt":'14',"vit":'13,28km/h'},
              {"idpt":'3',"kmt":'31,8 km',"kmp":'10,2 km',"dt":'1 500 m',"dp":'574 m',"p":"Saint-Gervais","a":'1 160 m',"n":"Les Contamines Montjoie","lon":'6.7261',"lat":'45.8221',"meet":'1',"hp":'Ve. 19:53',"tc":'02:52:12',"clt":'9',"vit":'10,35km/h'},
              {"idpt":'4',"kmt":'40,1 km',"kmp":'8,3 km',"dt":'2 067 m',"dp":'567 m',"p":"Les Contamines Montjoie","a":'1 714 m',"n":"La Balme","lon":'6.7107',"lat":'45.7575',"meet":'',"hp":'Ve. 20:49',"tc":'03:47:28',"clt":'7',"vit":'9,04km/h'},
              {"idpt":'5',"kmt":'45,7 km',"kmp":'5,6 km',"dt":'2 859 m',"dp":'792 m',"p":"La Balme","a":'2 456 m',"n":"Refuge de la Croix du Bonhomme","lon":'6.71752',"lat":'45.7221',"meet":'',"hp":'Ve. 21:47',"tc":'04:45:34',"clt":'5',"vit":'5,79km/h'},
              {"idpt":'6',"kmt":'50,8 km',"kmp":'5,0 km',"dt":'2 859 m',"dp":'0 m',"p":"Refuge de la Croix du Bonhomme","a":'1 551 m',"n":"Les Chapieux","lon":'6.73353',"lat":'45.6956',"meet":'1',"hp":'Ve. 22:12',"tc":'05:10:20',"clt":'4',"vit":'12,16km/h'},
              {"idpt":'7',"kmt":'61,4 km',"kmp":'10,6 km',"dt":'3 913 m',"dp":'1 054 m',"p":"Les Chapieux","a":'2 516 m',"n":"Col de la Seigne","lon":'6.80695',"lat":'45.7514',"meet":'',"hp":'Ve. 23:42',"tc":'06:40:22',"clt":'5',"vit":'7,09km/h'},
              {"idpt":'9',"kmt":'68,5 km',"kmp":'7,2 km',"dt":'4 170 m',"dp":'257 m',"p":"Col de la Seigne","a":'1 979 m',"n":"Lac Combal","lon":'6.85574',"lat":'45.7706',"meet":'1',"hp":'Sa. 00:32',"tc":'07:31:09',"clt":'4',"vit":'8,45km/h'},
              {"idpt":'10',"kmt":'72,5 km',"kmp":'4,0 km',"dt":'4 631 m',"dp":'461 m',"p":"Lac Combal","a":'2 434 m',"n":"Arête du Mont-Favre","lon":'6.89007',"lat":'45.7723',"meet":'',"hp":'Sa. 01:13',"tc":'08:11:42',"clt":'4',"vit":'5,90km/h'},
              {"idpt":'11',"kmt":'77,0 km',"kmp":'4,5 km',"dt":'4 648 m',"dp":'17 m',"p":"Arête du Mont-Favre","a":'1 976 m',"n":"Col Checrouit Maison Vieille","lon":'6.93107',"lat":'45.7907',"meet":'1',"hp":'Sa. 01:38',"tc":'08:36:32',"clt":'4',"vit":'10,85km/h'},
              {"idpt":'12',"kmt":'81,4 km',"kmp":'4,4 km',"dt":'4 671 m',"dp":'23 m',"p":"Col Checrouit Maison Vieille","a":'1 192 m',"n":"Courmayeur - Mountain Sport Center Entrée","lon":'6.96486',"lat":'45.7943',"meet":'1',"hp":'Sa. 02:04',"tc":'09:02:48',"clt":'4',"vit":'10,12km/h'},
              {"idpt":'13',"kmt":'81,4 km',"kmp":'0,0 km',"dt":'4 671 m',"dp":'0 m',"p":"Courmayeur - Mountain Sport Center Entrée","a":'1 192 m',"n":"Courmayeur - Mountain Sport Center Sortie","lon":'6.96486',"lat":'45.7943',"meet":'1',"hp":'Sa. 02:09',"tc":'09:07:21',"clt":'5',"vit":'-km/h'},
              {"idpt":'16',"kmt":'86,4 km',"kmp":'4,9 km',"dt":'5 476 m',"dp":'805 m',"p":"Courmayeur - Mountain Sport Center Sortie","a":'1 981 m',"n":"Refuge Bertone","lon":'6.97857',"lat":'45.8091',"meet":'',"hp":'Sa. 03:06',"tc":'10:04:26',"clt":'3',"vit":'5,17km/h'},
              {"idpt":'18',"kmt":'98,9 km',"kmp":'12,5 km',"dt":'5 874 m',"dp":'398 m',"p":"Refuge Bertone","a":'1 800 m',"n":"Arnouvaz","lon":'7.05387',"lat":'45.8713',"meet":'1',"hp":'Sa. 04:33',"tc":'11:31:31',"clt":'2',"vit":'8,62km/h'},
              {"idpt":'20',"kmt":'103,5 km',"kmp":'4,6 km',"dt":'6 619 m',"dp":'745 m',"p":"Arnouvaz","a":'2 529 m',"n":"Grand Col Ferret","lon":'7.07794',"lat":'45.889',"meet":'',"hp":'Sa. 05:30',"tc":'12:29:01',"clt":'2',"vit":'4,83km/h'},
              {"idpt":'23',"kmt":'113,4 km',"kmp":'9,9 km',"dt":'6 683 m',"dp":'64 m',"p":"Grand Col Ferret","a":'1 599 m',"n":"La Fouly","lon":'7.0984',"lat":'45.9358',"meet":'1',"hp":'Sa. 06:29<br/>Sa. 06:31',"tc":'13:27:45',"clt":'3',"vit":'10,13km/h'},
              {"idpt":'26',"kmt":'127,0 km',"kmp":'13,6 km',"dt":'7 230 m',"dp":'547 m',"p":"La Fouly","a":'1 470 m',"n":"Champex-Lac","lon":'7.12229',"lat":'46.0256',"meet":'1',"hp":'Sa. 07:58<br/>Sa. 08:02',"tc":'14:56:44',"clt":'2',"vit":'9,37km/h'},
              {"idpt":'28',"kmt":'138,5 km',"kmp":'11,5 km',"dt":'8 154 m',"dp":'924 m',"p":"Champex-Lac","a":'1 886 m',"n":"La Giète","lon":'7.03407',"lat":'46.0558',"meet":'',"hp":'Sa. 09:37',"tc":'16:36:10',"clt":'2',"vit":'7,25km/h'},
              {"idpt":'30',"kmt":'143,5 km',"kmp":'4,9 km',"dt":'8 286 m',"dp":'132 m',"p":"La Giète","a":'1 305 m',"n":"Trient","lon":'6.99493',"lat":'46.0556',"meet":'1',"hp":'Sa. 10:05<br/>Sa. 10:11',"tc":'17:03:28',"clt":'2',"vit":'10,84km/h'},
              {"idpt":'31',"kmt":'146,8 km',"kmp":'3,3 km',"dt":'8 945 m',"dp":'659 m',"p":"Trient","a":'1 931 m',"n":"Les Tseppes","lon":'6.97961',"lat":'46.0475',"meet":'',"hp":'Sa. 10:51',"tc":'17:49:40',"clt":'2',"vit":'4,89km/h'},
              {"idpt":'32',"kmt":'154,0 km',"kmp":'7,2 km',"dt":'9 100 m',"dp":'155 m',"p":"Les Tseppes","a":'1 292 m',"n":"Vallorcine Entrée","lon":'6.93221',"lat":'46.0323',"meet":'1',"hp":'Sa. 11:36',"tc":'18:34:23',"clt":'2',"vit":'9,71km/h'},
              {"idpt":'33',"kmt":'154,0 km',"kmp":'0,0 km',"dt":'9 100 m',"dp":'0 m',"p":"Vallorcine Entrée","a":'1 292 m',"n":"Vallorcine Sortie","lon":'6.93221',"lat":'46.0323',"meet":'1',"hp":'Sa. 11:39',"tc":'18:37:50',"clt":'2',"vit":'-km/h'},
              {"idpt":'43',"kmt":'161,7 km',"kmp":'7,7 km',"dt":'9 971 m',"dp":'871 m',"p":"Vallorcine Sortie","a":'2 118 m',"n":"La Tête aux vents","lon":'6.90654',"lat":'45.9824',"meet":'',"hp":'Sa. 12:54',"tc":'19:53:13',"clt":'2',"vit":'6,10km/h'},
              {"idpt":'44',"kmt":'165,2 km',"kmp":'3,5 km',"dt":'10 047 m',"dp":'76 m',"p":"La Tête aux vents","a":'1 882 m',"n":"La Flégère","lon":'6.88674',"lat":'45.9607',"meet":'1',"hp":'Sa. 13:20',"tc":'20:19:16',"clt":'2',"vit":'8,04km/h'},
              {"idpt":'142',"kmt":'172,1 km',"kmp":'7,0 km',"dt":'10 055 m',"dp":'8 m',"p":"La Flégère","a":'1 037 m',"n":"Chamonix","lon":'6.86875',"lat":'45.9237',"meet":'1',"hp":'Sa. 14:00',"tc":'20:58:31',"clt":'2',"vit":'10,65km/h'}
]

# Definition of a new virtual speed
def V(speed, distance, elevation_gain, elevation_lost, coeff_elevation_gain=0.008, coeff_elevation_lose=0.002):
    return round(speed * (1 + coeff_elevation_gain * 0.001 * (elevation_gain / distance) + coeff_elevation_lose * 0.001 * (elevation_lost / distance)), 2)

# Vector containing only the needed data
usefull_split_info = []
# [total km, 
# km of last section, 
# elevation gain on last section,
# elevation lose on last section,  
# speed on last section,
# virtual speed on last section ]

# Get altitude of every splits
altitude = []

for elem in input_data2:
    if((not elem.get("idpt") == '0') and (not elem.get("kmp") == '0,0 km')):
        curr_alti = elem.get("a").replace(",", ".").replace(" ", "")
        curr_alti = int(float(curr_alti[0 : len(curr_alti) - 1]))
        
        altitude.append(curr_alti)

        kil = elem.get("kmt").replace(",", ".").replace(" ", "")
        kil = float(kil[0 : len(kil) - 2])

        dkil = elem.get("kmp").replace(",", ".").replace(" ", "")
        dkil = float(dkil[0 : len(dkil) - 2])

        delevation_gain = elem.get("dp").replace(",", ".").replace(" ", "")
        delevation_gain = int(float(delevation_gain[0 : len(delevation_gain) - 1]))

        if(not len(altitude) == 1):
            delevation_lose = delevation_gain - (altitude[len(altitude) - 1] - altitude[len(altitude) - 2])
        else:
            delevation_lose = delevation_gain - (altitude[len(altitude) - 1] - 1037)

        dspeed = elem.get("vit").replace(",", ".").replace(" ", "")
        dspeed = float(dspeed[0 : len(dspeed) - 4])
        
        usefull_split_info.append([kil, dkil, delevation_gain, delevation_lose, dspeed, 0])

altitude = [1037] + altitude

# Coefficient to give a meaning to elevation differences
different_coeff = [(7.5, 1)]

plt.figure(figsize=(11, 5))

for coeff_gain, coeff_lose in different_coeff:
    for e in usefull_split_info:
        e[5] = V(e[4], e[1], e[2], e[3], coeff_gain, coeff_lose)
    
    X = [e[0]-e[1]/2 for e in usefull_split_info] # distance in the middle of the section
    Y = [e[5] for e in usefull_split_info] # virtual speed on the section

    # Linear regression
    # a, b = np.polyfit(X,Y,1)
    # x = np.array([0, 170])
    # y = a*x + b
    # plt.plot(x, y, '--k', linewidth = 0.2)

    # Main plot
    plt.plot(X,Y, marker='o', linestyle='dashed', label = str(coeff_gain) + ", " + str(coeff_lose))
    
    # Plot altitude
    x_alti = [e[0] for e in usefull_split_info] #distance in the middle of the section
    x_alti = [0] + x_alti
    plt.plot(x_alti, np.array(altitude)/166 + 3, marker='x', linestyle='dotted')

plt.legend()
plt.savefig("./dhaene.png")
plt.show()
