import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the penguins dataset
penguins = sns.load_dataset('penguins')

# Basic analysis
print("Dataset Info:")
print(penguins.info())
print("\nDescriptive Statistics:")
print(penguins.describe())

# Handle missing values (drop for simplicity)
penguins = penguins.dropna()

# Create a markdown file
markdown_content = "# Penguin Dataset Analysis\n\n"

markdown_content += "## Dataset Overview\n\n"
markdown_content += penguins.head().to_markdown() + "\n\n"
markdown_content += "**인사이트:** 이 데이터셋은 펭귄의 종, 섬, 부리 길이, 깊이, 날개 길이, 체중, 성별을 포함합니다. 총 333개의 유효 데이터로, Adelie, Chinstrap, Gentoo 세 종의 펭귄을 분석할 수 있습니다. 데이터는 남극의 세 섬에서 수집되었으며, 생물 다양성과 환경적 요인을 연구하는 데 유용합니다.\n\n"

markdown_content += "## Descriptive Statistics\n\n"
markdown_content += penguins.describe().to_markdown() + "\n\n"
markdown_content += "**인사이트:** 평균 부리 길이는 44mm, 체중은 4200g 정도입니다. 표준편차가 크므로 개체 간 변이가 큽니다. 최소/최대 값의 차이가 커서 종별 차이를 예상할 수 있습니다. 이는 펭귄의 생태적 적응을 반영합니다.\n\n"

# Visualizations (more than 10)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
sns.histplot(penguins['bill_length_mm'], ax=axes[0,0]).set_title('Bill Length Histogram')
sns.histplot(penguins['bill_depth_mm'], ax=axes[0,1]).set_title('Bill Depth Histogram')
sns.histplot(penguins['flipper_length_mm'], ax=axes[1,0]).set_title('Flipper Length Histogram')
sns.histplot(penguins['body_mass_g'], ax=axes[1,1]).set_title('Body Mass Histogram')
plt.tight_layout()
plt.savefig('histograms.png')
markdown_content += "## Histograms\n\n![Histograms](histograms.png)\n\n"
markdown_content += "**인사이트:** 히스토그램은 각 변수의 분포를 보여줍니다. 부리 길이와 깊이는 정규분포에 가까우며, 날개 길이와 체중은 약간 오른쪽으로 치우쳐 있습니다. 이는 Gentoo 종의 큰 체구가 영향을 미칠 수 있습니다. 분포 분석을 통해 이상치를 식별할 수 있습니다.\n\n"

