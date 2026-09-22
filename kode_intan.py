import pandas as pd
import matplotlib.pyplot as plt

#excel ke python
path = r"D:\intan.xlsx"
dataraw = pd.read_excel(path)
print(dataraw)

#frekuensi
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")
print("\n=== TABEL FREKUENSI ===")
print(datafrq)

categories = list(datafrq.index)
values = list(datafrq["Frekuensi"])
palette_colors = ["#6C5CE7", "#00B894", "#0984E3", "#FDCB6E", "#E17055"]


#grafik garis
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120)

ax.plot(categories, values, color="#6C5CE7", marker="o", linewidth=3, markersize=8, markerfacecolor="white", markeredgewidth=2.5)
ax.fill_between(categories, values, color="#6C5CE7", alpha=0.15)


for i, val in enumerate(values):
    ax.annotate(f"{val}", (categories[i], values[i]), textcoords="offset points", xytext=(0, 8), ha="center", fontweight="bold", color="#2D3436")

ax.set_title("Distribusi Frekuensi Grade", fontsize=14, fontweight="bold", pad=15, loc="left", color="#2D3436")
ax.set_ylabel("Frekuensi", fontsize=10, fontweight="semibold", color="#636E72")
ax.grid(axis="y", linestyle="--", alpha=0.4)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

#grafik batang
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120)

bars = ax.bar(categories, values, color=palette_colors[:len(categories)], width=0.55, zorder=3)

ax.bar_label(bars, padding=4, fontweight="bold", color="#2D3436", fontsize=10)

ax.set_title("Frekuensi Nilai Berdasarkan Grade", fontsize=14, fontweight="bold", pad=15, loc="left", color="#2D3436")
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
ax.yaxis.set_visible(False)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.tight_layout()
plt.show()

#grafik bulatan
fig, ax = plt.subplots(figsize=(6.5, 6.5), dpi=120)

wedges, texts, autotexts = ax.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    startangle=140,
    colors=palette_colors[:len(categories)],
    pctdistance=0.75,
    wedgeprops=dict(width=0.38, edgecolor="white", linewidth=3)
)

plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=11, weight="semibold", color="#2D3436")


total_val = sum(values)
ax.text(0, 0, f"Total\n{total_val}", ha="center", va="center", fontsize=13, fontweight="bold", color="#2D3436")

ax.set_title("Persentase Grade", fontsize=14, fontweight="bold", pad=15, color="#2D3436")

plt.tight_layout()
plt.show()

#statistika deskriptif
dataraw["NA"] = pd.to_numeric(dataraw["NA"], errors="coerce")
dt = dataraw["NA"]

stats = dt.describe()
stats["Standard Error"] = dt.sem()
stats["Median"] = dt.median()
stats["Mode"] = dt.mode().iloc[0]
stats["variance"] = dt.var()
stats["range"] = dt.max() - dt.min()
stats["skewness"] = dt.skew()
stats["kurtosis"] = dt.kurtosis()

print("\n=== STATISTIKA DESKRIPTIF NILAI AKHIR ===")
print(stats)