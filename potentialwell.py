import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

st.title('Quantum Mechanics')
st.header('1-D Potential Well',divider='rainbow')

st.text("In this site we are going to see the graphical representation of 1d pot well")

a=st.slider('Enter the Length of well',1,20)
x=np.linspace(-a,a,10000)
n=st.slider('Enter the state',1,100)

def psi(x, n):
    y = np.sqrt(2 / a) * np.sin((n * np.pi * x) / (a))
    return y
    
def psi1(x, n):
    y1 = np.sqrt(1 / (a)) * np.sin((n * np.pi * x) / (a))
    return y1
    
def psi2(x,n):
    y2=np.sqrt(2 / a) * np.cos((n * np.pi * x) / (a))
    
options = st.radio('choose type of well',["Asymmetric Potential Well","Symmetric Potential Well","Potential well with length 2a","Both",])
if options=='Asymmetric Potential Well':
    plt.subplot(2,1,1)
    plt.plot(x,(psi(x,n)))
    plt.xlim(0,a)
    plt.axhline(0,color='black')
    plt.subplot(2,1,2)
    plt.plot(x,(psi(x,n))**2)
    plt.ylabel('$\psi(x)^2$')
    plt.xlabel('x')
    plt.xlim(0,a)
    plt.ylim(bottom=0)
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

if options=='Symmetric Potential Well':
    plt.subplot(2,1,1)
    plt.plot(x,(psi1(x,n)))
    plt.xlim(-a,a)
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.subplot(2,1,2)
    plt.plot(x,(psi1(x,n))**2)
    plt.ylabel('$\psi1(x)^2$')
    plt.xlabel('x')
    plt.xlim(-a,a)
    plt.axvline(0,color='black')
    plt.ylim(bottom=0)
    plt.savefig('graph1.jpg')
    st.image('graph1.jpg')

if options=='Both':
    
    plt.subplot(2,1,1)
    plt.plot(x,(psi(x,n)))
    plt.xlim(0,a)
    plt.axhline(0,color='black')
    plt.subplot(2,1,2)
    plt.plot(x,(psi(x,n))**2)
    plt.ylabel('$\psi(x)^2$')
    plt.xlabel('x')
    plt.xlim(0,a)
    plt.ylim(bottom=0)
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

    plt.subplot(2,1,1)
    plt.plot(x,(psi1(x,n)))
    plt.xlim(-a,a)
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.subplot(2,1,2)
    plt.plot(x,(psi1(x,n))**2)
    plt.ylabel('$\psi1(x)^2$')
    plt.xlabel('x')
    plt.xlim(-a,a)
    plt.axvline(0,color='black')
    plt.ylim(bottom=0)
    #plt.tight_layout()
    plt.savefig('graph1.jpg')
    st.image('graph1.jpg')


