---
title: 머신러닝 기법 간 비교
category: Machine Learning
tag: comparison
---

이번 글에서는 다양한 머신러닝 모델을 서로 비교해 보면서 각 모델의 특징을 살펴보도록 하겠습니다. 이번 글은 [An Introduction to Stastical Learning](http://www-bcf.usc.edu/~gareth/ISL/)을 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## 선형회귀 vs K-NN

선형회귀는 **모수적 기법(parametric method)**입니다. 1차 선형식 모델을 가정하기 때문이죠. 명시적인 함수 형태의 모델을 가정하지 않는 비모수적 기법(non-parametric method)도 있습니다. 대표적인 것이 K-nearest Neighbors Regression 기법(K-NN)이 있습니다. 특정 데이터 포인트($x_0$)의 주변 $K$ 이웃의 $y$값 평균으로 회귀 문제를 풉니다. 선형회귀와 관련 자세한 내용은 [이곳](https://ratsgo.github.io/machine%20learning/2017/07/03/regression/)을, K-NN과 관련 자세한 내용은 [이곳](https://ratsgo.github.io/machine%20learning/2017/04/17/KNN/)을 참고하시면 좋을 것 같습니다.

데이터의 분포 양상과 모수적 모델이 가정하는 모양이 일치할 경우, 모수적 기법의 성능은 비모수적 모델보다 좋은 경향이 있다고 합니다. 아래 그림을 보겠습니다.

 

<a href="https://imgur.com/I2hVsTK"><img src="https://i.imgur.com/I2hVsTK.png" width="500px" title="source: imgur.com" /></a>



위 그림 왼쪽의 검정색 실선은 $x$와 $y$의 실제 관계를 나타냅니다. 그 관계가 선형(linear)임을 확인할 수 있습니다. 오른쪽 그림에서 검정색 점선은 선형회귀 모델, 녹색 실선은 K-NN의 오차를 나타냅니다. $x$와 $y$가 선형관계를 이루고 있어서, 선형관계를 가정하고 구축된 선형회귀 모델의 오차가 K-NN의 오차보다 작은 것을 확인할 수 있습니다.

하지만 데이터의 분포 양상과 모수적 모델이 가정하는 모양이 불일치할 경우, 비모수적 모델의 성능이 좋을 수 있습니다. 이와 관련해 다음 그림을 보겠습니다.



<a href="https://imgur.com/Zn4lVAX"><img src="https://i.imgur.com/Zn4lVAX.png" width="500px" title="source: imgur.com" /></a>



위 그림 왼쪽의 검정색 실선은 $x$와 $y$의 실제 관계를 나타냅니다. 비선형(non linear)임을 확인할 수 있습니다. 파란색 선은 $K$가 1일 때 K-NN의 예측곡선, 빨간색 선은 $K$가 9일 때 예측곡선을 가리킵니다. $K$가 클 수록 더 많은 이웃데이터를 고려해 예측하므로 곡선의 모양이 평탄화(smoothing)되는 걸 확인할 수 있습니다. 오른쪽 그림에서 검정색 점선은 선형회귀 모델, 녹색 실선은 K-NN의 오차를 나타냅니다. $x$와 $y$가 비선형 관계여서, 선형관계를 가정하고 구축된 선형회귀 모델의 오차가 K-NN보다 큰 것을 확인할 수 있습니다.

실제 분석에서는 K-NN보다는 선형회귀가 자주 쓰입니다. K-NN에서는 데이터의 차원 수가 커질 수록, 즉 변수가 많아질 수록 **차원의 저주(curse of dimensionality)** 현상이 나타나기 때문입니다. K-NN은 예측시 $K$개 이웃을 고려하는데, 고차원 데이터 공간에서는 특정 데이터 포인트에서 가장 가까운 이웃이라 하더라도 실제로는 그 거리가 매우 먼 경우가 많다고 합니다. 이 때문에 변수의 숫자($p$)가 커질 수록 K-NN의 오차가 커지는 경향이 있습니다. 다음 그림과 같습니다.



<a href="https://imgur.com/advxren"><img src="https://i.imgur.com/advxren.png" width="500px" title="source: imgur.com" /></a>







## LDA vs 로지스틱 회귀

범주 2개를 분류하는 선형판별분석(LDA)에서 데이터 $x$가 범주1일 확률을 $p_1(x)$, 범주2일 확률을 $p_2(x)$라고 두면 다변량 정규분포 확률함수로부터 다음과 같은 식을 유도할 수 있습니다. (LDA에서는 데이터가 정규분포를 따른다고 가정) LDA와 다음 식 유도와 관련해서는 [이곳](https://ratsgo.github.io/machine%20learning/2017/03/21/LDA/)을 참고하시면 좋을 것 같습니다.


$$
\log { \left( \frac { { p }_{ 1 }\left( x \right)  }{ 1-{ p }_{ 1 }\left( x \right)  }  \right)  } =\log { \left( \frac { { p }_{ 1 }\left( x \right)  }{ { p }_{ 2 }\left( x \right)  }  \right)  } ={ c }_{ 0 }+{ c }_{ 1 }x
$$


위 식에서 $c_0$와 $c_1$은 다변량 정규분포 확률함수의 파라메터 $μ_1$(범주1인 데이터의 평균), $μ_2$(범주2인 데이터의 평균), $σ^2$(데이터의 분산, 등분산 가정, 범주1인 데이터의 분산=범주2인 데이터의 분산)로 계산된 고정된 스칼라값입니다.

로지스틱 회귀분석은 다음과 같이 정의됩니다. 로지스틱 회귀와 관련해서는 [이곳](https://ratsgo.github.io/machine%20learning/2017/04/02/logistic/)을 참고하시면 좋을 것 같습니다.


$$
\log { \left( \frac { { p }_{ 1 }\left( x \right)  }{ 1-{ p }_{ 1 }\left( x \right)  }  \right)  } ={ \beta  }_{ 0 }+{ \beta  }_{ 1 }x
$$


LDA와 로지스틱 회귀 모두 $x$에 대해 1차 선형식(linear equation) 형태라는 점을 확인할 수 있습니다. LDA와 로지스틱 회귀의 결정경계(decision boundary)가 선형이라는 이야기입니다. 

다른 점이 있다면 로지스틱 회귀의 $β_0$과 $β_1$은 최대우도추정(maximum likelihood estimation)에 의해 도출됐고, LDA의 $c_0$과 $c_1$은 다변량 정규분포 확률함수로부터 유도됐다는 점입니다. 이러한 성질은 $x$의 차원수가 2 이상일 때도 성립한다고 합니다.

다른 점은 또 있습니다. LDA는 각 관측치가 다변량 정규분포(등분산 가정)로부터 뽑혔다고 가정합니다. 이 때문에 이러한 가정이 들어맞는 데이터에 대해서는 로지스틱 회귀보다 성능이 좋습니다. 반대로 데이터의 분포에 대해 별다른 가정을 하지 않는 로지스틱 회귀는 데이터가 정규분포를 따르지 않을 때 LDA보다 좋은 성능을 냅니다. 





## SVM vs 로지스틱 회귀

서포트벡터머신(SVM)에서 쓰이는 힌지 로스(hinge loss)는 로지스틱 회귀와 깊은 관련을 맺고 있다고 합니다. 학습데이터의 범주가 2, 차원 수가 $p$, 개수가 $n$일 때 힌지 로스는 다음과 같이 정의됩니다.


$$
L\left( X,y,\beta  \right) =\sum _{ i=1 }^{ n }{ \max { \left[ 0,1-{ y }_{ i }\left( { \beta  }_{ 0 }+{ \beta  }_{ 1 }{ x }_{ i1 }+...+{ \beta  }_{ p }{ x }_{ ip } \right)  \right]  }  }
$$


로지스틱 회귀의 손실함수는 크로스 엔트로피입니다. 다음과 같이 정의됩니다.


$$
\begin{align*}
L\left( X,y,\beta  \right) =&-\sum _{ i=1 }^{ n }{ { y }_{ i }\log { \left( { \beta  }_{ 0 }+{ \beta  }_{ 1 }{ x }_{ 1 }+...+{ \beta  }_{ p }{ x }_{ p } \right)  }  } \\ &-\sum _{ i=1 }^{ n }{ \left( 1-{ y }_{ i } \right) \log { \left( 1-{ \beta  }_{ 0 }-{ \beta  }_{ 1 }{ x }_{ 1 }-...-{ \beta  }_{ p }{ x }_{ p } \right)  }  } 
\end{align*}
$$


힌지 로스의 식을 살펴보면 $y_i(β_0+β_1x_{i1}+…+β_px_{ip})≥1$을 만족하는 데이터의 손실은 무시(=0)합니다. 하지만 로지스틱 회귀에서는 이를 만족하더라도 손실이 0에 가까워지기는 하지만, 완전히 0이 되지는 않습니다. 이를 나타낸 그림은 아래와 같습니다.



<a href="https://imgur.com/F7NcV08"><img src="https://i.imgur.com/F7NcV08.png" width="400px" title="source: imgur.com" /></a>



SVM과 로지스틱 회귀의 손실함수가 비슷하기 때문에 그 학습결과 또한 유사한 경향을 보인다고 합니다.





## 결정경계

로지스틱 회귀와 LDA는 선형 결정경계를, Quadratic Disciminant Analysis(QDA)는 비선형 결정경계를 만들어냅니다. K-Nearest Neighbor Regression(K-NN)은 비모수적 방법이라 결정경계 모양에 대한 가정이 전혀 없습니다. 다음은 LDA와 QDA 결정경계 모양을 나타낸 그림입니다.

<a href="https://imgur.com/Lz0ZaDK"><img src="https://i.imgur.com/Lz0ZaDK.png" width="500px" title="source: imgur.com" /></a>

다음은 K-NN의 결정경계 모양을 나타낸 그림입니다. 좌측 하단은 $K$가 1일 때, 우측 하단은 $K$가 9일 때 결정경계입니다. $K$가 커질 수록 예측시 고려하는 데이터가 많아지고 그 경계 또한 평탄화(smoothing)되는 걸 확인할 수 있습니다.



<a href="https://imgur.com/ClTLG5z"><img src="https://i.imgur.com/ClTLG5z.png" width="500px" title="source: imgur.com" /></a>



데이터의 범주가 선형 경계를 따라 분리될 수 있는 경우라면 LDA와 로지스틱 회귀의 성능이 좋습니다. 그 경계가 비선형적이라면 QDA가 좋은 성능을 낼 것입니다. 이도 저도 아니고 결정경계가 매우 복잡한 경우라면 K-NN이 좋은 선택이 될 겁니다. 하지만 K-NN의 성능은 $K$값에 상당히 민감하기 때문에 적절한 $K$값을 찾는 데 신중해야 한다고 합니다.

아래 그림은 의사결정나무(Decision Tree)의 결정경계를 나타냅니다. 의사결정나무는 한번에 하나의 설명변수를 기준으로 분기하기 때문에 축에 수직인 결정경계가 형성됩니다.



<a href="https://imgur.com/g8gtBlg"><img src="https://i.imgur.com/g8gtBlg.png" width="500px" title="source: imgur.com" /></a>



녹색과 노란색이 데이터의 실제 분포를 나타냅니다. 위 그림의 첫줄에 해당하는 데이터는 그 분포가 선형임을 확인할 수 있습니다. 이러한 데이터에는 축에 수직인 결정경계를 만들어내는 의사결정나무가 좋은 성능을 낼 수 없습니다. 반대로 두번째 줄에 해당하는 데이터는 그 분포가 의사결정나무의 결정경계와 잘 맞아서 좋은 성능을 낼 수 있습니다.

그런데 데이터가 첫줄에 해당하는 경우라도, 의사결정나무를 수백개 만들어서 그 결정경계를 실제 데이터 분포에 가깝게 만들 수도 있습니다(랜덤 포레스트). 아니면 데이터의 축을 회전하여 문제를 풀 수도 있습니다(로테이션 포레스트). 의사결정나무와 관련해 자세한 내용은 [이곳](https://ratsgo.github.io/machine%20learning/2017/03/26/tree/), 랜덤 포레스트와 로테이션 포레스트와 관련한 내용은 [이곳](https://ratsgo.github.io/machine%20learning/2017/03/17/treeensemble/)을 참고하시면 좋을 것 같습니다.









