---
layout: post
title:  "Modern Maximum-Likelihood Theory for High-Dimensional Logistic Regression"
date:   2019-09-19 11:00:55 -0500
categories: seminar
hidden: true
---

Speaker: Pragya Sur (Harvard University)

### Background

Logistic regression model, mainly for binary data.

$\mathbb{P}(y=1 \vert X)=\frac{e^{b^TX}}{1+e^{b^TX}}$

Classic MLE results, for fixed p, we have $\sqrt{n}(\hat{\beta}-\beta)\to N(0, I^{-1})$

​	 hypothesis testing, Wilks theorem.

how about diverging p? Some references.

### Data: 

Inspiration: 100~1000 sample size, 10~100 features. p close to n. When n/p is 5~10, can we trust results?

Obeservation: MLE will have systematic shift on both magnitudes and variance. Wilks theorem failed as well. 

When finite sample, do correction. Like LRT first order correction. $\mathbb{E}(-2 lnLRT) \sim 1+\frac{\alpha}{n}+O(1/n^2)$, which not enough for high dimension. 

### High dimensional behavior

($p, n \to \infty, p/n \text{ to a constant } \kappa$).

$\hat{\beta}-\alpha\beta\to N(0, \sigma^2_{h.d})$, which has a larger variance than classical result.

$-2lnLRT \sim r\chi^2, r>1$

Some assumptions, like Signal strength $\gamma$ should be strong enough(converge to a constant), $\sqrt{n}X_i \sim N(0, I)$ .   

When $\kappa$ is large, MLE may doesn’t exist. Associated with $\kappa, \gamma$, soltuion could be characterized as $\alpha, \sigma, \lambda$, which decide the final behavior.

### Results:

Given the asymptotical behaive for mle estimators and LRT in this case. 

Interpretation of $\lambda$, $r$ can be represented by $\sigma, \lambda$, and $\lambda$ captures the trace of Hessian matrix for estimation in high dimension.

### Some Tools:

robust M-estimation

Leave-one-out argument for \beta distribution

### Extension to penalty estimator

Distribution follows the proximal of penalty function with proper parameters.