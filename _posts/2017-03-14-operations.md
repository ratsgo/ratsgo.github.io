---
title: 기초 행렬연산
category: Linear Algebra
tag: matrix
---

이번 포스팅에서는 **머신러닝**, **데이터마이닝** 기초인 **행렬 연산(Matrix Operations)**에 대해 다뤄 보려고 합니다. 연산의 정의 정도를 간단히 다루는 것이니 깊은 내용을 원하시는 분들은 [이곳](http://darkpgmr.tistory.com/103)을 참고 바랍니다. 이번 포스팅은 기본적으로 [고려대 김성범 교수님](http://dmqm.korea.ac.kr/content/page.asp?tID=101&sID=108) 강의를 참고했습니다.



## 데이터마이닝에서의 행렬 연산

데이터마이닝은 기본적으로 아래와 같은 구조의 데이터를 다룹니다. 계산 편의성을 도모하기 위해 위와 같은 데이터를 행렬로 변환합니다. 그렇게 되면 R, Python 등 각종 언어의 수치해석 라이브러리 도움을 받아 빠르게 연산을 할 수 있게 됩니다.

| -    | X1   | X2   | ...  | Xp   |
| ---- | ---- | ---- | ---- | ---- |
| obs1 | x11  | x12  | ...  | x1p  |
| obs2 | x21  | x22  | ...  | x2p  |
| ...  | ...  | ...  | ...  | ...  |
| obsn | xn1  | xn2  | ...  | xnp  |



## 벡터(Vector)

위 데이터에서 X1(d1)이라는 열(행)을 하나 떼서 만든 것이라고 생각하면 되겠습니다. 이를 식으로 쓰면 다음과 같습니다. 벡터는 다음과 같은 연산이 가능합니다.

$$X=\begin{pmatrix} { x }_{ 1 } \\ { x }_{ 2 } \\ ... \\ { x }_{ n } \end{pmatrix}​$$



### 스칼라 곱(Scalar Multiplication)

$${ c }_{ 1 }=5,\quad Y=\begin{pmatrix} { 1 } \\ { 2 } \\ { 3 } \end{pmatrix}$$

$${ c }_{ 1 }Y=\begin{pmatrix} { 1 } \\ { 2 } \\ { 3 } \end{pmatrix}=5\cdot \begin{pmatrix} { 1 } \\ { 2 } \\ { 3 } \end{pmatrix}=\begin{pmatrix} { 5 } \\ 10 \\ 15 \end{pmatrix}$$



### 벡터 덧셈(Vector Addition)

$$X=\begin{pmatrix} { 1 } \\ 3 \\ 5 \end{pmatrix},\quad Y=\begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix}$$

$$X+Y=\begin{pmatrix} { 1 } \\ 3 \\ 5 \end{pmatrix}+\begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix}=\begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix}$$



### 벡터의 내적(inner product)

$$X=({ x }_{ 1 },{ x }_{ 2 },...,{ x }_{ n }{ ) }^{ T }\\ Y=({ y }_{ 1 },y_{ 2 },...,{ y }_{ n }{ ) }^{ T }\\ <X,Y>={ X }^{ T }Y=\sum _{ i=1 }^{ n }{ { x }_{ i }{ y }_{ i }= } { x }_{ 1 }{ y }_{ 1 }+{ x }_{ 2 }{ y }_{ 2 }+...+{ x }_{ n }{ y }_{ n }$$



### 벡터의 길이(Length)

X가 다음과 같은 벡터로 정의된다면 X의 길이(Lx)는 아래와 같습니다. 2차원 공간에서 삼각형의 빗변을 구하는 피타고라스의 정리를 떠올리시면 쉽게 이해하실 수 있을 겁니다.

$$X=({ x }_{ 1 },{ x }_{ 2 },...,{ x }_{ n }{ ) }^{ T }$$

