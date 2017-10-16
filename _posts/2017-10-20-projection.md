---
title: 사영(projection)
category: Linear Algebra
tag: projection
---

이번 글에서는 머신러닝의 다양한 분야에서 폭넓게 응용되고 있는 선형대수학의 기본 개념인 **사영(projection)**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 강필성 교수님, 역시 같은 대학의 김성범, 한성원 교수님 강의와 위키피디아 등의 자료를 제 나름대로 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## 벡터의 내적과 사영

벡터 $b$를 벡터 $a$에 사영한 결과($x$)는 아래 그림과 같습니다.



<a href="http://imgur.com/h21igrF"><img src="http://i.imgur.com/h21igrF.png" width="500px" title="source: imgur.com" /></a>

벡터 덧셈의 기하학적 성질을 이용해 위 그림에서 정보를 얻어낼 수 있는데요. 벡터 $b$를 빗변으로 하는 직각삼각형의 밑변은 벡터 $x$, 높이는 $b-x$가 될 겁니다(밑변과 높이를 더하면 빗변에 해당하는 $b$가 됨). 

서로 직교하는 벡터의 내적은 0이 되므로 스칼라 $p$는 아래와 같이 구할 수 있게 됩니다.


$$
{ (\overrightarrow { b } -\overrightarrow {x}) }^{ T }\overrightarrow { a } =0\\{ (\overrightarrow { b } -p\overrightarrow { a } ) }^{ T }\overrightarrow { a } =0\\ { \overrightarrow { b }  }^{ T }\overrightarrow { a } -p{ \overrightarrow { a }  }^{ T }\overrightarrow { a } =0\\ p=\frac { { \overrightarrow { b }  }^{ T }\overrightarrow { a }  }{ { \overrightarrow { a }  }^{ T }\overrightarrow { a }  }
$$


그런데 여기에서 벡터 $a$가 유닛벡터($a^Ta=1$)라면 $p$는 $b^Ta$, 즉 벡터 $a$와 $b$의 내적만으로도 그 값을 구할 수 있게 됩니다. 다시 말해 벡터의 내적과 사영이 깊은 관련을 맺고 있다는 얘기입니다. 이 때문에 '어떤 특정 축(벡터)에 다른 벡터를 사영'하는 것과 '두 벡터를 내적'한다는 표현이 거의 같은 의미로 널리 쓰이는 듯합니다.





## projection operator

사영을 3차원으로 확장해 생각해 보겠습니다. 다음 그림과 같습니다.



<a href="https://imgur.com/mTfcMYy"><img src="https://i.imgur.com/mTfcMYy.png" width="200px" title="source: imgur.com" /></a>



3차원 벡터 $u$를, 벡터 $v_1$과 $v_2$가 만드는 2차원 평면 공간에 사영시킨 결과는 $w$가 됩니다. 여기에서 사영 기능을 하는 3×3 크기의 정방행렬(projection operator) $P$를 가정해봅시다. 다시 말해 임의의 3차원 벡터 $u$에 $P$를 내적해주기만 하면 2차원 평면에 사영이 된다고 치자는 것입니다.


$$
P\cdot \overrightarrow { u } =\overrightarrow { w } 
$$


그럼 여기에서 $P$의 속성을 간단히 알아보겠습니다. 정의에 의해 다음 식이 성립합니다. 단 아래 식에서 $P$와 벡터 $w$의 내적이 다시 $w$가 되는 이유는 $P$는 임의의 3차원 벡터를 $v1$과 $v2$가 만드는 2차원 평면 공간에 사영시키는 역할을 하는데, $w$는 이미 $v1$과 $v2$가 만드는 2차원 평면 공간에 있기 때문입니다.


$$
P\cdot \left( P\cdot \overrightarrow { u }  \right) =P\cdot \overrightarrow { w } =\overrightarrow { w } =P\cdot \overrightarrow { u }
$$


위 식을 간단하게 정리하면 다음과 같습니다. 다시 말해 $P$는 멱등행렬(idempotent matrix, $P^2=P$)입니다.


$$
P\cdot \left( P\cdot \overrightarrow { u }  \right) =P\cdot \overrightarrow { u } \\ \left( { P }^{ 2 }-P \right) \overrightarrow { u } =0\\ { P }^{ 2 }=P
$$


