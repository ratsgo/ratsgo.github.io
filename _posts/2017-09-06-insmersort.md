---
title: Insertion Sort & Merge Sort
category: Data structure&Algorithm
tag: sort
---

이번 글에서는 알고리즘의 정의 및 **삽입정렬(Insertion Sort)**, **합병정렬(Merge Sort)**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님 강의를 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 알고리즘 정의

알고리즘의 정의는 다음과 같습니다.

> **A precisely defined sequence of computational steps** that transform a given input into a desired output. (주어진 입력을 원하는 출력으로 변환하는, **명확하게 정의된 일련의 계산 단계**)

알고리즘의 효율성 측정 기준은 연산시간(time)과 메모리(memory)입니다.



## 삽입정렬

삽입정렬은 다음과 같은 방식으로 동작합니다. 그림으로 예를 들어보겠습니다.



<a href="https://imgur.com/0CZLkCd"><img src="https://i.imgur.com/0CZLkCd.png" title="source: imgur.com" /></a>



(a)부터 볼까요? 비교 대상 key는 두번째 요소(2)부터 시작합니다. 해당 key의 왼쪽 요소와 크기 비교를 합니다. 따라서 (a)에서는 key(2)와 5를 비교하게 됩니다. 여기에선 5가 크므로 key(2)와 자리를 바꿔 줍니다.

(b)에서 key는 3번째 요소(4)입니다. 해당 key 왼쪽 요소인 5와 비교를 합니다. 여기에선 5가 크므로 key(4)의 자리를 바꿔 줍니다. 이번에는 2와 비교할 차례입니다만, key(4)가 2보다 크므로 자리를 바꿀 필요가 없습니다.

(c)에서 key는 4번째 요소(6)입니다. 해당 key 왼쪽 요소인 5와 비교를 합니다. key(6)가 5보다 크므로 자리를 바꿀 필요가 없습니다.



<a href="https://imgur.com/ajnGDWX"><img src="https://i.imgur.com/ajnGDWX.png" title="source: imgur.com" /></a>



(d)에서 key는 5번째 요소(1)입니다. 해당 key 왼쪽 요소인 6과 비교를 합니다. 여기에선 6이 크므로 key(1)의 자리를 바꿔 줍니다. 같은 방식으로 key(1)를 맨 처음 자리로 보내고 2, 4, 5, 6을 오른쪽으로 한칸씩 옮깁니다.

(e)에서 key는 6번째 요소(3)입니다. 해당 key 왼쪽 요소인 6과 비교를 합니다. 여기에선 6이 크므로 key(3)의 자리를 바꿔 줍니다. 같은 방식으로 key(3)을 세번째 자리로 보내고 4, 5, 6을 오른쪽으로 한칸씩 옮깁니다.

이런 방식으로 전체 데이터의 마지막 요소를 모두 고려하면 삽입정렬이 종료됩니다.



## 삽입정렬의 계산복잡성

삽입정렬의 의사코드와 계산 단계별 계산비용을 도식화한 표는 다음과 같습니다. 여기에서 $t_j$는 $j$번째 key를 정렬할 때 필요한 비교 연산 횟수를 가리킵니다. 예컨대 (c)에선 key(6)와 5, 딱 한 번만 비교하고 정렬이 끝났으니 $t_4$는 1입니다. 하지만 (d)에선 key(1)의 정렬을 위해 무려 5번이나 비교를 해야 했습니다. $t_j$는 데이터의 정렬 상태에 영향을 받는 값으로, 최소 1, 최대 $j$의 범위를 갖습니다.



<a href="https://imgur.com/znqmylP"><img src="https://i.imgur.com/znqmylP.png" width="400px" title="source: imgur.com" /></a>



그러면 정렬 대상 데이터 개수가 $n$이고, best case(즉 모든 $t_j$가 1인 상황)에 대해 계산복잡도를 구해보겠습니다. 다음 식과 같습니다.


$$
T(n)={ c }_{ 1 }n+{ c }_{ 2 }(n-1)+{ c }_{ 4 }(n-1)+{ c }_{ 5 }(n-1)+{ c }_{ 8 }(n-1)
$$


