---
title: 점근 표기법(asymptotic notation)
category: Data structure&Algorithm
tag: algorithm
---

이번 글에서는 내가 만든 알고리즘이 얼마나 효율적인지를 따져보기 위한 도구인 **점근 표기법(asymptotic notation)**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김황남 교수님과 역시 같은 대학의 김선욱 교수님 강의를 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 개요

내가 만든 알고리즘을 수퍼컴퓨터에서 돌릴 때와 노트북에서 수행할 때는 분명 속도 면에서 차이가 날 겁니다. 수행환경을 통제하지 않고서는 공정한 비교라고 할 수 없겠지요. 이 때문에 알고리즘의 계산복잡성은 컴퓨터 성능에 관계없이 machine independent한 방식으로 따져보게 됩니다. 알고리즘 자체의 효율성은 데이터 개수($n$)가 주어졌을 때 덧셈, 뺄셈, 곱셈 등 해당 알고리즘 수행시 필요한 '기본 연산(basic operation)의 횟수'로 표현하는 것이 일반적입니다.

이렇게 따져본 내 알고리즘의 계산복잡성이 $20/πn^2+n+100$이라고 칩시다. $n$이 증가함에 따라 이 알고리즘의 계산복잡성이 대략 어떻게 늘어나는지, 머릿 속에서 그 모양과 방향을 예측하기가 그렇게 쉽지만은 않습니다. 여기에 어떤 개발자가 내놓은 알고리즘은 $100000n+100000$이라고 가정해봅시다. 그러면 내가 만든 알고리즘과 비교해 어떤 것이 더 나은 알고리즘일까요? 이 문제도 역시 단박에 알아내기가 어렵습니다. 이럴 때는 가늠해보려는 알고리즘의 계산복잡성 증가 양상을 단순화시켜 우리가 익히 알고 있는 로그, 지수, 다항함수 등과의 비교로 표현하는 점근 표기법이 유용하게 쓰일 수 있습니다. 



<a href="https://imgur.com/EoUstgL"><img src="https://i.imgur.com/EoUstgL.png" width="300px" title="source: imgur.com" /></a>



점근 표기법에서는 원 함수를 단순화하여 최고차항의 차수만을 고려합니다. 최고차항을 제외한 모든 항과 최고차항의 계수는 무시합니다. 이 표기법을 따르면 내 알고리즘의 계산복잡도는 $n^2$, 다른 개발자의 알고리즘은 $n$이 됩니다. 따라서 데이터 수가 증가함에 따라 내 알고리즘의 계산복잡도는 지수적으로, 상대방의 알고리즘은 선형적으로 증가하며, 상대방의 알고리즘이 제 것보다 더 나은 알고리즘이라고 비교할 수 있게 됩니다. 만약 위 그림처럼 점근 표기법으로 표현된 계산복잡성이 $\log{n}$인 알고리즘이 등장한다면 state-of-the-art의 기법이 되겠지요.

점근 표기법에는 대표적으로 대문자 O 표기법, 대문자 오메가(Ω) 표기법, 대문자 세타(Θ) 표기법, 소문자 o 표기법, 소문자 오메가(ω) 표기법 다섯 종류가 있습니다. 다섯 표기법 모두 내가 만든 알고리즘 $f(n)$를 지수, 다항함수 등 우리가 익히 알고 있는 함수 $g(n)$와 어떤 관계가 있는지 표현해 줍니다. 차례로 살펴보겠습니다.



## Big-O notation

대문자 O 표기법에서는 아래 그림을 만족하는 $f(n)$를 $O(g(n))$이라고 표시합니다. 이 때 $g(n)$를 $f(n)$의 **점근 상한(an asymptotic upper bound)**이라고 합니다. 러프하게 보면, 내가 만든 알고리즘 $f(n)$이 $O(g(n))$에 속한다면, $f(n)$의 계산복잡도는 최악의 경우라도 $g(n)$과 같거나 혹은 작다는 뜻입니다. 



<a href="https://imgur.com/QmfDswm"><img src="https://i.imgur.com/QmfDswm.png" width="300px" title="source: imgur.com" /></a>



