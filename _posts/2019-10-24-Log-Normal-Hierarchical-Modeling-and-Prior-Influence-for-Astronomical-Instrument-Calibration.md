---
layout: post
title:  Log-Normal Hierarchical Modeling and Prior Influence for Astronomical Instrument Calibration
date:   2019-10-24 11:00:55 -0500
categories: seminar
hidden: true

---

Speaker:  Yang Chen, (Department of Statistics & MIDAS, University of Michigan)

### Background

Relationship between flux, effective area and measurements. Want to know the property of astronomical object, like flux. Measurements depend on effective area, which differs for each instrument, also changes by time.

Problem: The data from different instruments don’t agree, due to a lot of reasons. How to fix?

Goal: Know the effecitve area of each instruments to fix.

Assume true effective area is $A_i$(unknown), and estimated $a_i$(known). Flux for each source $F_j$ (unkown). Photon counts $c_{ij}$ (observations)

Counts = ExposureTime * Effective Area * FLux, set time to 1.

### Model: loglinear model with normal error term. 

$y_{ij}=log{c_{ij}}-\alpha_{ij}=B_i+G_i+e_{ij}, B_i=log A_i, G_i = logF_i, e_{ij}\sim N(0, \sigma^2_{ij})$

$\alpha_{ij}=\frac{\sigma_{ij}^2}{2}$ , ==Half variance correction.==

### Method: Bayesian hierarchical model

Piror $B_i \sim N(b_i, \tau_i^2), G_i \sim flat \ prior, \sigma \sim Inv-Gamma$ 

==Sensitive to prior!== Where experts experience come in for choose prior.

Investigate on condition number of variance of sigma, a big noise on B_i will make converge harder(worse posterior). (hurt identifiability)

Using HMC to sampling.

### Advantages using Bayesian way:

Narrow confidence interval (small variance) can cause false discvoeries if it’s not reliable.

Tolerance of model/error misspecification. 

### Extension:

In order to compatible with Poisson assumption, extend normal to t distribution will give a better results for low Poisson parameter.