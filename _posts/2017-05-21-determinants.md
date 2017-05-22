---
title: 행렬식(determinant)
category: Linear Algebra
tag: determinant
---

이번 글에서는 행렬식에 대해 살펴보겠습니다. 이번 글은 고려대 박성빈 교수님 강의와 David C. Lay의 Linear Algebra (4th edition)을 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다. 



## 행렬식의 정의

**행렬식(determinant)**은 행렬을 대표하는 값으로 n x n (n은 2 이상)의 정방행렬 $A$에 대해 다음과 같이 정의됩니다. $detA_{11}$이란 $A$에서 1행과 1열을 제외한 행렬의 행렬식을 의미합니다. 2 x 2 행렬의 요소값이 $a,b,c,d$라고 할 때 행렬식은 $ad-bc$입니다.


$$
\begin{align*}
detA&={ a }_{ 11 }det{ A }_{ 11 }-{ a }_{ 12 }det{ A }_{ 12 }+...+{ (-1) }^{ 1+n }det{ A }_{ 1n }\\ &=\sum _{ j=1 }^{ n }{ { (-1) }^{ 1+j }{ a }_{ 1j }det{ A }_{ 1j } } 
\end{align*}
$$

$A$가 다음 행렬이라고 칩시다.

$$
A=\begin{bmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{bmatrix}
$$

$detA$는 다음과 같이 계산할 수 있습니다.



$$
\begin{align*}
detA&={ a }_{ 11 }det{ A }_{ 11 }-{ a }_{ 12 }det{ A }_{ 12 }+{ a }_{ 13 }det{ A }_{ 13 }\\\\ &=1\cdot det\begin{bmatrix} 4 & -1 \\ -2 & 0 \end{bmatrix}-5\cdot det\begin{bmatrix} 2 & -1 \\ 0 & 0 \end{bmatrix}+0\cdot det\begin{bmatrix} 2 & 4 \\ 0 & -2 \end{bmatrix}\\\\ &=1(0-2)-5(0-0)+0(-4-0)=-2
\end{align*}
$$

지금까지는 행렬식을 구할 때 $A$의 첫번째 행을 쓰는 걸 기준으로 설명해드렸는데 사실 어떤 행이나 열을 택해서 구해도 행렬식은 같은 값이 나옵니다. 행렬식 계산을 일반화해서 나타내면 아래와 같습니다. 이 때 $C_{ij}$를 **(i,j)-cofactor**라고 합니다.



$$
\begin{align*}
&{ C }_{ ij }={ (-1) }^{ i+j }det{ A }_{ ij }\\\\ use\quad ith\quad row\quad :\quad &detA={ a }_{ i1 }det{ C }_{ i1 }+{ a }_{ i2 }det{ C }_{ i2 }+...+{ a }_{ in }det{ C }_{ in }\\\\ use\quad jth\quad col\quad :\quad &detA={ a }_{ 1j }det{ C }_{ 1j }+{ a }_{ 2j }det{ C }_{ 2j }+...+{ a }_{ nj }det{ C }_{ nj }
\end{align*}
$$



## 행렬식의 성질

행렬식의 성질은 다음과 같습니다.

>(1) 행렬 $A$의 임의의 행에 스칼라 곱을 한 뒤 다른 행에 더해 $B$를 만들었을 때 두 행렬의 행렬식은 같다.
>
>(2) 행렬 $A$의 임의의 행을 다른 행과 바꾸어 $B$를 만들었을 때 $detB=-detA$
>
>(3) 행렬 $A$의 임의의 행에 스칼라 곱을 해 $B$를 만들었을 때 $detB=kdetA$
>
>(4) **삼각행렬(triangular matrix)**의 행렬식은 주 대각원소들의 곱과 같다.
>
>(5) 행렬 $A$가 **가역(invertible)**임과 $detA≠0$임은 동치입니다.
>
>(6) $detA^T=detA$
>
>(7) $detAB=(detA)(detB)$



## 선형시스템의 해와 행렬식

**크래머의 법칙(Cramer's Rule)**은 다음과 같습니다. $n*n$ 크기의 행렬 $A$가 가역이고, 임의의 $n$차원 벡터 $b$에 대해 $Ax=b$가 유일한 해를 갖는다면 $x$의 $i$번째 요소값인 $x_i$는 아래 식과 같습니다. 

$$
x_{ i }=\frac { det{ A }_{ i }(b) }{ detA } 
$$

$e$는 $n*n$ 크기의 **단위행렬(identity matrix)**의 열벡터를 뜻하는데요. $A_i(b)$는 단위행렬의 $i$번째 열벡터 $e_i$를 $b$로 대체한 행렬에 $A$를 곱한 행렬을 가리킵니다. 다음과 같습니다.

$$
\begin{align*}
A\cdot { I }_{ i }(x)=&A\begin{bmatrix} { e }_{ 1 } & ... & x & ... & { e }_{ n } \end{bmatrix}\\ &=\begin{bmatrix} { Ae }_{ 1 } & ... & Ax & ... & A{ e }_{ n } \end{bmatrix}\\ &=\begin{bmatrix} { a }_{ 1 } & ... & b & ... & a_{ n } \end{bmatrix}\\ &={ A }_{ i }(b)
\end{align*}
$$

크래머의 법칙을 활용하면 행렬식만으로도 선형 시스템의 해를 구할 수 있게 됩니다.



## 역행렬과 행렬식

**기본행연산** 말고도 역행렬을 구할 수 있는 방법이 있습니다. 행렬식을 이용하는 것입니다. 다음과 같습니다.

$$
\begin{align*}
{ A }^{ -1 }&=\frac { 1 }{ detA } \begin{bmatrix} { C }_{ 11 } & { C }_{ 21 } & ... & { C }_{ n1 } \\ { C }_{ 12 } & { C }_{ 22 } & ... & { C }_{ n2 } \\ ... & ... & ... & ... \\ { C }_{ 1n } & { C }_{ 2n } & ... & { C }_{ nn } \end{bmatrix}\\ &=\frac { 1 }{ detA } adjA
\end{align*}
$$



## 행렬식의 기하학적 성질 : 부피

행렬식을 기하학적으로 살펴보겠습니다. $detA=detA^T$가 성립하고, 두 개 열벡터의 위치를 바꾸거나 임의의 열에 스칼라곱을 한 뒤 다른 열에 더해도 행렬식의 크기가 바뀌지 않으므로 임의의 $2*2$ 행렬 $A$를 아래와 같은 형태로 변형해 행렬식을 구해도 됩니다.


$$
\left| det\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix} \right| =\left| ad \right|
$$

이를 그림으로 나타내면 $2*2$ 행렬 $A$의 행렬식은 일종의 **넓이**로 이해할 수 있습니다.

<a href="http://imgur.com/qPBOBWA"><img src="http://i.imgur.com/qPBOBWA.png" width="200px" title="source: imgur.com" /></a>

이를 일반화해서 생각해 보겠습니다. $2*2$ 행렬 $A$의 영벡터가 아닌 열벡터를 각각 $a_1, a_2$, 그리고 임의의 스칼라를 $c$라고 둡시다. 아래 그림을 보겠습니다.


<a href="http://imgur.com/ZM77X8c"><img src="http://i.imgur.com/ZM77X8c.png" width="450px" title="source: imgur.com" /></a>


위 그림을 보시면 $a_1$과 $a_2+ca_1$이 이루는 직사각형의 넓이와 $a_1$과 $a_2$가 이루는 평행사변형의 넓이가 같습니다. 행렬식의 성질에 의해 임의의 열에 스칼라곱을 한 뒤 다른 열에 더해도 행렬식의 크기가 바뀌지 않으므로 자명한 사실입니다.

마찬가지로 $3*3$ 크기 행렬의 행렬식은 일종의 **부피**로 이해할 수 있습니다. 아래 그림과 같습니다.



<a href="http://imgur.com/l6pttjr"><img src="http://i.imgur.com/l6pttjr.png" width="200px" title="source: imgur.com" /></a>



이를 또 일반화해서 나타내면 아래와 같습니다.

<a href="http://imgur.com/efEXej2"><img src="http://i.imgur.com/efEXej2.png" width="500px" title="source: imgur.com" /></a>





## 선형변환과 행렬식

선형변환 $T: R^2 → R^2$에 대응하는 $2*2$ 크기의 **표준행렬(standard matrix)** $A$가 있다고 칩시다. $S$가 $R^2$에 존재하는 도형일 때 면적과 관계된 식과 그림은 다음과 같습니다.


$$
\left\{ area\quad of\quad T(S) \right\} =\left| detA \right| \cdot \{ area\quad of\quad S\} 
$$

<a href="http://imgur.com/yoUtSnh"><img src="http://i.imgur.com/yoUtSnh.png" width="200px" title="source: imgur.com" /></a>

마찬가지로 3차원에서는 아래와 같이 정의됩니다.


$$
\left\{ volume\quad of\quad T(S) \right\} =\left| detA \right| \cdot \{ volume\quad of\quad S\} 
$$



