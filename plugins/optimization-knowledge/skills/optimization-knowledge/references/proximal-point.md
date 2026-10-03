---
title: 近端点法与隐式梯度步
source: "https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf"
scope: "§1.1, p. 124; §3.2, pp. 137–138; §4.1, pp. 142–146"
status: verified
---

# 近端点法与隐式梯度步

## 近端子问题

令 $f:\mathbb R^d\to\mathbb R\cup\{+\infty\}$ 为闭、真、凸函数，$\lambda>0$。从当前点 $x^k$ 出发，近端点法计算

$$
x^{k+1}=\operatorname{prox}_{\lambda f}(x^k)
=\arg\min_u\left\{f(u)+\frac{1}{2\lambda}\|u-x^k\|_2^2\right\}.
$$

二次项既衡量新点与旧点的距离，又使子问题强凸，因此这个设定下极小点唯一。[Parikh、Boyd，§1.1，式 (1.2)，p. 124；§4.1，式 (4.1)，p. 142](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf) 给出定义与迭代。

## 为何叫“隐式”

近端子问题的最优性条件是

$$
0\in\partial f(x^{k+1})+\frac{x^{k+1}-x^k}{\lambda},
\qquad\text{即}\qquad
x^k\in x^{k+1}+\lambda\partial f(x^{k+1}).
$$

在上述凸性条件下，它既是必要条件，也是充分条件；原文 §3.2，pp. 137–138 将近端算子写成 $(I+\lambda\partial f)^{-1}$。若 $f$ 还可微，条件变为

$$
x^{k+1}=x^k-\lambda\nabla f(x^{k+1}).
$$

梯度在**未知的新点**取值，因而要解方程或子问题。显式梯度步使用的是旧点梯度 $\nabla f(x^k)$。[原文 §4.1.1，pp. 144–146](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf) 也把这一步解释为梯度流的后向 Euler 离散。

## 手算示例与适用边界

对 $f(x)=\tfrac12x^2$，近端最优性条件为 $x^{k+1}+\lambda x^{k+1}=x^k$，所以

$$
x^{k+1}=\frac{x^k}{1+\lambda}.
$$

这是对前述定义的直接演算。若换成非凸函数，写出 $x^{k+1}=x^k-\lambda\nabla f(x^{k+1})$ 仅得到子问题的驻点条件；单凭这个方程不能断定所得点是子问题的全局极小点。非凸情形必须单独核查子问题的最优性和相关算法结论。

## 证据类型与结论边界

- **论文原文：**[Neal Parikh、Stephen Boyd, *Proximal Algorithms*](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf)，§1.1、§3.2、§4.1，pp. 124、137–138、142–146。闭、真、凸函数的近端定义、最优性条件和隐式梯度流解释均由这些章节支持。
- **笔记演算：**二次函数的更新式与非凸驻点提醒是根据所列公式作出的推导；这里没有声称非凸近端点法的普遍收敛性。
