#coding=utf-8
import nltk, time
from threading import Thread
class VectorTexto(object):
	"""docstring for VectorTexto"""
	def __init__(self):
		super(VectorTexto, self).__init__()
		self.token=nltk.RegexpTokenizer(u"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\xe1\xe9\xed\xf3\xfa\xc1\xc9\xcd\xd3\xda\xf1\xd1\xfc\xdc']+")
		#Cadena de caracteres admitidos en Tokenizer
		self.BD=[]
		self.ultsaca=time.time()
		self.cadena=u''
		self.sigue=True
		self.TredSacador=Thread(target=self.saca)
		self.TredSacador.start()
		self.max=1000 #Máximo número de palabras a escribir en Words.txt por ciclo
	def mete(self,t):
		q=self.token.tokenize(t)
		self.BD=self.BD+q
		

	def saca(self):
		tant=time.clock()
		while self.sigue==True:
			time.sleep(0.002)
			tsaca=time.clock()
			trans=tsaca-tant #tiempo transcurrido desde última escritura en Words
			if self.BD!=[] and ((tsaca%1 >0.49 and tsaca%1 <0.51) or tsaca%1>0.99 or tsaca%1<0.01) and trans>0.48:

				u=1
				self.cadena=u''
				for s in self.BD:
					self.cadena=self.cadena+s+u'|'
					if u==1200:
						break
					u=u+1
				while u != 1:
					del self.BD[0]
					u=u-1
				with open('Words.txt','w') as Words:
					Words.write(self.cadena.encode('utf-8'))
					Words.close()
				tant=tsaca
	def muere(self):
		self.sigue=False

	
if __name__ == '__main__':
	Vector=VectorTexto()
	Vector.mete(u"casco patada colchón partido ñacañaca Güerita o'h")
	while Vector.BD!=[]:
		time.sleep(0.1)
	Vector.muere()