import Token
import json
import tweetstream

stream=tweetstream.SampleStream("","")
Vector=Token.VectorTexto()
try:
	for tweet in stream:
		s= tweet.get('text','')
		if s!='':
			Vector.mete(s)
except KeyboardInterrupt:
	stream.close()
	Vector.muere()