---
title: Clustering 개요
category: Machine Learning
tag: Clustering
---

이번 글에서는 **클러스터링(Clustering;군집화)**의 전반적 내용에 대해 살펴보도록 하겠습니다. 이번 글은 고려대 강필성 교수님과 역시 같은 대학의 김성범 교수님 강의를 정리했음을 먼저 밝힙니다. 이 글은 클러스터링의 개괄적 내용을 설명하는 데 방점을 두었으니 [K-means 군집화](https://ratsgo.github.io/machine%20learning/2017/04/19/KC/), [계층적 군집화](https://ratsgo.github.io/machine%20learning/2017/04/18/HC/) 등 구체적 알고리즘을 살펴보시려면 링크를 클릭하시기 바랍니다. 그럼 시작하겠습니다.



## 클러스터링의 목적

클러스터링의 목적은 간단합니다. 비슷한 개체끼리 한 그룹으로, 다른 개체는 다른 그룹으로 묶어보자는 겁니다. 이를 좀 있어보이게 표현하면 아래와 같습니다.

<p class="message">
(1) 군집 간 분산(inter-cluster variance) 최대화<br>

(2) 군집 내 분산(inner-cluster variance) 최소화

</p>

다만 여기서 주의해야 할 것은 클러스터링은 **분류(Classification)**와 구별해야 한다는 점입니다. 클러스터링은 정답이 없는 **비지도학습(unsupervised learning)**입니다. 다시 말해 각 개체의 그룹 정보 없이 비슷한 개체끼리 묶어보는 거죠. 반면 분류는 정답이 있는 **지도학습(supervised learining)**입니다. 분류 과제를 수행할 때는 데이터의 독립변수($X$)로 종속변수($Y$)를 예측하도록 학습을 진행하게 됩니다.



## 군집 타당성 평가

클러스터링 과업은 정답이 없기 때문에 일반적인 머신러닝 알고리즘처럼 **단순정확도(Accuracy)** 등 지표로 평가할 수 없습니다. 아래 예에서 볼 수 있듯 최적의 군집 개수를 정답 없이 알아내기란 쉽지 않습니다.

<a href="http://imgur.com/OhVcSqb"><img src="http://i.imgur.com/OhVcSqb.png" width="500px" title="source: imgur.com" /></a>

그렇다고 해서 군집이 제대로 만들어졌는지 평가할 수 있는 방법이 아주 없지는 않습니다. 군집을 만든 결과가 얼마나 유용한지 따지는 **군집타당성지표(Clustering Validity Index)**가 있기 때문입니다. 군집타당성지표는 아래 그림처럼 (1) 군집 간 거리 (2) 군집의 지름 (3) 군집의 분산 등을 고려합니다. 다시 말해 군집 간 분산과 군집 내 분산을 따진다는 겁니다. 이번 글에서는 **Dunn Index**와 **Silhouette** 두 가지 지표를 살펴보겠습니다.

<a href="http://imgur.com/dFliYHp"><img src="http://i.imgur.com/dFliYHp.png" width="600px" title="source: imgur.com" /></a>



### Dunn Index

Dunn Index는 군집 간 거리의 최소값(하단 좌측)을 분자, 군집 내 요소 간 거리의 최대값(하단 우측)을 분모로 하는 지표입니다. 

$$I(C)=\cfrac { \min _{ i\neq j }{ \{ { d }_{ c }({ C }_{ i },{ C }_{ j })\}  }  }{ \max _{ 1\le l\le k }{ \{ \triangle ({ C }_{ l })\}  }  } $$

군집 간 거리는 멀수록, 군집 내 분산은 작을 수록 좋은 군집화 결과라 말할 수 있는데요. 이 경우에 Dunn Index는 커지게 됩니다.

<a href="http://imgur.com/TClWvss"><img src="http://i.imgur.com/TClWvss.png" width="500px" title="source: imgur.com" /></a>



### Silhouette

실루엣 지표를 계산하는 식은 아래와 같습니다.

$$s(i)=\frac { b(i)-a(i) }{ \max { \{ a(i),b(i)\}  }  } $$

여기에서 $a(i)$는 $i$번째 개체와 같은 군집에 속한 요소들 간 거리들의 평균입니다. $b(i)$는 $i$번째 개체와 다른 군집에 속한 요소들 간 거리들의 평균을 군집마다 각각 구한 뒤, 이 가운데 가장 작은 값을 취한 것입니다. 다시 말해 $b(i)$는 $i$번째 개체가 속한 군집과 가장 가까운 이웃군집을 택해서 계산한 값이라고 보시면 됩니다.

예컨대 아래처럼 파란색 군집 안에 있는 네모 박스에 해당하는 개체를 중심으로 실루엣 지표를 구할 수 있습니다. 이 경우 $a(i)$는 네모 개체와 파란색 군집 내 개체들 사이의 거리들의 평균이고요. $b(i)$는 네모 개체와 오렌지색 군집 내 개체들 사이의 거리들의 평균을 의미합니다.

<a href="http://imgur.com/VfvGewn"><img src="http://i.imgur.com/VfvGewn.png" width="500px" title="source: imgur.com" /></a>

가장 이상적인 경우라면 $a(i)$가 0일 겁니다. 한 군집의 모든 개체가 한치도 떨어져 있지 않고 붙어있는 경우가 여기에 해당합니다. 그러면 실루엣 지표는 1이 됩니다. 최악의 경우에는 $b(i)$가 0입니다. 서로 다른 군집이 전혀 구분되지 않는 경우입니다. 이 때 실루엣 지표는 -1이 됩니다. 보통 실루엣 지표가 0.5보다 크면 군집 결과가 타당한 것으로 평가하게 된다고 합니다.



## 클러스터링의 종류

클러스터링에는 몇 가지 종류가 있는데 다음과 같습니다.

> **hard clustering** : 한 개체가 여러 군집에 속하는 경우를 허용하지 않는 군집화 방법입니다
>
> **soft clustering** : 한 개체가 여러 군집에 속할 수 있습니다.

> **pational clustering** : 전체 데이터의 영역을 특정 기준에 의해 동시에 구분하는 군집화 방법입니다. 각 개체들은 사전에 정의된 개수의 군집 가운데 하나에 속하게 됩니다. [K-mean 군집화](https://ratsgo.github.io/machine%20learning/2017/04/19/KC/)가 대표적입니다.
>
> [**hiarchical clustering**](https://ratsgo.github.io/machine%20learning/2017/04/18/HC/) : 개체들을 가까운 집단부터 차근차근 묶어나가는 방식입니다. 군집화 결과뿐 아니라 유사한 개체들이 결합되는 **덴드로그램(dendrogram)**을 생성합니다.

> [**Self-Organizing Map**](https://ratsgo.github.io/machine%20learning/2017/05/01/SOM/) : 뉴럴넷 기반의 군집화 알고리즘입니다.
>
> [**Spectual clustering**](https://ratsgo.github.io/machine%20learning/2017/04/27/spectral/) : 그래프 기반의 군집화 방법론입니다

