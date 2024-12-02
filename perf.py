from time import perf_counter_ns
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python perf.py <script>")
        exit(1)

    with open(argv[1]) as f:
        script = f.read()

    ns = []
    print("------ PROGRAM OUTPUT ------")
    for _ in range(100):
        start = perf_counter_ns()
        exec(script)
        ns.append(perf_counter_ns() - start)
    print("----------------------------")

    print(f"Average perf: {sum(ns) / len(ns)}ns")
