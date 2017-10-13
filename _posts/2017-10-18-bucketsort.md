---
title: 버킷 정렬(Bucket sort)
category: Data structure&Algorithm
tag: Algorithm
---

이번 글에서는 **버킷 정렬(Bucket sort)** 알고리즘을 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님 강의와 위키피디아를 참고해 정리하였음을 먼저 밝힙니다. 파이썬 코드는 [이곳](https://stackoverflow.com/questions/36688805/what-is-this-bucket-sort-implementation-doing)을 참고로 하였습니다. 그럼 시작하겠습니다.





## concepts

값을 비교하여 정렬하는 기법인 comparison sort의 계산복잡성은 최소 $O(n\log{n})$입니다. 버킷 정렬은 분석 대상 데이터의 분포 특성을 활용해 계산복잡성을 $O(n)$ 수준으로 개선시키려는 것을 목적으로 하고 있습니다. 버킷 정렬은 데이터가 특정 범위 내에 확률적으로 균등하게 분포한다고 가정할 수 있을 때 적용할 만한 기법입니다. 이해를 돕기 위해 다음 그림을 보겠습니다.



<a href="https://imgur.com/bf8nVZt"><img src="https://i.imgur.com/bf8nVZt.png" width="400px" title="source: imgur.com" /></a>



위와 같이 10개의 데이터 $A$가 주어졌을 때 같은 크기의 버킷 $B$를 만듭니다. 만약 $A$의 분포가 균등하다면 각 버킷에는 1~2개의 요소만 속해 있을 것입니다. 이렇게 1~2개 값들만 있는 버킷 하나를 정렬하는 데 필요한 계산복잡성은 $O(1)$이 될 것이고, 이 작업을 $n$개 버킷에 모두 수행한다고 하면 전체적인 계산복잡성은 $O(n)$이 될 것입니다. 이것이 바로 버킷 정렬이 노리는 바입니다.

버킷 정렬의 구체적인 프로세스는 다음과 같습니다.

- 데이터 $n$개가 주어졌을 때 데이터의 범위를 $n$개로 나누고 이에 해당하는 $n$개의 버킷을 만든다.
- 각각의 데이터를 해당하는 버킷에 집어 넣는다. (C 등에서는 [연결리스트](https://ratsgo.github.io/data%20structure&algorithm/2017/09/30/list/)를 사용하며 새로운 데이터는 연결리스트의 head에 *insert*한다)
- 버킷별로 정렬한다.
- 이를 전체적으로 합친다.





## 파이썬 구현

파이썬으로 구현한 버킷 정렬 코드는 다음과 같습니다. 버킷을 중첩 리스트로 구현했고, 각 버킷별로 정렬할 때 [퀵 정렬](https://ratsgo.github.io/data%20structure&algorithm/2017/09/28/quicksort/)을 적용했습니다.

```python
def bucket_sort(seq):
    # make buckets
    buckets =  [[] for _ in range(len(seq))]
    # assign values
    for value in seq:
        bucket_index = value * len(seq) // (max(seq) + 1)
        buckets[bucket_index].append(value)
    # sort & merge
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(quick_sort(bucket))
    return sorted_list

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

