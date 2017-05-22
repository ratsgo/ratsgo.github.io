---
title: Word Weighting(2)
category: From frequency to semantics
tag: Word Weighting
---

이번 글에서는 **TF-IDF**를 설명한 지난 [글](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/28/tfidf/)에 이어 단어에 대한 가중치를 부여하는 방법론 10가지에 대해 다뤄보려고 합니다. 이 가중치들은 문서의 특징을 추출하거나 분류하는 데 쓰입니다. 이번 글 역시 고려대 강필성 교수님 강의를 참고로 했음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 단어 가중치 계산 목적

리뷰(Document) 10개, 단어(Term) 10개로 구성된 말뭉치가 주어졌다고 가정해 봅시다. **binary Term-Document Matrix**는 아래와 같습니다. 여기에서 binary라는 건 특정 단어가 한번 쓰였든 열번 쓰였든 해당 리뷰 안에 등장하면 1, 한번도 나타난 적이 없으면 0으로 표시했다는 뜻입니다. 표 맨 밑에 범주(class) 정보가 있습니다. 첫번째 리뷰(D1)부터 여섯번째 리뷰(D6)까지는 긍정(Positive)적인 문서임을 확인할 수 있네요. 나머지 리뷰는 부정(Negative)인 것 또한 확인 가능합니다.


|   구분   |  D1  |  D2  |  D3  |  D4  |  D5  |  D6  |  D7  |  D8  |  D9  | D10  |
| :----: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Term1  |  1   |  1   |  1   |  1   |  1   |  1   |  0   |  0   |  0   |  0   |
| Term2  |  0   |  0   |  0   |  0   |  0   |  0   |  1   |  1   |  1   |  1   |
| Term3  |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |
| Term4  |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  0   |  0   |
| Term5  |  0   |  0   |  0   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |
| Term6  |  1   |  1   |  1   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |
| Term7  |  0   |  0   |  0   |  0   |  0   |  0   |  1   |  1   |  0   |  0   |
| Term8  |  1   |  0   |  1   |  0   |  1   |  0   |  1   |  0   |  1   |  0   |
| Term9  |  1   |  1   |  1   |  0   |  0   |  0   |  1   |  0   |  0   |  0   |
| Term10 |  1   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  1   |  1   |
| Class  | Pos  | Pos  | Pos  | Pos  | Pos  | Pos  | Neg  | Neg  | Neg  | Neg  |

우리의 목적은 단어 정보만으로 범주(긍정, 부정)를 예측하는 것입니다. 다시 말해 문서를 긍정/부정으로 분류할 때 어떤 단어가 중요한 역할을 하는지 알고 싶은거죠. 딱 보기엔 Term1과 Term2가 중요해 보이네요. Term1은 긍정적인 문서에서만 쓰인 단어이고, Term2는 부정적인 문서에만 나타났거든요. 우리가 범주 정보가 없는 새로운 리뷰를 분류해야 한다면, 우선 해당 리뷰에 Term1이나 Term2가 쓰였는지부터 확인해보면 되겠네요. 반면 모든 리뷰에 등장한 Term3는 같은 이유로 문서 분류에 별 도움이 되지 않을 것 같습니다. 

이번 글에서 다루는 단어 가중치 계산 방법 10가지는 이처럼 특정 단어가 문서 분류라는 과업에 얼마나 중요한 역할을 하는지 수치화하는 걸 목적으로 합니다.




## Document Frequency (DF)

Document Frequency(DF)는 $w$라는 단어가 몇 개의 문서에 등장했는지 빈도를 나타냅니다. 아래와 같이 정의됩니다.

$$DF(w)={ N }_{ D }(w)$$


## Accuracy(Acc)

Accuracy(Acc)는 $w$라는 단어가 긍정적인 문서에 나타난 빈도, $w$가 부정적인 문서에 나타낸 빈도 간 차이입니다. 

$$Acc(w)=N(Pos,w)-N(Neg,w)$$



## Accuracy Ratio(AccR)

$N(Pos,w)/N(Pos)$는 긍정적인 문서가 주어졌을 때 $w$라는 단어가 등장할 조건부 확률입니다. Accuracy Ratio(AccR)은 긍정과 부정 범주의 조건부확률 차이에 절대값을 취한 값입니다.

