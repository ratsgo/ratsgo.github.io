---
title: Augmented Data Structure
category: Data structure&Algorithm
tag: [Augmented Data Structure]
---

이번 글에서는 **Augmented Data Structure**에 대해 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님 강의와 위키피디아를 참고해 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## concept

*Augmented Data Stucture*란 기존 자료구조에 추가적인 정보를 저장해, 이를 바탕으로 계산효율성을 높이려는 자료구조의 일종입니다. [이진탐색트리(binary search tree)](https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/), [RB 트리](https://ratsgo.github.io/data%20structure&algorithm/2017/10/28/rbtree/) 등 노드에 서브트리 노드의 개수 정보를 추가해 중위탐색(inorder traverse) 성능을 높이는 사례가 바로 여기에 해당합니다. 이진탐색트리, RB 트리에서 중위탐색에 소요되는 계산복잡성은 $O(n)$인데, *Augmented Data Structure*를 써서 $O(\log{n})$의 계산복잡성을 달성할 수 있습니다.





## OS-Select

*OS-Select*는 주어진 이진탐색트리에서 $i$번째 작은 값을 찾는 문제입니다(1번째 작은 값=최소값). 아래 그림과 같이 기존 이진탐색트리 노드에 자기 자신을 포함한 자식노드의 개수를 별도로 저장해 둡니다. 예컨대 아래 이진탐색트리에서 잎새노드는 자식노드가 없으므로 그 값이 1이 됩니다. $F$에 해당하는 노드는 자식노드 2개에 자기 자신까지 해서 그 값이 3이 됩니다. 마찬가지로 $C$ 노드는 왼쪽 서브트리의 노드 1개, 오른쪽 서브트리의 노드 3개, 자기 자신, 이렇게 총 5가 됩니다.



<a href="https://imgur.com/HMoRAtM"><img src="https://i.imgur.com/HMoRAtM.png" width="500px" title="source: imgur.com" /></a>



예컨대 위 트리에서 6번째 작은 값을 찾는다고 칩시다. 이진탐색트리는 각 노드에 해당하는 값이 왼쪽 자식노드보다는 크고 오른쪽 자식노드보다는 작다는 성질을 가지고 있습니다. 주어진 이진탐색트리 루트노드의 왼쪽 서브트리 노드 수가 5개이므로, 위 트리에서 6번째 작은 값은 루트노드 $M$이 됩니다(`case 1`).

이번엔 4번째 작은 값을 찾아 봅시다. 루트노드의 왼쪽 서브트리 노드 수가 5개이므로, 우리가 찾고자 하는 값은 루트노드의 왼쪽 서브트리에 속해 있다는 걸 알 수 있습니다. 다시 말해 루트노드의 왼쪽 자식노드를 루트로 하는 새로운 서브트리 가운데 4번째 작은 값이 우리가 찾는 값이 됩니다(`case 2`이고 *OS-Select($C$, 4)* 재귀 호출). 

이번엔 8번째 작은 값을 찾아 봅시다. 루트노드의 왼쪽 서브트리와 루트노드를 포함한 노드 수가 6개이므로, 우리가 찾고자 하는 값은 루트노드의 오른쪽 자식노드를 루트로 하는 새로운 서브트리 가운데 2번째(8-6=2) 작은 값이 됩니다(`case 3`이고 *OS-Select($P$, 8-6)* 재귀 호출).

이를 의사코드로 표현하면 다음과 같습니다.

```python
# x: 주어진 이진탐색트리의 루트노드
# i: i번째 작은값의 i
OS-Select(x, i):
	r = x.left.size + 1
	# case 1
    if i == r:
		return x
    # case 2
	elif i < r:
		return OS-Select(x.left, i)
	# case 3
    else:
		return OS-Select(x.right, i-r)

# 최초 시작은 루트노드에서
# 이후 재귀적으로 함수 호출
OS-Select(T.root, i)
```

*OS-Select*는 최악의 경우에도 루트노드에서 잎새노드까지의 경로만을 탐색하게 됩니다. *OS-Select*의 계산복잡성은 트리 노드수가 전체 $n$개일 때 트리의 높이($\log{n}$)에 비례한다는 얘기입니다. 따라서 전체적으로 계산복잡성은 $O(\log{n})$이 됩니다.





## OS-Rank

*OS-Rank*는 주어진 이진탐색트리에서 $x$가 몇 번째로 큰 값인지 알아내는 문제입니다. *OS-Select*와 마찬가지로 기존 이진탐색트리에 자기 자신을 포함한 자식노드의 개수를 별도로 저장해 둡니다. 아래 그림은 *OS-Select* 때 예시로 든 것과 동일합니다.



<a href="https://imgur.com/HMoRAtM"><img src="https://i.imgur.com/HMoRAtM.png" width="500px" title="source: imgur.com" /></a>



이진탐색트리에서 각 노드의 rank는 왼쪽 서브트리의 노드 수가 중요합니다. 예컨대 몇 번째 큰 값인지 알고자 하는 노드가 $F$라고 칩시다. $F$의 rank는 다음과 같이 분리해서 생각해볼 수 있습니다.

- F와 F의 왼쪽 서브트리 : 1+D의 값(1)
- C와 C의 왼쪽 서브트리 :  1+A의 값(1)
- F의 rank = 2+2 = 4

이를 의사코드로 표현하면 다음과 같습니다. 아래 코드에서 *y.p.left.size*는 *y* 노드 부모의 왼쪽 서브트리 노드의 수를 가리킵니다.

```python
# T : 이진탐색트리
# x : 몇 번째 큰 값인지 알고자 하는 노드
OS-Rank(T, x):
	r = x.left.size + 1
	y = x
	while y != T.root:
      	# 위 그림 기준으로 C, F가 
        # 각각 부모노드, 오른쪽 자식노드인지 확인
		if y == y.p.right:
          	 # 기존 rank에 더해
             # 왼쪽 서브트리 + 자기 자신 반영
			r = r + y.p.left.size + 1
		y = y.p
	return r
```

*OS-Rank*는 최악의 경우 잎새노드에서 시작해 루트노드까지 올라가며 랭크를 계산합니다. *OS-Rank* 역시 계산복잡성은 $O(\log{n})$이 됩니다.





## subtree 크기 업데이트

지금까지 설명해드린 *OS-Select*, *OS-Rank*를 무리없이 구현하려면 각 노드별로 서브트리 노드 수를 반영해 주어야 합니다. 트리를 *build*할 때는 물론 새 노드를 *insert*, 기존 노드를 *delete*할 때마다 서브트리의 노드 수가 바뀌게 됩니다. 

우선 *insert*를 기준으로 생각해보면 이진탐색트리의 노드 삽입은 잎새에서 이루어지고, 이 잎새에서 루트에 이르는 경로에만 subtree 숫자들이 바뀌기 때문에 최대 트리의 높이에 해당하는 노드들에 대해서만 노드 수 업데이트를 해주면 됩니다($O(\log{n})$). 물론 RB 트리와 같이 삽입 과정에서 *rotation*이 이뤄지는 경우도 상정해볼 수는 있겠지만 아래처럼 상수시간 내 연산이 가능하기 때문에 전체적인 계산복잡성을 지배하지 않습니다. 



<a href="https://imgur.com/TI2X87q"><img src="https://i.imgur.com/TI2X87q.png" width="600px" title="source: imgur.com" /></a>



한편 *delete*로 인한 subtree 크기 업데이트에 대한 계산복잡성도 $O(\log{n})$이라고 합니다.





## interval tree

*interval tree*란 각 노드의 값이 구간(interval)인 이진탐색트리인 자료구조를 가리킵니다. 여기에 (1) 해당 노드 구간의 상한 (2) 해당 노드 왼쪽 서브트리의 값 가운데 최대값 (3) 해당 노드 오른쪽 서브트리의 값 가운데 최대값 등 세 가지 가운데 최대값을 각 노드에 구간 정보와 별도로 저장해 놓습니다. 예컨대 다음 그림과 같습니다.



<a href="https://imgur.com/yeZtSXM"><img src="https://i.imgur.com/yeZtSXM.png" width="450px" title="source: imgur.com" /></a>



우리가 알고 싶은 값은 특정 구간이 주어졌을 때 위 *interval tree*에서 겹치는 구간이 있는지, 있다면 어느 구간이 겹치는지 정보입니다. 예컨대 위와 같은 트리에서 [14, 16]이 겹치는지 알아보고 싶다고 칩시다. 그 과정은 다음과 같습니다.

- 알고 싶은 구간의 하한 14와 루트노드의 왼쪽 자식노드(18)를 비교합니다. **작으므로** 루트노드의 **왼쪽 자식노드로** 갑니다. 
- 알고 싶은 구간의 하한 14와 루트노드의 왼쪽 자식노드의 왼쪽 자식노드(8)를 비교합니다. **크므로** 루트노드의 왼쪽 자식노드의 **오른쪽 자식노드로** 갑니다.
- 알고 싶은 구간의 하한 14와 루트노드의 왼쪽 자식노드의 오른쪽 자식노드의 왼쪽 자식노드(10)를 비교합니다. **크므로** 루트노드의 왼쪽 자식노드의 오른쪽 자식노드의 **오른쪽 자식노드로** 가야 합니다. 그런데 [15, 18] 이 노드는 자식노드를 가지지 않고, [14, 16]과 그 구간이 겹치므로 [15, 18]을 결과값으로 반환합니다.

*interval-search*의 의사코드는 다음과 같습니다.

```python
Interval-Search(T, i):
	x = T.root
	while x != T.nil and i does not overlap x.int:
		if x.left != T.nil and x.left.max >= i.low:
			x = x.left
		else:
			x = x.right
	return x
```

원하는 결과를 찾기 위해 최악의 경우 루트노드에서 잎새노드에 이르기까지 탐색하게 됩니다. *interval-search*의 계산복잡성 또한 $O(\log{n})$이 됩니다.