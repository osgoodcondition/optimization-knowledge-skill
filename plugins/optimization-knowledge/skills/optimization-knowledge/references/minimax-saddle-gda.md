---
title: 极小极大鞍点、局部 Nash 点与同步 GDA
source: "https://arxiv.org/pdf/1902.00618"
scope: "§2.1, pp. 4–5；§3.1, p. 7；另核对 Daskalakis 等 arXiv:1711.00141, §4, pp. 6–7"
status: verified
---

# 极小极大鞍点、局部 Nash 点与同步 GDA

## 解的概念

对 $\min_{x\in X}\max_{y\in Y} f(x,y)$，全局鞍点（在零和同时博弈中也是纯策略 Nash 均衡）满足

$$
f(x^*,y)\le f(x^*,y^*)\le f(x,y^*)
\quad(\forall x\in X,\;\forall y\in Y).
$$

两个不等式分别表示：固定 $x^*$，$y^*$ 是全局最大化选择；固定 $y^*$，$x^*$ 是全局最小化选择。若不等式只在各自变量的某个邻域内成立，则是**局部 Nash 点**。这些定义见 [Jin、Netrapalli、Jordan，§2.1，定义 1–2，pp. 4–5](https://arxiv.org/pdf/1902.00618)。该论文在 [§3.1，定义 14，p. 7](https://arxiv.org/pdf/1902.00618) 另行定义顺序博弈的“局部 minimax 点”；不能自动和局部 Nash 点画等号。

对无约束可微内点，局部 Nash 点必满足

$$
\nabla_x f(x^*,y^*)=0,\qquad \nabla_y f(x^*,y^*)=0,
$$

见同论文 §2.1，命题 3。反向不成立：$f(x,y)=-x^2+y^2$ 在原点两块梯度都为零，但固定 $y=0$ 时原点是 $x$ 方向的局部最大点，固定 $x=0$ 时是 $y$ 方向的局部最小点。这个反例是直接代入定义得到的演算，并非论文中的例子。

## 有鞍点也不代表同步 GDA 收敛

取 $X=Y=\mathbb R$、$f(x,y)=xy$。原点是全局鞍点，因为 $f(0,y)=f(x,0)=0$。用相同固定步长 $\eta>0$ 同步做下降—上升：

$$
\begin{pmatrix}x_{k+1}\\y_{k+1}\end{pmatrix}
=\begin{pmatrix}1&-\eta\\\eta&1\end{pmatrix}
 \begin{pmatrix}x_k\\y_k\end{pmatrix}.
$$

直接相乘可得 $x_{k+1}^2+y_{k+1}^2=(1+\eta^2)(x_k^2+y_k^2)$。因此，除原点初值外，**这个离散的同步固定步长算法**离原点越来越远；这里只证明了这个例子，不是所有 GDA 变体的行为。[Daskalakis 等，§4，命题 1，pp. 6–7](https://arxiv.org/pdf/1711.00141) 也指出恒等矩阵双线性博弈中普通梯度下降—上升的发散现象。

## 适用条件与证据边界

- **定义和必要条件：**[Chi Jin、Praneeth Netrapalli、Michael I. Jordan, *What is Local Optimality in Nonconvex-Nonconcave Minimax Optimization?*](https://arxiv.org/pdf/1902.00618)，§2.1，定义 1–2、命题 3，pp. 4–5；局部 minimax 定义见 §3.1，定义 14，p. 7。局部 Nash 讨论的是零和博弈中各方固定对手变量的最优反应。
- **算法现象：**[Constantinos Daskalakis、Andrew Ilyas、Vasilis Syrgkanis、Haoyang Zeng, *Training GANs with Optimism*](https://arxiv.org/pdf/1711.00141)，§4，命题 1，pp. 6–7。上面的 $xy$ 距离递推是根据明示更新式进行的独立计算。
- **边界：**一阶驻点只满足梯度等于零，不保证局部或全局鞍点；有鞍点也不保证某个指定的迭代法收敛。顺序极小极大、局部 Nash、局部 minimax 与算法极限应分别判断。
