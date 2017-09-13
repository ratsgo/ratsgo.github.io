---
title: 점근 표기법(asymptotic notation)
category: Data structure&Algorithm
tag: algorithm
---

이번 글에서는 어떤 함수의 증가 양상을 다른 함수와의 비교로 표현하는 **점근 표기법(asymptotic notation)**에 대해 살펴보도록 하겠습니다. 이 표기법은 알고리즘의 계산복잡도나 무한급수를 단순화하여 표시하려고 할 때 쓰입니다. 점근 표기법에는 대표적으로 대문자 O 표기법, 대문자 오메가(Ω) 표기법, 대문자 세타(Θ) 표기법, 소문자 o 표기법, 소문자 오메가(ω) 표기법 다섯 종류가 있습니다. 이 글은 고려대 김선욱 교수님 강의를 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## Big-O notation

대문자 O 표기법에서는 아래 그림을 만족하는 $f(n)$를 $O(g(n))$와 동치라고 봅니다. 이 때 $g(n)$를 $f(n)$의 **점근 상한(an asymptotic upper bound)**이라고 합니다. 어떤 알고리즘 $f(n)$의 계산복잡도가 $O(g(n))$이라면, $f(n)$의 계산복잡도는 최악의 경우라도 $g(n)$과 같거나 혹은 작다는 뜻입니다.



<a href="https://imgur.com/QmfDswm"><img src="https://i.imgur.com/QmfDswm.png" width="300px" title="source: imgur.com" /></a>



이를 수식으로 나타내면 다음과 같습니다.



$$
O\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le f\left( n \right) \le c\cdot g\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∃c>0
$$



예를 들어보겠습니다. $2n^2=O(n^3)$입니다. 2($n_0$) 이상의 모든 $n$에 대해 $0≤2n^2≤cn^3$을 만족하는 $c$가 존재하기 때문입니다($c=1$). 

이를 그림으로 나타내면 다음과 같습니다. (빨간색 선=점근 상한=$n^3$) **이 알고리즘의 계산복잡도는 최악의 경우에도 빨간색 선보다는 작거나 같습니다.**



<a href="https://imgur.com/0xHjrdE"><img src="https://i.imgur.com/0xHjrdE.png" width="200px" title="source: imgur.com" /></a>



다음은 $O(n^2)$과 동치인 함수 $f(n)$입니다.

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

대문자 Ω 표기법에서는 아래 그림을 만족하는 $f(n)$를 $Ω(g(n))$와 동치라고 봅니다. 이 때 $g(n)$는 $f(n)$의 **점근 하한(an asymptotic lower bound)**이라고 합니다. 어떤 알고리즘 $f(n)$의 계산복잡도가 $Ω(g(n))$이라면, $f(n)$의 계산복잡도는 최선의 경우를 상정하더라도 $g(n)$과 같거나 혹은 크다는 뜻입니다.



<a href="https://imgur.com/1Hnuy1s"><img src="https://i.imgur.com/1Hnuy1s.png" width="300px" title="source: imgur.com" /></a>



이를 수식으로 나타내면 다음과 같습니다.



$$
\Omega\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le c\cdot g\left( n \right) \le f\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∃c>0
$$



예를 들어보겠습니다. $\sqrt{n}=Ω(\ln{n})$입니다. 2($n_0$) 이상의 모든 $n$에 대해 $0≤\ln{n}≤c\sqrt{n}$인 $c$가 존재하기 때문입니다($c=1$). 

이를 그림으로 나타내면 다음과 같습니다. (녹색 선=점근 하한=$\ln{n}$) 다시 말해 **이 알고리즘의 계산복잡도는 최선의 경우에도 녹색 선보다는 크거나 같습니다.**



<a href="https://imgur.com/27uFjy5"><img src="https://i.imgur.com/27uFjy5.png" width="400px" title="source: imgur.com" /></a>



다음은 $Ω(n^2)$과 동치인 함수 $f(n)$입니다.

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