이를 수식으로 나타내면 다음과 같습니다.



$$
O\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le f\left( n \right) \le c\cdot g\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∃c>0
$$



예를 들어보겠습니다. $2n^2=O(n^3)$입니다. 2($n_0$) 이상의 모든 $n$에 대해 $0≤2n^2≤cn^3$을 만족하는 $c$가 존재하기 때문입니다($c=1$). 

이를 그림으로 나타내면 다음과 같습니다. (빨간색 선=점근 상한=$n^3$) **이 알고리즘의 계산복잡도는 최악의 경우에도 빨간색 선보다는 작거나 같습니다.**



<a href="https://imgur.com/0xHjrdE"><img src="https://i.imgur.com/0xHjrdE.png" width="200px" title="source: imgur.com" /></a>



다음은 $O(n^2)$에 속한 함수 $f(n)$입니다. 최고차항의 차수가 2보다 작거나 같은 함수들입니다.

> $n^2$
>
> $n^2+n$
>
> $n^2+1000n$
>
> $1000n^2+1000n$
>
> $n$
>
> $n/1000$
>
> $n^{1.99999}$
>
> $n^2/\log\log\log{n}$





## Big-Ω notation

대문자 Ω 표기법에서는 아래 그림을 만족하는 $f(n)$를 $Ω(g(n))$이라고 표시합니다. 이 때 $g(n)$는 $f(n)$의 **점근 하한(an asymptotic lower bound)**이라고 합니다. 러프하게 보면, 내가 만든 알고리즘 $f(n)$의 계산복잡도가 $Ω(g(n))$에 속한다면, $f(n)$의 계산복잡도는 최선의 경우를 상정하더라도 $g(n)$과 같거나 혹은 크다는 뜻입니다.



<a href="https://imgur.com/1Hnuy1s"><img src="https://i.imgur.com/1Hnuy1s.png" width="300px" title="source: imgur.com" /></a>



이를 수식으로 나타내면 다음과 같습니다.



$$
\Omega\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le c\cdot g\left( n \right) \le f\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∃c>0
$$



예를 들어보겠습니다. $\sqrt{n}=Ω(\ln{n})$입니다. 2($n_0$) 이상의 모든 $n$에 대해 $0≤\ln{n}≤c\sqrt{n}$인 $c$가 존재하기 때문입니다($c=1$). 

이를 그림으로 나타내면 다음과 같습니다. (녹색 선=점근 하한=$\ln{n}$) 다시 말해 **이 알고리즘의 계산복잡도는 최선의 경우에도 녹색 선보다는 크거나 같습니다.**



<a href="https://imgur.com/27uFjy5"><img src="https://i.imgur.com/27uFjy5.png" width="400px" title="source: imgur.com" /></a>



다음은 $Ω(n^2)$에 속하는 함수 $f(n)$입니다. 최고차항의 차수가 2보다 크거나 같은 함수들입니다.

> $n^2$
>
> $n^2+n$
>
> $n^2-n$
>
> $1000n^2+1000n$
>
> $1000n^2-1000n$
>
> $n^3$
>
> $n^{2.00001}$
>
> $n^2\log\log\log{n}$
>
> $2^{2^n}$





## Big Θ-notation

대문자 Θ 표기법에서는 아래 그림을 만족하는 $f(n)$를 $Θ(g(n))$이라고 표시합니다. 이 때 $g(n)$은 $f(n)$의 **점근적 상한과 하한의 교집합(an asymptotic tight bound)**이라고 합니다. 러프하게 보면, 내가 만든 알고리즘 $f(n)$이 아무리 나쁘거나 좋더라도 그 계산복잡도는 $g(n)$의 범위 내에 있다는 뜻입니다. 다음과 같습니다.



<a href="https://imgur.com/Bx7ykk3"><img src="https://i.imgur.com/Bx7ykk3.png" width="300px" title="source: imgur.com" /></a>



이를 수식으로 나타내면 다음과 같습니다.



$$
\Theta \left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le {c}_{1}\cdot g\left( n \right) \le f\left( n \right) \le {c}_{2}\cdot g\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∃{c}_{1},{c}_{2}>0
$$



