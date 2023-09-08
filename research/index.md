---
layout: toc_default
title: Research
permalink: /research/
---

<style>
blockquote {
  background: #f9f9f9;
  border-left: 10px solid #ccc;
  margin: 0 auto;
  padding: 0 auto;
}
#wrap {
   width:700px;
   margin:0 auto;
}
#left_col {
   float:left;
   width:250px;
}
#right_col {
   float:right;
   width:400px;
}
.column {
  float: left;
  width: 33.33%;
}
/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
.h1s{
color: #1F70CB;
text-decoration: underline;
}
</style>


[comment]:<> {:style='color:#1F70CB'}
# **Machine Learning Safety**{:style='color:#6f6fd9'}

<!--
<div id="intro">
<div id="intro-text" style="float:left; width:450px">
<p> While machine learning (ML) has shown remarkable success in many applications such as content recommendation on social media platforms, medical image diagnosis, and autonomous driving, there is a growing concern regarding the potential safety hazards coming with ML. As exemplified in Figure 1, people are interested in multi-facets evaulation of machine learning models besides accuracy. 
</p> 
<p>My current research focuses on three main aspects: <b>data privacy</b>, <b>model privacy</b>, and <b>model fairness</b>.</p>
</div>
<div id="intro-figure" style="float:right; width:200px; margin-right:5%">
<figure >
<img  src="{{site.baseurl}}/assets/img/strobel01-3178187.gif.webp"  width="200px">
<figcaption style="text-align: left;">Figure 1. Different aspects of trustworthy ML. </figcaption></figure>
</div>
</div>
<p style="clear:both;"></p>
-->


<figure style="float:right; width:200px; margin-right:5%">
<img  src="{{site.baseurl}}/assets/img/strobel01-3178187.gif.webp"  width="200px">
<figcaption style="text-align: left;">Figure 1. Different aspects of trustworthy ML. </figcaption></figure>

While machine learning (ML) has shown remarkable success in many applications such as content recommendation on social media platforms, medical image diagnosis, and autonomous driving, there is a growing concern regarding the potential safety hazards coming with ML. As exemplified in Figure 1, people are interested in multi-facets evaulation of machine learning models besides accuracy. 

My current research focuses on three main aspects: <b>data privacy</b>, <b>model privacy</b>, and <b>model fairness</b>.

<br>


## **Data and Model Privacy**{:style='color:#6f6fd9'}

<figure  >
<img  src="{{site.baseurl}}/assets/img/privacy.png"  width="750px">
<figcaption style="text-align: left;">Figure 2. Illustration of the machine learning life cycle and potential attacks. </figcaption></figure>

The privacy threat is inconspicuous but widely exists in our daily lives. We risk privacy leakage for every step in the machine learning life cycle, such as collection, storage, release, and analysis, as illustrated in Figure 2. Our goal is to develop privacy-preserving methods with built-in privacy guarantees, especially for the collected data and built models. 

Data privacy pertains to the protection of sensitive information collected to build ML models. We have proposed a novel approach called `Subset Privacy` for protecting categorical data and developed an open-sourced software implementation [4, 8]. We have demonstrated its usage in multiple learning tasks and shown its potential to be useful in a wide range of fields beyond statistics due to its unique user-friendly implementation. 

In addition to data privacy, the reliability and security of the ML models built from the collected data are of paramount concern, which we refer to as model privacy. We have formulated the `Model Privacy` framework that can be applied to analyze multiple model attacks including stealing and backdoor attacks [3, 7, 9, 10]. 


[comment]:<> <embed src="{{site.baseurl}}/assets/resource/privacy.pdf" width="500" height="375" type="application/pdf">



## **Model Fairness**{:style='color:#6f6fd9'}

<figure style="float:right; width:350px; margin-right:5%">
<img  src="{{site.baseurl}}/assets/img/fair.webp">
<figcaption>Figure 3. Fairness in Machine Learning. </figcaption></figure>

The fairness of the ML model has attracted significant attention nowadays, especially in areas such as criminal justice and banking. It is well-known that ML models may inadvertently be unfair. For example, the COMPAS algorithm, which assigns recidivism risk scores to defendants based on their criminal history and demographic attributes, was found to have a significantly higher false positive rate for black defendants than white defendants, thereby violating the principle of equity on the basis of race.

