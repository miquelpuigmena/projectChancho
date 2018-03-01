import constants as C
import csv
import os
import time
import datetime
from shutil import copyfile

def priv_checkIfItIsTheSameMatch(line1, line2):
    if(line1[C.local_tag]==line2[C.local_tag]):
        if(line1[C.visitant_tag]==line2[C.visitant_tag]):
            if(line1[C.esport_tag]==line2[C.esport_tag]):
                return True
    return False

def priv_getMatchesOrdered():
	contador = 0
	list_by_matches=[]
	pos_taken = []
	copyfile(C.dataresultpath_tag, C.dataresultpathaux_tag)
	data = open(C.dataresultpath_tag, 'r')
	reader = csv.reader(data)

	for line in reader:
	    list_by_matches_aux=[]
	    if contador not in pos_taken:
		list_by_matches_aux.append(line)
		contadoraux = 0
		pos_taken.append(contador)
		dataaux = open(C.dataresultpathaux_tag, 'r')
		readeraux = csv.reader(dataaux)
		for lineaux in readeraux:
		    if contadoraux not in pos_taken:
		        if(priv_checkIfItIsTheSameMatch(line, lineaux)):
		            pos_taken.append(contadoraux)
		            list_by_matches_aux.append(lineaux)
		    contadoraux += 1
		dataaux.close()
		list_by_matches.append(list_by_matches_aux)
	    contador += 1
	os.remove(C.dataresultpathaux_tag)
	data.close()
	return list_by_matches

def priv_getAlpha2(q1, q2):
	alpha = ((float(q1)*float(q2))/(float(q1)+float(q2)))
	return round(alpha, 4)
def priv_AlphaCombination2(match1, match2, alpha_list):
	a1 = match1[C.cuota1_tag]
	a2 = match1[C.cuota2_tag]
	b1 = match2[C.cuota1_tag]
	b2 = match2[C.cuota2_tag]
	alpha1 = priv_getAlpha2(a1,b2)
	listaux=[]
	listaux.append(alpha1)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match1[C.casa_tag], match1[C.cuota1_tag], match2[C.casa_tag], match2[C.cuota2_tag]])
	alpha_list.append(listaux)
	alpha2 = priv_getAlpha2(b1,a2)
	listaux=[]
	listaux.append(alpha2)
	listaux.append([match2[C.local_tag],match1[C.visitant_tag]])
	listaux.append([match2[C.casa_tag], match2[C.cuota1_tag], match1[C.casa_tag], match1[C.cuota2_tag]])
	alpha_list.append(listaux)

def priv_getAlpha3(q1,qx,q2):
	alpha = ((float(q1)*float(qx)*float(q2))/((float(q1)*float(qx))+(float(q1)*float(q2))+(float(qx)*float(q2))))
	return round(alpha, 4)
def priv_AlphaCombination3(match1, match2, alpha_list):
	a1 = match1[C.cuota1_tag]
	ax = match1[C.cuotax_tag]
	a2 = match1[C.cuota2_tag]
	b1 = match2[C.cuota1_tag]
	bx = match2[C.cuotax_tag]
	b2 = match2[C.cuota2_tag]
	#alpha1 = priv_getAlpha3(a1,ax,a2)
	alpha2 = priv_getAlpha3(a1,ax,b2)
	listaux=[]
	listaux.append(alpha2)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match1[C.casa_tag], match1[C.cuota1_tag], match1[C.casa_tag], match1[C.cuotax_tag], match2[C.casa_tag], match2[C.cuota2_tag]])
	alpha_list.append(listaux)
	alpha3 = priv_getAlpha3(a1,bx,a2)
	listaux=[]
	listaux.append(alpha3)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match1[C.casa_tag], match1[C.cuota1_tag], match2[C.casa_tag], match2[C.cuotax_tag], match1[C.casa_tag], match1[C.cuota2_tag]])
	alpha_list.append(listaux)
	alpha4 = priv_getAlpha3(a1,bx,b2)
	listaux=[]
	listaux.append(alpha4)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match1[C.casa_tag], match1[C.cuota1_tag], match2[C.casa_tag], match2[C.cuotax_tag], match2[C.casa_tag], match2[C.cuota2_tag]])
	alpha_list.append(listaux)
	alpha5 = priv_getAlpha3(b1,ax,a2)
	listaux=[]
	listaux.append(alpha5)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match2[C.casa_tag], match2[C.cuota1_tag], match1[C.casa_tag], match1[C.cuotax_tag], match1[C.casa_tag], match1[C.cuota2_tag]])
	alpha_list.append(listaux)
	alpha6 = priv_getAlpha3(b1,ax,b2)
	listaux=[]
	listaux.append(alpha6)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match2[C.casa_tag], match2[C.cuota1_tag], match1[C.casa_tag], match1[C.cuotax_tag], match2[C.casa_tag], match2[C.cuota2_tag]])
	alpha_list.append(listaux)
	alpha7 = priv_getAlpha3(b1,bx,a2)
	listaux=[]
	listaux.append(alpha7)
	listaux.append([match1[C.local_tag],match2[C.visitant_tag]])
	listaux.append([match2[C.casa_tag], match2[C.cuota1_tag], match2[C.casa_tag], match2[C.cuotax_tag], match1[C.casa_tag], match1[C.cuota2_tag]])
	alpha_list.append(listaux)
	#alpha8 = priv_getAlpha3(b1,bx,b2)

def priv_orderListByColumn(list_to_order, index):
	return sorted(list_to_order,key=lambda x: x[index], reverse=True)
def define_Alphas():
	alpha_list=[]
	groups_matches = priv_getMatchesOrdered()
	for group_match in groups_matches:
	    group_match_aux = group_match
	    for element_match in group_match:
		after_position_of_the_match = False
		for element_match_aux in group_match_aux:
		    if element_match==element_match_aux: 
			after_position_of_the_match = True
		    elif after_position_of_the_match:
			if(element_match[C.cuotax_tag]==C.none_tag):
			    priv_AlphaCombination2(element_match, element_match_aux, alpha_list)
			else:
			    priv_AlphaCombination3(element_match, element_match_aux, alpha_list)

	t = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m_%H:%M')
	file_w = open("csv/script/"+str(t)+".csv", 'w')
	file_w.close()
	f = open("csv/script/"+str(t)+".csv",'a')
	writer = csv.writer(f)
	contador=0
	for line in priv_orderListByColumn(alpha_list, C.alpha_tag):
		if contador<10:
			print line
			contador += 1
		writer.writerow(line)
	f.close()
