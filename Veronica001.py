# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker", style="smoker", size="size")

sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")

sns.displot(data=tips, x="total_bill", col="time", kde=True)

sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)

sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)

sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")

sns.displot(data=tips, x="total_bill", col="time", kde=True)

plt.show()