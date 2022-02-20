---
layout: post
title:  "How to fit an elephant"
date:   2020-3-20 14:47:55 -0500
categories: story


---

Cited from [John D. Cook](https://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant/) 

>
> John von Neumann famously said
>
> > With four parameters I can fit an elephant, and with five I can make him wiggle his trunk.
>
> By this he meant that one should not be impressed when a complex model fits a data set well. With enough parameters, you can fit any data set.
> It turns out you can literally fit an elephant with four parameters if you allow the parameters to be complex numbers. See this paper for details: "Drawing an elephant with four complex parameters"[^1].
>
> [Piotr](https://twitter.com/zolnie) also sent me the following Python code he’d written to implement the method in the paper. This code produced the image above.
>
> ```python
> """
> Author: Piotr A. Zolnierczuk (zolnierczukp at ornl dot gov)
> 
> Based on a paper by:
> Drawing an elephant with four complex parameters
> Jurgen Mayer, Khaled Khairy, and Jonathon Howard,
> Am. J. Phys. 78, 648 (2010), DOI:10.1119/1.3254017
> """
> import numpy as np
> import pylab
> 
> # elephant parameters
> p1, p2, p3, p4 = (50 - 30j, 18 +  8j, 12 - 10j, -14 - 60j )
> p5 = 40 + 20j # eyepiece
> 
> def fourier(t, C):
>     f = np.zeros(t.shape)
>     A, B = C.real, C.imag
>     for k in range(len(C)):
>         f = f + A[k]*np.cos(k*t) + B[k]*np.sin(k*t)
>     return f
> 
> def elephant(t, p1, p2, p3, p4, p5):
>     npar = 6
>     Cx = np.zeros((npar,), dtype='complex')
>     Cy = np.zeros((npar,), dtype='complex')
> 
>     Cx[1] = p1.real*1j
>     Cx[2] = p2.real*1j
>     Cx[3] = p3.real
>     Cx[5] = p4.real
> 
>     Cy[1] = p4.imag + p1.imag*1j
>     Cy[2] = p2.imag*1j
>     Cy[3] = p3.imag*1j
> 
>     x = np.append(fourier(t,Cx), [-p5.imag])
>     y = np.append(fourier(t,Cy), [p5.imag])
> 
>     return x,y
> 
> x, y = elephant(np.linspace(0,2*np.pi,1000), p1, p2, p3, p4, p5)
> pylab.plot(y,-x,'.')
> pylab.show()
> ```

Some comments:

- Actually the code above used five complex numbers, four for the contour and one for the eyepiece, thus ten parameters to fit the whole elephant.
- We need one additional parameter to make its trunk wiggle, along with some code modification. [Animation]({{site.baseurl}}/assets/img/elephant_ffmpeg.gif), [Download code]({{site.baseurl}}/assets/resource/elephant.py){:target="_blank"} 
- [Fourier](http://en.wikipedia.org/wiki/Joseph_Fourier) strikes again!

<!--

>All stable processes we shall predict. All unstable processes we shall control.
>
>Anyone attempting to generate random numbers by deterministic means is, of course, living in a state of sin.
>
>If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.
>
>In mathematics you don't understand things. You just get used to them.
>
>It is just as foolish to complain that people are selfish and treacherous as it is to complain that the magnetic field does not increase unless the electric field has a curl. Both are laws of nature.
>
>It would appear that we have reached the limits of what it is possible to achieve with computer technology, although one should be careful with such statements, as they tend to sound pretty silly in five years.
>
>Life is a process which may be abstracted from other media.
>
>The sciences do not try to explain, they hardly even try to interpret, they mainly make models. By a model is meant a mathematical construct which, with the addition of certain verbal interpretations describes observed phenomena. The justification of such a mathematical construct is solely and precisely that it is expected to work.
>
>There is an infinite set *A* that is not too big.
>
>There probably is a God. Many things are easier to explain if there is than if there isn't.
>
>There's no sense in being precise when you don't even know what you're talking about.
>
>We willingly pay 30,000 - 40,000 fatalities per year for the advantages of individual transportation by automobile.
>
>When we talk mathematics, we may be discussing a secondary language built on the primary language of the nervous system.
>
>With four parameters I can fit an elephant, and with five I can make him wiggle his trunk.
>
>You don't have to be responsible for the world that you're in.
>
>You insist that there is something a machine cannot do. If you tell me precisely what it is a machine cannot do, then I can always make a machine which will do just that.
>
>You wake me up early in the morning to tell me that I'm right? Please wait until I'm wrong.
>
>Young man, in mathematics you don't understand things. You just get used to them.
-->

[^1]: [Mayer, Jürgen, Khaled Khairy, and Jonathon Howard. "Drawing an elephant with four complex parameters." *American Journal of Physics* 78.6 (2010): 648-649.](https://aapt.scitation.org/doi/10.1119/1.3254017)

