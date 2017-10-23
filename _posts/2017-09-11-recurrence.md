---
title: 재귀함수의 계산복잡도
category: Data structure&Algorithm
tag: algorithm
---

이번 글에서는 알고리즘의 계산복잡도 함수가 **재귀식(Recurrence relation)** 내지 **점화식** 형태로 표현되는 경우를 살펴보도록 하겠습니다. 재귀식 또는 점화식이란 피보나치 수열(다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 되는 수열)처럼 수열의 항 사이에서 성립하는 관계식을 말합니다. 이로부터 데이터 수 $n$에 대해 **닫힌 형태(closed-form expression)**의 정확한 계산복잡도 함수를 찾는 것이 이 글의 목표입니다. (복잡도의 기준은 알고리즘이 필요로 하는 시간과 메모리 등 자원인데 전자를 '시간복잡도', 후자를 '공간복잡도'라 합니다) 이번 글 역시 고려대 김선욱 교수님 강의를 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## 재귀식 형태로 표현된 시간복잡성

알고리즘의 계산복잡도 함수가 재귀식으로 표현되는 대표적인 사례 가운데 하나가 **분할-정복(divide-and-conquer) 문제**입니다. 다음과 같이 풉니다. 우선 원래 문제를 부분문제로 쪼갭니다(divide). 부분 문제를 풉니다(conquer). 이를 합칩니다(merge). 원래 문제에 $n$개의 데이터가 있고, 이를 푸는 데 드는 시간복잡도를 $T(n)$이라고 할 때 $T(n)$은 다음과 같이 분해할 수 있습니다.



$$
T\left (n\right)=T\left (divide\right)+T\left (conquer\right)+T\left (merge\right)
$$