예를 들어보겠습니다. $n^2/2-2n=Θ(n^2)$입니다. 8($n_0$) 이상인 모든 $n$에 대하여 $0≤c_1n^2≤n^2/2-2n≤c_2n^2$을 만족하는 $c_1, c_2$가 존재하기 때문입니다($c_1=1/4, c_2=1/2$). 

이를 그림으로 나타내면 다음과 같습니다. (노란색 선=점근 하한=$1/4n^2$, 검정색 선=점근 상한=$1/2n^2$) 다시 말해 **이 알고리즘의 계산복잡도는 최선의 경우에도 보라색 선보다는 크거나 같고, 최악의 경우에도 검정색 선보다는 작거나 같습니다.**



<a href="https://imgur.com/9pPcm8o"><img src="https://i.imgur.com/9pPcm8o.png" width="400px" title="source: imgur.com" /></a>







## o-notation, ω-notation

소문자 o 표기법, 소문자 오메가(ω) 표기법은 각각 대문자 O 표기법, 대문자 오메가(Ω) 표기법과 비교해 등호가 빠지는 등 조건이 약간 더 엄격합니다. $o(g(n))$의 정의는 다음과 같습니다.



$$
O\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le f\left( n \right) < c\cdot g\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∀c>0 \\another \quad view:\quad\lim _{ n\rightarrow \infty  }{ \frac { f\left( x \right)  }{ g\left( x \right)  }  } =0
$$



그 예시는 다음과 같습니다. 최고차항의 차수가 2보다 작은 함수(정확히 2인 것은 제외)입니다.

> $n^{1.99999}=o(n^2)$
>
> $n^2/\log{n}=o(n^2)$
>
> $n^2≠o(n^2)$ (마치 $2 ≮ 2$ 인 것과 같음)
>
> $n^2≠o(n^2)$



$ω(g(n))$의 정의는 다음과 같습니다.



$$
\Omega\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0< c\cdot g\left( n \right) \le f\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∀c>0 \\another \quad view:\quad\lim _{ n\rightarrow \infty  }{ \frac { f\left( x \right)  }{ g\left( x \right)  }  } =\infty
$$


그 예시는 다음과 같습니다. 최고차항의 차수가 2보다 큰 함수(정확히 2인 것은 제외)입니다.

> $n^{2.00001}=ω(n^2)$
>
> $n^2\log{n}=ω(n^2)$
>
> $n^2≠ω(n^2)$





## 표기법 간의 관계

다섯가지 점근 표기법을 한눈에 정리하면 다음 표와 같습니다.

|   표기법    |          대략적 의미          |
| :------: | :----------------------: |
| $f=ω(g)$ |   $f$는 $g$보다 크다, $f>g$   |
| $f=Ω(g)$ | $f$는 $g$보다 크거나 같다, $f≥g$ |
| $f=Θ(g)$ |  $f$는 $g$와 대략 같다, $f=g$  |
| $f=O(g)$ | $f$는 $g$보다 작거나 같다, $f≤g$ |
| $f=o(g)$ |   $f$는 $g$보다 작다, $f<g$   |

엄밀히 말해 $ω(g), Ω(g), Θ(g), O(g), o(g)$는 각각 함수의 **집합**을 의미합니다. 각 집합의 요소 수는 무한히 많을 것입니다. 다섯 집합 사이의 관계를 따져보면 다음과 같습니다.



<a href="https://imgur.com/tMfg0j8"><img src="https://i.imgur.com/tMfg0j8.png" width="400px" title="source: imgur.com" /></a>



알고리즘 계산복잡도를 따질 때 보통 가장 많이 쓰이는 것은 대문자 O 표기법이라고 합니다. 최악의 경우에도 해당 알고리즘이 어떤 성능을 낼지 가늠해볼 수 있기 때문입니다.





## 점근 표기법의 속성

점근 표기법은 다음과 같은 속성을 지닌다고 합니다. 저 또한 정리 용도로 올려둡니다.



<a href="https://imgur.com/x171NET"><img src="https://i.imgur.com/x171NET.png" width="500px" title="source: imgur.com" /></a>