$$AccR(w)=\left| \frac { N(Pos,w) }{ N(Pos) } -\frac { N(Neg,w) }{ N(Neg) }  \right| $$



## Probability Ratio (PR)

Probability Ratio(PR)은 AccR와 유사하나 긍/부정 조건부확률 차이의 절대값 대신 두 값 사이의 비율을 계산했습니다.

$$PR(w)=\frac { N(Pos,w) }{ N(Pos) } /\frac { N(Neg,w) }{ N(Neg) } $$



이상 네 지표를 예시 말뭉치에 적용한 결과는 아래와 같습니다. 값이 높을 수록 해당 단어가 긍/부정 범주 분류에 중요하다는 뜻입니다. PR의 경우 $w$가 부정 범주에 한번도 쓰이지 않았을 경우 PR 식의 분모가 0이 돼 무한대값이 나오는 걸 확인할 수 있습니다.

<a href="http://imgur.com/37uTcea"><img src="http://i.imgur.com/37uTcea.png" width="600px" title="source: imgur.com" /></a>



## Odds ratio (OddR)

**승산(odds)**이란 임의의 사건 $A$가 발생하지 않을 확률 대비 일어날 확률 사이의 비율입니다. $P(A)/(1-P(A))$로 정의됩니다. 그렇다면 '긍정적인 문서에 $w$가 등장'한 경우를 사건 $A$라고 정의한다면 $A$에 대한 승산은 아래와 같이 쓸 수 있습니다.


$$
\begin{align*}
Odd(A)&=\frac { P(A) }{ 1-P(A) } \\ &=\frac { P(w|Pos) }{ 1-P(w|Pos) } \\ &=\frac { \frac { N(Pos,w) }{ N(Pos) }  }{ 1-\frac { N(Pos,w) }{ N(Pos) }  } \\ &=\frac { N(Pos,w) }{ N(Pos)-N(Pos,w) } \\ &=\frac { N(Pos,w) }{ N(Pos,\bar { w } ) }
\end{align*}
$$


위 식 마지막의 분모는 $w$가 포함되지 않은 긍정적인 문서의 개수를 뜻합니다. 한편 사건 $B$를 '부정적인 문서에 $w$가 등장'한 경우로 정의하면 사건 B의 승산은 아래와 같이 쓸 수 있습니다. 아래식 마지막의 분모 역시 $w$가 없는 부정적인 문서의 개수입니다.

$$Odd(B)=\frac { N(Neg,w) }{ N(Neg,\bar { w } ) } $$

사건 $A$의 승산과 사건 $B$의 승산은 사이의 비율, 즉 **Odds ratio(OddR)**은 아래와 같이 쓸 수 있습니다. OddR이 클수록 긍정 범주 판별에 유용한 단어라는 의미를 지닙니다.


$$
\begin{align*}
OddR(w)&=\frac { Odd(A) }{ Odd(B) } \\ &=\frac { \frac { N(Pos,w) }{ N(Pos,\bar { w } ) }  }{ \frac { N(Neg,w) }{ N(Neg,\bar { w } ) }  } \\ &=\frac { N(Pos,w) }{ N(Neg,w) } \times \frac { N(Neg,\bar { w } ) }{ N(Pos,\bar { w } ) }
\end{align*}
$$


## Odds ratio Numerator (OddN)

계산 효율성을 목적으로 OddR에서 분자 부분만 떼어낸 식입니다.

$$OddN(w)=N(Pos,W)\times N(Neg,\bar { w } )$$



## F1-Measure

임의의 단어 $w$에 대해 말뭉치로부터 아래와 같은 표를 만들 수 있습니다. 아래 표에서 \~$w$는 $w$가 포함되지 않은 문서라는 뜻입니다.

|  구분  | $w$  | \~$w$ |
| :--: | :--: | :---: |
| Pos  | $a$  |  $b$  |
| Neg  | $c$  |  $d$  |

위 표를 **머신러닝(Machine Learining)** 모델의 성능 측정을 위한 **혼동행렬(confusion matrix)**처럼 생각할 경우 **재현율(Recall)**은 $a/(a+b)$, **정밀도(precision)**는 $a/(a+c)$입니다. **F1**은 이 둘의 조화평균인데요. 임의의 단어 $w$에 대한 F1 지표는 아래와 같습니다. F1 역시 클수록 긍정 범주 판별에 유용한 단어라는 의미를 가집니다. 


