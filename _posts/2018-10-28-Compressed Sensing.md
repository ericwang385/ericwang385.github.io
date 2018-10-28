---
layout:     post
title:      "简单压缩感知"
subtitle:   ""
date:       2018-10-28 15:07:00
author:     "Psyduck"
header-img: "img/2017-7-23/header.jpg"
catalog: true
tags:
    - Signal processing
    - Compressed Sensing
typora-root-url: ../
---

> 其实也是因为自己手头一篇论文有想用到图像压缩的方法，在频域上来提取图像信息，而非无脑nn，所以才顺藤摸瓜找到的Compressed Sensing 相比起纯靠参数无脑堆砌的AutoEncoder CS这样的方法无疑就优美很多了。 最后会提一下2017 ICML的一个work，“Compressed Sensing using generative model”

与其说CS是一种压缩技术其实更不如说它是一种新的采样方法，抛弃了传统等距采样的思想，利用给欠定方程组加上稀疏(Sparsity)的约束来获得唯一解。

## Nyquist–Shannon sampling theorem

香农奈奎斯特采样定理并不是什么很深奥的东西了，稍微有一点信号分析基础的同学应该都了解的。

![image-20181028152450327](/img/2018-10-28-Compressed Sensing/image-20181028152450327.png)

他所描述的其实就是如下图这样的一个对于连续信号的等距采样过程中所需要添加的约束。

当我们时域以τ为间隔进行采样，频域会以1/τ为周期发生周期延拓。由此为了不让采样后的信号发生混叠我们需要采样频率大于最大信号频率的两倍。这个定理很大程度上限制了我们得到更小的采样率。一个很自然的想法，我们可以使用不等间距采样来绕过香农奈奎斯特采样定理。

## Compressed Sensing

![image-20181028153244471](/img/2018-10-28-Compressed Sensing/image-20181028153244471.png)

上图是压缩感知的概览。其中

|     记号     |     名称     | 大小 |
| :----------: | :----------: | :--: |
|      Φ       |   观测矩阵   | M×N  |
|      Ψ       |   稀疏矩阵   | N×N  |
| Θ(后文记作H) |   传感矩阵   | M×N  |
|      S       |   输入信号   | N*1  |
|    Y=Θ*S     | 压缩后的信号 | M*1  |

我们先做出假设，信号S在某个空间中是K-sparse的，这个也是压缩感知的前提。这样，在S经过稀疏矩阵Ψ变换后再乘上Φ就可以得到压缩后的信号。一般稀疏矩阵我们会使用DCT或者wavelet transform这样的方法，观测矩阵在陶哲轩的证明下，我们可以直接用随机高斯矩阵就可以了。

### 工作原理

![image-20181028154802893](/img/2018-10-28-Compressed Sensing/image-20181028154802893.png)

如果$m\ge n$

​	那么我们可以使用最小二乘法通过Y解得S

![image-20181028155918145](/img/2018-10-28-Compressed Sensing/image-20181028155918145.png)

如果$n> m$

​	我们称这个方程组为欠定线性系统，一般而言有无数个解，因此我们无法使用最小平方法去求得要重建的讯号。但是，如果这个欠定线性系统只有唯一一个稀疏解，那么我们可以利用压缩感知理论和方法来寻找这个解。值得注意的是，并不是所有欠定线性方程组都具有稀疏解。

​	$ 2=s_{1}+s_{2}$就是一个典型的欠定线性系统，我们可以有无限多个解，但如果我们要求S是稀疏的，我们就可以很轻易地得到这个欠定线性系统的解为$(2,0)$或是$(0,2)$

### 稀疏性

我们定义一个向量的稀疏性，也就是$l_0$范数如下图

![image-20181028160131949](/img/2018-10-28-Compressed Sensing/image-20181028160131949.png)

其中，我们优化的结果如下

![image-20181028160157764](/img/2018-10-28-Compressed Sensing/image-20181028160157764.png)

但由于对于$l_0$范数的优化实际上是一个全域上的搜索问题，NP-Hard 所以我们将其转化为对于$l_1$范数的优化

![image-20181028160304973](/img/2018-10-28-Compressed Sensing/image-20181028160304973.png)

这个$l_0$范数与$l_1$范的等价陶哲轩等人在论文中给出了很好的证明。

### RIP 有限等距性

![image-20181028161454068](/img/2018-10-28-Compressed Sensing/image-20181028161454068.png)

​                                                                            ![image-20181028161503625](/img/2018-10-28-Compressed Sensing/image-20181028161503625.png)                     ![image-20181028161509452](/img/2018-10-28-Compressed Sensing/image-20181028161509452.png)

RIP就是对于观测矩阵H的一个约束，数学上表述成上式的形式。

RIP其实保证的是原空间到稀疏空间的一一映射关系，在δ < 1的时候我们认为HS是有唯一的$l_0$最优解的，当δ < √2 − 1时，我们可以将$l_0$与$l_1$的优化等价。

![image-20181028162051435](/img/2018-10-28-Compressed Sensing/image-20181028162051435.png)

矩阵满足2K阶RIP保证了能够把任意一个K稀疏信号θK映射为唯一的y，

也就是说要想通过压缩观测y恢复K稀疏信号θK，必须保证传感矩阵满足2K阶RIP，满足2K阶RIP的矩阵任意2K列线性无关。

## Compressed Sensing using Generative Model

Compressed Sensing 中

Y = Θ*x     Θ ∊R^(M×N)		其中 M = O(klog⁡(n))

CSGM中提出，可以使用一个生成模型来复建图像，此时

M = O(kdlog(n)) 		其中d为生成模型的层数

### S-REC

这条性质其实是本文中对于REC条件的一个扩展，将REC限制在生成模型所映射到的空间S中

![image-20181028172444596](/img/2018-10-28-Compressed Sensing/image-20181028172444596.png)

### 几个引理

我们假设对于一个RELU-based 的生成模型第一层的输出是一个$n^k$ k-维的超平面

那么我们网络最后的输出可以理解为一个$n^{dk}$的k-维的超平面

由此可得我们的最终结论

![image-20181028181058049](/img/2018-10-28-Compressed Sensing/image-20181028181058049.png)



## Reference

> 1) Candes E. Therestricted isometry property and its implications for compressed sensing[J].Comptes Rendus Mathematique, 2008,346(8-9): 589-592.
>
> 2) Candes E, Tao T.Decoding by linear programming. IEEE Transactions on Information Theory,2005,59(8):4203-4215.
>
> 3）Bora A, Jalal A, Price E, et al. Compressed sensing using generative models[J]. arXiv preprint arXiv:1703.03208, 2017.
>
>



