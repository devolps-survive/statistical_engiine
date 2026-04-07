from src import StatEngine, run_experiments


def main():
    data = [10, 20, 30, 40, 1000]

    engine = StatEngine(data)

    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance:", engine.get_variance())
    print("Std Dev:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers())

    print("\nMonte Carlo Simulation:")
    results = run_experiments()
    for days, prob in results.items():
        print(f"{days} days -> {prob:.4f}")


if __name__ == "__main__":
    main()