$$Lx=\sqrt { { x }_{ 1 }^{ 2 }+{ x }_{ 2 }^{ 2 }+...+{ x }_{ n }^{ 2 } } =\sqrt { { X }^{ T }X } $$



### 벡터 간 각도(Angle)

벡터 X와 Y 사이의 각도(θ)는 [코사인 법칙으로 유도](http://wiki.mathnt.net/index.php?title=%EB%B2%A1%ED%84%B0%EC%9D%98_%EB%82%B4%EC%A0%81#.EC.BD.94.EC.82.AC.EC.9D.B8_.EB.B2.95.EC.B9.99.EC.9C.BC.EB.A1.9C.EB.B6.80.ED.84.B0.EC.9D.98_.EC.9C.A0.EB.8F.84)하여 다음과 같이 표현할 수 있습니다. 다시 말해 두 벡터 내적값을 각각의 벡터 길이로 나눠준 값입니다.

$$cos(\theta )=\frac { ({ x }_{ 1 }{ y }_{ 1 }+{ x }_{ 2 }{ y }_{ 2 }+...+{ x }_{ n }{ y }_{ n }) }{ Lx\cdot Ly } =\frac { { x }^{ T }y }{ \sqrt { { x }^{ T }x } \cdot \sqrt { { y }^{ T }y }  } $$



### 벡터의 사영(projection)

벡터 x를 y에 사영한 결과는 다음과 같습니다.

$$projection\quad of\quad x\quad on\quad y=\frac { { x }^{ T }y }{ { y }^{ T }y } \cdot y$$



## 행렬(Matrix)

머신러닝, 데이터마이닝에서의 행렬은 위 표의 데이터 행과 열이 각각 행렬로 변환된 것이라고 보면 됩니다. 예컨대 3 x 2 **차원(dimension)**의 행렬 A는 다음과 같이 쓸 수 있습니다.

 $$A=\begin{pmatrix} -7 & 2 \\ 0 & 1 \\ 3 & 4 \end{pmatrix}$$



### 행렬 덧셈(Matrix Addition)

$$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}+\begin{pmatrix} 0 & 1 & 0 \\ 2 & -1 & 5 \end{pmatrix}=\begin{pmatrix} 1 & 3 & 3 \\ 6 & 4 & 11 \end{pmatrix}$$



### 스칼라 곱(Scalar Multiplication)

$${ c }_{ 1 }=2,\quad A=\begin{pmatrix} 1 & 0 \\ 2 & 5 \end{pmatrix}$$

$${ c }_{ 1 }\cdot A=\begin{pmatrix} 2 & 0 \\ 4 & 10 \end{pmatrix}$$



### 전치(transpose)

$$A=\begin{pmatrix} 2 & 1 & 3 \\ 0 & 1 & -1 \end{pmatrix},\quad { A }^{ T }=\begin{pmatrix} 2 & 0 \\ 1 & 1 \\ 3 & -1 \end{pmatrix}$$



### 정방행렬(Square Matrix)과 대칭행렬(Symmetric Matrix)

정방행렬은 행 개수와 열 개수가 같은 행렬이며 대칭행렬은 원래 행렬과 전치가 같은 행렬을 뜻합니다.



### 행렬 곱셈(Matrix Multiplication)

$$A=\begin{pmatrix} 3 & -1 & 2 \\ 4 & 0 & 5 \end{pmatrix},\quad B=\begin{pmatrix} 3 & 4 \\ 6 & -2 \\ 4 & 3 \end{pmatrix}$$

$$A\cdot B=\begin{pmatrix} 11 & 20 \\ 32 & 31 \end{pmatrix}$$