만약 $P$가 대칭행렬(symmetric matrix, $P^T=P$)이라고 가정해 봅시다. 그리고 나서 위 그림에서 직각삼각형의 밑변($w$)과 높이($u-w$)를 내적해 보는 것입니다. 다음과 같이 수식을 전개할 수 있습니다.


$$
\begin{align*}
{ \left( { \overrightarrow { u }  }-\overrightarrow { w }  \right)  }^{ T }{ \overrightarrow { w }  }=&{ \left( { \overrightarrow { u }  }-P\overrightarrow { u }  \right)  }^{ T }{ \left( P\overrightarrow { u }  \right)  }\\ =&\left( { { \overrightarrow { u }  }^{ T } }-{ \overrightarrow { u }  }^{ T }{ P }^{ T } \right) { \left( P\overrightarrow { u }  \right)  }\\ =&{ { \overrightarrow { u }  }^{ T } }P\overrightarrow { u } -{ \overrightarrow { u }  }^{ T }{ P }^{ T }P\overrightarrow { u } \\ =&{ { \overrightarrow { u }  }^{ T } }P\overrightarrow { u } -{ \overrightarrow { u }  }^{ T }P\overrightarrow { u } \\ =&0
\end{align*}
$$


$P$가 멱등행렬이고 대칭행렬일 경우 해당 $P$는 orthogonal projection operator가 된다고 합니다.





## 선형회귀와 사영

$n$개 데이터가 있고 $x$의 변수가 $p$개 일 때 선형회귀 모델은 다음과 같이 나타낼 수 있습니다.



<a href="https://imgur.com/ZbXnuyZ"><img src="https://i.imgur.com/ZbXnuyZ.png" width="400px" title="source: imgur.com" /></a>


$$
\overrightarrow { Y } ={ \beta  }_{ 0 }\overrightarrow { 1 } +{ \beta  }_{ 1 }\overrightarrow { X_{ 1 } } +...+{ \beta  }_{ p }\overrightarrow { X_{ P } } +\overrightarrow { \varepsilon  } \\ \overrightarrow { Y } =X\overrightarrow { \beta  } +\overrightarrow { \varepsilon  }
$$


선형회귀의 목적함수는 오차제곱합(sum of least square)이며 이를 최소로 하는 파라메터 $β$를 찾는 것이 모델의 학습이 되겠습니다. 식을 전개해서 정리하면 다음과 같습니다. (네번째 줄에서 두번째, 세번째 항은 스칼라값이므로 transpose를 취해주어도 같은 값을 지니기 때문에 하나로 합쳐줍니다)


$$
\begin{align*}
f\left( \overrightarrow { \beta  }  \right) =&{ \overrightarrow { \varepsilon  }  }^{ T }\overrightarrow { \varepsilon  } \\ =&{ \left( \overrightarrow { Y } -X\overrightarrow { \beta  }  \right)  }^{ T }\left( \overrightarrow { Y } -X\overrightarrow { \beta  }  \right) \\ =&\left( { \overrightarrow { Y }  }^{ T }-{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T } \right) \left( \overrightarrow { Y } -X\overrightarrow { \beta  }  \right) \\ =&{ \overrightarrow { Y }  }^{ T }\overrightarrow { Y } -{ \overrightarrow { Y }  }^{ T }X\overrightarrow { \beta  } -{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T }\overrightarrow { Y } +{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T }X\overrightarrow { \beta  } \\ =&{ \overrightarrow { Y }  }^{ T }\overrightarrow { Y } -2{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T }\overrightarrow { Y } +{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T }X\overrightarrow { \beta  } 
\end{align*}
$$


위 식은 우리의 관심인 $β$에 대해 2차식의 형태를 가지므로 $β$에 대해 미분한 식이 0이 되는 지점에서 최소값을 가집니다. 이를 식으로 쓰면 다음과 같습니다.


