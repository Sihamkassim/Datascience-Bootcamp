import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes


def run_statistics():
    with open("data/sample_salaries.json") as f:
        data = json.load(f)

    engine = StatEngine(data)

    print("---- STATISTICS ----")
    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance:", engine.get_variance())
    print("Standard Deviation:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers())


def run_simulation():
    print("\n---- MONTE CARLO SIMULATION ----")
    for days in [30, 365, 10000]:
        prob = simulate_crashes(days)
        print(f"{days} days → crash probability: {prob}")


if __name__ == "__main__":
    run_statistics()
    run_simulation()