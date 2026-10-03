---
title: 增广拉格朗日法与两块 ADMM
source: "https://web.stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf"
scope: "§2.3, pp. 10–11; §3.1–3.2, pp. 13–17"
status: verified
---

# 增广拉格朗日法与两块 ADMM

## 优化问题与记号

考虑两个原变量块的等式约束问题

$$
\min_{x,z}\; f(x)+g(z)\quad\text{s.t.}\quad Ax+Bz=c.
$$

记原始残差为 $r(x,z)=Ax+Bz-c$，乘子为 $y$，罚参数为 $\rho>0$。增广拉格朗日函数是

$$
L_\rho(x,z,y)=f(x)+g(z)+y^{\mathsf T}r(x,z)
                 +\frac{\rho}{2}\|r(x,z)\|_2^2.
$$

这是 [Boyd 等，§3.1，式 (3.1)](https://web.stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf) 的模型和符号。二次项在可行点为零；在迭代点，它会影响原变量子问题和违反约束的代价。

## 两种更新方式

增广拉格朗日法（method of multipliers）在固定 $y^k$ 时联合求解两个原变量：

$$
(x^{k+1},z^{k+1})\in\arg\min_{x,z}L_\rho(x,z,y^k),\qquad
y^{k+1}=y^k+\rho r(x^{k+1},z^{k+1}).
$$

两块 ADMM 用依次最小化代替上面的联合最小化：

$$
\begin{aligned}
x^{k+1}&\in\arg\min_x L_\rho(x,z^k,y^k),\\
z^{k+1}&\in\arg\min_z L_\rho(x^{k+1},z,y^k),\\
y^{k+1}&=y^k+\rho(Ax^{k+1}+Bz^{k+1}-c).
\end{aligned}
$$

“交替”发生在 $x,z$ 两个原变量子问题上；乘子随后用**新的**原始残差更新。两种方法的差别是联合求解与顺序分块求解，[原文 §3.1，式 (3.2)–(3.4)，pp. 13–14](https://web.stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf) 直接给出了这些更新式。

若令 $u^k=y^k/\rho$，配方后得到常用的缩放形式，其乘子步骤为 $u^{k+1}=u^k+r(x^{k+1},z^{k+1})$；这是同一迭代的变量重写，见原文 §3.1.1，pp. 15–16。

## 已核对的结论与适用条件

原文 §3.2，pp. 16–17 的基本收敛陈述针对**两块、精确子问题更新、固定正参数**的上述形式，并列出两项假设：$f,g$ 是闭、真、凸函数；未增广拉格朗日函数存在鞍点。在这些假设以及迭代可执行的前提下，原始残差趋于零、目标函数值趋于最优值、对偶变量趋于某个对偶最优点。该陈述**没有保证** $x^k,z^k$ 本身都收敛到某个最优点；原文明确提醒，这需要额外条件。

这里的公式也可作为其他模型的算法模板，但上述收敛结论不可不核对条件就套用于非凸问题、更多变量块或近似求解的子问题。

## 证据与边界

- **论文原文：**[S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein, *Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers*](https://web.stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf)，§2.3、§3.1–3.2，pp. 10–17。更新式、缩放形式与上述基本收敛条件均来自所列章节。
- **笔记中的解释：**“二次项在可行点为零”“交替的是原变量子问题”是根据这些公式作出的直接解释；它们不构成额外收敛定理。
