---
title: 합병정렬(Merge Sort)
category: Data structure&Algorithm
tag: sort
---

이번 글에서는 **합병정렬(Merge Sort)**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님 강의를 정리했고, 코드는 [이곳](http://starblood.tistory.com/entry/merge-sort-in-Python-Python-%EC%9C%BC%EB%A1%9C-merge-sort-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)을 참고했음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## 합병정렬

합병정렬은 다음과 같은 방식으로 동작합니다. ([그림 출처](https://ko.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort))



<a href="https://imgur.com/ood27RZ"><img src="https://i.imgur.com/ood27RZ.png" width="400px" title="source: imgur.com" /></a>



우선 데이터를 잘게 쪼갭니다(divide). 위 예시에선 8개로 쪼갰습니다. 둘씩 크기를 비교해 정렬합니다(conquer). 이를 합칩니다(merge). 이를 더 이상 합칠 array가 없을 때까지 반복합니다. 데이터 개수가 홀수개여서 정확히 둘로 쪼갤 수 없을 때는 왼쪽 배열에 요소 하나를 더 포함시킵니다. 여기에서 $p$는 하위 배열의 시작점, $r$은 끝점입니다. $q$는 하위 배열을 가르는 기준점입니다. 





## 파이썬 구현

합병정렬을 파이썬으로 구현한 코드는 다음과 같습니다. 우선 주어진 리스트를 중간 지점인 mid($q$)를 중심으로 왼쪽 리스트(*leftList*)와 오른쪽 리스트(*rightList*)로 쪼갭니다. *leftList*와 *rightList* 각각에 다시 이 작업을 재귀적으로 적용합니다.

```python
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)
```

*merge_sort* 함수가 돌면서 리스트를 분리하는 과정은 다음과 같습니다.

| Iter |    변수명    |            리스트            |
| :--: | :-------: | :-----------------------: |
|  0   | raw list  | 14, 7, 3, 12, 9, 11, 6, 2 |
|  1   | leftList  |       14, 7, 3, 12        |
|  1   | rightList |        9, 11, 6, 2        |
|  2   | leftList  |           14, 7           |
|  2   | rightList |           3, 12           |
|  3   | leftList  |            14             |
|  3   | rightList |             7             |
|  4   | leftList  |             3             |
|  4   | rightList |            12             |
|  5   | leftList  |           9, 11           |
|  5   | rightList |           6, 2            |
|  6   | leftList  |             9             |
|  6   | rightList |            11             |
|  7   | leftList  |             6             |
|  7   | rightList |             2             |

분리된 리스트를 합치는 *merge* 함수는 다음과 같습니다. 위에서 분리한 왼쪽 리스트(*left*)와 오른쪽 리스트(*right*)의 첫번째 요소를 비교해 작은 값을 결과 리스트(*result*)에 저장해 놓고, 해당 값을 해당 리스트에서 지웁니다. 이를 *left*와 *right*의 요소가 하나도 없을 때까지 반복합니다.

```python
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
```

우선 *merge* 함수가 1회 돌 때 어떻게 작동하는지 살펴보겠습니다. 예컨대 [3, 7, 12, 14]가 *left*, [2, 6, 9, 11]이 *right*인 상황에서 *merge* 함수는 다음과 같이 동작합니다. 볼드 표시는 비교 대상입니다.

| *left*           | *right*         | *result*              |
| ---------------- | --------------- | --------------------- |
| **3**, 7, 12, 14 | **2**, 6, 9, 11 |                       |
| **3**, 7, 12, 14 | **6**, 9, 11    | 2                     |
| **7**, 12, 14    | **6**, 9, 11    | 2, 3                  |
| **7**, 12, 14    | **9**, 11       | 2, 3, 6               |
| **12**, 14       | **9**, 11       | 2, 3, 6, 7            |
| **12**, 14       | **11**          | 2, 3, 6, 7, 9         |
| 12, 14           |                 | 2, 3, 6, 7, 9, 11     |
| 12               |                 | 2, 3, 6, 7, 9, 11     |
|                  |                 | 2, 3, 6, 7, 9, 11, 14 |

*merge* 함수가 여러 차례 호출되면서 연산하는 과정은 다음과 같습니다.

|          병합된 리스트          |
| :-----------------------: |
|           7, 14           |
|           3, 12           |
|       3, 7, 12, 14        |
|           9, 11           |
|           2, 6            |
|        2, 6, 9, 11        |
| 2, 3, 6, 7, 9, 11, 12, 14 |





## 합병정렬의 계산복잡성

데이터 개수가 $n$이라고 할 때 이를 정렬하는 데 $cn$의 시간이 걸린다고 칩시다. $c$는 컴퓨팅 파워 등과 관계 있는 어떤 상수를 나타냅니다. 우선 아래 그림을 봅시다.



<a href="https://imgur.com/M6hih5n"><img src="https://i.imgur.com/M6hih5n.png" width="400px" title="source: imgur.com" /></a>



예컨대 위에서부터 세 번째 층의 경우 원래 데이터를 4개로 쪼갰기 때문에 각각은 $cn/4$의 시간이 걸리지만, 데이터 덩어리 역시 4개이기 때문에 이에 해당하는 층의 계산시간은 $4*cn/4=cn$이 됩니다. 

전체 층의 수가 $\log{n}$이 되는 이유는 $n$에 구체적인 수를 넣어보면 명확해집니다. 예컨대 데이터 개수($n$)가 8개라고 칩시다. 그러면 전체 층의 수는 3이 됩니다. 따라서 상수항($c$)을 무시하고 생각해보면 합병정렬의 계산복잡성은 $n\log{n}$(각 층의 계산시간 x 전체 층의 수)가 되는 것입니다.