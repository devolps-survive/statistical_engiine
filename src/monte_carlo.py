import random


CRASH_PROBABILITY = 0.045


def simulate_crashes(days: int) -> float:
    crashes = 0

    for _ in range(days):
        if random.random() < CRASH_PROBABILITY:
            crashes += 1

    return crashes / days


def run_experiments():
    trials = [30, 365, 10000]

    results = {}
    for days in trials:
        prob = simulate_crashes(days)
        results[days] = prob

    return results


if __name__ == "__main__":
    results = run_experiments()
    for k, v in results.items():
        print(f"{k} days -> {v:.4f}")
