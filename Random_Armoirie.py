'''
Flag_Randomizer
Creator: Gael
'''
import random 

list_part01 = ["coupé","parti","tranché","taillé","fascé","burelé","bandé","coticé en bande","palé","vergeté","barré","coticé en barre","ecartelé","ecartelé en sautoir","gironné","gironné de six pièces","echiqueté","losangé","fuselé","endenté","tiercé en fasce","tiercé en pal","tiercé en bande","tiercé en barre","tiercé en chevron","chapé","chaussé","mantelé"]
list_objet1 = ["abeille","croisillion","colombe","arbre","feuille de chene","branche de noyer","pin","buis","fleur de lys","oeillets","quartefeuille","quintefeuille","rose","gerbe","cerise","trefle","vigne","aiguille","compas","ciseaux","couteau","lame","demi-lune","enclume","marteau","tenaille","tonneau","baillonette","cimeterre","dard","épée","fer de lance","lance","hache","faisceau","masse d'arme","chapelle","tour","castel","croix latine","croix tréflé"," croix recroiseté","croix fleurdelysée","croix fourché","croix ancré","croix patté","croix pomée","croix potencé","croix patriarcale","croix celtique","croix gammé","lion","aigle","léopard","panthère","brochets","lions affronté","ours","agneau pascal","sanglier","cerf","massacre de cerf","ramures","demi ramure","belier","cheval","cheval cabré","aigle bicéphale","alérons","merlettes","coq","cygne","faucon","vol","dauphin","bar","serpent","serpent en redorte","guivre","griffon","dragon","basilique","licorne","phenix","salamandre","sirênes"]
#list_metal1 = ["or","argent"]
#liste_color = ["de gueules","de sable","d'azur","de sinople","de pourpre",]
liste_color = ["de gueules","de sable","d'azur","de sinople","de pourpre","d'or","d'argent"]
x=0 
y=0
while x < 10:
    parti = random.choice(list_part01)
    color = random.choice(liste_color)
    metal = random.choice(liste_color)
    meta2 = random.choice(liste_color)
    symbl = random.choice(list_objet1)
    nombr = random.randint(1,6)
    
    if color != metal :
        if color != meta2 :
            if symbl == symbl:
                print( color + " " + parti + " " + metal + " accompagné de " + str(nombr) + " " + symbl + " " + meta2)
                x+=1
    y+=1
    
print(y)
    


