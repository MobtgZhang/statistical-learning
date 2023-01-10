# AdaBoost 算法
## 算法基本概述
+ AdaBoost 指的是Adaptive Boosting,由Yoav Freund和Robert Schapire 在1995年提出。
+ 这种算法的自适应指的是在于前一个基本分类器分类错误的样本权重会得到加强，加强之后的全体样本再次被用来训练下一个基本分类器。同时，在每一轮训练当中加入一个新的弱分类器，直到达到某个预定的足够小的错误率或者达到预先指定的最大迭代次数的时候停止训练。
+ AdaBoost算法是一种集成学习的算法，其中核心思想就是对多个机器学习模型进行组合形成一个精度更高的模型，参与组合的模型成为弱学习器。
## 算法原理
下面叙述Adaboost算法的基本原理。假设给定一个二类分类的训练数据集

$$T=\left\\{(x_{1},y_{1}),(x_{2},y_{2}),\dots,(x_{N},y_{N})\right\\}$$

其中每个样本点是由实例与标记组成。实例 $x_{i}\in\mathcal{X}\subseteq{{R}^{n}}$ ，其中标记 $y_{i}\in\mathcal{Y}=\left\\{+1,-1\right\\}$ ， $\mathcal{X}$ 是实例空间， $\mathcal{Y}$ 是标记集合。AdaBoost利用以下算法，从训练数据中学习一系列弱分类器或者基本分类器，并将这些若分类器线性组合成为一个强分类器。

**输入：** 训练数据集 $T=\left\\{(x_{1},y_{1}),(x_{2},y_{2}),\dots,(x_{N},y_{N})\right\\}$ ，其中 $x_{i}\in\mathcal{X}\subseteq{{R}^{n}},y_{i}\in\mathcal{Y}=\left\\{+1,-1\right\\}$ ;弱学习算法；

**输出：** 最终分类器$G(x)$。

(1) 初始化训练数据的权值分布

$$D_{1}=\left(w_{11},\dots,w_{1i},\dots,w_{1N}\right),w_{1i}=\dfrac{1}{N},i=1,2,\dots,N$$

(2) 对 $m=1,2,\dots,M$

(a) 使用具有权值分布 $D_{m}$ 的训练数据集学习，得到基本分类器

$$G_{m}(x):\mathcal{X}\rightarrow\left\\{+1,-1\right\\}$$

(b) 计算 $G_{m}(x)$ 在训练数据集上的分类错误率

$$e_{m}=\sum\limits_{i=1}^{N}P\left(G_{m}(x_{i})\neq{y_{i}}\right)=\sum\limits_{i=1}^{N}w_{mi}I\left(G_{m}(x_{i})\neq{y_{i}}\right)$$

(c) 计算 $G_{m}(x)$ 的系数

$$\alpha_{m}=\dfrac{1}{2}\log\dfrac{1-e_{m}}{e_{m}}$$

`log`指的是自然对数

(d) 更新训练数据集的权值分布

$$D_{m+1}=\left(w_{m+1,1},\dots,w_{m+1,i},\dots,w_{m+1,N}\right)$$

$$w_{m+1,i}=\dfrac{w_{mi}}{Z_{m}}\exp\left(-\alpha_{m}y_{i}G_{m}(x_{i})\right),i=1,2,\dots,N$$

$Z_{m}$ 是规范化因子

$$Z_{m}=\sum\limits_{i=1}^{N}w_{mi}\exp\left(-\alpha_{m}y_{i}G_{m}(x_{i})\right)$$

这样使得 $D_{m+1}$ 成为一个概率分布。

(e) 构建基本分类器的线性组合

$$f(x)=\sum\limits_{m=1}^{M}\alpha_{m}G_{m}(x)$$

从而得到最终的分类器

$$G(x)=\text{sign}(f(x))=\text{sign}\left(\sum\limits_{m=1}^{M}\alpha_{m}G_{m}(x)\right)$$