대문자 Θ 표기법에서는 아래 그림을 만족하는 $f(n)$를 $Θ(g(n))$과 동치라고 봅니다. 이 때 $g(n)$은 $f(n)$의 **점근적 상한과 하한의 교집합(an asymptotic tight bound)**이라고 합니다. 알고리즘 $f(n)$이 아무리 나쁘거나 좋더라도 그 계산복잡도는 $g(n)$의 범위 내에 있다는 뜻입니다. 다음과 같습니다.



<a href="https://imgur.com/Bx7ykk3"><img src="https://i.imgur.com/Bx7ykk3.png" width="300px" title="source: imgur.com" /></a>



이를 수식으로 나타내면 다음과 같습니다.



$$
\Theta \left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le {c}_{1}\cdot g\left( n \right) \le f\left( n \right) \le {c}_{2}\cdot g\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∃{c}_{1},{c}_{2}>0
$$



예를 들어보겠습니다. $n^2/2-2n=Θ(n^2)$입니다. 8($n_0$) 이상인 모든 $n$에 대하여 $0≤c_1n^2≤n^2/2-2n≤c_2n^2$을 만족하는 $c_1, c_2$가 존재하기 때문입니다($c_1=1/4, c_2=1/2$). 

이를 그림으로 나타내면 다음과 같습니다. (노란색 선=점근 하한=$1/4n^2$, 검정색 선=점근 상한=$1/2n^2$) 다시 말해 **이 알고리즘의 계산복잡도는 최선의 경우에도 보라색 선보다는 크거나 같고, 최악의 경우에도 검정색 선보다는 작거나 같습니다.**



<a href="https://imgur.com/9pPcm8o"><img src="https://i.imgur.com/9pPcm8o.png" width="400px" title="source: imgur.com" /></a>





$f(n)=Θ(g(n))$일 필요충분조건은 $f(n)=O(g(n))=Ω(g(n))$입니다. 이를 직관적으로 이해해본다면 대문자 Θ 표기법은 그 정의상 $f(x)$의 점근적 상한과 하한 사이의 범위를 나타내므로, 딱 떨어지는 Θ값이 나오려면 $f(n)$의 점근 상한 $O(g(n))$과 하한 $Ω(g(n))$이 일치해야 할 것입니다.



## o-notation, ω-notation

소문자 o 표기법, 소문자 오메가(ω) 표기법은 각각 대문자 O 표기법, 대문자 오메가(Ω) 표기법에서 등호가 빠지고 양수인 모든 $c$에 대해 성립해야 하는 등 조건이 약간 더 엄격합니다. 

$o(g(n))$의 정의는 다음과 같습니다.



$$
O\left( g\left( n \right)  \right) =\left\{ f\left( n \right) |0\le f\left( n \right) < c\cdot g\left( n \right) \quad for\quad all\quad n\ge { n }_{ 0 }>0 \right\} \quad for\quad ∀c>0 \\another \quad view:\quad\lim _{ n\rightarrow \infty  }{ \frac { f\left( x \right)  }{ g\left( x \right)  }  } =0
$$



그 예시는 다음과 같습니다

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


그 예시는 다음과 같습니다.

> $n^{2.00001}=ω(n^2)$
>
> $n^2\log{n}=ω(n^2)$
>
> $n^2≠ω(n^2)$





## 점근 표기법의 의미

- 점근 표기법을 쓰는 이유는 수행 환경에 관계없는, 알고리즘의 순수 성능을 간편하게 따져보기 위함입니다. 
- 이 표기법에서 $n$은 데이터 크기를 의미합니다. 
- 점근 상한과 하한에 포함돼 있는 상수 $c$는 컴퓨터 연산능력을 의미한다고 볼 수도 있습니다. 좋은 컴퓨터라면 $c$가 작고, 나쁜 컴퓨터라면 클 것입니다.
- 알고리즘 계산복잡도를 따질 때 보통 가장 많이 쓰이는 것은 대문자 O 표기법이라고 합니다. 최악의 경우에도 해당 알고리즘이 어떤 성능을 낼지 가늠해볼 수 있기 때문입니다.



## 점근 표기법의 속성

점근 표기법은 다음과 같은 속성을 지닌다고 합니다. 저 또한 정리 용도로 올려둡니다.



<a href="https://imgur.com/x171NET"><img src="https://i.imgur.com/x171NET.png" width="500px" title="source: imgur.com" /></a>