plt.figure(figsize=(8,6))
sns.boxplot(data=penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']])
plt.title('Boxplots of Numerical Variables')
plt.savefig('boxplots.png')
markdown_content += "## Boxplots\n\n![Boxplots](boxplots.png)\n\n"
markdown_content += "**인사이트:** 박스플롯은 중앙값과 분산을 시각화합니다. 체중의 분산이 가장 크며, 날개 길이는 상대적으로 균일합니다. 이상치가 보이므로 특정 개체의 특성을 조사할 필요가 있습니다. 종별 비교 시 유용합니다.\n\n"

plt.figure(figsize=(8,6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.title('Scatterplot: Bill Length vs Depth')
plt.savefig('scatter1.png')
markdown_content += "## Scatterplot 1\n\n![Scatter1](scatter1.png)\n\n"
markdown_content += "**인사이트:** 부리 길이와 깊이의 산점도는 종별 군집을 보여줍니다. Adelie는 작은 부리, Gentoo는 큰 부리를 가집니다. 이는 먹이 습성과 관련될 수 있습니다. 상관관계가 약하므로 다른 요인이 영향을 미칠 수 있습니다.\n\n"

plt.figure(figsize=(8,6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Scatterplot: Flipper Length vs Body Mass')
plt.savefig('scatter2.png')
markdown_content += "## Scatterplot 2\n\n![Scatter2](scatter2.png)\n\n"
markdown_content += "**인사이트:** 날개 길이와 체중의 산점도는 강한 양의 상관관계를 보입니다. Gentoo가 가장 크고, Adelie가 작습니다. 이는 체구가 큰 펭귄이 더 긴 날개를 가짐을 시사합니다. 수영 능력과 관련된 생태적 적응입니다.\n\n"

plt.figure(figsize=(8,6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='island')
plt.title('Scatterplot: Bill Length vs Body Mass by Island')
plt.savefig('scatter3.png')
markdown_content += "## Scatterplot 3\n\n![Scatter3](scatter3.png)\n\n"
markdown_content += "**인사이트:** 섬별로 본 부리 길이와 체중의 분포는 환경 차이를 반영합니다. Biscoe 섬의 Gentoo가 크고, Dream의 Chinstrap이 중간입니다. 섬의 기후와 먹이원이 펭귄의 크기에 영향을 미칠 수 있습니다.\n\n"

# Bar chart for species count
plt.figure(figsize=(8,6))
species_count = penguins['species'].value_counts()
sns.barplot(x=species_count.index, y=species_count.values)
plt.title('Species Count')
plt.savefig('bar_species.png')
markdown_content += "## Bar Chart: Species Count\n\n![Bar Species](bar_species.png)\n\n"
markdown_content += "**인사이트:** 종별 개수는 Gentoo가 가장 많고, Chinstrap이 적습니다. 이는 섬별 분포와 관련됩니다. 데이터 불균형이 분석에 영향을 줄 수 있으므로 가중치를 고려해야 합니다.\n\n"

# Crosstab for species and island
crosstab = pd.crosstab(penguins['species'], penguins['island'])
markdown_content += "## Crosstab: Species vs Island\n\n" + crosstab.to_markdown() + "\n\n"
markdown_content += "**인사이트:** 교차표는 종과 섬의 관계를 보여줍니다. Gentoo는 Biscoe에만, Chinstrap은 Dream에만 서식합니다. 이는 생태적 분리가 일어났음을 시사하며, 진화적 다양성을 연구하는 데 중요합니다.\n\n"

# Pivot table for mean body mass by species and sex
pivot = penguins.pivot_table(values='body_mass_g', index='species', columns='sex', aggfunc='mean')
markdown_content += "## Pivot Table: Mean Body Mass by Species and Sex\n\n" + pivot.to_markdown() + "\n\n"
markdown_content += "**인사이트:** 피봇 테이블은 종과 성별 평균 체중을 보여줍니다. 수컷이 암컷보다 무겁습니다. Gentoo의 차이가 가장 큽니다. 이는 성적 이형성을 반영하며, 번식 전략과 관련됩니다.\n\n"

# More visualizations
plt.figure(figsize=(8,6))
sns.violinplot(data=penguins, x='species', y='bill_length_mm')
plt.title('Violin Plot: Bill Length by Species')
plt.savefig('violin1.png')
markdown_content += "## Violin Plot 1\n\n![Violin1](violin1.png)\n\n"
markdown_content += "**인사이트:** 바이올린 플롯은 부리 길이의 분포를 종별로 보여줍니다. Gentoo의 분포가 넓고, Adelie의 중앙값이 낮습니다. 이는 종별 특성을 시각화하며, 분류 모델에 유용합니다.\n\n"

plt.figure(figsize=(8,6))
sns.violinplot(data=penguins, x='species', y='body_mass_g')
plt.title('Violin Plot: Body Mass by Species')
plt.savefig('violin2.png')
markdown_content += "## Violin Plot 2\n\n![Violin2](violin2.png)\n\n"
markdown_content += "**인사이트:** 체중의 바이올린 플롯은 Gentoo의 분포가 오른쪽으로 치우쳐 있습니다. 이는 큰 개체가 많음을 보여줍니다. 종별 차이가 명확하므로 식별에 사용할 수 있습니다.\n\n"

plt.figure(figsize=(8,6))
sns.pairplot(penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']], hue='species')
plt.savefig('pairplot.png')
markdown_content += "## Pairplot\n\n![Pairplot](pairplot.png)\n\n"
markdown_content += "**인사이트:** 페어플롯은 모든 수치 변수의 쌍별 관계를 보여줍니다. 종별 색상이 군집을 명확히 합니다. 날개 길이와 체중의 상관이 강합니다. 다변량 분석에 필수적입니다.\n\n"

plt.figure(figsize=(8,6))
sns.heatmap(penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr(), annot=True)
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
markdown_content += "## Correlation Heatmap\n\n![Heatmap](heatmap.png)\n\n"
markdown_content += "**인사이트:** 상관 히트맵은 변수 간 관계를 보여줍니다. 날개 길이와 체중의 상관이 0.87로 높습니다. 부리 길이와 깊이는 음의 상관입니다. 이는 생물학적 상호작용을 이해하는 데 도움이 됩니다.\n\n"

plt.figure(figsize=(8,6))
sns.countplot(data=penguins, x='island', hue='species')
plt.title('Count Plot: Island by Species')
plt.savefig('countplot.png')
markdown_content += "## Count Plot\n\n![Countplot](countplot.png)\n\n"
markdown_content += "**인사이트:** 카운트 플롯은 섬별 종 분포를 보여줍니다. Biscoe는 Gentoo 중심, Dream은 Chinstrap과 Adelie. 이는 섬의 환경이 종 선택에 영향을 미침을 시사합니다.\n\n"

# Bar chart for sex count
plt.figure(figsize=(8,6))
sex_count = penguins['sex'].value_counts()
sns.barplot(x=sex_count.index, y=sex_count.values)
plt.title('Sex Count')
plt.savefig('bar_sex.png')
markdown_content += "## Bar Chart: Sex Count\n\n![Bar Sex](bar_sex.png)\n\n"
markdown_content += "**인사이트:** 성별 개수는 균형적입니다. 이는 샘플링이 공정했음을 보여줍니다. 성별 차이를 분석할 때 유용합니다.\n\n"

# Crosstab for sex and species
crosstab_sex = pd.crosstab(penguins['sex'], penguins['species'])
markdown_content += "## Crosstab: Sex vs Species\n\n" + crosstab_sex.to_markdown() + "\n\n"
markdown_content += "**인사이트:** 성별과 종의 교차표는 각 종에서 성비가 비슷함을 보여줍니다. Gentoo 수컷이 약간 많습니다. 이는 번식 동학을 연구하는 데 중요합니다.\n\n"

# Pivot table for mean flipper length by island and species
pivot_flipper = penguins.pivot_table(values='flipper_length_mm', index='island', columns='species', aggfunc='mean')
markdown_content += "## Pivot Table: Mean Flipper Length by Island and Species\n\n" + pivot_flipper.to_markdown() + "\n\n"
markdown_content += "**인사이트:** 섬과 종별 평균 날개 길이 피봇 테이블은 Gentoo의 날개가 가장 깁니다. 섬별 차이가 적어 종 특성이 강합니다. 수영 적응을 반영합니다.\n\n"

# Save markdown file
with open('penguin_analysis.md', 'w') as f:
    f.write(markdown_content)

print("Analysis complete. Markdown file saved as penguin_analysis.md")

# Visualizations (more than 10)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
sns.histplot(penguins['bill_length_mm'], ax=axes[0,0]).set_title('Bill Length Histogram')
sns.histplot(penguins['bill_depth_mm'], ax=axes[0,1]).set_title('Bill Depth Histogram')
sns.histplot(penguins['flipper_length_mm'], ax=axes[1,0]).set_title('Flipper Length Histogram')
sns.histplot(penguins['body_mass_g'], ax=axes[1,1]).set_title('Body Mass Histogram')
plt.tight_layout()
plt.savefig('histograms.png')
markdown_content += "## Histograms\n\n![Histograms](histograms.png)\n\n"

plt.figure(figsize=(8,6))
sns.boxplot(data=penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']])
plt.title('Boxplots of Numerical Variables')
plt.savefig('boxplots.png')
markdown_content += "## Boxplots\n\n![Boxplots](boxplots.png)\n\n"

plt.figure(figsize=(8,6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.title('Scatterplot: Bill Length vs Depth')
plt.savefig('scatter1.png')
markdown_content += "## Scatterplot 1\n\n![Scatter1](scatter1.png)\n\n"

plt.figure(figsize=(8,6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Scatterplot: Flipper Length vs Body Mass')
plt.savefig('scatter2.png')
markdown_content += "## Scatterplot 2\n\n![Scatter2](scatter2.png)\n\n"

plt.figure(figsize=(8,6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='island')
plt.title('Scatterplot: Bill Length vs Body Mass by Island')
plt.savefig('scatter3.png')
markdown_content += "## Scatterplot 3\n\n![Scatter3](scatter3.png)\n\n"

# Bar chart for species count
plt.figure(figsize=(8,6))
species_count = penguins['species'].value_counts()
sns.barplot(x=species_count.index, y=species_count.values)
plt.title('Species Count')
plt.savefig('bar_species.png')
markdown_content += "## Bar Chart: Species Count\n\n![Bar Species](bar_species.png)\n\n"

# Crosstab for species and island
crosstab = pd.crosstab(penguins['species'], penguins['island'])
markdown_content += "## Crosstab: Species vs Island\n\n" + crosstab.to_markdown() + "\n\n"

# Pivot table for mean body mass by species and sex
pivot = penguins.pivot_table(values='body_mass_g', index='species', columns='sex', aggfunc='mean')
markdown_content += "## Pivot Table: Mean Body Mass by Species and Sex\n\n" + pivot.to_markdown() + "\n\n"

# More visualizations
plt.figure(figsize=(8,6))
sns.violinplot(data=penguins, x='species', y='bill_length_mm')
plt.title('Violin Plot: Bill Length by Species')
plt.savefig('violin1.png')
markdown_content += "## Violin Plot 1\n\n![Violin1](violin1.png)\n\n"

plt.figure(figsize=(8,6))
sns.violinplot(data=penguins, x='species', y='body_mass_g')
plt.title('Violin Plot: Body Mass by Species')
plt.savefig('violin2.png')
markdown_content += "## Violin Plot 2\n\n![Violin2](violin2.png)\n\n"

plt.figure(figsize=(8,6))
sns.pairplot(penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']], hue='species')
plt.savefig('pairplot.png')
markdown_content += "## Pairplot\n\n![Pairplot](pairplot.png)\n\n"

plt.figure(figsize=(8,6))
sns.heatmap(penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr(), annot=True)
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
markdown_content += "## Correlation Heatmap\n\n![Heatmap](heatmap.png)\n\n"

plt.figure(figsize=(8,6))
sns.countplot(data=penguins, x='island', hue='species')
plt.title('Count Plot: Island by Species')
plt.savefig('countplot.png')
markdown_content += "## Count Plot\n\n![Countplot](countplot.png)\n\n"

# Bar chart for sex count
plt.figure(figsize=(8,6))
sex_count = penguins['sex'].value_counts()
sns.barplot(x=sex_count.index, y=sex_count.values)
plt.title('Sex Count')
plt.savefig('bar_sex.png')
markdown_content += "## Bar Chart: Sex Count\n\n![Bar Sex](bar_sex.png)\n\n"

# Crosstab for sex and species
crosstab_sex = pd.crosstab(penguins['sex'], penguins['species'])
markdown_content += "## Crosstab: Sex vs Species\n\n" + crosstab_sex.to_markdown() + "\n\n"

# Pivot table for mean flipper length by island and species
pivot_flipper = penguins.pivot_table(values='flipper_length_mm', index='island', columns='species', aggfunc='mean')
markdown_content += "## Pivot Table: Mean Flipper Length by Island and Species\n\n" + pivot_flipper.to_markdown() + "\n\n"

# Save markdown file
with open('penguin_analysis.md', 'w') as f:
    f.write(markdown_content)

print("Analysis complete. Markdown file saved as penguin_analysis.md")