직관적으로 이해할 수 있는 예제 하나 더 첨부했습니다. ([출처](https://www.facebook.com/cpbeg/posts/1673363789639663))

<a href="http://imgur.com/3PVaEXE"><img src="http://i.imgur.com/3PVaEXE.gif" width="400px" title="source: imgur.com" /></a>



### 역행렬(Inverse)

$$AB=BA=I\\ B={ A }^{ -1 },\quad A={ B }^{ -1 }\\ A{ A }^{ -1 }=I$$



### 행렬식(Determinant)

역행렬 존재여부에 대한 판별식이자 행렬의 부피 역할을 하는 값입니다. 데이터마이닝 분야에선 행렬의 차원수가 아무리 크더라도 행렬식이 스칼라값으로 나오기 때문에 중요하게 취급됩니다. 행렬로 표현된 데이터를 요약한 결과로 해석될 여지가 있기 때문입니다. 자세한 내용은 [이곳](http://darkpgmr.tistory.com/104)을 참고하세요.



### 행렬의 대각합(trace)

**대각합(trace)** 또한 행렬식과 마찬가지로 행렬 차원수에 관계없이 하나의 값을 지니기 때문에 데이터의 의미를 압축 표현했다는 점에서 중요합니다.



### 정부호행렬(Definite Matrix)

모든 **고유값(eigenvalue)**이 양수인 행렬을 **양의 정부호행렬(Positive Definite Matrix)**이라고 합니다. 모든 고유값이 음수가 아닌 행렬을 **양의 준정부호행렬(Postive Semi-Definite Matrix)**라고 합니다. 아래 예시에선 임의의 벡터 c에 대해 A가 전자, B가 후자입니다.

$$A=\begin{pmatrix} 4 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}\quad is\quad Postive\quad Definite\quad Matrix$$

$$\because \begin{pmatrix} { c }_{ 1 } & { c }_{ 2 } & { c }_{ 3 } \end{pmatrix}\begin{pmatrix} 4 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} { c }_{ 1 } \\ { c }_{ 2 } \\ { c }_{ 3 } \end{pmatrix}=4{ c }_{ 1 }^{ 2 }+2{ c }_{ 2 }^{ 2 }+{ c }_{ 3 }^{ 2 }\ge 0$$

$$B=\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\quad  is\quad Postive\quad Semi-Definite\quad Matrix$$

$$\because \begin{pmatrix} { c }_{ 1 } & { c }_{ 2 } \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} { c }_{ 1 } \\ { c }_{ 2 } \end{pmatrix}=({ c }_{ 1 }^{ 2 }+{ c }_{ 2 }^{ 2 })\ge 0$$





## 공분산 행렬(Covariance Matrix)

변수가 여러 개인 **다변량 데이터**에선 변수 간 관련성, 즉 **상관성(correlation)**이 매우 중요한 문제가 됩니다. 확률변수 X의 값이 X의 평균보다 클 때 Y의 값도 Y의 평균보다 커지고, X의 값이 X의 평균보다 작을 때에는 Y의 값도 Y의 평균보다 작아지는 경향이 있으면 표준화된 X와 Y의 곱인 **상관계수(correlation coefficient)**는 양의 값을 가질 가능성이 큽니다. 바꿔 말하면 두 확률변수의 직선 관계가 얼마나 강하고 어떤 방향인지를 나타내는 값이라고 볼 수 있습니다. 

확률변수 X와 Y의 상관계수와 **공분산(Covariance)**는 다음과 같이 정의되는데요, 공분산을 X, Y의 표준편차로 나누어 표준화한 값이 X와 Y의 상관관계라고 할 수 있겠습니다. (N=데이터 개수, u1=X의 평균, u2=Y의 평균, s1=X의 표준편차, s2=Y의 표준편차)

$$
\begin{align*}
\rho &=\frac { 1 }{ N } \sum _{ i=1 }^{ N }{ \left( \frac { { X }_{ i }-{ \mu  }_{ 1 } }{ { \sigma  }_{ 1 } }  \right) \left( \frac { Y_{ i }-{ \mu  }_{ 2 } }{ { \sigma  }_{ 2 } }  \right)  } \\ 
&=E\left[ \left( \frac { { X }-{ \mu  }_{ 1 } }{ { \sigma  }_{ 1 } }  \right) \left( \frac { Y-{ \mu  }_{ 2 } }{ { \sigma  }_{ 2 } }  \right)  \right] \\ 
&=\frac { E\left[ (X-{ \mu  }_{ 1 })(Y-{ \mu  }_{ 2 }) \right]  }{ { \sigma  }_{ 1 }{ \sigma  }_{ 2 } } \\
&=\frac { Cov(X,Y) }{ { \sigma  }_{ 1 }{ \sigma  }_{ 2 } }
\end{align*}
$$

