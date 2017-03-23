---
title: Linearity, Linear combination
category: Linear Algebra
tag: Linear Discriminant Analysis
html header: <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_SVG"></script>
---

이번 포스팅에선 **선형대수학(Linear Algebra)**의 **선형성(linearity)**, **선형결합(linear combination)** 등 주요 개념을 중심으로 기본을 짚어보도록 하겠습니다. 이번 글은 [고려대 박성빈 교수님]([hyperspace@korea.ac.kr](mailto:hyperspace@korea.ac.kr))과 [한양대 이상화 교수님](http://www.kocw.net/home/search/kemView.do?kemId=977757) 강의를 참고했음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 선형성

선형성이란 직선처럼 똑바른 도형, 또는 그와 비슷한 성질을 갖는 대상이라는 뜻으로, 함수의 경우 그 모양이 '직선'이라는 의미로 사용됩니다. 수학에서 선형성의 정의는 다음과 같습니다. 임의의 수 x, y와 함수 f에 대해 아래 두 조건을 동시에 만족해야 합니다.

> **superposition** : f(x+y) = f(x) + f(y)
>
> **homogeneity** : 임의의 수 a에 대해 f(ax) = af(x)

위 조건을 만족하는 예로는 1차 다항함수(y=mx), 미분/적분연산 등이 있습니다. 또한 행렬과 벡터 곱셈(multiplication)도 선형성을 가집니다. 다만 여기서 주의해야할 것은 원점을 지나지 않는 직선의 방정식(예를 들면 y=2x+1)은 위 선형성 조건에 위배됨을 확인할 수 있습니다. 원점을 통과하지 않는 직선에 굳이 선형성을 정의하려면 **x의 변화량과 y의 변화량에 선형성이 있다** 정도로 언급해야 할 것입니다. 선형대수학은 기본적으로 선형성을 지닌 방정식이나 함수에 대해 다룹니다.



## 1차 연립방정식 풀이의 두 가지 접근

보통 고등학교 수학과정에선 두 개의 1차 연립방정식의 해를 찾을 때 2차원 사분면에 두 개 직선을 그려, 두 직선의 교점을 찾는 것으로 설명을 하곤 합니다. 다시 말해 아래 그림과 같습니다.



$$3x-y=-2\\ x+y=2$$



<a href="http://imgur.com/Al0vdJ2"><img src="http://i.imgur.com/Al0vdJ2.png" title="source: imgur.com" /></a>



위 직선의 방정식은 아래와 같이 고쳐쓸 수 있습니다.

$$x\begin{bmatrix} 3 \\ 1 \end{bmatrix}+y\begin{bmatrix} -1 \\ 1 \end{bmatrix}=\begin{bmatrix} -2 \\ 2 \end{bmatrix}$$

