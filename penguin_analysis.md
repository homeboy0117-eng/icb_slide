# Penguin Dataset Analysis

## Dataset Overview

|    | species   | island    |   bill_length_mm |   bill_depth_mm |   flipper_length_mm |   body_mass_g | sex    |
|---:|:----------|:----------|-----------------:|----------------:|--------------------:|--------------:|:-------|
|  0 | Adelie    | Torgersen |             39.1 |            18.7 |                 181 |          3750 | Male   |
|  1 | Adelie    | Torgersen |             39.5 |            17.4 |                 186 |          3800 | Female |
|  2 | Adelie    | Torgersen |             40.3 |            18   |                 195 |          3250 | Female |
|  4 | Adelie    | Torgersen |             36.7 |            19.3 |                 193 |          3450 | Female |
|  5 | Adelie    | Torgersen |             39.3 |            20.6 |                 190 |          3650 | Male   |

**인사이트:** 이 데이터셋은 펭귄의 종, 섬, 부리 길이, 깊이, 날개 길이, 체중, 성별을 포함합니다. 총 333개의 유효 데이터로, Adelie, Chinstrap, Gentoo 세 종의 펭귄을 분석할 수 있습니다. 데이터는 남극의 세 섬에서 수집되었으며, 생물 다양성과 환경적 요인을 연구하는 데 유용합니다.

## Descriptive Statistics

|       |   bill_length_mm |   bill_depth_mm |   flipper_length_mm |   body_mass_g |
|:------|-----------------:|----------------:|--------------------:|--------------:|
| count |        333       |       333       |            333      |       333     |
| mean  |         43.9928  |        17.1649  |            200.967  |      4207.06  |
| std   |          5.46867 |         1.96924 |             14.0158 |       805.216 |
| min   |         32.1     |        13.1     |            172      |      2700     |
| 25%   |         39.5     |        15.6     |            190      |      3550     |
| 50%   |         44.5     |        17.3     |            197      |      4050     |
| 75%   |         48.6     |        18.7     |            213      |      4775     |
| max   |         59.6     |        21.5     |            231      |      6300     |

**인사이트:** 평균 부리 길이는 44mm, 체중은 4200g 정도입니다. 표준편차가 크므로 개체 간 변이가 큽니다. 최소/최대 값의 차이가 커서 종별 차이를 예상할 수 있습니다. 이는 펭귄의 생태적 적응을 반영합니다.

## Histograms

![Histograms](histograms.png)

**인사이트:** 히스토그램은 각 변수의 분포를 보여줍니다. 부리 길이와 깊이는 정규분포에 가까우며, 날개 길이와 체중은 약간 오른쪽으로 치우쳐 있습니다. 이는 Gentoo 종의 큰 체구가 영향을 미칠 수 있습니다. 분포 분석을 통해 이상치를 식별할 수 있습니다.

## Boxplots

![Boxplots](boxplots.png)

**인사이트:** 박스플롯은 중앙값과 분산을 시각화합니다. 체중의 분산이 가장 크며, 날개 길이는 상대적으로 균일합니다. 이상치가 보이므로 특정 개체의 특성을 조사할 필요가 있습니다. 종별 비교 시 유용합니다.

## Scatterplot 1

![Scatter1](scatter1.png)

**인사이트:** 부리 길이와 깊이의 산점도는 종별 군집을 보여줍니다. Adelie는 작은 부리, Gentoo는 큰 부리를 가집니다. 이는 먹이 습성과 관련될 수 있습니다. 상관관계가 약하므로 다른 요인이 영향을 미칠 수 있습니다.

## Scatterplot 2

![Scatter2](scatter2.png)

**인사이트:** 날개 길이와 체중의 산점도는 강한 양의 상관관계를 보입니다. Gentoo가 가장 크고, Adelie가 작습니다. 이는 체구가 큰 펭귄이 더 긴 날개를 가짐을 시사합니다. 수영 능력과 관련된 생태적 적응입니다.

## Scatterplot 3

![Scatter3](scatter3.png)

**인사이트:** 섬별로 본 부리 길이와 체중의 분포는 환경 차이를 반영합니다. Biscoe 섬의 Gentoo가 크고, Dream의 Chinstrap이 중간입니다. 섬의 기후와 먹이원이 펭귄의 크기에 영향을 미칠 수 있습니다.

## Bar Chart: Species Count

![Bar Species](bar_species.png)

**인사이트:** 종별 개수는 Gentoo가 가장 많고, Chinstrap이 적습니다. 이는 섬별 분포와 관련됩니다. 데이터 불균형이 분석에 영향을 줄 수 있으므로 가중치를 고려해야 합니다.

## Crosstab: Species vs Island

| species   |   Biscoe |   Dream |   Torgersen |
|:----------|---------:|--------:|------------:|
| Adelie    |       44 |      55 |          47 |
| Chinstrap |        0 |      68 |           0 |
| Gentoo    |      119 |       0 |           0 |

**인사이트:** 교차표는 종과 섬의 관계를 보여줍니다. Gentoo는 Biscoe에만, Chinstrap은 Dream에만 서식합니다. 이는 생태적 분리가 일어났음을 시사하며, 진화적 다양성을 연구하는 데 중요합니다.

## Pivot Table: Mean Body Mass by Species and Sex

