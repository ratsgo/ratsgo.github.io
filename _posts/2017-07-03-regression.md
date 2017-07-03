---
title: 선형회귀 파라메터 추정
category: Machine Learning
tag: regression
---

이번 글에서는 선형회귀 모델의 계수를 추정하는 방법을 살펴보도록 하겠습니다. 이번 글은 고려대 김성범 교수님 강의와 '밑바닥부터 시작하는 데이터과학(조엘 그루스 지음, 인사이트 펴냄)'을 정리하였음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## 선형회귀

**선형회귀(Multiple Linear Regression)**는 수치형 설명변수 X와 연속형 숫자로 이뤄진 종속변수 Y간의 관계를 선형으로 가정하고 이를 가장 잘 표현할 수 있는 회귀계수를 데이터로부터 추정하는 모델입니다. 다음 그림처럼 집 크기와 가격의 관계를 나타내는 직선을 찾는 것이 선형회귀의 목표입니다.

<a href="http://imgur.com/lCKBBDV"><img src="http://i.imgur.com/lCKBBDV.png" width="350px" title="source: imgur.com" /></a>



독립변수들로 이뤄진 행렬 $X$와 종속변수 벡터 $Y$가 주어졌을 때 선형회귀 모델은 다음과 같이 정의됩니다.


$$
\begin{bmatrix} { y }_{ 1 } \\ { y }_{ 2 } \\ ... \\ { y }_{ n } \end{bmatrix}=\begin{bmatrix} 1 & x_{ 11 } & ... & { x }_{ 1k } \\ 1 & { x }_{ 21 } & ... & { x }_{ 2k } \\ ... & ... &  & ... \\ 1 & { x }_{ n1 } & ... & { x }_{ nk } \end{bmatrix}\begin{bmatrix} { \beta  }_{ 1 } \\ { \beta  }_{ 2 } \\ ... \\ { \beta  }_{ k } \end{bmatrix}+\begin{bmatrix} { \varepsilon  }_{ 1 } \\ { \varepsilon  }_{ 2 } \\ ... \\ { \varepsilon  }_{ n } \end{bmatrix}\\ \\ \overrightarrow { y } =X\overrightarrow { \beta  } +\overrightarrow { \varepsilon  } ,\quad \overrightarrow { \varepsilon  } \sim N(E(\overrightarrow { \varepsilon  } ),V(\overrightarrow { \varepsilon  } ))\\ \\ E(\overrightarrow { \varepsilon  } )=\begin{bmatrix} 0 \\ 0 \\ ... \\ 0 \end{bmatrix},\quad V(\overrightarrow { \varepsilon  } )={ \sigma  }^{ 2 }I
$$



## Direct Solution

선형회귀의 계수들은 실제값과 모델 예측값의 차이, 즉 **오차제곱합(error sum of squares)**을 최소로 하는 값들입니다. 이를 만족하는 최적의 계수들은 회귀계수에 대해 미분한 식을 0으로 놓고 풀면 아래와 같이 **명시적인 해**를 구할 수 있습니다. 다시 말해 우리에게 주어진 $X$, $Y$ 데이터만 가지고 계수를 단번에 추정할 수 있다는 이야기입니다.


$$
\overrightarrow { \beta  } ={ \left( { X }^{ T }X \right)  }^{ -1 }{ X }^{ T }\overrightarrow { y }
$$





## 분석 대상 데이터

분석 대상 데이터는 '밑바닥부터 시작하는 데이터 과학'에서 제시된 예시데이터입니다. 사용자의 친구 수가 $X$, 사용자가 사이트에서 보내는 시간이 $Y$에 해당합니다. 

<a href="http://imgur.com/ZhMINpC"><img src="http://i.imgur.com/ZhMINpC.png" width="400px" title="source: imgur.com" /></a>

```python
num_friends_good = [49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
daily_minutes_good = [68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]
```

$i$번째 데이터 포인트에 대한 회귀식은 다음과 같습니다. 우리는 여기에서 회귀계수 $α$와 $β$를 추정해야 합니다.


$$
{ y }_{ i }=\beta { x }_{ i }+\alpha
$$


위의 방식대로 데이터로부터 명시적인 해를 구한 결과 $α$와 $β$는 각각 22.9476, 0.9039로 추정되었습니다.





## Numerical Search

