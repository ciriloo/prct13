#!usr/bin/python
#import pi
import sys
import time
import timeit
import numpy
#import mathplotlib.pyplot as pl
import pylab as pl
l=3.1415926535897931159979634685441852
def pi(n):
 PI=0
 for i in range(1,n+1):
    x=(i-.5)/float(n)
    fx=4/(1+(x*x))
    PI=PI+(fx)/n 
   # print 'subintervalo: [%3.2f,%3.2f] x: %f fx: %6.5f '    %  ((i-1)/float(n), i/float(n), x, fx)
 return PI
 
if (__name__=="__main__"):
 #veces=0
 n=7
 #if(len(sys.argv)==2):
  # n=int(sys.argv[1])
   #veces=int(sys.argv[2])
 #else:
 #  print 'la longitud no es la correcta, deben ser 3 argumentos de entrada'
  
 k=[]
 a=[]
 #b=[]
 i=1
 print 'i         PI35DT                   lista i                    PI35DT - lista i      error%'
 x1=(1e2,1e3,1e-4,1e-5,1e-6,1e-7,1e-8)
 x2=(10, 50, 100, 150, 500, 550, 1000)
 y=(0,10,20,40,60,80,100)
 for i in x1:          #10,veces+1,50):
  start=time.time()
  
  s=pi(int(i*n))
  m=(s-l)/l
  #print '%i     %.10f               %.10f                   %.10f    %f'   % (i,l,s,s-l,m)
  
  n=n+1
  k=k+[s]
  finish=time.time()-start
  a=a+[finish]
  #b=b+[m]
 #print ' la lista de las aproximaciones es: '
 p1=pl.subplot(211)
 pl.title('Porcentaje de fallos')
 pl.plot(x1,y,'--',color='y')
 p1=pl.subplot(212)
 pl.xlabel('intervalos')
 pl.ylabel('tiempo en segundos')
 pl.plot(x2,a,'-',color='r')
 pl.plot(n,s,'.-',color='g')
 pl.show()
 pl.savefile('figura.png')
 print k
 #print 'el tiempo requerido en este proceso es: %f' %finish
 