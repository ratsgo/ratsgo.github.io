---
title: Representation Learning
category: Deep Learning
tag: Representation Learning
---

이번 글에서는 **representation learning** 개념에 대해 살펴보도록 하겠습니다. 딥뉴럴네트워크가 높은 성능을 내는 배경에는 복잡한 데이터 공간을 선형 분류가 가능할 정도로 단순화해 표현하기 때문이라는 이론인데요. 저도 공부하는 입장이니 많은 의견 부탁드립니다. 

이번 글은 김현중, 고태훈 서울대 박사과정이 진행한 2017년 패스트캠퍼스 강의를 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 선형 모델의 한계

**다중선형회귀(Multiple Linear Regression)**는 설명변수(X)와 종속변수(Y) 사이의 관계를 선형으로 가정하고, 데이터와의 오차가 가장 작은 **직선**을 찾는 것을 목표로 합니다. 분류 문제도 마찬가지인데요. [선형판별분석(Linear Discriminant Analysis)](https://ratsgo.github.io/machine%20learning/2017/03/21/LDA/)이나 [로지스틱 회귀분석(Logistic Regression)](https://ratsgo.github.io/machine%20learning/2017/04/02/logistic/)도 항상 선형 분류 경계면을 만들어 냅니다. 

이를 시각적으로 이해해 보면, 아래 그림의 경우 모델의 학습 결과로 하나의 직선(hyperplane), 즉  $[-1,1,1]^T$가 도출된 것을 확인할 수 있습니다. 선형 모델은 바로 이런 직선을 찾는 것이 학습의 목표가 됩니다.

<a href="http://imgur.com/nnfHiIx"><img src="http://i.imgur.com/nnfHiIx.png" width="500px" title="source: imgur.com" /></a>

하지만 XOR 문제와 같이 데이터가 선형 관계가 아닐 경우 이들 모델은 높은 성능을 낼 수 없습니다. 아래 그림처럼 어떤 직선을 그어도 두 범주를 분류할 수가 없게 되거든요. 뉴럴네트워크의 할아버지격인 **퍼셉트론(Perceptron)**이 제시된 배경이기도 합니다.

<a href="http://imgur.com/hEJRUQT"><img src="http://i.imgur.com/hEJRUQT.png" width="250px" title="source: imgur.com" /></a>



## 뉴럴네트워크의 기본 구조

뉴럴네트워크를 이해해 보겠다면서 선형모델의 한계를 먼저 언급하고 있는 이유는 뉴럴네트워크의 본질이 사실상 **선형 모델**이기 때문입니다. 아래 그림은 뉴럴네트워크를 구성하고 있는 하나의 **뉴런(neuron)**을 나타낸 것입니다. 보시다시피 **활성함수(activation function)** 적용 직전의 값들은 가중치($w_i$)와 입력값($x_i$) 사이의 **선형결합(linear combination)**임을 확인할 수 있습니다. (아래 그림은 미국 스탠포드대학의 CS231n 강좌에서 퍼왔습니다)

<a href="http://imgur.com/euw7qQu"><img src="http://i.imgur.com/euw7qQu.png" width="500px" title="source: imgur.com" /></a>

다만 여기에서 활성함수에 주목해야 합니다. 퍼셉트론과 뉴럴네트워크의 큰 차이점 가운데 하나는 바로 활성함수 여부에 있거든요. 활성함수는 보통 시그모이드, 하이퍼볼릭탄젠트, ReLU 등과 같이 비선형 함수를 씁니다. 이를 통해 선형모델의 한계를 극복하고자 한 것이죠. 활성함수에 대한 자세한 내용은 [이곳](https://ratsgo.github.io/deep%20learning/2017/04/22/NNtricks/)을 참고하시기 바랍니다.



## XOR문제를 풀기 위한 단순 뉴럴네트워크

그럼 XOR 예시를 통해 뉴럴네트워크가 Representation Learining와 어떤 관련을 맺고 있는지 살펴보겠습니다. 아래 중앙 그림과 같은 XOR 문제를 풀기 위해 층이 두 개인 단순 뉴럴네트워크를 구축해 보겠습니다. 

학습 결과 1층 첫번째 뉴런의 $h_1$이 아래 식처럼 도출될 경우 분류경계면은 하단 중앙의 연두색 선이 되고, 네트워크 전체 구조는 하단 좌측의 그림이 될 겁니다.


$$
{ h }_{ 1 }={ x }_{ 1 }+{ x }_{ 2 }-\frac { 3 }{ 2 }
$$

<a href="http://imgur.com/bHebe4m"><img src="http://i.imgur.com/bHebe4m.png" width="700px" title="source: imgur.com" /></a>

1층 첫번째 뉴런의 출력값인 $z_1$은 입력값과 가중치들의 선형결합으로 이뤄진 $h_1$이 활성함수($g$)에 의해 활성화된 것입니다. 뉴럴네트워크는 퍼셉트론과 흡사하나 활성함수가 추가됐다는 점이 다르다고 합니다. $g$는 아래와 같이 단순한 비선형 함수입니다.

$${ z }_{ 1 }=g({ h }_{ 1 })=\begin{Bmatrix} 1\quad if\quad { h }_{ 1 }\ge 0 \\ 0\quad if\quad { h }_{ 1 }<0 \end{Bmatrix}$$

이번엔 1층 두번째 뉴런의 출력값 $z_2$를 만들어 보겠습니다. $h_2$는 아래와 같고요, 활성함수는 $g$ 그대로 입니다.


$$
{ h }_{ 2 }={ x }_{ 1 }+{ x }_{ 2 }-\frac { 5 }{ 2 },\quad  { z }_{ 2 }=g({ h }_{ 2 })
$$
<a href="http://imgur.com/oOHrFYK"><img src="http://i.imgur.com/oOHrFYK.png" width="700px" title="source: imgur.com" /></a>

자, 이제 거의 다 왔습니다. 이번엔 전체 네트워크의 출력값 $z$를 만들어 보겠습니다. 학습 결과물은 다음과 같다고 칩시다. 


$$
{ o }_{ 1 }={ z }_{ 1 }-{ z }_{ 2 }-1,\quad  z=g({ o }_{ 1 })
$$
<a href="http://imgur.com/qTgnxBd"><img src="http://i.imgur.com/qTgnxBd.png" width="600px" title="source: imgur.com" /></a>

최종 결과물 $z$를 보시면 동그라미와 네모 두 범주를 잘 분리하고 있는 점을 확인할 수 있습니다.



## 뉴럴네트워크와 Represention Learning

위에서 예시로 든 단순 뉴럴네트워크의 학습과정을 좌표 축 위에 그리면 아래 그림과 같습니다. 이 모델의 첫번째 층은 입력값 $(x_1, x_2)$를 받아서 $(z_1, z_2)$를 출력합니다. 이 덕분에 모델의 두번째 층은 **직선** 하나만으로도 데이터의 범주를 분리해낼 수 있게 됐습니다. 기존대로라면 선형으로 분리할 수 없는 데이터가 선형 분리가 가능하게끔 데이터가 변형됐다는 얘기입니다. 다시 말해 뉴럴네트워크의 학습 과정에서 데이터의 **representaion**이 $(x_1, x_2)$에서 $(z_1, z_2)$로 바뀐 겁니다.

<a href="http://imgur.com/udEynOf"><img src="http://i.imgur.com/udEynOf.png" width="300px" title="source: imgur.com" /></a>

이 글에서는 설명의 편의를 위해 단순 뉴럴네트워크를 예로 들었으나, 깊고 방대한 뉴럴네트워크는 학습데이터가 꽤 복잡한 represention이어도 이를 선형 분리가 가능할 정도로 단순화하는 데 좋은 성능을 낸다고 합니다. 이 때문에 뉴럴네트워크를 **representation learner**라고 부르는 사람들도 있습니다.