자세히 보면 $an+b$ 형태의 1차식입니다. 따라서 best case일 때 삽입정렬의 계산복잡도는 $n$에 대해 선형적으로 증가합니다.

이번엔 worst case(즉 모든 $t_j$가 $j$인 상황)에 대해 살펴봅시다. 다음 식과 같습니다.



$$
T(n)={ c }_{ 1 }n+{ c }_{ 2 }(n-1)+{ c }_{ 4 }(n-1)+{ c }_{ 5 }(\frac { n(n+1) }{ 2 } -1)\\+{ c }_{ 6 }(\frac { n(n-1) }{ 2 } )+{ c }_{ 7 }(\frac { n(n-1) }{ 2 } )+{ c }_{ 8 }(n-1)
$$


위 식은 $an^2+bn+c$ 형태의 2차식입니다. 따라서 worst case일 때 삽입정렬의 계산복잡도는 $n^2$에 비례하여 증가합니다. 따라서 삽입정렬의 계산복잡도는 best와 worst case 어딘가쯤에 위치하게 될 겁니다.

그런데 알고리즘의 계산복잡도를 구할 때 사실 이렇게까지 자세히 뜯어볼 필요는 없습니다. 가능한 경우의 수를 고려해 어림짐작하는 방법도 얼마든지 있어야 하니까요. best case일 때는 데이터 개수 $n$개만큼의 비교 연산을 수행하면 됩니다. worst case일 때는 $j$가 1일 때는 $t_j$가 1, 2일 땐 (1+2), 3일 땐 (1+2+3)... 이렇게 되므로 $Σn=n(n+1)/2$이 되는 걸 확인할 수 있습니다.

아울러 $T(n)$의 계수($c$)들은 컴퓨팅 파워 등에 따라 커질 수도, 작아질 수도 있습니다. 다만 보통의 알고리즘은 데이터 개수($n$)에 민감하기 때문에 계산복잡성을 구할 때는 계수는 보통 무시하게 됩니다.



## 합병정렬

합병정렬은 다음과 같은 방식으로 동작합니다. ([그림 출처](https://ko.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort))



<a href="https://imgur.com/ood27RZ"><img src="https://i.imgur.com/ood27RZ.png" width="400px" title="source: imgur.com" /></a>



우선 데이터를 잘게 쪼갭니다(divide). 위 예시에선 8개로 쪼갰습니다. 둘씩 크기를 비교해 정렬합니다(conquer). 이를 합칩니다(merge). 이를 더 이상 합칠 array가 없을 때까지 반복합니다. 데이터 개수가 홀수개여서 정확히 둘로 쪼갤 수 없을 때는 왼쪽 배열에 요소 하나를 더 포함시킵니다. 여기에서 $p$는 하위 배열의 시작점, $r$은 끝점입니다. $q$는 하위 배열을 가르는 기준점입니다. 합병정렬의 의사코드는 다음과 같습니다.



<a href="https://imgur.com/qgqjupk"><img src="https://i.imgur.com/qgqjupk.png" width="700px" title="source: imgur.com" /></a>





## 합병정렬의 계산복잡성

데이터 개수가 $n$이라고 할 때 이를 정렬하는 데 $cn$의 시간이 걸린다고 칩시다. $c$는 컴퓨팅 파워 등과 관계 있는 어떤 상수를 나타냅니다. 우선 아래 그림을 봅시다.



<a href="https://imgur.com/M6hih5n"><img src="https://i.imgur.com/M6hih5n.png" width="400px" title="source: imgur.com" /></a>



예컨대 위에서부터 세 번째 층의 경우 원래 데이터를 4개로 쪼갰기 때문에 각각은 $cn/4$의 시간이 걸리지만, 데이터 덩어리 역시 4개이기 때문에 이에 해당하는 층의 계산시간은 $4*cn/4=cn$이 됩니다. 

전체 층의 수가 $lgn$이 되는 이유는 $n$에 구체적인 수를 넣어보면 명확해집니다. 예컨대 데이터 개수($n$)가 8개라고 칩시다. 그러면 전체 층의 수는 3이 됩니다. 따라서 상수항($c$)을 무시하고 생각해보면 합병정렬의 계산복잡성은 $nlgn$(각 층의 계산시간 x 전체 층의 수)가 되는 것입니다.