# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:20:19 2017

@author: 11222
"""

from pylab import *

t = linspace(0,1,100)

x= 6*pi*cos(2*pi*t)
y = -4*pi*sin(2*pi*t)


figure(1)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y)
    plot([0,x[it]],[0,y[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

    text(1.1*x[it]/10,1.1*y[it]/10,r'$\vec{a}$',color='red',size=15)
    grid()
     #    savefig('frame_%03d.png' % it)

    pause(.001)