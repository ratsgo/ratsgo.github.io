---
title: 재귀함수의 계산복잡성
category: Data structure&Algorithm
tag: algorithm
---

이번 글에서는 **재귀식(Recurrence relation)** 내지 **점화식** 형태로 표현된 알고리즘의 계산복잡성을 따져보도록 하겠습니다. 재귀식 또는 점화식이란 피보나치 수열(다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 되는 수열)처럼 수열의 항 사이에서 성립하는 관계식을 말합니다. 이로부터 **닫힌 형태(closed-form expression)**의 정확한 표현을 찾는 것이 이 글의 목표입니다. 이번 글 역시 고려대 김선욱 교수님 강의를 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 재귀식 형태로 표현된 시간복잡성

**분할-정복(divide-and-conquer) 문제**는 다음과 같이 풉니다. 우선 우선 원래 문제를 두 개의 부분문제로 쪼갭니다(divide). 부분 문제를 풉니다(conquer). 이를 합칩니다(merge). 원래 문제에 $n$개의 데이터가 있고, 이를 푸는 데  드는 시간복잡성을 $T(n)$이라고 할 때 $T(n)$은 다음과 같이 분해할 수 있습니다.


$$
T\left (n\right)=T\left (divide\right)+T\left (conquer\right)+T\left (merge\right)
$$


이를 **합병정렬(merge sort)**을 예시로 설명하겠습니다. 합병정렬 관련 자세한 내용은 [이곳](https://ratsgo.github.io/data%20structure&algorithm/2017/09/06/insmersort/)을 참고하시면 좋을 것 같습니다. 

$T(divide)$는 문제를 분할하는 데 걸리는 시간을 가리킵니다. 합병정렬을 예로 들면 원래 문제를 두 개로 나누기 위해 데이터를 반으로 자를 위치(인덱스) 하나만 고르면 되므로 $T(divide)=Θ(1)$입니다. (Big Θ notation 관련해서는 [이곳](https://ratsgo.github.io/data%20structure&algorithm/2017/09/13/asymptotic/)을 참고하시면 좋을 것 같습니다)

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





## Iteration method





## Master method





## 실제 문제에 적용

지금까지 말씀드린 기법을 실제 알고리즘에 적용해보겠습니다.



### 합병정렬



### Recursive Matrix Multiplication









