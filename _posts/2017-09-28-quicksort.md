---
title: 퀵 정렬(Quick Sort)
category: Data structure&Algorithm
tag: algorithm
---

이번 글에서는 **퀵 정렬(Quick Sort)** 알고리즘에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님 강의와 위키피디아를 정리하였음을 먼저 밝힙니다. 파이썬 코드 구현은 [이곳](https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py)을 참고하였습니다. 그럼 시작하겠습니다.





## 개념

퀵 정렬은 분할정복(divide and conquer) 방식으로 작동합니다. 그 절차는 다음과 같습니다.

- 리스트 가운데서 하나의 원소를 고릅니다. 이를 피벗(pivot)이라 합니다.
- 피벗 앞에는 피벗보다 작은 값, 뒤에는 큰 값이 오도록 하여 리스트를 둘로 분할합니다.
- 분할된 두 개 리스트 각각에 재귀적으로 이 과정을 반복합니다.







## 예시

다음과 같은 리스트를 정렬해보겠습니다.

> [5, 3, 7, 6, 2, 1, 4]

첫번째 값(5)을 피벗으로 택해보겠습니다. (마지막 요소 4를 택해도 관계 없습니다) 이 값보다 작은 값들로만 구성된 리스트와 큰 값들로만 구성된 리스트 둘로 분할합니다. 이를 각각 *LESSOR*와 *GREATER*라고 명명해보겠습니다.

> LESSOR = [3, 2, 1, 4]
>
> GREATER = [7, 6]

그리고 나서 LESSOR와 GREATER 각각에 같은 작업을 해당 리스트의 요소 개수가 하나가 될 때까지 재귀적으로 반복합니다. 





## 구현

퀵 정렬을 파이썬으로 구현한 코드는 다음과 같습니다.

```python
def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
```





## 계산복잡성

퀵 정렬의 계산복잡성은 피벗을 어떻게 선택하느냐에 따라 달라집니다. 최악의 경우는 다음과 같습니다. 다시 말해 피벗의 왼쪽(LESSOR) 요소가 매번 하나인 경우입니다. 이렇게 되면 높이가 $n$, 각 층에서 $n$개의 요소에 대해 정렬을 수행해야 하므로 $O(n^2)$의 계산복잡도를 가지게 됩니다.



<a href="https://imgur.com/v3xPU5E"><img src="https://i.imgur.com/v3xPU5E.png" width="200px" title="source: imgur.com" /></a>

가장 좋은 경우는 다음과 같습니다. 분할 과정이 다음과 같이 균형적이어서, 계산 트리의 높이가 $n$에서 $\log_2{n}$으로 줄어들게 되기 때문입니다. 이렇게 되면 높이가 $\log_2{n}$, 각 층에서 $n$개의 요소에 대해 정렬을 수행해야 하므로 $O(n\log_2{n})$의 계산복잡도를 가지게 됩니다.



<a href="https://imgur.com/hw72vWm"><img src="https://i.imgur.com/hw72vWm.png" width="350px" title="source: imgur.com" /></a>



Average case의 경우에도 퀵 정렬은 $O(n\log{n})$의 계산복잡도를 가진다고 합니다. 아울러 피벗을 선택할 때 정해진 위치가 아니라 랜덤하게 선택하거나, 몇 개 값을 랜덤 샘플링해 이 값들의 중앙값(median)에 가까운 값을 피벗으로 정하면 계산복잡도를 다소 낮추는 데 도움이 된다고 합니다.





## 퀵 정렬의 특징

설명의 편의를 위해 피봇을 기준으로 작은 값을 왼쪽, 나머지를 오른쪽으로 보내는 과정을 재귀적으로 반복한다고 했습니다만, *original code*는 이보다는 살짝 더 복잡합니다. 정렬 수행 과정에서 별도 저장 공간을 필요로 하지 않는 *in-place sort*를 지향하고자 하기 때문인데요. *original code*의 수행 과정을 보시려면 [이곳](https://www.youtube.com/watch?v=tIYMCYooo3c&feature=share)을 참고하시면 좋을 것 같습니다. 수행과정을 도식화하면 다음 그림과 같습니다. 이 과정에서 같은 값의 상대적 위치가 바뀔 수 있습니다(*unstable sort*).



<a href="https://imgur.com/1BFdNBc"><img src="https://i.imgur.com/1BFdNBc.jpg" width="500px" title="source: imgur.com" /></a>