$$
\begin{align*}
cov(X,Y)&=E\left[ (X-{ \mu  }_{ 1 })(Y-{ \mu  }_{ 2 }) \right] \\ 
&=E\left[ XY-{ \mu  }_{ 2 }X-{ \mu  }_{ 1 }Y+{ \mu  }_{ 1 }{ \mu  }_{ 2 } \right] \\ 
&=E[XY]-{ \mu  }_{ 2 }E[X]-{ \mu  }_{ 1 }E[Y]+{ \mu  }_{ 1 }{ \mu  }_{ 2 }\\ 
&=E[XY]-{ \mu  }_{ 2 }{ \mu  }_{ 1 }-{ \mu  }_{ 1 }{ \mu  }_{ 2 }+{ \mu  }_{ 1 }{ \mu  }_{ 2 }\\ 
&=E[XY]-{ \mu  }_{ 1 }{ \mu  }_{ 2 }
\end{align*}
$$

공분산 행렬은 행렬의 각 요소가 공분산인 매트릭스를 의미합니다. 임의의 공분산행렬 A를 예를 들어 보겠습니다.

$$A=\begin{pmatrix} 2 & 4 \\ 4 & 6 \end{pmatrix}$$

첫 행은 확률변수 X, 두번째 행은 확률변수 Y에 해당한다고 치면, 마찬가지로 첫번째 열은 X, 두번째 열은 Y를 가리킵니다. 그렇다면 cov(X, X)=var(X)=2가 되겠네요. 역시 cov(Y, Y)=var(Y)=6입니다. cov(X, Y)=cov(Y, X)=4입니다.

그럼 공분산 행렬은 어떻게 구할까요? 아래와 같은 데이터가 있다고 칩시다.

| -    | X    | Y    | Z    |
| ---- | ---- | ---- | ---- |
| obs1 | 1    | 4    | 3    |
| obs2 | 2    | 3    | 5    |
| obs3 | 3    | 2    | 2    |
| obs4 | 4    | 1    | 7    |

위 데이터는 아래와 같이 행렬과 벡터 형태로 바꿀 수 있습니다.

$$D= \begin{pmatrix} 1 & 4 & 3 \\ 2 & 3 & 5 \\ 3 & 2 & 2 \\ 4 & 1 & 7 \end{pmatrix}$$

$$X=\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix},\quad Y=\begin{pmatrix} 4 \\ 3 \\ 2 \\ 1 \end{pmatrix},\quad Z=\begin{pmatrix} 3 \\ 5 \\ 2 \\ 7 \end{pmatrix}$$

위에서 정리한 공분산 공식을 벡터 형태로 바꾸면 다음과 같습니다.

$$
\begin{align*}
cov(X,Y)&=E[XY]-{ \mu  }_{ 1 }{ \mu  }_{ 2 }\\
&=\frac { 1 }{ n -1 } \sum _{ i=1 }^{ n }{ { X }_{ i }{ Y }_{ i } } -{ \mu  }_{ 1 }{ \mu  }_{ 2 }\\
&=\frac { 1 }{ n-1 } <X,Y>-{ \mu  }_{ 1 }{ \mu  }_{ 2 }\\
\end{align*}
$$

위의 식을 뜯어보면 벡터 X와 Y의 평균이 0으로 centering돼 있다면 cov(X,Y)는 X와 Y의 내적에 (데이터 개수 - 1)로 나눠준 값과 같습니다. 즉 아래처럼 되는 것이죠.

