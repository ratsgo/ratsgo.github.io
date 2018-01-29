---
title: generative model 응용 사례
category: generative model
tag: [Enhancenet, SimGAN, Pix2Pix, CycleGAN, StarGAN, TripleGAN]
---

이번 글에서는 *Generative model*, 특히 Generative Adversarial Network(GAN)의 다양한 응용 연구들에 대해 살펴보도록 하겠습니다. 이 글은 전인수 서울대 박사과정이 2017년 12월에 진행한 패스트캠퍼스 강의와 위키피디아 등을 정리했음을 먼저 밝힙니다. PyTorch 코드는 [이곳](https://github.com/InsuJeon/Hello-Generative-Model)을 참고하였습니다. GAN과 관련해서는 [이곳](https://ratsgo.github.io/generative%20model/2017/12/20/gan/)을 참고하시면 좋을 것 같습니다. 그럼 시작하겠습니다.





## EnhanceNet

EnhanceNet은 GAN의 손실함수를 적용해 *Super Resolution* 기법의 성능을 높였습니다. *Super Resolution*(SR)이란 아래 그림처럼 저해상도의 이미지/영상을 고해상도로 변환하는 작업을 가리킵니다.



<a href="https://imgur.com/VxuNxlQ"><img src="https://i.imgur.com/VxuNxlQ.png" width="400px" title="source: imgur.com" /></a>



EnhanceNet이 SR 문제에 GAN 구조를 적용한 아이디어는 이렇습니다. 생성자 $G$의 인풋으로 노이즈 대신 저해상도의 이미지를 입력합니다. 판별자 $D$는 $G$가 생성한 가짜 고해상도 이미지와 실제 고해상도 이미지를 구분하는 역할을 합니다. $G$는 $D$를 속이도록 고해상도 이미지를 생성하도록 학습됩니다. 이처럼 EnhanceNet은 어떤 task이든 GAN 손실함수를 사용하여 원하는 결과를 얻어낼 수 있다는 점에서 눈길을 끕니다.

GAN 손실함수의 효과를 직관적으로 나타낸 그림은 아래와 같습니다. 원본 고해상도 이미지 $I_{HR}$에서 인위적으로 해상도를 낮춘 이미지 $I_{LR}$이 있다고 칩시다. $I_{LR}$을 인풋, $I_{HR}$을 정답으로 놓고 학습시킬 때 평균제곱오차(Mean Squared Error)를 손실함수로 많이들 씁니다. MSE는 아래 그림처럼 입력값과 정답을 평균(average)하려는 성향이 강하다(MSE와 관련해서는 [이곳](https://ratsgo.github.io/linear%20algebra/2017/10/20/projection/) 참고)는 점이 단점입니다. 그런데 GAN 손실함수(adversarial loss)를 썼더니 $I_{HR}$을 제법 잘 근사하는 걸 확인했다고 합니다.



<a href="https://imgur.com/95muNZL"><img src="https://i.imgur.com/95muNZL.png" width="300px" title="source: imgur.com" /></a>





## SimGAN

SimGAN의 목적은 현실감 있는 인공데이터를 만들어내는 데 있습니다. 이 때 GAN을 씁니다. 아이디어는 이렇습니다. 기존 GAN의 생성자 역할을 하는 Refiner $R$은 인공데이터를 받아서 실제 데이터로 변환하는 역할을 합니다. 판별자 $D$는 $R$이 생성한 가짜(refined) 데이터와 실제(real) 데이터를 구분하는 역할을 합니다. $R$이 $D$를 속이려고 하는 과정에서 $R$이 학습됩니다. 이 과정을 도식적으로 나타내면 다음 그림과 같습니다.



<a href="https://imgur.com/1EiwI8F"><img src="https://i.imgur.com/1EiwI8F.png" width="500px" title="source: imgur.com" /></a>



SimGAN에서는 다른 연구에 참고가 될 만한 몇 가지 기술들이 포함돼 있습니다. 우선 Self-Regularization입니다.  $R$을 학습시킬 때 기존 GAN 손실함수만 사용할 경우, $R$이 그저 $D$를 속이는 데만 집중하게 되면서 $R$이 생성한 데이터가 실제 데이터와 완전히 동떨어지게 될 염려가 크기 때문입니다. $R$의 입력값인 인공데이터도 조악하나마 실제 데이터의 특징을 담고 있으므로 $R$의 손실함수에 다음과 같은 regularization 항을 추가했습니다.


$$
{ L }_{ reg }={ \left\| \psi \left( R\left( x \right)  \right) -\psi \left( x \right)  \right\|  }_{ 1 }
$$


위와 같은 항을 손실함수에 추가하게 되면 $R$에 입력되는 인공데이터 $x$와 $R$이 산출한 데이터 $R(x)$ 사이의 오차가 줄어들게 됩니다. 결과적으로 $R$이 생성하는 데이터가 입력데이터에서 너무 벗어나지 않게 되는 셈이죠. 단 여기에서 $ψ$는 입력값의 *feature*를 뽑는 함수인데요. 논문에서는 *identity mapping*을 사용했다고 합니다.

또 한가지 기법은 Local patch-Discriminator입니다. 기존 GAN에서 $D$는 입력데이터 전체를 보고 real/fake 여부를 판별합니다. 이 때문에 $G$는 대개 $D$를 속이기 위해 데이터의 일부 특징을 과장하려는 경향이 있습니다. 이 문제를 완화하기 위해 다음 그림과 같이 $D$가 데이터의 일부 영역만 보도록 하고, 전체적인 판단은 이들 패치의 평균이라든지 가중합이라든지 하는 방식으로 취하도록 했습니다. 그 결과 $D$의 능력을 어느 정도 제한하면서 $R$의 성능을 높일 수 있었다고 합니다. 





<a href="https://imgur.com/s7LygPQ"><img src="https://i.imgur.com/s7LygPQ.png" width="400px" title="source: imgur.com" /></a>



마지막으로 언급할 부분은 History Buffer입니다. 기존 GAN에선 $D$를 학습시키는 과정에서 최근 학습샘플에만 적합하는 문제가 있었습니다. 이를 *continual learning issue* 내지 *catastrophic forgetting problem*이라고도 합니다. 이 문제를 해결하기 위해 도입된 것이 바로 History Buffer입니다. buffer에 예전 학습 데이터를 모아뒀다가 최신 데이터와 함께 학습시키자는 아이디어입니다. 결과적으로 $D$로 하여금 $R$이 예전에 생성한 데이터를 지속적으로 기억할 수 있게 도와줍니다. SimGAN에서는 아래와 같이 적용됐습니다. 



<a href="https://imgur.com/uTXIhEh"><img src="https://i.imgur.com/uTXIhEh.png" width="400px" title="source: imgur.com" /></a>

- 학습 도중 $R$이 생성한 데이터가 가운데 랜덤하게 반을 선택하여 buffer에 넣는다.
- 각 step에서 buffer에서 랜덤하게 선택한 반과 $R$이 현재 생성한 데이터 반을 $D$에 전달한다.





## Pix2Pix

Pix2Pix는 다음과 같이 *image to image translation*을 하는 데 GAN을 접목한 연구입니다.



<a href="https://imgur.com/iH3KG4T"><img src="https://i.imgur.com/iH3KG4T.png" width="600px" title="source: imgur.com" /></a>



아키텍처는 다음과 같습니다. 우선 $G$는 소스 도메인의 데이터를 입력 받아 타겟 도메인의 데이터를 생성합니다. $G$는 소스 도메인의 데이터와 생성된 타겟 도메인의 데이터를 쌍으로 묶어 $D$에 전달합니다. $D$는 $G$가 생성한 가짜 데이터 pair와 실제 데이터 pair를 구분합니다. $G$는 $D$를 속이도록 하는 과정에서 데이터를 더 잘 생성하게 됩니다.



<a href="https://imgur.com/jigPX5b"><img src="https://i.imgur.com/jigPX5b.png" width="450px" title="source: imgur.com" /></a>



$G$는 다음과 같이 오토인코더(autoencoder)에 *Unet*을 결합한 아키텍처를 썼다고 합니다. *encoder*, *decoder* 사이에 발생할 수 있는 정보손실을 *skip-connection*을 이용해 완화한 겁니다. Pix2Pix 역시 SimGAN의 Local Patch Disciriminator를 사용했다고 합니다.



<a href="https://imgur.com/FSGh3or"><img src="https://i.imgur.com/FSGh3or.png" width="300px" title="source: imgur.com" /></a>





## CycleGAN

Pix2Pix의 단점은 학습데이터가 항상 pair로 존재해야 한다는 겁니다. CycleGAN은 이러한 문제를 해결하기 위해 제안됐습니다. 이를 도식적으로 나타낸 그림은 다음과 같습니다.

<a href="https://imgur.com/cgynmJJ"><img src="https://i.imgur.com/cgynmJJ.png" width="400px" title="source: imgur.com" /></a>



CycleGAN의 기본 프레임워크는 다음과 같습니다. 두 개의 생성자 $G$, $F$와 두 개의 판별자 $D_X$, $D_Y$를 씁니다. $G$는 $X$ 도메인의 데이터를 $Y$ 도메인으로 변환하는 역할을 합니다. $F$는 $Y$ 도메인의 데이터를 $X$ 도메인으로 변환합니다. $D_X$는 $F$가 생성한 가짜 데이터와 $X$ 도메인의 실제 데이터를 구분합니다. $D_Y$는 $G$가 생성한 가짜 데이터와 $Y$ 도메인의 실제 데이터를 구분합니다. $G$와 $F$는 반대 도메인의 구분자를 속이도록 적대적으로 학습됩니다. 이렇게 학습이 진행되면서 굳이 데이터가 pair 형태로 존재하지 않아도 됩니다.



<a href="https://imgur.com/ZWjYGVU"><img src="https://i.imgur.com/ZWjYGVU.png" width="200px" title="source: imgur.com" /></a>



CycleGAN에는 기존 GAN loss 이외에 *cycle-consitency loss*라는 것이 추가됐습니다. 아래 그림처럼 도메인을 변경했다가 다시 돌아왔을 때 모습이 원래 입력값과 비슷한 형태가 되도록 regularization을 걸어주는 것입니다. 이렇게 되면 도메인을 넘나들 때 더욱 현실감 있는 데이터가 생성될 것입니다. 



<a href="https://imgur.com/ZhUHD2i"><img src="https://i.imgur.com/ZhUHD2i.png" width="500px" title="source: imgur.com" /></a>



CycleGAN을 PyTorch로 구현한 코드를 살펴보겠습니다. 우선 두 개의 $G$와 두 개의 $D$를 정의합니다. (일반적인 *generator*, *discriminator* 사용)

```python
# Generator arguments : input_dim, num_filter, output_dim, num_resnet
G_A = Generator(3, params.ngf, 3, params.num_resnet) 
G_B = Generator(3, params.ngf, 3, params.num_resnet)
# Discriminator arguments : input_dim, num_filter, output_dim
D_A = Discriminator(3, params.ndf, 1) 
D_B = Discriminator(3, params.ndf, 1) 
```

$G$의 loss를 구하는 코드는 다음과 같습니다.

```python
# A -> B
fake_B = G_A(real_A)
D_B_fake_decision = D_B(fake_B)
G_A_loss = MSE_loss(D_B_fake_decision, Variable(torch.ones(D_B_fake_decision.size())))

# forward cycle loss
recon_A = G_B(fake_B)
cycle_A_loss = L1_loss(recon_A, real_A) * params.lambdaA

# B -> A
fake_A = G_B(real_B)
D_A_fake_decision = D_A(fake_A)
G_B_loss = MSE_loss(D_A_fake_decision, Variable(torch.ones(D_A_fake_decision.size())))

# backward cycle loss
recon_B = G_A(fake_A)
cycle_B_loss = L1_loss(recon_B, real_B) * params.lambdaB

# Back propagation
G_loss = G_A_loss + G_B_loss + cycle_A_loss + cycle_B_loss
```

$D$의 loss를 구하는 코드는 다음과 같습니다.

```python
# Train discriminator D_A
D_A_real_decision = D_A(real_A)
D_A_real_loss = MSE_loss(D_A_real_decision, Variable(torch.ones(D_A_real_decision.size())))
fake_A = fake_A_pool.query(fake_A)
D_A_fake_decision = D_A(fake_A)
D_A_fake_loss = MSE_loss(D_A_fake_decision, Variable(torch.zeros(D_A_fake_decision.size())))
D_A_loss = (D_A_real_loss + D_A_fake_loss) * 0.5

# Train discriminator D_B
D_B_real_decision = D_B(real_B)
D_B_real_loss = MSE_loss(D_B_real_decision, Variable(torch.ones(D_B_real_decision.size())))
fake_B = fake_B_pool.query(fake_B)
D_B_fake_decision = D_B(fake_B)
D_B_fake_loss = MSE_loss(D_B_fake_decision, Variable(torch.zeros(D_B_fake_decision.size())))
D_B_loss = (D_B_real_loss + D_B_fake_loss) * 0.5
```





## StarGAN

StarGAN은 CycleGAN의 단점을 보완한 연구입니다. CycleGAN은 도메인 수가 늘어나게 되면 필요한 $G$의 수가 기하급수적으로 증가하고, $D$는 선형적으로 증가합니다. 아래 그림의 (a)의 경우 도메인 수가 4개가 되자, $G$는 12개, $D$는 4개가 필요한 것을 확인할 수 있습니다. 반면 StarGAN은 (b)와 같이 생겼습니다. $D$와 $G$는 각각 하나만 있으면 됩니다.



<a href="https://imgur.com/vuvKH72"><img src="https://i.imgur.com/vuvKH72.png" width="400px" title="source: imgur.com" /></a>



StarGAN의 학습 방식을 저자가 든 예시 기준으로 설명해 보겠습니다. *CelebA* 데이터셋과 *RaFD* 데이터 셋이 있고 각각의 레이블은 아래 그림과 같이 주황색, 녹색 박스라고 칩시다. *Mask Vector*는 모델이 현재 다루는 데이터가 *CelebA*에 속하는지, *RaFD*에 속하는지 나타내는 one-hot-vector입니다. 

우선 (b)의 $G$에 입력되는 데이터를 보겠습니다. 이 데이터는 검은색 머리의 젊은 여성인데요, 타겟 도메인을 검은색 머리의 젊은 남자로 설정하였습니다. $G$의 입력데이터는 소스 도메인의 원래 이미지, 레이블 벡터, *Mask Vector* 셋을 합친 형태입니다. 어쨌든 $G$는 이 데이터를 검은색 머리의 젊은 남자로 변환해야 합니다. 이 데이터를 (d)의 $D$에 보내서 $D$가 실제 데이터로 구분하도록, 그리고 검은색 머리의 젊은 남자($[1,0,0,1,1]$)로 분류하도록 속여야 하니까요. $G$는 $D$를 잘 속일 수 있도록 학습됩니다.



<a href="https://imgur.com/O1VrGT1"><img src="https://i.imgur.com/O1VrGT1.png" width="600px" title="source: imgur.com" /></a>



(b)의 $G$가 생성한 데이터는 다시 $G$에 보내집니다. 이번에 $G$에 입력되는 데이터는 방금 전 $G$가 생성한 타겟 도메인의 이미지, 원 데이터의 레이블 벡터(검은색 머리의 젊은 여성, $[0,0,1,0,1]$), *Mask Vector* 셋을 합친 형태입니다. $G$는 이렇게 만든 데이터가 원래 이미지와 유사하도록 학습됩니다. 이는 CycleGAN의 *cycle-consitency loss*를 그대로 차용했습니다. 결과적으로 $G$는 하나의 이미지 데이터로 $D$를 속이는 과정에서, *cycle-consitency loss*를 줄이는 과정에서 두 번 학습되는 셈이죠. StarGAN의 목적함수는 다음과 같습니다.

<a href="https://imgur.com/EwPxI06"><img src="https://i.imgur.com/EwPxI06.png" width="600px" title="source: imgur.com" /></a>



## Anormaly detection with GAN

GAN을 이상치 탐지, 즉 *Novelty Detection*에 활용한 연구도 있습니다. GAN은 $G$가 노이즈 $z$를 받아 현실감 있는 데이터를 생성하도록 학습되는데요. $G$가 생성한 데이터를 역추적해 latent space를 분석하면 이 latent space 내에서 특정 영역이 이상치에 해당할 것이라는 전제가 깔려 있습니다. 이를 도식적으로 나타낸 그림은 다음과 같습니다.



<a href="https://imgur.com/zl0xWyh"><img src="https://i.imgur.com/zl0xWyh.png" width="250px" title="source: imgur.com" /></a>





## TripleGAN

TripleGAN은 GAN으로 새롭게 생성한 데이터를 활용해 성능이 좋은 분류기(classifier)를 만들어내는 게 목표입니다. 아키텍처와 목적함수를 도식화한 그림은 다음과 같습니다.

<a href="https://imgur.com/D7lm8MW"><img src="https://i.imgur.com/D7lm8MW.png" title="source: imgur.com" /></a>

차근차근 살펴보겠습니다. 우선 생성자 $G$는 노이즈 $z$를 받아서 인공데이터 $x$를 산출하고 $y$는 실제 데이터로부터 샘플링합니다. $G$가 만든 데이터는 판별자 $D$와 분류기 $C$로 보내집니다. $D$는 이 데이터가 진짜인지 가짜인지 구분하며, $C$는 $G$가 만든 $x$를 입력으로 하고 역시 $G$가 만든 $y$를 출력으로 하는 classification task를 수행합니다.

레이블이 있는 실제 데이터($x_l, y_l$)는 분류기 $C$를 학습하는 데 사용됩니다(supervised learning). 이 데이터는 $D$에도 들어가 $D$가 진짜인지 가짜인지 구분하도록 학습됩니다. 마지막으로 레이블이 없는 실제 데이터($x_c$)가 분류기 $C$에 입력되면 $C$는 이 데이터의 레이블을 예측합니다. $C$가 잘 학습되어 있다면 $x_c$ 역시 레이블이 있는 데이터처럼 역할을 하게 되겠지요. 어쨌든 이렇게 레이블이 추가된 $x_c$ 역시 $D$에 입력돼 진짜/가짜 여부를 판별합니다.

TripleGAN에서는 $G$가 $D$를 속이는 과정에서 생성한 데이터가 $C$ 학습에 활용돼 $C$의 성능을 높일 수 있습니다. 뿐만 아니라 $C$는 레이블이 없는 데이터 $x_c$의 레이블을 예측할 때 $D$가 가짜라고 구분하지 않도록 그럴듯한 레이블을 달도록 학습이 진행됩니다. 결과적으로 TripleGAN의 학습이 잘 되면 기존 데이터만 가지고 학습한 것보다 성능이 좋은 분류기 $C$가 도출되리라고 기대할 수 있습니다.