경사하강법 같은 반복적인 방식으로 선형회귀 계수를 구할 수도 있습니다. 경사하강법이란 어떤 함수값을 최소화하기 위해 임의의 시작점을 잡은 후 해당 지점에서의 그래디언트(경사)를 구하고, 그래디언트의 반대 방향으로 조금씩 이동하는 과정을 여러번 반복하는 것입니다. 예컨대 아래 그림([출처](http://neuralnetworksanddeeplearning.com/chap1.html))과 같습니다.

<a href="http://imgur.com/hs1AlFR"><img src="http://i.imgur.com/hs1AlFR.png" width="400px" title="source: imgur.com" /></a>

이 글에서는 경사하강법 가운데 **Stochastic Gradient Descent(SGD)** 기법을 쓰겠습니다. SGD는 반복문을 돌 때마다 **개별 데이터 포인트에 대한 그래디언트를 계산**하고 이 그래디언트의 반대 방향으로 파라메터를 업데이트해 함수의 최소값을 구하는 기법입니다.

SGD 관련 메인 코드는 다음과 같습니다. 코드에서 'value'는 우리가 최소화하고 싶은 값으로 선형회귀 모델에서는 오차제곱합을 가리킵니다. 'target_fn'은 목적함수로 오차제곱합을 아웃풋으로 산출하는 함수를 의미합니다. 'theta'는 해당 목적함수의 파라메터인데요, 우리 문제에선 $α$와 $β$를 말합니다. 'gradient_fn'은 각 파라메터에 대한 목적함수의 그래디언트를 가리킵니다.

```python
def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    # SGD 방식으로 gradient descent
    # minimize_batch보다 훨씬 빠르다

    data = zip(x, y)
    # theta_0를 초기 theta로
    theta = theta_0
    # alpha_0를 초기 이동거리(step_size)로
    alpha = alpha_0
    # 시작할 때의 최소값
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0

    # 만약 100번 넘게 반복하는 동안 value가 더 작아지지 않으면 멈춤
    while iterations_with_no_improvement < 100:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )

        # 새로운 최솟값을 찾았다면
        if value < min_value:
            # 이 값을 저장
            min_theta, min_value = theta, value
            # 100번 카운트도 초기화
            iterations_with_no_improvement = 0
            # 기본 이동거리로 돌아감
            alpha = alpha_0

        # 만약 최솟값이 줄어들지 않는다면
        else:
            # 이동거리 축소
            alpha *= 0.9
            # 100번 카운트에 1을 더함
            iterations_with_no_improvement += 1
		
        # 반복문이 돌 때마다 in_random_order를 호출하기 때문에
        # 매 iter마다 그래디언트를 계산하는 순서가 달라짐
        for x_i, y_i in in_random_order(data):
            # 각 데이터 포인트에 대해 그래디언트를 계산
            gradient_i = gradient_fn(x_i, y_i, theta)
            # 기존 theta에서, 학습률(alpha)과 그래디언트를 뺀 것을 업데이트
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta
```

그러면 이제는 value와 target_fn, gradient_fn, theta를 정의해야 합니다. 우선 우리가 구해야 하는 파라메터는 $α, β$ 두 개뿐이므로 theta는 2차원 벡터로 선언했습니다.

```python
import random
random.seed(1)
theta = [random.random(), random.random()] # alpha, beta
```

우리가 최소화하고자 하는 값(value)은 오차제곱합입니다. $i$번째 데이터 포인트에 대한 오차제곱(Squared Error)은 다음과 같은 식으로 나타낼 수 있습니다. 


$$
{SE}_{i}={ \left\{ { y }_{ i }-\left( \beta { x }_{ i }+\alpha  \right)  \right\}  }^{ 2 }
$$
이를 'squared_error' 함수로 표현할 수 있습니다.

```python
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2

def error(alpha, beta, x_i, y_i):
    # 실제값 y_i와 예측값 사이의 편차
    return y_i - predict(alpha, beta, x_i)
    
def predict(alpha, beta, x_i):
    # 현재 회귀계수들을 가지고 예측
    return beta * x_i + alpha
```

gradient_fn은 다음과 같습니다. 목적함수인 'squared_error'를 'theta'로 미분한 값입니다. 이를 식으로 정리하면 다음과 같습니다.


$$
\frac { \partial { SE }_{ i } }{ \partial \alpha  } =-2\left\{ { y }_{ i }-\left( \beta { x }_{ i }+\alpha  \right)  \right\} \\ \frac { \partial { SE }_{ i } }{ \partial \beta  } =-2\left\{ { y }_{ i }-\left( \beta { x }_{ i }+\alpha  \right)  \right\} { x }_{ i }
$$
이를 코드로 나타내면 다음과 같습니다.

```python
def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    # alpha에 대한 편미분, beta에 대한 편미분 반환
    return [-2 * error(alpha, beta, x_i, y_i),
            -2 * error(alpha, beta, x_i, y_i) * x_i]
```

이밖에 'minimize_stochastic' 구동에 필요한 함수도 정의하겠습니다.

```python
def in_random_order(data):
    # Stochastic Gradient Descent 수행을 위한 함수로,
    # 한번 반복문을 돌 때마다 임의의 순서로 데이터 포인트를 반환
    # 데이터 포인트의 인덱스를 list로 생성
    indexes = [i for i, _ in enumerate(data)]
    # 이 인덱스를 랜덤하게 섞는다
    random.shuffle(indexes)
    # 이 순서대로 데이터를 반환한다
    for i in indexes:
        yield data[i]

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]
```

마지막으로 코드 전체를 구동하는 명령문은 다음과 같습니다.

```python
alpha, beta = minimize_stochastic(target_fn=squared_error,
                                  gradient_fn=squared_error_gradient,
                                  x=num_friends_good,
                                  y=daily_minutes_good,
                                  theta_0=theta,
                                  alpha_0=0.0001)
```

SGD 기법으로 해를 구한 결과 명시적인 해를 구한 결과 $α$와 $β$는 각각 22.94799, 0.903982로 추정되었습니다. 이는 명시적인 해와 거의 근사합니다.