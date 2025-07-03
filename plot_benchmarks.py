import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bench.csv")

print(df.head())

# Exemple : courbe de performance en fonction de la taille du problème
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Filtrer ou pivoter si nécessaire
# Supposons que les colonnes sont : algorithm, p, q, n, b, time
# Tu peux adapter selon la structure réelle de bench.csv

sns.lineplot(
    data=df,
    x="n",        # ou une autre métrique comme m ou k
    y="time",     # ou "flops" si c'est disponible
    hue="algorithm",
    style="algorithm",
    markers=True,
    dashes=False
)

plt.title("Comparaison des performances des algorithmes MPI")
plt.xlabel("Taille du problème (n)")
plt.ylabel("Temps d'exécution (s)")
plt.legend(title="Algorithme")
plt.tight_layout()
plt.savefig("benchmark_comparison.png")
plt.show()
