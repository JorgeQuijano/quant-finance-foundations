# Stochastic Processes

## Definition

A stochastic process is a family of random variables $\{X_t\}_{t \in T}$ indexed by time. Think of it as a random signal evolving over time.

For each fixed $\omega \in \Omega$, the map $t \mapsto X_t(\omega)$ is a *sample path* (or realization) of the process — a single outcome of how the system evolves over time.

## Filtrations and Information

A filtration $\{\mathcal{F}_t\}$ is an increasing sequence of sigma-algebras representing the information available up to time $t$.

- $\mathcal{F}_t \subseteq \mathcal{F}_s$ for $t < s$ (information accumulates)
- A process $X_t$ is *adapted* to $\mathcal{F}_t$ if $X_t$ is $\mathcal{F}_t$-measurable (you know its value at time $t$ given the available information)

This is critical: at time $t$, your information set is $\mathcal{F}_t$, and you can only make decisions based on what you know.

## Martingales

A stochastic process $M_t$ is a **martingale** with respect to filtration $\mathcal{F}_t$ if:
1. $M_t$ is adapted to $\mathcal{F}_t$
2. $\mathbb{E}[|M_t|] < \infty$ for all $t$
3. $\mathbb{E}[M_{t+s} | \mathcal{F}_t] = M_t$ for all $s \geq 0$

Property (3) is the martingale property: the best prediction of the future value is the current value. No drift, no mean reversion — just "fair game."

**Examples:**
- Simple symmetric random walk: $S_n = \sum_{i=1}^n X_i$ where $X_i$ are i.i.d. with $\mathbb{P}(X_i = 1) = \mathbb{P}(X_i = -1) = 1/2$. Then $S_n$ is a martingale.
- Brownian motion (see below) is a martingale.
- If $M_t$ is a martingale and $t < s$, then $\mathbb{E}[M_s - M_t | \mathcal{F}_t] = 0$ — the expected increment over any future interval is zero.

**Why martingales matter in finance:**
In an efficient market with no arbitrage, discounted asset prices must be martingales. This is the fundamental theorem of asset pricing. If you can find a price dynamics under which discounted prices are martingales, you've found a pricing measure.

## Brownian Motion (Wiener Process)

**Definition:** A standard Brownian motion $W_t$ is a stochastic process satisfying:
1. $W_0 = 0$ almost surely
2. Independent increments: $W_{t_2} - W_{t_1}, W_{t_4} - W_{t_3}$ are independent for $t_1 < t_2 < t_3 < t_4$
3. $W_{t+s} - W_t \sim N(0, s)$ for all $t, s \geq 0$
4. Continuous paths: $t \mapsto W_t$ is continuous almost surely

**Properties:**
- $W_t$ is a martingale (and also a martingale with respect to its own filtration)
- Variance grows linearly: $\text{Var}(W_t) = t$
- Scaling: $W_{ct}$ has the same distribution as $\sqrt{c} W_t$ for fixed $c$
- Paths are continuous but nowhere differentiable — classic fractal, "rough everywhere"

**Financial interpretation:**
In the Black-Scholes model, the log-price process is modeled as a Brownian motion with drift:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

The $dW_t$ term is the source of randomness. The stock price evolves as a geometric Brownian motion.

## Itô's Lemma

This is the chain rule for stochastic calculus. If $X_t$ follows the SDE:
$$dX_t = \mu_t dt + \sigma_t dW_t$$

and $f(t, x)$ is a twice-differentiable function, then $Y_t = f(t, X_t)$ satisfies:

$$df(t, X_t) = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial x}dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(dX_t)^2$$

Expanding using $(dW_t)^2 = dt$ (Itô calculus rule) and $dW_t \cdot dt = 0$:

$$df = \left(\frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2 \frac{\partial^2 f}{\partial x^2}\right)dt + \sigma_t \frac{\partial f}{\partial x} dW_t$$

**Why the second derivative matters:** Unlike ordinary calculus, stochastic integrals pick up a quadratic variation term from the $dW_t^2 = dt$ contribution.

**Black-Scholes PDE derivation:**
If $V(S_t, t)$ is the option price and $S_t$ follows $dS_t = rS_t dt + \sigma S_t dW_t$, Itô's lemma gives the dynamics of $V$. Then by constructing a delta-hedge portfolio and eliminating the stochastic component, you get the Black-Scholes PDE:
$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0$$

## Geometric Brownian Motion (GBM)

The stock price model in Black-Scholes:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

**Solution (closed form):**
$$S_t = S_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)$$

**Properties:**
- $S_t > 0$ for all $t$ (stock price can't go negative)
- Log-returns over interval $[0, t]$: $\log(S_t/S_0) \sim N\left(\left(\mu - \frac{\sigma^2}{2}\right)t, \sigma^2 t\right)$
- $S_t$ is lognormal — prices are lognormal in the BS model

**Special case:** If $\mu = r$ (the risk-free rate under risk-neutral pricing), then $\log(S_t/S_0) \sim N\left(\left(r - \frac{\sigma^2}{2}\right)t, \sigma^2 t\right)$. This is used for option pricing via risk-neutral valuation.

## Stochastic Integration

The stochastic integral $\int_0^t \phi_s dW_s$ is defined for predictable, square-integrable processes $\phi_s$.

Key properties:
- $\mathbb{E}\left[\int_0^t \phi_s dW_s\right] = 0$ (mean zero)
- $\text{Var}\left(\int_0^t \phi_s dW_s\right) = \mathbb{E}\left[\int_0^t \phi_s^2 ds\right]$ (Itô isometry)

This is fundamentally different from ordinary integrals — you can't use Riemann sums. The paths of $W_t$ are too irregular. Itô's approach defines the integral via a limit of backward sums (Itô integration), which is why the $(dW_t)^2 = dt$ rule emerges.