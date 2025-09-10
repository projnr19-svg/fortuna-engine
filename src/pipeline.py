# Loads a CSV, computes something trivial, writes an output CSV
# Replace with real logic as you learn.
import csv, os
from .probability import simple_probability

def run_pipeline():
    in_csv  = os.path.join("data","raw_draws.csv")
    out_csv = os.path.join("data","processed_results.csv")

    # Ensure input exists (create tiny sample)
    if not os.path.exists(in_csv):
        with open(in_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["trial","success"])
            w.writerow([1,1])
            w.writerow([2,0])
            w.writerow([3,1])

    # Compute a toy probability
    trials=0; successes=0
    with open(in_csv) as f:
        r=csv.DictReader(f)
        for row in r:
            trials += 1
            successes += int(row["success"])

    p = simple_probability(successes, trials)

    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["trials","successes","probability"])
        w.writerow([trials,successes,p])

    print(f"Wrote {out_csv} with probability={p:.3f}")