Our goal is to build a model that makes equitable decisions for different groups in the population. We have identified the conditions under which a broad class of distributed ML algorithms can produce fair models. Additionally, we have proposed a new algorithm that directly optimizes model fairness with theoretical guarantees [5]. 





## **Other Safety Aspects**{:style='color:#6f6fd9'}

[comment]:<> <figure  ><img  src="{{site.baseurl}}/assets/img/kd.png"  width="750px"><figcaption style="text-align: left;">Figure 4. Illustration of knowledge distribution. Picture credit to [Gao et al. 2021]. </figcaption></figure>

**Explainability:** We studied the effect of the LASSO regularization on variable selection in terms of neural networks [2]. Our understanding indicates that neural networks can consistently select significant variable while achieving satisfactory accuracy.

**Model compression:** An emerging demand of machine learning models is to reduce the model size while retaining a comparable prediction performance to address limitations in computation and memory.
We investigated a fundamental problem in model pruning: quantifying how much one can prune a model with theoretically guaranteed accuracy degradation. Insipred by the developed theory, we proposed a data-driven, adaptive pruning algorithm [1, 6].




# **Publications**{:style='color:#6f6fd9'}

### **Peer-reviewed**

\* indicates equal contributions, <sup>†</sup> indicates corresponding author(s)

[1] Enmao Diao\*, **Ganghua Wang**\*, Jie Ding, Yuhong Yang, and Vahid Tarokh<sup>†</sup>. “Pruning deep neural networks from a sparsity perspective”. Proc. ICLR (2023) [[pdf]](https://openreview.net/pdf?id=i-DleYh34BM)

[2] Gen Li, **Ganghua Wang**, and Jie Ding<sup>†</sup>. “Provable Identifiability of ReLU Neural Networks via LASSO Regularization”. IEEE Trans. Inf. Theory (2023) [[pdf]](https://ieeexplore.ieee.org/document/10121469)

[3] Xun Xian\*, **Ganghua Wang**\*, Jayanth Srinivasa, Ashish Kundu, Xuan Bi, Mingyi Hong, and Jie Ding. “Understanding backdoor attacks through the adaptability hypothesis”. Proc. ICML (2023). [[pdf]](https://openreview.net/pdf?id=iIuLNEnOue)

[4] **Ganghua Wang**,  Jie Ding,  and Yuhong Yang<sup>†</sup>.  “Regression with Set-Valued  Categorical Predictors”. Statistica Sinica, (2022) [[pdf]](https://www3.stat.sinica.edu.tw/ss_newpaper/SS-2021-0332_na.pdf)

### **Under Review**

[5] **Ganghua Wang**<sup>†</sup>, Ali Payani, Myungjin Lee, and Ramana Kompella. “Federated learning with group bias mitigation: beyond local fairness”. arXiv prepreint (2023) [[pdf]](https://arxiv.org/pdf/2305.09931.pdf)

[6] Wenjing Yang\*, **Ganghua Wang**\*, Jie Ding, and Yuhong
Yang<sup>†</sup>. “A Theoretical Understanding of Neural Network Compression from Sparse Linear Approximation”. arXiv preprint (2022) [[pdf]](https://arxiv.org/pdf/2206.05604.pdf)

[7] **Ganghua Wang**\*, Xun Xian\*, Jayanth Srinivasa, Ashish Kundu, Xuan Bi, Mingyi Hong, Yuhong Yang, and Jie Ding. “A Statistical Learning Perspective of Backdoor Attacks”. Preprint (2023).

[8] **Ganghua Wang** and  Jie Ding<sup>†</sup>. “Subset Privacy: Draw from an Obfuscated Urn”. arXiv preprint (2021). [[pdf]](https://arxiv.org/pdf/2107.02013.pdf)

[9]  Xun Xian\*, **Ganghua Wang**\*, Jayanth Srinivasa, Ashish Kundu, Xuan Bi, Mingyi Hong, and Jie Ding. “A Unified Framework for Inference-Stage Backdoor Defenses”. Preprint (2023)

### **Manuscript**

[10] **Ganghua Wang**, Jie Ding, and Yuhong Yang<sup>†</sup>. “Model Privacy: A Framework to Understand Model Stealing Attack and Defense”. Manuscript 