---
layout: post
title:  "Latex related topics"
date:   2019-10-10 22:25:55 -0500
categories: tools


---

A learning note for latex.

## For symbols

- [Quick reference](/assets/resource/Symbols.pdf)

- Using Roman

  ```latex
  \makeatletter
  \newcommand*{\rom}[1]{\expandafter\@slowromancap\romannumeral #1@}
  \makeatother
  ```

  `\romannumeral` is $\LaTeX$  kernel primitive

  Alternatively, using packages like `\usepackage{romannum}` 

- Put word/symbol above a symnol

  ```latex
  \overset{}
  ```

  For arrows `\xRightarrow[below]{above}`
  
- Accents, Special letters

  [Accents](https://i.stack.imgur.com/fQHoV.png)

  Link to TeX overflow: [Here](https://tex.stackexchange.com/questions/8857/how-to-type-special-accented-letters-in-latex).

  OS based method, directly type accents: [Here](https://spanish.meta.stackexchange.com/questions/10/easy-way-to-type-accented-characters). For Macintosh, option+e+LETTER.

## Figures and Tables

- Mixed Alignment 

  - `floatrow` Based Solution
  
    ```latex
    \begin{figure}
    	\CenterFloatBoxes
    	\begin{floatrow}
    		\ffigbox[\FBwidth]
    		{\cpation{figure caption goes here}\label{fig: figure-label}}
    		{figure puts here}
    		\killfloatstyle\ttabbox[\Xhsize]
    		{\caption{table caption goes  here}\label{tab: table-label}}
    		{table puts here}
    	\end{floatrow}
    \end{figure}
    ```
  
    - In two column environment, `\begin{figure}...\end{figure}` should be replaced by `\begin{figure*}...\begin{figure*}` if you want your mixed results occupy both of the columns.
    - If you have used `float` package, you can not use this solution. Because they are incompitable.
  
  - `minipage` Based Solution
  
    For each minipage, use `\captionsetup{type=...}` to change float type.

