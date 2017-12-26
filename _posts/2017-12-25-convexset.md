---
title: Convex Sets
category: Convex optimization
tag: [Convex Sets]
---

이번 글에서는 **Convex Set(볼록집합)**과 관련된 개념들을 살펴보도록 하겠습니다. 이 글은 미국 카네기멜런대학 [강의](http://www.stat.cmu.edu/~ryantibs/convexopt/)를 기본으로 하되 저희 연구실의 김해동 석사과정이 만든 자료를 정리했음을 먼저 밝힙니다. 영문 위키피디아 또한 참고하였습니다. 그럼 시작하겠습니다.





## 벡터 결합하기

벡터 $x_1$, $x_2$, ..., $x_n$이 주어졌을 때 이들을 결합하는 것은 다음 세 가지 방식이 있습니다.

- **[Linear combination](https://ratsgo.github.io/linear%20algebra/2017/03/24/Ldependence/)** : $α_1x_1+...+α_nx_n$ ($α_i$는 실수)
- **Affine combination** : $α_1x_1+...+α_nx_n$ ($Σ_iα_i=1$)
- **Convex combination** : $α_1x_1+...+α_nx_n$ ($Σ_iα_i=1$이고, $0≤α_i≤1$)

*affine combination*에 대해 **닫힌(closed)** 집합을 **Affine set**이라고 합니다. 예컨대 벡터 $x_1$, $x_2$가 집합 $A$에 속해 있고, 이들의 *affine combination* 또한 $A$에 속할 때 $A$는 *affine set*이 됩니다. 마찬가지로 *convex combination*에 대해 닫힌 집합을 *convex set*이라고 합니다.

2차원 벡터 두 개(즉 $x_1$, $x_2$)를 세 가지 방식으로 결합해 각각 나타내면 다음 그림과 같습니다. 



<a href="https://imgur.com/ANZXnOV"><img src="https://i.imgur.com/ANZXnOV.png" width="500px" title="source: imgur.com" /></a>



- *linear combination* 결과 $x_1$과 $x_2$를 포함하는 $R^2$의 평면이 **생성(span)**된다.
- 2차원 공간의 *affine set*은 $x_1$과 $x_2$를 지나는 직선이다.
- 2차원 공간의 *convex set*은 $x_1$과 $x_2$를 연결하는 선분이다.

벡터 $x_1$과 $x_2$의 *affine set*이 직선, *convex set*이 선분이 되는 것과 관련해서는 고1 수학 과정의 [내분과 외분](http://mathbang.net/439)과 연관성이 있을 거란 생각이 듭니다. 다시 말해 벡터 앞에 붙는 계수의 부호가 중요하다는 이야기이죠.





## Convex Set

*convex set* $C$는 다음과 같이 정의됩니다.

- $x$와 $y$가 $C$에 속한다면, $tx+(1-t)y$ 또한 $C$에 포함된다. ($0≤t≤1$)

직관적으로 따져보겠습니다. 어떤 집합 $C$에 속한 임의의 두 점을 골랐을 때 둘을 연결하는 선분 또한 $C$에 포함될 경우 $C$를 *convex set*이라고 합니다. 따라서 다음 도형은 *convex set*입니다.

 <a href="https://imgur.com/0Gec7Rf"><img src="https://i.imgur.com/0Gec7Rf.png" width="150px" title="source: imgur.com" /></a>



다음은 *convex set*이 아닙니다. 아래 두 점을 잇는 선분의 일부가 해당 집합 바깥에 있기 때문입니다.



<a href="https://imgur.com/PToXoC0"><img src="https://i.imgur.com/PToXoC0.png" width="170px" title="source: imgur.com" /></a>



마찬가지로 다음은 *convex set*이 아닙니다. 임의의 두 점이 경계에 있을 경우 해당 점을 잇는 선분의 일부가 집합에 포함되어 있지 않습니다.



<a href="https://imgur.com/cWdQQtc"><img src="https://i.imgur.com/cWdQQtc.png" width="150px" title="source: imgur.com" /></a>





## Convex set의 종류

*convex set*의 예는 다음과 같습니다.



<a href="https://imgur.com/wq0WY58"><img src="https://i.imgur.com/wq0WY58.png" width="450px" title="source: imgur.com" /></a>



*Norm ball*의 예시는 다음과 같습니다. ($x_1, x_2$의 L2 norm, *radius* $y$에 대한 집합) $y$축을 기준으로 잘라보면 그 모양이 원 모양이고 볼록해 *convex set*을 만족하리라고 직관적으로 추론해볼 수 있습니다.



<a href="https://imgur.com/GKHpfjL"><img src="https://i.imgur.com/GKHpfjL.png" width="250px" title="source: imgur.com" /></a>



*Hyperplane* $a^Tx=b$ 위의 임의의 두 점 $x_1$, $x_2$ 사이를 잇는 선분은 다시 $a^Tx=b$에 포함됩니다. 따라서 *Hyperplane*은 *convex set*입니다. 마찬가지 이유로 *Halfspace*, *Affine space* 또한 *convex set*이 됩니다.

*Polyhedron*은 다음과 같이 정의되며 그 예시는 다음 그림과 같습니다.

- {$x$\|$Ax≤b$}

<a href="https://imgur.com/tGrzXL3"><img src="https://i.imgur.com/tGrzXL3.png" width="300px" title="source: imgur.com" /></a>

행렬 $A$에 벡터 $x$를 내적한 결과인 $b$는 벡터일 것입니다. 이를 잠시 다시 생각해보면 선형부등식 여러 개가 한꺼번에 적용된 거라고 보아도 될 것 같습니다. 예를 들어 '행렬 $A$의 첫번째 벡터와 $x$를 내적한 결과는 벡터 $b$의 첫번째 스칼라값보다 작거나 같다'는 식으로 말이죠. 

*Polyhedron*은 **선형계획법(linear)**에서 중요하게 다뤄진다고 하는데요. 각각의 선형부등식이 제약식 역할을 수행하며 결과적으로 *Polyhedron*은 해당 제약 조건 하의 가능해(possible solutions) 영역이 된다는 것입니다. 어쨌거나 *Polyhedron* 또한 *convex set*입니다.

*simplex*는 삼각형 또는 사면체(tetrahedron)의 일반화 버전이라고 합니다. *simplex* 역시 *convex set*입니다.



<a href="https://imgur.com/uLioyc4"><img src="https://i.imgur.com/uLioyc4.png" width="500px" title="source: imgur.com" /></a>





## convex set의 성질

*convex set*과 관련해 두 가지 중요한 정리가 있습니다. 첫번째는 *sepaating hyperplane theorem*입니다. 두 개의 겹치지 않는(disjoint) *convex set*을 분리해주는 하이퍼플레인(hyperplane)이 존재한다는 것입니다. 아래 그림에서 $D$와 $C$를 가르는 벡터 $a$가 바로 그러한 역할을 하는 하이퍼플레인입니다. 

단 여기에서 $D$와 $C$는 **닫힌집합**(closed set, 스스로의 경계를 모두 포함하는 위상공간의 부분집합)이어야 하며, 둘 중 하나가 **유계집합**(bounded set, 유한한 영역을 가지는 집합)이어야 합니다.



<a href="https://imgur.com/AXf0pbp"><img src="https://i.imgur.com/AXf0pbp.png" width="300px" title="source: imgur.com" /></a>



두번째는 *supporting hyperplane theorem*입니다. *convex set*의 경계 점을 지나는 접선이 항상 존재한다는 것입니다. 다음 그림과 같습니다.



<a href="https://imgur.com/NGqIA7I"><img src="https://i.imgur.com/NGqIA7I.png" width="250px" title="source: imgur.com" /></a>





## convexity를 보존하는 연산

*convex set* $C$와 $D$에 대해 다음 연산(operation)은 *convexity*를 보존합니다. 다시 말해 $C$와 $D$가 *convex set*이라는 사실이 증명돼 있고, 다음 연산을 수행한다면 연산 수행 결과로 나타난 새로운 집합은 별도의 증명 없이도 *convex set*이라는 겁니다.

- **intersection**(교집합)
- **scaling and translation**(스칼라곱, bias 더하기) : $C$가 *convex set*이라면 $aC+b$ 또한 *convex set* ($a,b$는 스칼라)
- **affine images and preimages** : $f(x)=Ax+b$이고 $C$가 *convex set*이라면 $f(C)$ 또한 *convex set*, $f(x)=Ax+b$이고 $D$가 *convex set*이라면 $f^{-1}(D)$ 또한 *convex set*

이밖에 다음 연산도 *convexity*를 보존합니다.



<a href="https://imgur.com/CKJWcgD"><img src="https://i.imgur.com/CKJWcgD.png" width="450px" title="source: imgur.com" /></a>