$$
\begin{align*}
cov(X,Y)&=\frac { 1 }{ 3 } \begin{pmatrix} 1 & 2 & 3 & 4 \end{pmatrix}\begin{pmatrix} 4 \\ 3 \\ 2 \\ 1 \end{pmatrix}-(2.5\times 2.5)\\ 
&=\frac { 1 }{ 3 } \begin{pmatrix} -1.5 & -0.5 & 0.5 & 1.5 \end{pmatrix}\begin{pmatrix} 1.5 \\ 0.5 \\ -0.5 \\ -1.5 \end{pmatrix}
\\&=-1.667
\end{align*}
$$

그럼 데이터 전체의 공분산을 구해볼까요? 앞서 정리한 **행렬 곱셈(Matrix Multiplication)**의 정의에 의해 행렬끼리의 곱셈결과는 각 요소에 해당하는 벡터들끼리의 내적값과 같습니다. 이러한 성질을 이용해 D를 각 변수별(열 기준)로 평균을 0으로 맞춰주고($D'$) 이를 제곱해주면 데이터 전체의 공분산 행렬을 한번에 구할 수 있습니다.

$$
\begin{align*}
cov(D)&={ \frac { 1 }{ 3 } D' }^{ T }D'\\ 
&=\frac { 1 }{ 3 } \begin{pmatrix} 1-2.5 & 2-2.5 & 3-2.5 & 4-2.5 \\ 4-2.5 & 3-2.5 & 2-2.5 & 1-2.5 \\ 3-4.25 & 5-4.25 & 2-4.25 & 7-4.25 \end{pmatrix}\begin{pmatrix} 1-2.5 & 4-2.5 & 3-4.25 \\ 2-2.5 & 3-2.5 & 5-4.25 \\ 3-2.5 & 2-2.5 & 2-4.25 \\ 4-2.5 & 1-2.5 & 7-4.25 \end{pmatrix}\\ 
&=\begin{pmatrix} 1.67 & -1.67 & 1.5 \\ -1.67 & 1.67 & -1.5 \\ 1.5 & -1.5 & 4.92 \end{pmatrix}
\end{align*}
$$

위 공분산 행렬의 해석은 이미 설명드린 바와 같습니다. X, Y, Z의 분산은 각각 1.67, 1.67, 4.92입니다. $cov(X,Y)=cov(Y,X)=-1.67$, $cov(Y,Z)=cov(Z,Y)=-1.5$,  $cov(X,Z)=cov(Z,X)=1.5$입니다.






## 독립(independence)과 직교(orthogonality)

확률변수 X의 값이 확률변수 Y의 값에 아무런 영향을 미치지 않는다면 X와 Y는 서로 **독립(independent)**이라고 합니다. 두 변수가 독립이라면 아래와 같은 식이 성립합니다.

$$E[XY]=E[X]\cdot E[Y]$$

두 확률변수 X와 Y가 서로 독립이라면 아래 식에 의해 공분산이 0이 됩니다. 바꿔 말하면 확률변수 X와 Y가 아무런 선형관계가 없다는 뜻입니다.

$$cov(X,Y)=E[XY]-E[X]\cdot E[Y]=E[X]\cdot E[Y]-E[X]\cdot E[Y]=0$$

**직교성(Orthogonality)**은 이미 설명드린 **벡터 간 각도**에서 도출된 개념입니다. 90도 직각에 해당하는 코사인값은 0이므로 두 벡터가 직교할 경우 그 내적은 0이 됩니다. 

통계학의 '독립', 선형대수학의 '직교성'이라는 개념은 엄밀히 말해 정확히 같지는 않지만 **공분산(covariance)**을 고리로 연결할 수 있게 됩니다. 확률변수(벡터) X와 Y의 평균을 각각 0으로 맞추고 공분산 공식에서 전체 데이터 개수로 나눠주는 부분(1/n)을 무시하면 공분산과 내적 관계를 아래 식처럼 쓸 수가 있습니다.

$$cov(X,Y)=<X,Y>$$

위 식을 지금까지 논의한 걸 바탕으로 해석하면 이렇습니다. 두 확률변수 X와 Y가 서로 독립이면 공분산은 0입니다. X와 Y의 내적 또한 0이 됩니다. 이를 다시 벡터 간 각도와 연관지어 생각하면 그 내적이 0인 두 벡터는 직교한다는 결론을 도출할 수 있게 됩니다. 따라서 '독립'과 '직교성'을 연결지어 생각할 수 있게 된다는 얘기입니다.




## 그램-슈미트 단위직교화(Gram-Schmidt Orthogonalization)

**그램슈미트 단위직교화**는 직교하지 않는 k개의 벡터(x)를 직교하는 k개 벡터(u)로 변환하는 방법입니다. 그림으로 이해하려면 [이곳](http://blog.naver.com/PostView.nhn?blogId=release&logNo=220279427020)을 참고하세요. 데이터마이닝에선 변수들끼리 상관관계를 지니게 되면(즉 서로 독립이지 않으면) 분석의 정확성이 떨어지게 됩니다.  이미 언급했듯이 독립과 직교성은 긴밀한 관계를 지니게 되므로 그램-슈미트 단위직교화를 통해 각 변수를 직교 벡터로 바꿀 경우 변수간 상관관계가 제거됩니다. 

$$
\begin{align*}
{ u }_{ 1 }&={ x }_{ 1 }\\ 
{ u }_{ 2 }&={ x }_{ 2 }-\frac { { x }_{ 2 }^{ T }{ u }_{ 1 } }{ { u }_{ 1 }^{ T }{ u }_{ 1 } } { u }_{ 1 }
\\ ...\\ 
{ u }_{ k }&={ x }_{ k }-\frac { { x }_{ k }^{ T }{ u }_{ 1 } }{ { u }_{ 1 }^{ T }{ u }_{ 1 } } { u }_{ 1 }-...-\frac { { x }_{ k }^{ T }{ u }_{ k-1 } }{ { u }_{ k-1 }^{ T }{ u }_{ k-1 } } { u }_{ k-1 }
\end{align*}
$$

한번 예를 들어보겠습니다. 다음과 같은 두 벡터가 있다고 합시다. 내적해보면 알겠지만 직교하지 않습니다.

$${ X }_{ 1 }=\begin{pmatrix} 4 \\ 0 \\ 0 \\ 2 \end{pmatrix},\quad X_{ 2 }=\begin{pmatrix} 3 \\ 1 \\ 0 \\ -1 \end{pmatrix}$$

위 식을 바탕으로 u를 만들어 봅시다.

$${ u }_{ 1 }={ X }_{ 1 }=\begin{pmatrix} 4 \\ 0 \\ 0 \\ 2 \end{pmatrix}$$

$${ u }_{ 1 }^{ T }{ u }_{ 1 }={ 4 }^{ 2 }+{ 0 }^{ 2 }+{ 0 }^{ 2 }+{ 2 }^{ 2 }=20$$

$$x_{ 2 }^{ T }{ u }_{ 1 }=12+0+0-2=10$$





$$u_{ 2 }=\begin{pmatrix} 3 \\ 1 \\ 0 \\ -1 \end{pmatrix}-\frac { 10 }{ 20 } \begin{pmatrix} 4 \\ 0 \\ 0 \\ 2 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \\ 0 \\ -2 \end{pmatrix}$$

u1, u2를 각각의 벡터 길이로 나누어 정규화한 것이 그램-슈미트 방법의 최종 결과물이 되겠습니다.

$$z_{ 1 }=\frac { 1 }{ \sqrt { 20 }  } \begin{pmatrix} 4 \\ 0 \\ 0 \\ 2 \end{pmatrix},\quad z_{ 2 }=\frac { 1 }{ \sqrt { 6 }  } \begin{pmatrix} 1 \\ 1 \\ 0 \\ -2 \end{pmatrix}$$



## 고유값(eigenvalue)과 고유벡터(eigenvector)

고유값과 고유벡터의 개념에 관해서는 [이곳](http://darkpgmr.tistory.com/105)을 참고하세요. 다음 식을 만족하는 람다와 X가 각각 정방행렬 A의 고유값과 고유벡터가 됩니다. 고유값과 고유벡터는 분석대상 데이터 행렬를 잘 표현하는 요약 결과이기 때문에 행렬식, 대각합 등과 더불어 중요한 정보가 되겠습니다.

$$AX=\lambda X$$

간단하게 고유값과 고유벡터를 구해보겠습니다.

$$A=\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$$

$$\left| A-\lambda I \right| =\left| \begin{matrix} 1-\lambda  & 0 \\ 1 & 3-\lambda  \end{matrix} \right| =(1-\lambda )(3-\lambda )=0\\ \lambda =1\quad or\quad 3$$

람다가 1일 때

$$AX=1\cdot X=\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} { X }_{ 1 } & { X }_{ 2 } \end{pmatrix}=\begin{pmatrix} { X }_{ 1 } \\ { X }_{ 2 } \end{pmatrix}$$

$${ X }_{ 1 }={ X }_{ 1 },\quad { X }_{ 1 }+3{ X }_{ 2 }={ X }_{ 2 }\\ \therefore \quad { X }_{ 1 }=-2{ X }_{ 2 }$$

람다가 3일 때

$$AX=3\cdot X=\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} { X }_{ 1 } & { X }_{ 2 } \end{pmatrix}=\begin{pmatrix} { 3X }_{ 1 } \\ { 3X }_{ 2 } \end{pmatrix}$$

$${ X }_{ 1 }={ 3X }_{ 1 },\quad { X }_{ 1 }+3{ X }_{ 2 }={ 3X }_{ 2 }\\ \therefore \quad X=\begin{pmatrix} 0 \\ 1 \end{pmatrix}$$



## 고유값 분해(Spectral Decomposition)

데이터 행렬을 고유값(람다)과 고유벡터(e)로 분해하는 방법입니다. 아래와 같이 정의됩니다.

$$A=\sum _{ i=1 }^{ k }{ { \lambda  }_{ i }{ e }_{ i }{ e }_{ i }^{ T } } $$

고유값 분해를 간단하게 해보겠습니다. 행렬 A의 고유값과 고유벡터는 다음과 같습니다.

$$A=\begin{pmatrix} 2.2 & 0.4 \\ 0.4 & 2.8 \end{pmatrix}\\ { \lambda  }_{ 1 }=3,\quad { \lambda  }_{ 2 }=2\\ { e }_{ 1 }=\begin{pmatrix} \frac { 1 }{ \sqrt { 5 }  }  \\ \frac { 2 }{ \sqrt { 5 }  }  \end{pmatrix},\quad { e }_{ 2 }=\begin{pmatrix} \frac { 2 }{ \sqrt { 5 }  }  \\ \frac { -1 }{ \sqrt { 5 }  }  \end{pmatrix}$$

그러면 행렬 A는 아래와 같이 다시 쓸 수 있습니다.
$$
\begin{align*}
A&=\begin{pmatrix} 2.2 & 0.4 \\ 0.4 & 2.8 \end{pmatrix}\\ &=3\begin{pmatrix} \frac { 1 }{ \sqrt { 5 }  }  \\ \frac { 2 }{ \sqrt { 5 }  }  \end{pmatrix}\begin{pmatrix} \frac { 1 }{ \sqrt { 5 }  }  & \frac { 2 }{ \sqrt { 5 }  }  \end{pmatrix}+2\begin{pmatrix} \frac { 2 }{ \sqrt { 5 }  }  \\ \frac { -1 }{ \sqrt { 5 }  }  \end{pmatrix}\begin{pmatrix} \frac { 2 }{ \sqrt { 5 }  }  & \frac { -1 }{ \sqrt { 5 }  }  \end{pmatrix}
\end{align*}
$$






