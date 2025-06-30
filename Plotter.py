import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class LivePlotter:
    def __init__(self, xlabel='Time (s)', ylabel='Value', title='Live Plot'):
        self.x_data = []
        self.y_data = []

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)

        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

        self.ax.set_xlim(0, 10)   # 초기 X 범위
        self.ax.set_ylim(0, 1)    # 초기 Y 범위

        # ⚡ 애니메이션은 속성에 꼭 저장!
        self.ani = FuncAnimation(
            self.fig,
            self._update_plot,
            interval=100,
            cache_frame_data=False   # 경고 방지!
        )

    def update(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)

    def _update_plot(self, frame):
        self.line.set_data(self.x_data, self.y_data)

        if self.x_data:
            xmin, xmax = self.ax.get_xlim()
            ymin, ymax = self.ax.get_ylim()

            if self.x_data[-1] > xmax:
                self.ax.set_xlim(0, self.x_data[-1] + 5)

            if max(self.y_data) > ymax:
                self.ax.set_ylim(0, max(self.y_data) * 1.1)

        return self.line,

    def show(self):
        plt.show()
