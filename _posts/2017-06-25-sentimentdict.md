---
title: 통계 기반 감성사전 구축
category: From frequency to semantics
tag: Sentiment Analysis
---

이번 글에서는 통계 기반 감성사전 구축 방법에 대해 살펴보도록 하겠습니다. 이 글은 고려대 강필성 교수님 강의와 [Hur et al.(2016)](http://ac.els-cdn.com/S0020025516306016/1-s2.0-S0020025516306016-main.pdf?_tid=78f198fe-5989-11e7-9811-00000aacb361&acdnat=1498383443_5601767d8c2a2f859323480fb98553e1)을 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 모델의 가정

이 모델은 평점 정보가 있는 영화 리뷰를 대상으로 합니다. 가정은 이렇습니다. 긍정적인 어휘가 쓰인 리뷰의 평점 분포는 전체 분포보다 오른쪽에 있을 것이고, 반대로 부정적인 어휘는 왼쪽에 있을 것이라는 겁니다. 이를 그림으로 나타내면 다음과 같습니다.



<a href="http://imgur.com/2kdiYUf"><img src="http://i.imgur.com/2kdiYUf.png" width="400px" title="source: imgur.com" /></a>



이 모델은 각 단어별 평점의 분포가 t분포를 따를 것이라고 가정합니다. 다음과 같이 **t-test**를 실시하여 **검정통계량**이 일정 수치를 넘으면 해당 단어를 긍정 범주, 일정 수치보다 작으면 부정 범주로 할당하게 됩니다.

> $H_0$ : 전체 평균과 해당 단어의 평균 평점이 동일하다.
>
> $H_1$ : 전체 평균과 해당 단어의 평균 평점이 같지 않다.



## 검정통계량

아래 식에서 $w_q$는 영화 리뷰 말뭉치에 $q$번째로 등장한 단어, $r_{i,j}$는 $i$번째 사용자가 $j$번째로 작성한 리뷰의 평점, $R(r_{i,j},w_q)$는 $i$번째 사용자가 $j$번째로 작성한 리뷰에 $q$번째 단어가 쓰였을 경우 해당 리뷰의 평점($r_{i,j}$)을 가리킵니다. 만약 해당 리뷰에 $w_q$가 포함돼 있지 않을 경우 $R(r_{i,j},w_q)$은 0이 됩니다. 한편 $m$은 전체 사용자 수, $n_i$는 $i$번째 사용자가 작성한 리뷰의 총수, $n(w_q)$는 $w_q$의 빈도수를 뜻합니다.


$$
\begin{align*}
Score({ w }_{ q })=E({ w }_{ q })&=\frac { 1 }{ n({ w }_{ q }) } \sum _{ i=1 }^{ m }{ \sum _{ j=1 }^{ { n }_{ i } }{ R({ r }_{ i,j },{ w }_{ q }) }  }\\Var({ w }_{ q })&=\frac { 1 }{ n({ w }_{ q })-1 } \sum _{ i=1 }^{ m }{ \sum _{ j=1 }^{ { n }_{ i } }{ { \left\{ R({ r }_{ i,j },{ w }_{ q })-Score({ w }_{ q }) \right\}  }^{ 2 } }  }
\end{align*}
$$


**가설검정**을 위한 검정통계량 $T_w$와 t분포의 자유도 $v$는 다음과 같습니다. $W$는 전체 단어, $w$는 가설검정 대상이 되는 개별 단어를 가리킵니다. $s^2_w$는 $Var(w)$, $E(w)$는 $Score(w)$를 뜻합니다.


$$
\begin{align*}
{ T }_{ w }&=\frac { E(W)-E(w) }{ \sqrt { \frac { { s }_{ W }^{ 2 } }{ n(W) } +\frac { { s }_{ w }^{ 2 } }{ n(w) }  }  } \\ v&=\frac { { \left\{ { s }_{ W }^{ 2 }/n(W)+{ s }_{ w }^{ 2 }/n(w) \right\}  }^{ 2 } }{ \frac { { \left\{ { s }_{ W }^{ 2 }/n(W) \right\}  }^{ 2 } }{ n(W)-1 } +\frac { { \left\{ { s }_{ w }^{ 2 }/n(w) \right\}  }^{ 2 } }{ n(w)-1 }  }
\end{align*}
$$




## 가설검정

$w$에 대한 검정통계량 $T_w$와 자유도 $v$가 주어졌을 때 가설검정은 다음과 같이 실시합니다. (유의수준=$α$)


$$
Positive\quad if\quad { T }_{ w }>t(\alpha ,v)\\ Negative\quad if\quad { T }_{ w }<t(\alpha ,v)\\ Neutral\quad if\quad otherwise
$$


## 실험결과

Hur et al.(2016)의 실험 결과 일부는 다음과 같습니다. 통계 기반의 기법으로도 감성 어휘를 골라내는 데 좋은 성능을 나타냄을 알 수 있습니다.



<a href="http://imgur.com/jcrhIGI"><img src="http://i.imgur.com/jcrhIGI.png" title="source: imgur.com" /></a>



