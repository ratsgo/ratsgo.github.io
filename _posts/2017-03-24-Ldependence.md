---
title: Linear independence, Linear Transformation
category: Linear Algebra
tag: linear
---

이번 포스팅에서는 **선형독립(linear independence)**과 **선형변환(linear transformation)**에 대해 살펴보도록 하겠습니다. 이번 글 역시 [고려대 박성빈 교수님](http://info.korea.ac.kr/page_professor.php) 강의를 참고했음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 선형독립과 선형종속

아래 조건을 만족하는 유한한 $n$개의 벡터는 **선형종속**(線型從屬, linear dependence)이라고 정의됩니다.

$$S=\left\{ { v }_{ 1 },{ v }_{ 2 },...,{ v }_{ n } \right\} 에\quad 대해\\{ c }_{ 1 }{ v }_{ 1 }+{ c }_{ 2 }{ v }_{ 2 }+...+{ c }_{ n }=0을\quad만족하는\\0이\quad 아닌\quad { c }_{ 1 },{ c }_{ 2 },...,{ c }_{ n }이\quad존재한다$$

반대로 c가 모두 0일 때만 위 조건을 만족하는 경우에는 **선형독립**(線型獨立, linear independence)이라고 합니다. 그 정의에 의해 **동차선형방정식(homogeneous linear equation)** $Ax=0$가 자명해($x=0$)를 유일한 해로 가질 때 **계수행렬(coefficient matrix)** $A$의 **열벡터(column vector)**들은 서로 선형독립입니다. 

무슨 말인지 알쏭달쏭하시죠? 예를 들어보겠습니다. 다음과 같은 두 개의 1차 연립방정식이 있습니다.

$$3{ x }_{ 1 }+6{ x }_{ 2 }=0\\ 2{ x }_{ 1 }+2{ x }_{ 2 }=0$$

위 연립방정식의 계수행렬 $A$는 아래와 같습니다. $A$의 열벡터와 $x$의 선형결합으로 위 연립방정식을 다시 표현한 것 또한 아래와 같습니다.

$$A=\begin{bmatrix} 3 & 6 \\ 2 & 2 \end{bmatrix},\quad x=\begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}\\ { x }_{ 1 }\begin{bmatrix} 3 \\ 2 \end{bmatrix}+{ x }_{ 2 }\begin{bmatrix} 6 \\ 2 \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

위 식을 살펴보면 $A$의 열벡터들을 선형결합해 영벡터를 만들기 위해선 $x_1$과 $x_2$가 동시에 0인 경우 말고는 해가 존재하지 않습니다. 이 경우 벡터 (3,2)와 (6,2)는 선형독립이라고 말할 수 있습니다. 그럼 아래의 경우는 어떨까요?

$${ x }_{ 1 }\begin{bmatrix} 3 \\ 1 \end{bmatrix}+{ x }_{ 2 }\begin{bmatrix} 6 \\ 2 \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

위와 같은 경우엔 식을 만족하는 $x$가 무수히 많습니다. (3,1)과 (6,2)는 동일한 직선 위에 있기 때문입니다. 이를 그림으로 보면 아래와 같습니다. 

<a href="http://imgur.com/hVmV0na"><img src="http://i.imgur.com/hVmV0na.png" width="350px" title="source: imgur.com" /></a>

그럼 3차원에선 어떨까요? 아래와 같이 벡터 $u$, $v$가 주어졌을 때 $u$, $v$가 만드는 공간과 $w$가 선형독립일 필요충분조건은 무엇일까요? 답은 이렇습니다. $x_1$과 $x_2$가 어떤 값을 가지든 상관없지만 $x_3$는 반드시 0이어야 합니다. 이해를 돕기 위해 그림으로도 표현해보겠습니다.

$$u=\begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix},\quad v=\begin{bmatrix} 1 \\ 6 \\ 0 \end{bmatrix},\quad w=\begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \\ { x }_{ 3 } \end{bmatrix}$$

