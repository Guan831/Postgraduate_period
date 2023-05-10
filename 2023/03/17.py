from scipy.stats import binom


def calculate_probability(n, k):
    p_head = 0.5  # コインの表が出る確率
    cum_prob = binom.cdf(k, n, p_head)  # 二項累積分布関数を使って k 回以下の確率を求める
    return cum_prob


n = 600
k = 550
probability = calculate_probability(n, k)
print(f"{n} 回コインを投げたとき、表の出る回数が {k} 回以下である確率: {probability:.4f}")
