---
title: disciminative models
category: generative model
tag: [linear regression, logistic regression]
---

이번 글에서는 **discriminative model** 개념을 [선형회귀](https://ratsgo.github.io/machine%20learning/2017/07/03/regression/)와 [로지스틱회귀](https://ratsgo.github.io/machine%20learning/2017/04/02/logistic/)를 중심으로 살펴보도록 하겠습니다. 이 글은 전인수 서울대 박사과정이 2017년 12월에 진행한 패스트캠퍼스 강의를 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## discriminative model

*discriminative model*이란 데이터 $x$가 주어졌을 때 레이블 $y$가 나타날 조건부확률 $p(y$\|$x)$를 반환하는 모델을 가리킵니다. 레이블 정보가 있어야 하기 때문에 지도학습(supervised learning) 범주에 속하며 $x$의 레이블을 잘 구분하는 **결정경계(decision boundary)**를 학습하는 것이 목표가 됩니다. *discriminative model*은 [generative model]()에 비해 가정이 단순하고, 학습데이터 양이 충분하다면 좋은 성능을 내는 것으로 알려져 있습니다. 선형회귀와 로지스틱회귀는 *disciminative model*의 대표적인 예시입니다.





## 선형회귀

선형회귀는 **제곱오차(squared error)**를 최소화하는 선형식을 찾는 것이 목적입니다. 이 글에서는 선형회귀를 확률모형 관점에서 살펴보겠습니다. 선형회귀는 잔차(error)가 **IID Zero Mean Gaussian**을 따른다고 가정합니다. 다음과 같습니다.



$$
\overrightarrow { e } =\overrightarrow { y } -X\overrightarrow { \beta  } ,\quad \overrightarrow { e } \sim N(E(\overrightarrow { e } ),V(\overrightarrow { e } ))\\ E(\overrightarrow { e } )=\begin{bmatrix} 0 \\ 0 \\ ... \\ 0 \end{bmatrix},\quad V(\overrightarrow { e } )={ \sigma  }^{ 2 }I
$$


잔차와 모델 파라메터 $β$에 대한 로그우도(log-likelihood) 함수는 다음과 같습니다. 아래 로그우도 함수를 최대화하는 $β$가 바로 우리가 찾고자 하는 값입니다.



$$
\begin{align*}
l(\overrightarrow { \beta  } )=&\log { L(\overrightarrow { \beta  } ) } \\ =&\log { \prod _{ i=1 }^{ m }{ \frac { 1 }{ \sqrt { 2\pi  } \sigma  } exp\left( -\frac { { \left( { y }^{ (i) }-{ \overrightarrow { \beta  }  }^{ T }{ x }^{ (i) } \right)  }^{ 2 } }{ 2{ \sigma  }^{ 2 } }  \right)  }  } \\ =&m\log { \frac { 1 }{ \sqrt { 2\pi  } \sigma  }  } -\frac { 1 }{ { \sigma  }^{ 2 } } \frac { 1 }{ 2 } \sum _{ i=1 }^{ m }{ { \left( { y }^{ (i) }-{ \overrightarrow { \beta  }  }^{ T }{ x }^{ (i) } \right)  }^{ 2 } } 
\end{align*}
$$



위 식에서 $m$는 데이터 수, $π$는 상수, $σ$는 사용자가 지정하는 하이퍼파라메터로 위의 로그우도 함수 최대화에 영향을 끼치는 값이 아닙니다. 따라서 선형회귀 모델의 로그우도 함수를 최대화하는 것은 제곱오차를 최소화하는 것과 정확히 같은 일이 됩니다.





## 로지스틱회귀

로지스틱회귀 모델의 손실함수는 **크로스엔트로피(cross entropy)**입니다. 범주가 1일 확률을 $p$, 0일 확률을 $1-p$라고 했을 때 [로지스틱회귀 모델](https://ratsgo.github.io/machine%20learning/2017/04/02/logistic/)은 다음과 같이 정의됩니다($σ$는 시그모이드 함수).


$$
p=\frac { 1 }{ 1+exp\left( -{ \overrightarrow { \beta  }  }^{ T }x \right)  } =\sigma ({ \overrightarrow { \beta  }  }^{ T }x)
$$

로지스틱회귀의 로그우도 함수는 다음과 같습니다.



$$
\begin{align*}
l(\overrightarrow { { \beta  } } )=&\log { L(\overrightarrow { { \beta  } } ) } \\ =&\log { \prod _{ i }^{  }{ { \sigma (\overrightarrow { { \beta  } } ^{ T }{ x }_{ i }) }^{ { y }_{ i } }{ \left\{ 1-\sigma (\overrightarrow { { \beta  } } ^{ T }{ x }_{ i }) \right\}  }^{ 1-{ y }_{ i } } }  } \\ =&\sum _{ i }^{  }{ { y }_{ i }\log { \left\{ \sigma (\overrightarrow { { \beta  } } ^{ T }{ x }_{ i }) \right\}  }  } +\sum _{ i }^{  }{ \left( 1-{ y }_{ i } \right) \log { \left\{ 1-\sigma (\overrightarrow { { \beta  } } ^{ T }{ x }_{ i }) \right\}  }  } 
\end{align*}
$$


최종 도출된 로그우도 함수는 음의 [크로스엔트로피](https://ratsgo.github.io/deep%20learning/2017/09/24/loss/)인 점을 확인할 수 있습니다. 따라서 로지스틱회귀 모델의 로그우도 함수를 최대화하는 것은 크로스엔트로피를 최소화하는 것과 정확히 같은 일이 됩니다.