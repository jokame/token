#!/usr/bin/python
import Token
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#def textProcessing(text):
 #   print text

u=0
path = "telcel.json"
tweets = [json.loads(line) for line in open(path)]
Vector=Token.VectorTexto()
for tw in tweets:
#	u=u+1
#	if u==300:
#		break
	t = tw['text']
	
	Vector.mete(t)
while len(Vector.BD) > 0:
	Vector.saca()
 #   textProcessing(t)