$$
\begin{align*}
Recall(w)&=\frac { N(Pos,w) }{ N(Pos,w)+N(Pos,\bar { w } ) } \\ Precision(w)&=\frac { N(Pos,w) }{ N(Pos,w)+N(Neg,w) } \\F1(w)&=\frac { 2\times Recall(w)\times Precision(w) }{ Recall(w)+Precision(w) } \\ &=\frac { 2\times N(Pos,w) }{ N(Pos)+N(w) } 
\end{align*}
$$



이상 세 가지 지표를 예시 말뭉치에 적용한 결과는 아래 표와 같습니다. OddR, OddN, F1 모두 긍정 범주 판별에 유의미한 단어들을 골라내고 있지만, 부정 범주 판별에 쓸모 있는 Term2에 대해선 아무런 스코어를 내고 있지 않다는 점을 확인할 수 있습니다. 다시 말해 세 지표는 긍정 범주 판별에 의미있는 단어들만을 골라냅니다.

<a href="http://imgur.com/2RSjbuA"><img src="http://i.imgur.com/2RSjbuA.png" width="600px" title="source: imgur.com" /></a>



## Information Gain

정보이론에서 **엔트로피(Entropy)**란 불확실성 내지 혼잡도의 척도로 쓰입니다. 만약 어떤 데이터의 범주는 두 개인데, 전체 관측치의 절반이 한 범주이고 나머지 절반이 다른 범주라면 엔트로피는 최대값(1)을 가집니다. 반대로 모든 관측치가 하나의 범주로 구성돼 있다면 엔트로피는 최소값(0)이 됩니다. **정보이득(information gain)**이란 특정 조건과 비교한 엔트로피 간 차이를 의미합니다. 이와 관련해 위 표를 다시 볼까요?

|  구분  | $w$  | \~$w$ |
| :--: | :--: | :---: |
| Pos  | $a$  |  $b$  |
| Neg  | $c$  |  $d$  |

우리의 목적은 $w$가 문서의 극성을 분류하는 데 얼마나 중요한지를 따지는 것입니다. 그렇다면 이렇게 생각해보면 어떨까요? $w$가 쓰인 문서의 엔트로피(혼잡도)와 $w$가 쓰이지 않은 문서의 엔트로피를 비교해보는거죠. 위 표 기준으로는 $(a, c)$와 $(b,d)$의 엔트로피를 구해보는 것입니다. 여기에서 만약 $(b,d)$로 계산한 엔트로피가 $(a,c)$보다 크다면, $w$가 긍정, 부정 범주의 문서를 가르는 데 유의미하다는 결론을 내게 되는 것입니다. 이를 식으로 쓰면 아래와 같습니다.


$$
\begin{align*}
Entropy(absent\quad w)&=\sum _{ c\in \{ Pos,Neg\}  }^{  }{ -P(C)\times \log { (P(C)) }  } \\ Entropy(given\quad w)&=P(w)\left[ \sum _{ c\in \{ Pos,Neg\}  }^{  }{ -P(C|w)\times \log { (P(C|w)) }  }  \right] \\ &+P(\bar { w } )\left[ \sum _{ c\in \{ Pos,Neg\}  }^{  }{ -P(C|\bar { w } )\times \log { (P(C|\bar { w } )) }  }  \right] \\\\ IG(w)=Entropy(absent\quad w)&-Entropy(given\quad w)
\end{align*}
$$



## Chi-squared Statistic

말뭉치(리뷰 20건)가 아래와 같이 구성돼 있다고 합니다. 

|  구분   |     최고     |    ~최고    | total |
| :---: | :--------: | :-------: | :---: |
|  Pos  | 12(=$o_1$) | 2(=$o_2$) |  14   |
|  Neg  | 3(=$o_3$)  | 3(=$o_4$) |   6   |
| total |     15     |     5     |  20   |

우리의 관심은 **최고**라는 단어가 극성을 나누는 데 의미가 있는지 여부입니다. 이를 통계학의 **귀무가설(null hypothesis)**과 **대립가설(alternative hypothesis)**로 표현하면 아래와 같습니다.

