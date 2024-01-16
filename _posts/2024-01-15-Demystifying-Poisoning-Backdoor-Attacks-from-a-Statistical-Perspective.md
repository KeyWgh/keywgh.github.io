---
layout: post
title: "Demystifying Poisoning Backdoor Attacks from a Statistical Perspective"
date: 2024-01-12 16:00:00 -0500
categories: stat

---

This article is intended to introduce our recent research on a fundamental understanding of backdoor in machine learning models, including discriminative and generative models, based on our recent work published at the International Conference on Machine Learning (ICML)[^2] and International Conference on Learning Representations (ICLR) [^1]. 

As machine learning models become integral to various applications, their security emerges as a critical concern. In real-world scenarios, these models are often constructed from datasets whose intricacies may be obscured from users. This lack of transparency poses a risk for exploitation through **backdoor attacks**, a growing concern in AI security. These attacks are designed to make a model operate normally until it encounters specific, altered inputs that activate the backdoor, causing the model to behave unpredictably, as demonstrated in Figure 1.

[<>]:  <img src="{{site.baseurl}}/assets/img/bd_example.pdf" width="500" />

<object data="{{site.baseurl}}/assets/img/bd_example.pdf" width="400" height="200" type='application/pdf'></object>
Figure 1: An example of a backdoor attack that compromises the traffic sign classifier for autonomous driving.

A powerful backdoor attack has a **dual-goal**: being stealthy and useful, meaning that it (1) prompt the compromised model to exhibit manipulated behavior when a specific attacker-defined trigger is present and (2) maintain normal functionality in the absence of the trigger, rendering the attack difficult to detect.

A research team led by Ashish Kundu and Jayanth Srinivasa from Cisco Research, in collaboration with a research team from the University of Minnesota, including [Jie Ding](https://jding.org/), [Mingyi Hong](https://people.ece.umn.edu/~mhong/mingyi.html), [Xuan Bi](https://sites.google.com/site/xuanbigts/home), [Xun Xian](https://jeremyxianx.github.io/), and [Ganghua Wang](https://gwang.umn.edu/), has been dedicated to the fundamental understanding of backdoor attacks and defenses, a critical challenge in AI safety that has garnered rapidly increasing attention. Their collaborative effort delves into developing provable quantification of backdoor risks and effective mitigation strategies in diverse AI applications.

Their research aims to tackcle the following crucial yet previously underexplored questions:
1. What are the key factors determining backdoor attack’s success?
2. What shape or direction of a trigger signal constitutes the most potent backdoor while maintaining the same level of utility distortion?
3. When will a human-imperceptible trigger succeed?

To address these questions, this research team has quantitatively revealed three key factors that jointly determine the performance of any backdoor attack: **the ratio of poisoned data $\rho$**, **the direction and magnitude of the trigger $\eta$**, and **the clean data distribution $\mu$**, as shown in Figure 2. 


[<>]: ![factors]({{site.baseurl}}/assets/img/bd_factor.pdf)

<object data="{{site.baseurl}}/assets/img/bd_factor.pdf" width="600" height="300" type='application/pdf'></object>

Figure 2: Illustration of three factors jointly determining the effectiveness of a backdoor attack: poisoning ratio, backdoor trigger, and clean data distribution.

This research has further *quantified* the prediction performance, denoted by $r_n$, of a backdoored model on both clean or backdoored data through a finite-sample analysis. Briefly speaking, the team has shown
$
\begin{equation}
r_n \sim g(\rho,\eta,\mu)
\end{equation}
$
where $g(\cdot)$ is an explicit function delineating the prediction performance's dependence on three principal factors. This analytical framework is **applicable to both discriminative and generative models**. More technical details can be found in [1].

The above result then implies answers to the last two questions: 

- The **optimal trigger** direction is where the clean data distribution decays the most. 
- Constructing a **human-imperceptible backdoor attack could be more feasible** when the clean data distribution degenerates more.

The above fundamental understanding also serves as a basis for developing improved defense mechanisms against backdoor attacks, which are detailed in another article accessible [here]().

[^1]: [Ganghua Wang, Xun Xian, Jayanth Srinivasa, Ashish Kundu, Xuan Bi, Mingyi Hong, and Jie Ding. “Demystifying Poisoning Backdoor Attacks from a Statistical Perspective,” International Conference on Learning Representations (ICLR), 2024.](https://arxiv.org/pdf/2310.10780.pdf) 

[^2]: [Xun Xian, Ganghua Wang, Jayanth Srinivasa, Ashish Kundu, Xuan Bi, Mingyi Hong, and Jie Ding. “Understanding backdoor attacks through the adaptability hypothesis,” International Conference on Machine Learning (ICML), 2023.](https://openreview.net/pdf?id=4zWEyYGGfI) 

{% details **Click** to expand Bib info. %}
@article{wang2024demystify,
  title={Demystifying Poisoning Backdoor Attacks from a Statistical Perspective},
  author={Wang, Ganghua and Xian, Xun and Srinivasa, Jayanth and Kundu, Ashish and Bi, Xuan and Hong, Mingyi and Ding, Jie},
  journal={Proc. ICLR},
  year={2024}
}

@article{xian2023under,
  title={Understanding backdoor attacks through the adaptability hypothesis},
  author={Xian, Xun and Wang, Ganghua and Srinivasa, Jayanth and Kundu, Ashish and Bi, Xuan and Hong, Mingyi and Ding, Jie},
  journal={Proc. ICML},
  year={2023}
}
{% enddetails %}

