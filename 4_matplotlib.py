# 파이썬 표준 시각화 도구 matplotlib - 아름다운 스타일링, 다양한 그래프
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import platform
from matplotlib import font_manager, rc

# matplotlib 한글 폰트 깨짐 현상 해결 - windows에서 제공하는 font를 넣어줘야함
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

# matplotlib 마이너스 깨짐 현상 해결
matplotlib.rcParams['axes.unicode_minus'] = False

# 밑그림그리기 - 단일 그래프
data = np.arange(1, 100)
plt.plot(data)

# 그래프 보여주기
plt.show()

# 밑그림그리기 - 다중 그래프
data1 = np.arange(1, 51)
data2 = np.arange(51, 101)

plt.plot(data1)
plt.plot(data2)
# 새로운 캔버스를 만들어서 그래프를 새로 그리고 싶을 때
plt.figure()
plt.plot(data2+50)

plt.show()

# 여러개의 plot을 그리는 방법(subplot)
data = np.arange(100, 201)
# 행에 2개가 표현되고, 열에는 1개, 그중에 첫번째 인덱스
plt.subplot(2, 1, 1) # 콤마 제거해도 가능
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(2, 1, 2)
plt.plot(data2)

# 여러개의 plot을 그리는 방법(subplot+s)
data = np.arange(1, 51)

# 미리 6개짜리 plot 생성
fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(data)
axes[0, 1].plot(data * data)
axes[0, 2].plot(data ** 3)
axes[1, 0].plot(data % 10)
axes[1, 1].plot(-data)
axes[1, 2].plot(data // 20)

plt.tight_layout()
plt.show()