> $H_0$ : '최고'라는 단어 등장 여부와 긍,부정 극성은 서로 **독립(independent)**이다.
>
> $H_1$ : $H_0$가 참이 아니다.

$H_0$가 참이라면 각 요소의 비율은 아래 표가 될 것입니다. 통계적 독립의 정의에 의해 각 행과 열의 **주변확률(marginal probability)**을 서로 곱한 값이 각 요소의 **결합확률(joint probability)**가 되기 때문입니다.

|  구분   |        최고         |        ~최고        |    total    |
| :---: | :---------------: | :---------------: | :---------: |
|  Pos  | 0.525(=$P_1*P_A$) | 0.175(=$P_1*P_B$) | 0.7(=$P_1$) |
|  Neg  | 0.225(=$P_2*P_A$) | 0.075(=$P_2*P_B$) | 0.3(=$P_2$) |
| total |   0.75(=$P_A$)    |   0.25(=$P_B$)    |      1      |

위 표에 전체 문서 수 20을 모두 곱하면 $H_0$ 하에서의 **기대값(expected value)**이 됩니다. 아래 표와 같습니다.

|  구분   |      최고      |     ~최고     | total |
| :---: | :----------: | :---------: | :---: |
|  Pos  | 10.5(=$e_1$) | 3.5(=$e_2$) |  14   |
|  Neg  | 4.5(=$e_3$)  | 1.5(=$e_4$) |   6   |
| total |      15      |      5      |  20   |

이렇게 나온 기대값($e_i$)과 실제 관측치($o_i$)를 아래와 같이 계산한 **통계량(statistic)**은 자유도 $(c-1)(r-1)$인 **카이제곱분포(chi-squared distribution)**을 따른다고 합니다. 여기에서 $c$는 위 표의 total 열을 제외한 열(column)의 개수, $r$은 total 행을 제외한 행(row)의 개수입니다. 예시 기준으로는 자유도가 1이 됩니다.

$$\sum _{ i=1 }^{ 4 }{ \frac { { ({ o }_{ i }-{ e }_{ i }) }^{ 2 } }{ { e }_{ i } }  } \sim { \chi  }_{ 1 }^{ 2 }$$

여기에서 통계량이 커질 수록 $H_0$를 기각할 가능성 역시 커지게 된다고 합니다. 바꿔 말하면 통계량이 클수록 '최고'라는 단어가 긍정, 부정 극성 분리에 중요한 term이라는 이야기입니다. 카이제곱 통계량을 지금까지 우리가 논의한 단어 가중치 부여 방식으로 일반화해서 식을 쓰면 아래와 같습니다.

$${ \chi  }^{ 2 }(w)=\frac { N\times { \left[ P(Pos,w)\times P(Neg,\bar { w } )-P(Neg,w)\times P(Pos,\bar { w } ) \right]  }^{ 2 } }{ P(w)\times P(\bar { w } )\times P(Pos)\times P(Neg) } $$



## Bi-Normal Separation (BNS)

**Bi-Normal Separation**은 아래와 같은 식으로 정의됩니다. 여기에서 F는 **정규분포(Normal distribution)**의 **누적분포함수(cumulative distribution function)**입니다.

$$BNS(w)=\left| { F }^{ -1 }(\frac { N(Pos,w) }{ N(Pos) } )-{ F }^{ -1 }(\frac { N(Neg,w) }{ N(Neg) } ) \right| $$



세 가지 지표를 첫 예시에 맞춰 적용하면 아래 표와 같습니다.

<a href="http://imgur.com/hQgUCJ6"><img src="http://i.imgur.com/hQgUCJ6.png" width="600px" title="source: imgur.com" /></a>



## 마치며

이상 10가지 방식을 요약하면 아래 표와 같습니다. 각 지표마다 특성이 다르고 일장일단이 있으므로 목적에 맞게 적절히 선택해서 쓰면 좋을 것 같습니다. 의견이나 질문 있으시면 언제든지 이메일이나 댓글로 알려주시기 바랍니다. 여기까지 읽어주셔서 감사합니다.

<a href="http://imgur.com/7meHpla"><img src="http://i.imgur.com/7meHpla.png" width="600px" title="source: imgur.com" /></a>