이를 **합병정렬(merge sort)**을 예시로 설명하겠습니다. 합병정렬 관련 자세한 내용은 [이곳](https://ratsgo.github.io/data%20structure&algorithm/2017/09/06/insmersort/)을 참고하시면 좋을 것 같습니다. 

$T(divide)$는 문제를 분할하는 데 걸리는 시간을 가리킵니다. 합병정렬을 예로 들면 원래 문제를 두 개로 나누기 위해 데이터를 반으로 자를 위치(인덱스) 하나만 고르면 되므로 $T(divide)=Θ(1)$입니다. (Big $Θ$ notation 관련해서는 [이곳](https://ratsgo.github.io/data%20structure&algorithm/2017/09/13/asymptotic/)을 참고하시면 좋을 것 같습니다)

$T(conquer)$는 (분할한 문제의 수 * 하위문제를 푸는 데 걸리는 시간)을 의미합니다. 원래 문제를 절반씩 두 개로 나누었고, 각 하위문제는 $n/2$개의 데이터가 있으므로 $T(conquer)=2*T(n/2)$가 될 것입니다.

$T(merge)$는 하위문제를 합치는 데 걸리는 시간입니다. 합병정렬에서는 하위문제를 합치면서 정렬을 수행합니다. $n=8$일 때 다음 그림과 같습니다.



<a href="https://imgur.com/mx0Hyvk"><img src="https://i.imgur.com/mx0Hyvk.png" width="300px" title="source: imgur.com" /></a>



위 그림을 자세히 보면 하위 첫번째 array의 첫번째 요소(2)와 두번째 array의 첫번째 요소(1)을 비교해 sorted array의 첫번째 요소를 결정(1)합니다. 그 다음으로 첫번째 array의 첫번째 요소(2)와 두번째 array의 두번째 요소(2)를 비교해 sorted array의 두번째 요소를 결정(2)합니다. 이런 방식으로 merge를 모두 수행하는 데 총 $n=8$회의 연산을 수행하게 됩니다. 따라서 데이터 수가 $n$일 때 $T(merge)=Θ(n)$이 됩니다.

이를 바탕으로 합병정렬의 시간복잡도를 다시 쓰면 다음과 같습니다. 



$$
T(n)=\Theta \left( 1 \right) +2\cdot T\left( \frac { n }{ 2 }  \right) +\Theta \left( n \right)
$$



하지만 위와 같은 재귀식 형태로는 해당 알고리즘의 시간복잡도를 정확히 알기가 어렵습니다. $T(n)$을 어렵게 구했지만 내부에 $T(n/2)$가 또 있어서 꼬리에 꼬리를 물고 $n$이 1이 될 때까지 식을 길게 늘여뜨려 써야하기 때문입니다. 이를 닫힌 형태로 구해보기 위해 다음 세 가지 방법을 씁니다.





## Substitution method

이 방법은 (1) 해당 알고리즘의 시간복잡도를 $n$에 대한 함수로 가정한 뒤 (2) 이를 귀납(induction)에 의해 증명하는 방식입니다. 합병정렬을 예로 들면, 시간복잡도 함수 $T(n)=2T(n/2)+Θ(n)$의 $T(n)$이 $n\log_{2}{n}+n$일 거라 우선 가정해보는 것입니다. (알고리즘 계산복잡도를 따질 때 상수항은 무시하므로 $Θ(1)$은 없는 것으로 취급)

이를 바탕으로 (2) 귀납에 의한 증명을 해보면 다음과 같습니다.

(2-1) $n=1$일 때 성립함을 보임 



$$
1\log _{ 2 }{ 1 } +1=0+1=T(1)
$$



(2-2) $n$보다 작은 임의의 $k$에 대해 성립한다고 가정 



$$
k\log _{ 2 }{ k } +k=T(k)
$$



(2-3) $k/2$일 때도 성립함을 보임



$$
\begin{align*}
T\left( \frac { k }{ 2 }  \right) &=2T\left( \frac { k }{ 4 }  \right) +\frac { k }{ 2 } \\ &=2\left( \frac { k }{ 4 } \log _{ 2 }{ \frac { k }{ 4 }  } +\frac { k }{ 4 }  \right) +\frac { k }{ 2 } \\ &=\frac { k }{ 2 } \log _{ 2 }{ \frac { k }{ 4 }  } +\frac { k }{ 2 } +\frac { k }{ 2 } \\ &=\frac { k }{ 2 } \left( \log _{ 2 }{ \frac { k }{ 2 }  } -\log _{ 2 }{ 2 }  \right) +\frac { k }{ 2 } +\frac { k }{ 2 } \\ &=\frac { k }{ 2 } \log _{ 2 }{ \frac { k }{ 2 }  } -\frac { k }{ 2 } +\frac { k }{ 2 } +\frac { k }{ 2 } \\ &=\frac { k }{ 2 } \log _{ 2 }{ \frac { k }{ 2 }  } +\frac { k }{ 2 } 
\end{align*}
$$


따라서 $T(n)=n\log_{2}{n}+n=Θ(n\log{n})$입니다. 하지만 Substitution method의 첫 단추인 가정 부분을 제대로 설계하지 않으면 증명이 불가능하다는 단점이 있습니다.





## Iteration method

이 방법은 점화식을 무한히 풀어 헤쳐 모두 더하는 방식으로 구합니다. $T(n)=n+4T(n/2)$을 구해보겠습니다.



$$
\begin{align*}
T\left( n \right) &=n+4T\left( \frac { n }{ 2 }  \right) \\ &=n+4\left( \frac { n }{ 2 } +4T\left( \frac { n }{ 4 }  \right)  \right) =n+4\frac { n }{ 2 } +4T\left( \frac { n }{ 4 }  \right) \\ &=n+4\left( \frac { n }{ 2 } +4\left( \frac { n }{ 4 } +4T\left( \frac { n }{ 8 }  \right)  \right)  \right) =n+4\frac { n }{ 2 } +{ 4 }^{ 2 }\frac { n }{ 4 } +{ 4 }^{ 3 }T\left( \frac { n }{ 8 }  \right) \\ &=...\\ &=n+4\frac { n }{ 2 } +{ 4 }^{ 2 }\frac { n }{ 4 } +{ 4 }^{ 3 }\frac { n }{ 8 } +...+{ 4 }^{ k }T\left( \frac { n }{ { 2 }^{ k } }  \right)
\end{align*}
$$



위 식에서 $n/2^k$가 1이 될 때까지 끝까지 반복해서 더합니다. 이 때 $k$는 $\log_{2}{n}$입니다. ($2^k=n$) 그런데 여기에서 로그의 성질에 의해 $4^{\log_{2}{n}}=2^{2\log_{2}{n}}=n^{2\log_{2}{2}}=n^2$이 되므로 다음이 성립합니다.



$$
\begin{align*}
T\left( n \right) &=n+4\frac { n }{ 2 } +{ 4 }^{ 2 }\frac { n }{ 4 } +{ 4 }^{ 3 }\frac { n }{ 8 } +...+{ 4 }^{ \log _{ 2 }{ n }  }T\left( 1 \right) \\ &=\sum _{ i=0 }^{ \log _{ 2 }{ n } -1 }{ \left( 4^{ i }\frac { n }{ { 2 }^{ i } }  \right)  } +{ n }^{ 2 }T\left( 1 \right) \\ &=n\sum _{ i=0 }^{ \log _{ 2 }{ n } -1 }{ { 2 }^{ i } } +{ n }^{ 2 }T\left( 1 \right) \\ &=n(\frac { { 2 }^{ \log _{ 2 }{ n }  }-1 }{ 2-1 } )+{ n }^{ 2 }T\left( 1 \right) \\ &=n(n-1)+{ n }^{ 2 }T\left( 1 \right) \\ &=\Theta \left( { n }^{ 2 } \right) +\Theta \left( { n }^{ 2 } \right) \\ &=\Theta \left( { n }^{ 2 } \right)
\end{align*}
$$


수식 말고도 트리 구조를 활용해 직관적으로 구하는 방법도 있습니다. $T(n)=T(n/3)+T(2n/3)$을 구해보겠습니다. 다음 그림과 같습니다.





<a href="https://imgur.com/K9WrTvy"><img src="https://i.imgur.com/K9WrTvy.png" width="400px" title="source: imgur.com" /></a>



우선 알고리즘이 한 개의 데이터를 처리하는 데 필요한 시간을 $c$라고 두면, $n$개 데이터를 처리하는 데 드는 시간복잡도는 $cn$입니다. 위 점화식은 한번 분기할 때마다 데이터를 각각 1/3, 2/3씩 나누게 됩니다. 

따라서 위 그림 트리를 $i$번 분기했을 때 말단 좌측 끝 노드의 처리 대상 데이터 수는 $n/3^i$가 됩니다. 이 말단 노드의 데이터 수가 1이 될 때까지 분기를 했을 경우 그 분기 횟수 $i$는 $\log_{3}{n}$이 됩니다. ($3^i=n$) 

마찬가지로 트리를 $j$번 분기했을 때 말단 우측 끝 노드의 데이터 수는 $n*{(2/3)}^j$가 됩니다. 이 말단 노드의 데이터 수가 1이 될 때까지 분기를 했을 경우 그 분기 횟수 $j$는 $\log_{3/2}{n}$이 됩니다. (${(3/2)}^j=n$)

점근 표기법(자세한 내용은 [이곳](https://ratsgo.github.io/data%20structure&algorithm/2017/09/13/asymptotic/) 참고)은 데이터 수 $n$에 대해 최고차항의 차수만 따집니다. 그런데 위 트리에서 각 층을 연산하는 데 $cn$, 분기 횟수는 최대 $\log_{3/2}{n}$이 되므로 이 알고리즘의 계산복잡도는 $Θ(n\log{n})$가 됩니다.

이렇게 놓고 보면 재귀적으로 분기하는 함수에서 분기 횟수는 분기 비율의 역수를 밑으로 하고 데이터 수를 진수로 하는 로그값임을 알 수 있습니다. 하지만 Iteration method은 점화식이 수렴하지 않고 발산하는 형태일 경우 적용할 수 없습니다.





## Master method

이 기법은 알고리즘의 계산복잡도 함수가 $T(n)=aT(n/b)+f(n)$ 형태일 경우 단번에 닫힌 형태를 구할 수 있는 마법과 같은 방법입니다. (단 $a≥1, b>1, f(n)>0$) 여기에서 $n^{\log_{b}{a}}$와 $f(n)$의 크기를 비교해 다음과 같이 한번에 닫힌 형태를 도출합니다. 그러나 아래 세 가지 경우를 제외한 함수에 대해서는 Master method를 적용할 수 없습니다.



`case 1` $n^{\log_{b}{a}}>f(n)$ → $T(n)=Θ(n^{\log_{b}{a}})$

`case 2` $n^{\log_{b}{a}}×\log{k}≓f(n)$ → $T(n)=Θ(n^{\log_{b}{a}}×\log{(k+1)}×n)$

- 단 로그를 제외한 최고차항의 차수가 같고 $k≥0$이어야 함

`case 3` $n^{\log_{b}{a}}<f(n)$ → $T(n)=f(n)$

- 단 충분히 큰 $n$과 1보다 작은 $c$에 대해 $af(n/b)≤cf(n)$을 만족해야 함



예를 들어보겠습니다.



- $T(n)=9T(n/3)+n$ 
  - $n^{\log_{3}{9}}=n^2$이고 $f(n)=n$이므로 `case 1`에 해당
  - 따라서 $T(n)=Θ(n^2)$
- $T(n)=27T(n/3)+Θ(n^3\log{n})$ 
  - $n^{\log_{3}{27}}=n^3$이고 $f(n)=Θ(n^3\log{n})$이므로 `case 2`에 해당하는지 체크 : $n^3$, $n^3\log{n}$ 비교
  - 로그를 제외한 최고차항의 차수가 3으로 같고 $k=1$일 때 `case 2`가 성립
  - 따라서 $T(n)=Θ(n^3×\log2×n)$
- $T(n)=5T(n/2)+Θ(n^3)$
  - $n^{\log_{2}{5}}<n^3$이므로 `case 3 `에 해당
  - $af(n/b)=5{(n/2)}^2=5n^3/8≤cn^3$를 만족하는 1보다 작은 $c$가 존재
  - 따라서 $T(n)=Θ(n^3)$






## Recursive Matrix Multiplication에 적용

지금까지 말씀드린 기법을 **Recursive Matrix Multiplication**에 적용해보겠습니다. 이 기법은 $n×n$ 정방행렬을 $n/2×n/2$ 행렬 4개로 나눈 뒤 내적(inner product)해 공간복잡도를 줄이는 방법입니다. 이같은 방식을 **타일링(tiling)**이라고 합니다. $A$와 $B$를 내적해 $C$를 얻는 연산($C=AB$)의 경우 다음과 같이 분할-정복 방식으로 나눠풀 수 있습니다.


$$
\begin{align*}
\begin{pmatrix} { C }_{ 11 } & { C }_{ 12 } \\ { C }_{ 21 } & { C }_{ 22 } \end{pmatrix}&=\begin{pmatrix} { A }_{ 11 } & A_{ 12 } \\ { A }_{ 21 } & A_{ 22 } \end{pmatrix}\cdot \begin{pmatrix} { B }_{ 11 } & B_{ 12 } \\ B_{ 21 } & { B }_{ 22 } \end{pmatrix}\\ \\ { C }_{ 11 }&={ A }_{ 11 }\cdot { B }_{ 11 }+{ A }_{ 12 }\cdot { B }_{ 21 }\\ { C }_{ 12 }&={ A }_{ 11 }\cdot { B }_{ 12 }+{ A }_{ 12 }\cdot { B }_{ 22 }\\ { C }_{ 21 }&={ A }_{ 21 }\cdot { B }_{ 11 }+{ A }_{ 22 }\cdot { B }_{ 21 }\\ { C }_{ 22 }&={ A }_{ 21 }\cdot { B }_{ 12 }+{ A }_{ 22 }\cdot { B }_{ 22 }
\end{align*}
$$


$n×n$ 정방행렬을 내적하는 데 필요한 계산복잡도를 $T(n)$이라 할 때 이를 다음과 같이 분해할 수 있습니다.


$$
T\left (n\right)=T\left (divide\right)+T\left (conquer\right)+T\left (merge\right)
$$


$T(divide)=Θ(1)$입니다. 1부터 $n$의 범위에서 행렬을 어디서 나눌지 한번만 결정하면 되기 때문입니다.

$T(conquer)=8T(n/2)$입니다. 위의 수식처럼 $n/2×n/2$ 행렬 내적을 8번 수행해야 합니다.

$T(merge)=Θ(n^2)$입니다. 예컨대 $A_{11}B_{11}$과 $A_{12}B_{21}$을 더해 $C_{11}$을 만든다고 할 때 $n×n$ 정방행렬의 전체 요소 $n^2$개의 1/4만큼 덧셈 연산을 수행해야할 것입니다. 이를 4회 반복해야 하므로 이같은 결과가 나옵니다.

이를 바탕으로 $T(n)$을 다시 쓰면 다음과 같습니다.


$$
T(n)=8\cdot T\left( \frac { n }{ 2 }  \right) +\Theta \left( {n}^{2} \right)
$$


위 점화식 형태의 함수를 Master method를 이용해 닫힌 형태로 나타내면 다음과 같습니다.



- $n^{\log_{2}{8}}=n^3>n^2$이므로 `case 1 `에 해당
- 따라서 $T(n)=Θ(n^{\log_{2}{8}})=Θ(n^3)$









