---
title: Random Forest, Rotation Forest
category: Machine Learning
tag: tree-based ensemble
---

이번 포스팅에서는 트리 기반의 대표적인 앙상블 기법인 **랜덤포레스트(Random Forest)**와 **로테이션포레스트(Rotation Forest)**에 대해 알아보고자 합니다. 관련 R패키지를 소개하고, 저희 연구실 김해동 석사과정이 만든 코드와 성능 실험도 함께 소개해보고자 합니다. 그럼 시작해보겠습니다.



## Tree-based Ensemble 소개

**의사결정나무(Decision Tree)**는 한번에 하나씩의 설명변수를 사용하여 예측 가능한 규칙들의 집합을 생성하는 알고리즘입니다. 한번 분기 때마다 변수 영역을 두개로 구분해 구분 뒤 각 영역의 순도(homogeneity)가 증가/불확실성(엔트로피)가 감소하도록 하는 방향으로 학습을 진행합니다. 의사결정나무는 입력 변수 영역을 두 개로 구분하는 **재귀적 분기(recursive partitioning)**와 너무 자세하게 구분된 영역을 통합하는 **가지치기(pruning)** 두 가지 과정으로 나뉩니다. 자세한 내용은 [이곳](https://ratsgo.github.io/machine%20learning/2017/03/26/tree/)을 참고하세요.

<a href="http://imgur.com/RUUXzP8"><img src="http://i.imgur.com/RUUXzP8.png" width="500px" title="source: imgur.com" /></a>

**랜덤포레스트**는 같은 데이터에 의사결정나무 여러 개를 동시에 적용해서 학습성능을 높이는 앙상블 기법입니다. 나무(tree)가 여럿 있다고 하는 의미에서 forest라는 이름이 붙었습니다. 참 직관적인 작명이죠. 위 그림을 보시면 조금 더 쉽게 이해하실 수 있으실 겁니다. 어쨌든 랜덤포레스트는 동일한 데이터로부터 복원추출을 통해 30개 이상의 데이터 셋을 만들어 각각에 의사결정나무를 적용한 뒤 학습 결과를 취합하는 방식으로 작동합니다. 단 여기서 각각의 나무들은 전체 변수 중 일부만 학습을 하게 됩니다. 개별 트리들이 데이터를 바라보는 관점을 다르게 해 다양성을 높이려는 시도입니다.

**로테이션포레스트**는 학습데이터에 **주성분분석(PCA)**를 적용해 데이터 축을 회전(rotation)한 후 학습한다는 점을 제외하고는 랜덤포레스트와 같습니다. PCA로 회전한 축(아래 그림의 경우 핑크색 선을 지나는 축)은 학습데이터의 분산을 최대한 보존하면서도 학습성능 향상에도 유의미할 것이라는 전제에서 고안된 방법론으로 풀이됩니다. 아래 움짤을 보시면 PCA의 효과를 눈으로도 확인하실 수 있습니다.

![PCA](http://i.imgur.com/Uv2dlsH.gif)

** 출처 : [[Making sense of principal component analysis, eigenvectors & eigenvalues]](http://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579#140579)





## 기법 구현

R에서 의사결정나무를 수행하는 패키지는 **rpart**입니다. 아래와 같이 동작합니다. 의사결정나무는 범주를 예측하는 **분류(classification)**는 물론 연속형 숫자를 맞추는 **회귀(regression)** 모두 적용 가능한 모델인데요. 분류를 하고 싶다면 아래처럼 type 변수로 'class'를, 회귀를 하고 싶으면 'anova'를 쓰면 됩니다. 물론 이렇게 명시적으로 적어주지 않아도 예측해야 하는 변수 Y의 자료형이 범주에 해당하는 **factor**일 경우 분류를, 연속형 숫자에 해당하는 **numeric**일 경우 회귀를 자동 수행합니다.
```R
# Decision Tree
library(rpart)
Fit1 <- rpart(fomula, data, type=“anova”) # regression
Fit2 <- rpart(fomula, data, type=“class”) # classification
```
랜덤포레스트와 관련된 패키지명은 말 그대로 **randomForest**입니다. rpart와 마찬가지로 Y의 자료형이 factor이면 분류, numeric이면 회귀를 자동 수행합니다. **mrty**는 앞서 설명드렸던 것처럼 변수의 부분집합을 만들 때 샘플링하는 변수 개수이며 **ntree**는 앙상블을 할 의사결정나무 개수가 됩니다.

```R
# Random Forest
library(randomForest)
Fit <- randomForest(fomula, data, ntree, mtry,…)
```
로테이션포레스트 관련 패키지명은 **rotationForest**입니다. 다른 패키지와 달리 명시적으로 입력변수(x)와 예측변수(y)를 나눠서 넣어주어야 하며 **2범주 분류**만 수행할 수 있습니다. PCA를 수행해야 하기 때문에 x의 자료형은 반드시 숫자여야 하며 y 역시 0 또는 1로 바꿔주어야 합니다. **K**와 **L**은 각각 randomForest 패키지의 mtry, ntree와 같습니다.
```R
# Rotation Forest
library(rotationForest)
Fit <- rotationForest(x, y, K, L)
```
마지막으로 설명드릴 코드는 저희 연구실에서 만든겁니다. rotationForest 기존 패키지를 다소 보완했습니다. 범주형 변수는 자동으로 숫자로 바꾸어 더미변수화를 해주고 다범주 분류는 물론 회귀도 역시 가능하도록 개선했습니다. **k**는 학습데이터를 몇 개로 나눌지 선택하는 변수이며, **bootstrapRate**는 학습데이터 부분집합을 만들 때 레코드를 얼마나 선택할지 지정하는 변수입니다. **numTrees**는 트리 개수, **type**은 분류/회귀를 선택하는 변수입니다. 이 코드는 이 포스트 맨 마지막에 첨부를 했는데요. 패키지 형태가 아니기 때문에 실제 실행을 위해선 R에서 사용자 정의 함수를 호출하듯 사용하시면 됩니다.

```R
# advanced Rotation Forest
Fit <- rotationForest(data, k, numTrees, bootstrapRate, type)
```



## 성능 비교 실험

### 2범주 분류 문제

[UCI datasets](https://archive.ics.uci.edu/ml/datasets.html) 등 수집 가능한 데이터셋을 수집해 30회 반복실험했습니다. 지금부터 보여드릴 표의 성능 지표는 **단순정확도(accuracy)**입니다.  표에서도 알 수 있듯 단일 의사결정나무보다 앙상블 기법인 포레스트가 나은 성능을 보여주고 있습니다. 앙상블 기법 중엔 랜덤포레스트가 로테이션포레스트보다 나은 성능을 나타냈습니다. (2범주 분류 문제에 사용한 로테이션포레스트 함수는 R패키지인 ratationForest입니다)

<a href="http://imgur.com/crkbOFS"><img src="http://i.imgur.com/crkbOFS.png" width="500px" title="source: imgur.com" /></a>



### 다범주 분류 문제

다범주 분류 문제에 있어서도 랜덤포레스트가 나은 성능을 보여주고 있습니다. 다범주 분류 말고 회귀 문제에 있어서도 랜덤포레스트가 로테이션포레스트보다 성능이 좋은 것으로 파악됐습니다. (여기서 사용된 로테이션포레스트 함수는 저희 연구실에서 작성한 코드입니다)

<a href="http://imgur.com/tkKXMWq"><img src="http://i.imgur.com/tkKXMWq.png" width="500px" title="source: imgur.com" /></a>



### randomForest 패키지의 파라메터 실험

앙상블 기법 가운데 그 성능이 강건하면서도 좋은 것으로 알려진 랜덤포레스트의 강점을 실험을 통해 확인할 수 있었습니다. 그럼 랜덤포레스트의 최적 하이퍼파라메터는 무엇일까요?

**ntree** (트리 개수)

<a href="http://imgur.com/5ccbeMp"><img src="http://i.imgur.com/5ccbeMp.png" width="400px" title="source: imgur.com" /></a>

분류 문제에서 트리 개수는 250개 이상부터 단순정확도 향상에 정체 현상이 나타났습니다(57개 데이터 30회 반복실험 평균 기준). 회귀 문제의 경우에도 트리 개수가 250개 이상부터 RMSE가 크게 줄지 않는 것으로 파악됐습니다. 패키지의 기본값인 500을 그대로 써도 무방할 것 같습니다. 



**mtry** (변수 개수)

<a href="http://imgur.com/aI0zbxt"><img src="http://i.imgur.com/aI0zbxt.png" width="400px" title="source: imgur.com" /></a>

개별 트리 학습용 부분집합을 만들 때 선택한 변수의 비율은 전체의 30%를 기점으로 클 수록 되레 분류 성능(단순정확도)이 떨어지는 것으로 나타났습니다(57개 데이터 30회 반복실험 평균 기준). 회귀 문제의 경우에도 변수 비율이 30%를 전후로 RMSE가 줄지 않는 경향을 보였습니다. **mtry**도 역시 패키지 기본값을 써도 크게 관계 없을 것 같습니다.



## 마치며

이상으로 트리 기반 머신러닝 기법들에 대해 살펴보았습니다. 실험 결과에서 보셨던 것처럼 단일 의사결정나무보다 여러 개 트리를 동시에 적용한 앙상블 기법들이 강세를 보였습니다. 랜덤포레스트는 로테이션포레스트와 비교해 그 성능이 강건하고 우수한 것으로 파악됐습니다. 로테이션포레스트의 R패키지인 rotationForest를 보완한 코드는 아래에 게시했습니다. 여기까지 읽어주셔서 감사합니다.



<script src="https://gist.github.com/ratsgo/e426e92e4a88dca8f8a3f59d41f891be.js"></script>