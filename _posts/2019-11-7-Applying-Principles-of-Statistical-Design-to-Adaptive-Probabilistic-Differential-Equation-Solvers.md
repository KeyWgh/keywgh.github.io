---
layout: post
title:  Applying Principles of Statistical Design to Adaptive Probabilistic Differential Equation Solvers
date:   2019-11-7 11:00:55 -0500
categories: seminar
hidden: true

---

Speaker:   Oksana Chkrebtii, Department of Statistics, The Ohio State University

### **Abstract**:
When models are defined implicitly by systems of differential equations with no closed-form solution, small local errors in finite-dimensional solution approximations can propagate into deviations from the true underlying model. Some recent perspectives in quantifying this uncertainty are based on Bayesian probability modeling: a prior is defined over the unknown solution and updated by conditioning on interrogations of the forward model. We apply principles of Bayesian statistical design to sequentially adapt time-steps for state-space probabilistic differential equation solvers and investigate the behaviour of local error under the adaptive scheme which underlies numerical variable step-size methods. 

### Background

Dynamical system, inference on the variables of system states which are defined implicitly.
$$
Du = f(u, \text{derivatives of u w.r.t x}, \theta), x\in\mathcal{X}\in\mathbb{R}^q \\
u = u_0(x,\theta), x\in\partial\mathcal{X}
$$
D is a linear operator.  $x$ is spatial-temporal location. Approximation of solution will introduce structured uncertainty into the inverse problem.

We want to estiamte unknown parameters $\theta$, while we only observe 
$$
y(x_i) = A(u(x_i, \theta))+\epsilon(x_i)
$$
Use $\hat{u}$ to approximate true u. 

Goal and motivation: Characterize the uncertainty in this approximation to enable exact inference on $\theta$.

Tool: Using a Bayesian paradigm to PDE/ODE. Instead update the belief on $\theta$, we try to update our belief on $u$!

Example?

Method:
$$
y|u,\theta : likelihood
\\ u|\theta : model, represent the uncertainty
\\ \theta : prior
$$
Several competeing methods:

- Gaussian Process Prior on $(Du, u)^T$

- Stepwise sampling and interrogate 