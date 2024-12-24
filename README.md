# MCVRP - Calculate the Approximation Ratio

We use $\epsilon$ to denote a small positive constant.

Given $\epsilon$, the function `f(epsilon)` in the `MCVRP.py` file refers to the function $f$ in [9]. Specifically, we have

$$
f(\epsilon)=\min_{\substack{0<\theta\leq1-\tau, \\ 0<\tau,\rho\leq 1/6}} \\{\frac{1+\zeta}{\theta}+\frac{1-\tau-\theta}{\theta\cdot(1-\tau)}+\frac{3\epsilon}{1-\theta}+\frac{3\rho}{(1-\rho)\cdot(1-\tau)}\\}-1,
$$

where $\theta$ is let to be $1-\tau$ in [9] and

$$
\zeta=\frac{3\rho+\tau-4\tau\cdot\rho}{1-\rho}+\frac{\epsilon}{\tau\cdot\rho}\cdot(1-\tau\cdot\rho-\frac{3\rho+\tau-4\tau\cdot\rho}{1-\rho}).
$$

Since $f$ is an optimization function, we compute the optimal value using a grid-based brute-force search, which may introduce a small error.

The `MCVRP.py` file consists of three cases: `splittable`, `unsplittable`, and `splittable with fixed capacity`.

For example, in the first case, we need to find the proper value of $\epsilon^*$ such that

$$
\epsilon^* = \arg\min_{\epsilon > 0} \max\\{ 4 - 2\epsilon, 3 + 2f(\epsilon) \\}.
$$

The `MCVRP.py` file defaults to setting $\epsilon = 1/3000$, and the output is `epsilon can be bigger`, meaning that $\epsilon^* > 1/3000$.

However, we note that $\epsilon^\*$ is very close to $1/3000$, as even setting $\epsilon = 1.01/3000$ causes the output to be `epsilon should be smaller`, meaning that $\epsilon^\* < 1.01/3000$.

The other two cases follow a similar pattern.



[9] J. Blauth, V. Traub, J. Vygen, "Improving the approximation ratio for capacitated vehicle routing," *Mathematical Programming*, 197(2) (2023) 451–497.
