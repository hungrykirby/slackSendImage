import matplotlib.pyplot as plt
import numpy as np
from os.path import join, dirname
import os

class GraphGenerator:
  label_x = "x"
  label_y = "y"
  fig = None
  title = None
  file_name = None
  def __init__(self, title, file_name):
    self.title = title
    self.file_name = file_name

  def set_labels(self, label_x, label_y):
    self.label_x = label_x
    self.label_y = label_y

  def create_pressure_graph(self, x, y):
    plt.title(self.title)
    plt.xlabel(self.label_x)
    plt.ylabel(self.label_y)
    plt.ylim(850, 1250)
    plt.plot(x, y)
    rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    plt.savefig(join(rootdir, 'imgs', self.file_name))
    # plt.show()