![linear dependence](http://i.imgur.com/Ss2LDRI.png)

벡터 $u$와 $v$는 평면을 **생성(span)**합니다. 하지만 $u$와 $v$의 어떤 조합으로도 $x_3$이 0이 아닌 벡터(상단 좌측 그림의 파란색 벡터)를 만들어 낼 수는 없습니다. $x_3$에 대응하는 세번째 요소가 $u$, $v$ 모두 0이기 때문입니다. 

$x_3$이 0이 아니라면 $w$는 $u$, $v$가 만들어내는 평면에 속하지 않게 됩니다. 다시 말해 $w$와 Span{$u$, $v$}가 선형독립이라는 얘기입니다. 

반대로 $x_3$가 0이면 $w$는 $u$, $v$가 만드는 평면에 속하게 됩니다. 바꿔 말하면 $w$가 $u$, $v$의 선형결합으로 표시할 수 있다는 얘기입니다.

벡터 요소의 수/벡터 개수와 선형독립과의 관계를 살펴보겠습니다. 벡터가 다음과 같이 주어졌다고 칩시다.

$$a=\begin{bmatrix} 2 \\ 1 \end{bmatrix},\quad b=\begin{bmatrix} 4 \\ -1 \end{bmatrix},\quad c=\begin{bmatrix} -2 \\ 2 \end{bmatrix}$$

벡터 $b$와 $c$를 더하면 $a$와 같습니다. 즉 $a$, $b$, $c$는 서로 선형종속입니다. 

한편 벡터의 요소 수(위의 경우 2)보다 벡터 숫자(위 예시에서 3)가 많으면 해당 벡터들은 선형종속 관계를 갖습니다. 이는 **차원(dimension)**과 **기저(basis)**와 연관되는 개념인데요, 이번 포스팅 주제를 넘어서므로 추후에 논의하도록 하겠습니다.

마지막으로 영벡터를 포함한 벡터 집합은 서로 선형종속 관계입니다. $v_1$을 0으로 놓으면(사실 $v_2$, $v_3$… 아무렇게나 지정해도 관계 없습니다) 아래와 같은 식이 성립하기 때문입니다.

$$1{ v }_{ 1 }+0{ v }_{ 2 }+...+0{ v }_{ n }=0$$



## 선형변환의 정의

아래 조건을 만족하는 매핑 함수 $T$를 Linear하다고 정의합니다. 즉 $T$는 **선형변환**(線型變換, linear transformation)입니다.

> 임의의 두 벡터 $v$, $w$에 대해 $T(v+w)=T(v)+T(w)$
>
> 임의의 스칼라 $a$와 벡터 $v$에 대해 $T(av)=aT(v)$
>
> 임의의 스칼라 $c, d$와 벡터 $u,v$에 대해 $T(cu+dv)=cT(u)+dT(v)$

지금까지 논의한 선형시스템(1차 연립방정식) $Ax=b$을 선형변환으로 이해할 수도 있습니다. 행렬 $A$가 m x n 크기이고, $x$가 $n$차원, $b$가 $m$차원 벡터라고 할 때 행렬 $A$는 $n$차원 벡터 $x$를 $m$차원 벡터 $b$로 변환하는 선형변환 함수라는 것이지요. 이를 그림으로 도시하면 아래와 같습니다.

<a href="http://imgur.com/Eq53kxG"><img src="http://i.imgur.com/Eq53kxG.png" width="400px" title="source: imgur.com" /></a>

선형변환 함수 $T$를 아래와 같이 정의했다고 합시다. 그러면 아래 그림과 수식처럼 2차원 벡터 (2, -1)은 3차원 벡터 (5, 1, -9)로 변환됩니다.

$$T(x)=\begin{bmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \end{bmatrix}\begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}$$

<a href="http://imgur.com/ynM9tFL"><img src="http://i.imgur.com/ynM9tFL.png" width="250px" title="source: imgur.com" /></a>



## 선형변환 예시

그럼 이제부터 몇 가지 전형적인 선형변환과 그 행렬 형태를 살펴보도록 하겠습니다. 직관적으로 이해가능한데다 저도 보관 용도로 정리해두었으니 참고하시기 바랍니다.



### reflections

<a href="http://imgur.com/uPnbpUw"><img src="http://i.imgur.com/uPnbpUw.png" width="400px" title="source: imgur.com" /></a>

<a href="http://imgur.com/RoDXSuM"><img src="http://i.imgur.com/RoDXSuM.png" width="400px" title="source: imgur.com" /></a>

<a href="http://imgur.com/ospTeBE"><img src="http://i.imgur.com/ospTeBE.png" width="400px" title="source: imgur.com" /></a>

<a href="http://imgur.com/QC495wq"><img src="http://i.imgur.com/QC495wq.png" width="400px" title="source: imgur.com" /></a>

<a href="http://imgur.com/bnlpdpx"><img src="http://i.imgur.com/bnlpdpx.png" width="400px" title="source: imgur.com" /></a>



### contractions and expansions

<a href="http://imgur.com/Jwihag1"><img src="http://i.imgur.com/Jwihag1.png" width="450px" title="source: imgur.com" /></a>

<a href="http://imgur.com/cQP4sU8"><img src="http://i.imgur.com/cQP4sU8.png" width="450px" title="source: imgur.com" /></a>



### shears

<a href="http://imgur.com/VVAf9kP"><img src="http://i.imgur.com/VVAf9kP.png" width="450px" title="source: imgur.com" /></a>

<a href="http://imgur.com/dP2dXad"><img src="http://i.imgur.com/dP2dXad.png" width="450px" title="source: imgur.com" /></a>



### projections

<a href="http://imgur.com/u4ZTNdX"><img src="http://i.imgur.com/u4ZTNdX.png" width="400px" title="source: imgur.com" /></a>

<a href="http://imgur.com/vy3DFXB"><img src="http://i.imgur.com/vy3DFXB.png" width="400px" title="source: imgur.com" /></a>