| species   |   Female |    Male |
|:----------|---------:|--------:|
| Adelie    |  3368.84 | 4043.49 |
| Chinstrap |  3527.21 | 3938.97 |
| Gentoo    |  4679.74 | 5484.84 |

**인사이트:** 피봇 테이블은 종과 성별 평균 체중을 보여줍니다. 수컷이 암컷보다 무겁습니다. Gentoo의 차이가 가장 큽니다. 이는 성적 이형성을 반영하며, 번식 전략과 관련됩니다.

## Violin Plot 1

![Violin1](violin1.png)

**인사이트:** 바이올린 플롯은 부리 길이의 분포를 종별로 보여줍니다. Gentoo의 분포가 넓고, Adelie의 중앙값이 낮습니다. 이는 종별 특성을 시각화하며, 분류 모델에 유용합니다.

## Violin Plot 2

![Violin2](violin2.png)

**인사이트:** 체중의 바이올린 플롯은 Gentoo의 분포가 오른쪽으로 치우쳐 있습니다. 이는 큰 개체가 많음을 보여줍니다. 종별 차이가 명확하므로 식별에 사용할 수 있습니다.

## Pairplot

![Pairplot](pairplot.png)

**인사이트:** 페어플롯은 모든 수치 변수의 쌍별 관계를 보여줍니다. 종별 색상이 군집을 명확히 합니다. 날개 길이와 체중의 상관이 강합니다. 다변량 분석에 필수적입니다.

## Correlation Heatmap

![Heatmap](heatmap.png)

**인사이트:** 상관 히트맵은 변수 간 관계를 보여줍니다. 날개 길이와 체중의 상관이 0.87로 높습니다. 부리 길이와 깊이는 음의 상관입니다. 이는 생물학적 상호작용을 이해하는 데 도움이 됩니다.

## Count Plot

![Countplot](countplot.png)

**인사이트:** 카운트 플롯은 섬별 종 분포를 보여줍니다. Biscoe는 Gentoo 중심, Dream은 Chinstrap과 Adelie. 이는 섬의 환경이 종 선택에 영향을 미침을 시사합니다.

## Bar Chart: Sex Count

![Bar Sex](bar_sex.png)

**인사이트:** 성별 개수는 균형적입니다. 이는 샘플링이 공정했음을 보여줍니다. 성별 차이를 분석할 때 유용합니다.

## Crosstab: Sex vs Species

| sex    |   Adelie |   Chinstrap |   Gentoo |
|:-------|---------:|------------:|---------:|
| Female |       73 |          34 |       58 |
| Male   |       73 |          34 |       61 |

**인사이트:** 성별과 종의 교차표는 각 종에서 성비가 비슷함을 보여줍니다. Gentoo 수컷이 약간 많습니다. 이는 번식 동학을 연구하는 데 중요합니다.

## Pivot Table: Mean Flipper Length by Island and Species

| island    |   Adelie |   Chinstrap |   Gentoo |
|:----------|---------:|------------:|---------:|
| Biscoe    |  188.795 |     nan     |  217.235 |
| Dream     |  189.927 |     195.824 |  nan     |
| Torgersen |  191.532 |     nan     |  nan     |

**인사이트:** 섬과 종별 평균 날개 길이 피봇 테이블은 Gentoo의 날개가 가장 깁니다. 섬별 차이가 적어 종 특성이 강합니다. 수영 적응을 반영합니다.

## Histograms

![Histograms](histograms.png)

## Boxplots

![Boxplots](boxplots.png)

## Scatterplot 1

![Scatter1](scatter1.png)

## Scatterplot 2

![Scatter2](scatter2.png)

## Scatterplot 3

![Scatter3](scatter3.png)

## Bar Chart: Species Count

![Bar Species](bar_species.png)

## Crosstab: Species vs Island

| species   |   Biscoe |   Dream |   Torgersen |
|:----------|---------:|--------:|------------:|
| Adelie    |       44 |      55 |          47 |
| Chinstrap |        0 |      68 |           0 |
| Gentoo    |      119 |       0 |           0 |

## Pivot Table: Mean Body Mass by Species and Sex

| species   |   Female |    Male |
|:----------|---------:|--------:|
| Adelie    |  3368.84 | 4043.49 |
| Chinstrap |  3527.21 | 3938.97 |
| Gentoo    |  4679.74 | 5484.84 |

## Violin Plot 1

![Violin1](violin1.png)

## Violin Plot 2

![Violin2](violin2.png)

## Pairplot

![Pairplot](pairplot.png)

## Correlation Heatmap

![Heatmap](heatmap.png)

## Count Plot

![Countplot](countplot.png)

## Bar Chart: Sex Count

![Bar Sex](bar_sex.png)

## Crosstab: Sex vs Species

| sex    |   Adelie |   Chinstrap |   Gentoo |
|:-------|---------:|------------:|---------:|
| Female |       73 |          34 |       58 |
| Male   |       73 |          34 |       61 |

## Pivot Table: Mean Flipper Length by Island and Species

| island    |   Adelie |   Chinstrap |   Gentoo |
|:----------|---------:|------------:|---------:|
| Biscoe    |  188.795 |     nan     |  217.235 |
| Dream     |  189.927 |     195.824 |  nan     |
| Torgersen |  191.532 |     nan     |  nan     |

