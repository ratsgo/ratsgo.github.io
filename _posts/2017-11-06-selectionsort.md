---
title: 선택정렬
category: Data structure&Algorithm
tag: [Selection sort, sort]
---

이번 글에서는 **선택정렬(selection sort)**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김황남 교수님 강의와 위키피디아를 정리하였음을 먼저 밝힙니다. 파이썬 코드는 [이곳](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSelectionSort.html)을 참고하였습니다. 그럼 시작하겠습니다.





## concepts

선택정렬은 위치 변경 횟수를 줄여, [버블정렬](https://ratsgo.github.io/data%20structure&algorithm/2017/11/05/bubblesort/)을 일부 개선한 기법입니다. 선택정렬의 작동 원리는 다음과 같습니다.



<a href="https://imgur.com/3Goa2af"><img src="https://i.imgur.com/3Goa2af.png" width="600px" title="source: imgur.com" /></a>



버블정렬은 왼쪽에 있는 값이 비교 대상인 오른쪽에 있는 값보다 크면 자리를 바꿔줬는데 반해, 선택정렬은 일단 최대값(혹은 최소값)을 찾은 뒤에야 이 값을 정해진 위치로 보내주게 됩니다. 다시 말해 비교 횟수 측면에서는 버블정렬과 선택정렬이 같고 둘 모두 $O(n^2)$의 계산복잡성을 갖지만 자리이동(*swap*) 측면에서는 선택정렬이 효율적입니다. 위 그림 예시의 경우 9번의 *iteration*에서 9번의 자리이동(*iteration*당 1번의 *swap*)이 있었습니다.





## 파이썬 구현

선택정렬의 파이썬 코드는 다음과 같습니다.

```python
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
```