$$
\begin{align*}
\frac { \partial f\left( \overrightarrow { \beta  }  \right)  }{ \partial \overrightarrow { \beta  }  } =&{ \overrightarrow { Y }  }^{ T }\overrightarrow { Y } -2{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T }\overrightarrow { Y } +{ \overrightarrow { \beta  }  }^{ T }{ X }^{ T }X\overrightarrow { \beta  } \\ =-&2{ X }^{ T }\overrightarrow { Y } +2{ X }^{ T }X\overrightarrow { \beta  } =0 \\ \\ \therefore &\overrightarrow { \hat{\beta}  } ={ \left( { X }^{ T }X \right)  }^{ -1 }{ X }^{ T }\overrightarrow { Y } \\\Rightarrow \hat { Y } &=X\overrightarrow { \hat { \beta  }  } =X{ \left( { X }^{ T }X \right)  }^{ -1 }{ X }^{ T }\overrightarrow { Y }
\end{align*}
$$


위 식에서 $X(X^TX)^{-1}X^T$를 $H$로 치환해 보겠습니다. 이 $H$가 대칭행렬인지 여부를 따져보니 대칭행렬임을 확인할 수 있습니다.


$$
\begin{align*}
{ H }^{ T }=&{ \left\{ { X\left( { X }^{ T }X \right)  }^{ -1 }{ X }^{ T } \right\}  }^{ T }\\ =&X\left\{ { \left( { X }^{ T }X \right)  }^{ -1 } \right\} ^{ T }{ X }^{ T }\\ =&X\left\{ { \left( { X }^{ T }X \right)  }^{ T } \right\} ^{ -1 }{ X }^{ T }\\ =&X\left( { X }^{ T }X \right) ^{ -1 }{ X }^{ T }=H
\end{align*}
$$


이번엔 $H$가 멱등행렬인지를 따져봤습니다. 멱등행렬임을 확인할 수 있습니다.


$$
\begin{align*}
HH=&{ X\left( { X }^{ T }X \right)  }^{ -1 }{ X }^{ T }\cdot { X\left( { X }^{ T }X \right)  }^{ -1 }{ X }^{ T }\\ =&{ X\left( { X }^{ T }X \right)  }^{ -1 }I{ X }^{ T }=H
\end{align*}
$$


따라서 $H$는 orthogonal projection operator가 됩니다. 이를 그림으로 도식화하면 다음과 같습니다. 다시 말해 $H$는 정답 벡터 $Y$를 '(학습 결과물인)선형식'이라는 기저에 사영하는 역할을 수행한다는 것입니다. 



<a href="https://imgur.com/x9tsnt3"><img src="https://i.imgur.com/x9tsnt3.png" width="400px" title="source: imgur.com" /></a>







## 테일러 급수 전개와 사영

예컨대 3차원 벡터를 2차원 평면에 사영했을 경우에 벡터의 세 요소값들 가운데 하나는 특정 숫자로 고정되게 됩니다. 이를 통해 기저 2개로도 해당 벡터를 표현할 수가 있게 되죠. 이것이 바로 차원축소(dimensionality reduction)입니다. 

그런데 테일러 급수 전개도 사영, 그리고 차원축소 개념과 연관지어 생각해볼 수 있다고 합니다. 테일러급수 전개는 함수값을 다음과 같이 무한합으로 표시하는 걸 가리킵니다.


$$
\begin{align*}
f\left( t \right) =&f\left( 0 \right) +f'\left( 0 \right) \cdot t+f''\left( 0 \right) \cdot \frac { { t }^{ 2 } }{ 2! } +f'''\left( 0 \right) \cdot \frac { { t }^{ 3 } }{ 3! } +...\\ =&f\left( 0 \right) +\sum _{ k=1 }^{ \infty  }{ f^{ \left( k \right)  }\left( 0 \right)  } \cdot \frac { { t }^{ k } }{ k! } 
\end{align*}
$$


그런데 $f(t)$를 테일러 급수 전개식의 $n$번째 항까지만 써서 근사할 수 있습니다. $f(t)$를 일종의 벡터로 본다면, 테일러 급수 전개식의 각 항을 벡터의 요소값으로 봐도 큰 무리가 없을 것입니다. $n$번째 항까지만 써서 $f(t)$를 근사하는 경우 무한차원의 함수공간에 존재하는 벡터 $f(t)$를 $n$차원의 함수공간으로 사영했다고 보는 해석도 가능하다는 것이죠. 다음 그림과 같습니다.



<a href="https://imgur.com/xl0Dq6v"><img src="https://i.imgur.com/xl0Dq6v.png" width="400px" title="source: imgur.com" /></a>