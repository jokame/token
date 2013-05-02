#coding=utf-8
from datetime import datetime, date, timedelta
import nltk

class VectorTexto(object):
	"""docstring for VectorTexto"""
	def __init__(self):
		super(VectorTexto, self).__init__()
		self.BD=[]
		self.hora=datetime.now()
		self.delta=timedelta(milliseconds=500)
		self.token=nltk.RegexpTokenizer('[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\á\é\í\ó\ú\Á\É\Í\Ó\Ú\ñ\Ñ\'\ü\Ü]+')
		self.cadena=""
		self.cont=0
		
	def mete(self,t):
		q=self.token.tokenize(t)
		self.BD=self.BD+q
		self.saca()

		#print q

	def saca(self):
		m=datetime.now()
		if m > (self.hora+self.delta) and len(self.BD)>0:
			print m 
			print len(self.BD)
			u=1
			self.cadena=''
			for s in self.BD:
				self.cadena=self.cadena+s+'|'
				if u==1200:
					print 'perro'
					break
				u=u+1
			while u != 1:
				del self.BD[0]
				u=u-1
			Words=open('Words'+str(self.cont)+'.txt','w')
			Words.write(self.cadena.decode('utf-8',errors='ignore'))
			Words.close
			self.hora=m
			self.cont=self.cont+1



	
if __name__ == '__main__':
	m=VectorTexto()
	m.mete("carro cáca mañana si.po es, ver|.dad , .* a $900")
	print m.BD



	
	
	
	

		