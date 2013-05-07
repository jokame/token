#!/usr/bin/python
import Token
import json
import time



u=0
path = "telcel.json"
tweets = [json.loads(line) for line in open(path)]
Vector=Token.VectorTexto()
for tw in tweets:
	t = tw['text']
	Vector.mete(t)
while Vector.BD!=[]:
	time.sleep(0.1)
Vector.muere()
