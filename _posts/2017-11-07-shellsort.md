---
title: 쉘정렬
category: Data structure&Algorithm
tag: [Shell sort, sort]
---

이번 글에서는 **쉘정렬(selection sort)**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김황남 교수님 강의와 위키피디아를 정리하였음을 먼저 밝힙니다. 예시 그림과 파이썬 코드는 [이곳](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html)을 참고하였습니다. 그럼 시작하겠습니다.





## concepts

쉘정렬은 정렬되지 않은 배열을 정렬하는 데 많은 계산량이 드는 [삽입정렬](https://ratsgo.github.io/data%20structure&algorithm/2017/09/06/insmersort/)을 개선한 기법입니다. 다음과 같은 배열을 정렬한다고 칩시다.

> 54, 26, 93, 17, 77, 31, 44, 55, 20

쉘정렬에서는 *gap*이라는 개념이 있습니다. 데이터를 띄엄띄엄 봐서 정렬한다는 개념인데요. 우선 위 숫자들을 아래와 같이 세 개 서브리스트로 나눕니다(*gap*=3).



<a href="https://imgur.com/9GmgdzX"><img src="https://i.imgur.com/9GmgdzX.png" width="350px" title="source: imgur.com" /></a>



이번엔 서브리스트별로 삽입정렬을 적용해 정렬한 뒤 세 서브리스트를 합칩니다. 다음과 같습니다.



<a href="https://imgur.com/g53byCb"><img src="https://i.imgur.com/g53byCb.png" width="350px" title="source: imgur.com" /></a>



마지막으로 위 리스트(`17, 26, 20, 44, 55, 31, 54, 77, 93 `)에 삽입정렬을 수행하면 쉘 정렬이 끝납니다. 쉘 정렬에서 *gap*은 정렬 대상 리스트의 절반으로 시작해 *iteration*이 돌 때마다 반씩 줄여가게 됩니다.





## 파이썬 코드

쉘정렬을 파이썬으로 구현한 코드는 다음과 같습니다.

```python
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
```

