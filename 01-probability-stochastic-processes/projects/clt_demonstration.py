"""
Central Limit Theorem — Numerical Demonstration
Module 01 | Project 1

Goal: Show that the distribution of sample means approaches N(0,1)
regardless of the underlying population distribution, as n → ∞.

We test this with three different distributions:
- Uniform (flat, nothing like a normal)
- Exponential (right-skewed, positive only)
- Bimodal mixture (two peaks — definitely not normal)

For each, we draw many samples, compute the sample mean,
standardize it, and compare the histogram to the standard normal.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

def simulate_clt(distribution_fn, n: int, n_samples: int, params: dict, title: str):
    """
    Draw n_samples of size n from the given distribution,
    compute standardized sample means, and plot the histogram.
    """
    # Generate samples: each row is one draw of n observations
    samples = distribution_fn(**params, size=(n_samples, n))
    
    # Compute sample means
    sample_means = samples.mean(axis=1)
    
    # True mean and variance of the underlying distribution
    # (for the distributions below, we know these analytically)
    true_mean = params.get("mean", 0)
    true_std = params.get("std", 1)
    
    # Standardize: (X̄ - μ) / (σ / √n)
    standardized = (sample_means - true_mean) / (true_std / np.sqrt(n))
    
    return standardized

def uniform_fn(loc, scale, size):
    return np.random.uniform(loc, loc + scale, size=size)

def exponential_fn(scale, size):
    return np.random.exponential(scale=scale, size=size)

def mixture_fn(w1, mu1, sigma1, mu2, sigma2, size):
    """Two-point mixture: p*N(mu1,sigma1) + (1-p)*N(mu2,sigma2)"""
    indicators = np.random.random(size) < w1
    samples = np.where(
        indicators,
        np.random.normal(mu1, sigma1, size=size),
        np.random.normal(mu2, sigma2, size=size)
    )
    return samples

# Set up figure
fig, axes = plt.subplots(3, 4, figsize=(16, 10))
fig.suptitle("Central Limit Theorem — Sample Means Approach Normal as n Increases", fontsize=14)

distributions = [
    {
        "name": "Uniform",
        "fn": lambda size: uniform_fn(0, 2, size),
        "params": {"loc": 0, "scale": 2},
        "mean": 1,
        "std": np.sqrt(2**2 / 12),  # uniform(0,2) variance = (b-a)^2/12
    },
    {
        "name": "Exponential",
        "fn": lambda size: exponential_fn(1.0, size),
        "params": {"scale": 1.0},
        "mean": 1.0,
        "std": 1.0,  # exponential variance = scale^2
    },
    {
        "name": "Bimodal Mixture",
        "fn": lambda size: mixture_fn(0.5, -3, 0.5, 3, 0.5, size),
        "params": {},
        "mean": 0,  # symmetric mixture
        "std": 3.0,  # approximate
    },
]

sample_sizes = [1, 5, 30, 100]
n_samples = 10_000
x = np.linspace(-4, 4, 200)
standard_normal = stats.norm.pdf(x)

for row_idx, dist in enumerate(distributions):
    for col_idx, n in enumerate(sample_sizes):
        ax = axes[row_idx, col_idx]
        
        standardized_means = simulate_clt(
            dist["fn"], n, n_samples, dist["params"], dist["name"]
        )
        
        ax.hist(standardized_means, bins=50, density=True, alpha=0.6, color=f"C{row_idx}")
        ax.plot(x, standard_normal, 'k-', lw=1.5, label='N(0,1)')
        ax.set_xlim(-4, 4)
        ax.set_title(f"{dist['name']} | n={n}")
        ax.set_xlabel("Standardized sample mean")
        
        # Overlay KS test result
        ks_stat, p_val = stats.kstest(standardized_means, 'norm')
        ax.text(0.05, 0.92, f"KS p={p_val:.3f}", transform=ax.transAxes, fontsize=8,
                verticalalignment='top', color='darkred')

for col_idx, n in enumerate(sample_sizes):
    axes[0, col_idx].annotate(
        f'n = {n}', xy=(0.5, 1.12), xycoords='axes fraction',
        ha='center', fontsize=12, fontweight='bold'
    )

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("clt_demonstration.png", dpi=150)
plt.close()

print("Figure saved: clt_demonstration.png")

# Summary statistics for convergence
print("\n--- Convergence of sample means to N(0,1) ---")
print(f"{'Distribution':<20} {'n=1':>12} {'n=5':>12} {'n=30':>12} {'n=100':>12}")
print("-" * 68)

for dist in distributions:
    row_name = dist["name"]
    for n in sample_sizes:
        means = simulate_clt(dist["fn"], n, 5000, dist["params"], dist["name"])
        ks_stat, _ = stats.kstest(means, 'norm')
        # Just print final n for compact output
    final_ks = stats.kstest(
        simulate_clt(dist["fn"], 100, 5000, dist["params"], dist["name"]), 'norm'
    )[0]
    print(f"{row_name:<20} {' ':>12} {' ':>12} {' ':>12} {final_ks:>12.4f}")

print("\nNote: With n=100, KS statistic should be very small (<0.03) for all distributions.")
print("This demonstrates that the CLT is distribution-agnostic — any finite-variance")
print("underlying distribution produces normal sample means as n grows.")