import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def parse_time(t):
    parts = t.split(":")
    return int(parts[0]) * 60 + int(parts[1])


def fmt_seconds(s):
    return f"{int(s)//60}:{int(s)%60:02d}"


times_raw = ["5:24", "4:37", "2:00", "2:13", "2:00", "1:52", "2:07", "2:18", "2:25", "3:47", "2:22", "2:23"]
times = [parse_time(t) for t in times_raw]
window = 5

moving_avg = [
    sum(times[i - window:i]) / window
    for i in range(window, len(times) + 1)
]
avg_indices = list(range(window, len(times) + 1))

print(f"{'#':>3}  {'Time':>6}  {'Ao5':>8}")
print("-" * 22)
for i, (raw, sec) in enumerate(zip(times_raw, times), 1):
    ao5 = moving_avg[i - window] if i >= window else "-"
    ao5_str = fmt_seconds(ao5) if ao5 != "-" else "-"
    print(f"{i:>3}  {raw:>6}  {ao5_str:>8}")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(range(1, len(times) + 1), times, "o-", color="#4a90d9", label="Solve time", linewidth=1.5, markersize=5)
ax.plot(avg_indices, moving_avg, "s--", color="#e05c5c", label="Ao5 (moving avg)", linewidth=2, markersize=6)

for i, sec in enumerate(times, 1):
    ax.annotate(fmt_seconds(sec), (i, sec), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8, color="#4a90d9")

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda s, _: fmt_seconds(s)))
ax.set_xlabel("Solve #")
ax.set_ylabel("Time (mm:ss)")
ax.set_title("Rubik's Cube 3x3 — Solve Times & Ao5 Evolution")
ax.set_xticks(range(1, len(times) + 1))
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rubiks_progress.png", dpi=150)
print("\nChart saved to rubiks_progress.png")
