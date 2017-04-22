fichier = open("regles.txt","r")

atomes = []
etiquettes = []
regles = []

"""
Construction de l'espace conceptuel
"""

for line in fichier:
	if line[0] != '\n':
		symbole = line.split("\t")[0]
		premisses = line.split("\n")[0].split("\t")[1:]

		if symbole not in etiquettes:
			etiquettes.append(symbole)

		for elt in premisses:
			if elt[0]=="'" and elt[len(elt)-1]=="'":
				atom = elt[1:len(elt)-1]
				if atom not in atomes:
					atomes.append(atom)

		regles.append([symbole,premisses])

"""
Recuperation de l'input et prétraitement
"""

phrase = input("Veuillez entrer une phrase a analyser : \n")

tokensNonPretraites = phrase[0:len(phrase)-1].split(" ")
tokensPretraites = []

for tok in tokensNonPretraites:
	buf = []
	buf.append(tok)

	while buf:
		elem = buf.pop(0)
		if "'" in elem and elem[len(elem)-1]!="'":
			buf.append(elem.split("'")[0]+"'")
			buf.append(elem.split("'")[1])
		elif "," in elem and elem!=",":
			buf.append(elem.split(",")[0])
			buf.append(",")
		else:
			tokensPretraites.append(elem.lower())
print("@-----PRETRAITEMENT-----@")
print(str(tokensPretraites))
print("@-----------------------@")
print("\n\n")

"""
Identification des symboles terminaux 
"""

def possibilitesPremierSymboleTerminal(tokens):
	if not tokens:
		return  []
	else:
		possibilites = []
		for i in range (1,len(tokens)+1):
			symb = " ".join(tokens[0:i])
			if symb in atomes:
				possibilites.append([symb,tokens[i:]])
		return possibilites

def analyseSyntaxiqueTerminaux(tokens):
	if not tokens:
		return []
	else:
		preums = possibilitesPremierSymboleTerminal(tokens)
		if not preums:
			return []
		else :
			retour = []
			for possibilite in preums:
				if not possibilite[1]:
					retour.append([possibilite[0]])
				else:
					deuz = analyseSyntaxiqueTerminaux(possibilite[1])
					for elt in deuz:
						retour.append([possibilite[0]]+elt)
			return retour


possibilites = analyseSyntaxiqueTerminaux(tokensPretraites)

print("@-----ANALYSE TERMINAL-----@")
for possibilite in possibilites:
	print(str(possibilite))
print("@------------------------@")
print("\n\n")

def chercheRegle(liste):
	retour = []
	for l in regles:
		if l[1]==liste:
			retour.append(l)
	return retour

def tableau(tokens):
	retour = []
	ligne1=[]
	for token in tokens:
		ligne1.append([["'"+token+"'"],[]])
	retour.append(ligne1)

	for i in range(0,len(tokens)):
		ligne = []
		for j in range(0,len(tokens)):
			ligne.append([[],[]])
		retour.append(ligne)
	return retour

def affichageTableauPremisses(tableau):
	print("\n")
	tailleCellule = 15
	ligneSep = ""
	for i in range(0,(tailleCellule+1)*len(tableau[0])+1):
		ligneSep+="-"
	for line in tableau:
		ligneAff = ""
		for cell in line:
			texte = ",".join(cell[0])
			marge = tailleCellule - len(texte)
			#print((int)(marge/2))
			for i in range(1,(int)(marge/2)):
				texte = " "+texte+" "
			while len(texte)<tailleCellule:
				texte+=" "
			ligneAff += "|"+texte
		ligneAff += "|"
		print(ligneSep)
		print(ligneAff)
	print(ligneSep)
	print("\n")

def calculCellule(tab, i, jx):
	# i exprime le numero de la ligne (de 1 a 6), 0 contenant les lettres du mot
	# jx exprime le numero de colonne de 1 a 6, or les colonnes vont de 0 a 5
	# c'est pourquoi on utilise j = jx-1
	j = jx -1

	if i==1 and jx>0 and jx<=len(tab[0]): #c'est facile
		premisses = chercheRegle(tab[0][j][0])
		for p in premisses:
			tab[i][j][0].append(p[0])
			tab[i][j][1].append({'regle':p, 'atome':True, 'origin':(0,jx)})

	elif i<=len(tab) and i>1 and jx>0 and jx<=len(tab[0])-i+1:
		for k in range(1,i):
			partieGauche = tab[k][j][0]
			partieDroite = tab[i-k][j+k][0]
			#print(partieGauche)
			#print(partieDroite)
			premisses = []
			for eltG in partieGauche:
				for eltD in partieDroite:
					premisses+=chercheRegle([eltG,eltD])
			for p in premisses:
				if p[0] not in tab[i][j][0]:
					tab[i][j][0].append(p[0])
				tab[i][j][1].append({'regle':p, 'atome':False, 'origin':[(k,jx),(i-k,jx+k)]})


	else :
		print("les valeur i et j : "+str((i,jx))+" ne correspondent pas")
		print("le nombre de mots est "+str(len(tab[0])))

def algoCyk(tab):
	for i in range(1,len(tab[0])+1):
		for j in range(1,len(tab[0])+2-i):
				calculCellule(tab,i,j)

def reussite(tab):
	if 'ph' in tab[len(tab)-1][0][0]:
		print("reussi")
		return tracebackRec(tab, len(tab)-1, 0, 'ph')
	else :
		#print('echec')
		return []

def tracebackRec(tab, i, j, symb):
	if symb not in tab[i][j][0]:
		print("erreur, cette cellule ne peut etre identifier au symbole "+symb)
		return []
	else:
		for elt in tab[i][j][1]:
			if elt['regle'][0]==symb:
				if not elt['atome']:
					coordsG = elt['origin'][0]
					coordsD = elt['origin'][1]
					#print(str((i,j+1))+ " "+str(elt['regle']) + " origins : "+str(coordsG)+", "+str(coordsD))
					arbre1 = tracebackRec(tab,coordsG[0],coordsG[1]-1, elt['regle'][1][0])
					arbre2 =tracebackRec(tab,coordsD[0],coordsD[1]-1, elt['regle'][1][1])
					return [elt['regle'],[arbre1,arbre2]]
				else:	
					#print(str((i,j+1))+ " "+str(elt['regle']))
					return [elt['regle'],[]]

def afficherArbre(arb,indentation):
	#print(arb)
	if arb :
		regle = arb[0]
		fils = arb[1]
		texte = "|- "+regle[0]+" -> "+",".join(regle[1])

		indent = ""

		if indentation >1:
			for i in range(1,indentation):
				indent+= "     "
		if indentation > 0:
			indent2 = indent + "|----"
		else:
			indent2 = indent

		print(indent2+texte)

		if fils:
			print(indent+"     |")

			for f in fils:

				afficherArbre(f,indentation+1)

for possibilite in possibilites:
	tab = tableau(possibilite)
	algoCyk(tab)
	arbre = reussite(tab)
	if arbre:
		affichageTableauPremisses(tab)
		afficherArbre(arbre,0)
"""for r in regles:
	print(r)
print("\n\n")
for a in atomes:
	print(a)
"""
fichier.close()