---
title: 어텐션 매커니즘
category: From frequency to semantics
tag: attention
---

이번 글에서는 딥러닝 모델이 특정 벡터에 주목하게 만들어 모델의 성능을 높이는 기법인 **어텐션(attention)** 매커니즘에 대해 살펴보도록 하겠습니다. 이 글은 미국 스탠포드 대학의 CS224d 강의와 [원 논문](https://arxiv.org/abs/1409.0473)을 정리하였음을 먼저 밝힙니다. 혹시 제가 잘못 알고 있는 점이나 보완할 점 있다면 댓글로 알려주시면 감사하겠습니다. 그럼 시작하겠습니다.



## 동기

어텐션 매커니즘은 기계번역(machine translation)을 위한 sequence-to-sequence 모델(S2S)에 처음 도입됐습니다. S2S 아키텍처를 간단히 나타낸 그림은 다음과 같습니다. 소스랭귀지($A,B,C$)를 입력으로 해서 벡터로 만드는 앞부분을 인코더(encoder), 인코더가 출력한 벡터를 입력으로 해서 타겟랭귀지($W,X,Y,Z$)를 출력하는 뒷부분을 디코더(decoder)라고 합니다.

<a href="https://imgur.com/6mbfPZR"><img src="https://i.imgur.com/6mbfPZR.png" width="500px" title="source: imgur.com" /></a>

그런데 여기에서 소스랭귀지와 타겟랭귀지의 길이가 길어질 수록 모델의 성능이 나빠집니다. $W$를 예측할 때 $A,B,C$ 모두에 집중해 보게 되면 정확도가 떨어질 수 있습니다. 모델로 하여금 '중요한 부분만 집중(attention)하게 만들자'가 어텐션 매커니즘의 핵심 아이디어가 되겠습니다.





## 핵심 아이디어

예컨대 독일어 "Ich mochte ein bier"를 영어 "I'd like a beer"로 번역하는 S2S 모델을 만든다고 칩시다. 모델이 네번째 단어인 'beer'를 예측할 때 'bier'에 주목하게 만들고자 합니다. 어텐션 매커니즘의 가정은 **인코더가 'bier'를 받아서 벡터로 만든 결과(인코더 출력)는 디코더가 'beer'를 예측할 때 쓰는 벡터(디코더 입력)와 유사할 것**이라는 점입니다.





## 인코더 계산과정

먼저 인코더 계산과정을 살펴보겠습니다. 인코더는 $i$번째 단어벡터 $x_i$를 받아서 그에 해당하는 히든스테이트 벡터 $h_i$를 만듭니다. 이후 $h_i$가 $i$번째 열벡터가 되도록 행렬 형태로 차곡차곡 쌓아놓습니다. 이 행렬을 $F$라고 정의합시다. 아래 그림은 양방향(bi-directional) 모델을 가정한 것입니다.



<a href="https://imgur.com/CbQjPWo"><img src="https://i.imgur.com/CbQjPWo.png" width="400px" title="source: imgur.com" /></a>





## 디코더 계산과정

$e_{ij}$는 디코더가 $i$번째 단어를 예측할 때 쓰는 직전 스텝의 히든스테이트 벡터 $s_{i-1}$이 인코더의 $j$번째 열벡터 $h_j$와 얼마나 유사한지를 나타내는 스코어(스칼라)값입니다. 예컨대 어텐션 매커니즘이 제대로 작동한다면 'bier'에 해당하는 디코더 출력 벡터와 'beer'를 예측할 때 쓰이는 인코더 입력벡터의 유사도가 높게 나타날 겁니다. 다음과 같이 정의됩니다.


$$
{ e }_{ ij }=a\left( { s }_{ i-1 },{ h }_{ j } \right) 
$$


위 식에서 $a$는 원 논문에는 alignment model이라 소개돼 있습니다. $s_{i-1}$과 $h_j$ 간 유사도를 잘 뽑아낼 수 있다면 다양한 변형이 가능하다고 합니다. 실제로 $e_{ij}$를 구할 때 쓰이는 $a$는 (1) $F^TVs_{i-1}$ (2) $v^T\tanh{(WF+Vs_{i-1})}$ 등 다양하게 쓰입니다. 여기에서 $v, V, W$ 등은 어텐션을 적용하기 위한 학습 파라메터입니다.

$e_{ij}$에 소프트맥스 함수를 적용해 합이 1이 되도록 확률값으로 변환합니다. $T_x$는 디코더 입력 단어의 수를 가리킵니다.


$$
\alpha _{ ij }=\frac { exp\left( { e }_{ ij } \right)  }{ \sum _{ k=1 }^{ { T }_{ x } }{ exp\left( { e }_{ ik } \right)  }  } 
$$


디코더가 $i$번째 단어를 예측할 때 쓰이는 attention vector $a_i$는 다음과 같이 정의됩니다.


$$
\overrightarrow { \alpha _{ i } } =\left[ { \alpha  }_{ i1 },{ \alpha  }_{ i2 },...,{ \alpha  }_{ i{ T }_{ x } } \right] 
$$


디코더가 $i$번째 단어를 예측할 때 쓰이는 context vector $c_i$는 다음과 같이 정의됩니다. 인코더의 $j$번째 열벡터를 어텐션 확률값으로 가중합을 한 것이라고 볼 수 있겠습니다. 


$$
\overrightarrow { { c }_{ i } } =\sum _{ j=1 }^{ { T }_{ x } }{ { \alpha  }_{ ij }{ h }_{ j } } =F \overrightarrow { { \alpha  }_{ i } }
$$




## 디코더 계산 예시

디코더에서 계산되는 과정을 나타낸 그림은 다음과 같습니다. alignment model $a$는 디코더가 2번째 단어 'like'를 예측할 때 쓰이는 첫번째 히든스테이트 벡터 $s_1$과 가장 유사한 인코더의 열벡터가 $h_2$라고 판단했습니다. 디코더가 2번째 단어를 예측할 때 쓰이는 attention vector $α_2$를 보면 두번째 요소값이 가장 높기 때문입니다.



<a href="https://imgur.com/4zdzDKL"><img src="https://i.imgur.com/4zdzDKL.png" width="300px" title="source: imgur.com" /></a>



디코더가 2번째 단어를 예측할 때 쓰이는 context vector $c_2$는 인코더 출력벡터들로 구성된 행렬 $F$에 $α_2$를 내적해 구합니다. 인코더 모델은 타겟랭귀지 단어벡터(I'd)와 $c_2$를 concat해서 현시점의 히든스테이트 벡터 $s_i$를 만들어 냅니다.



