from audioop import add
import numpy as np

class Croos_Correlation_Calculator:
  def __init__(self, feature_map, kernel, Stride=1, Padding=0):
    self.feature_map = feature_map
    self.kernel = kernel
    self.I = len(feature_map)
    self.K = len(kernel)
    self.S = Stride
    self.P = Padding
    self.O = int(((self.I - self.K + (2 * self.P)) / self.S) + 1)
    self.new_feature_map = np.zeros((self.O, self.O))
    self.validation()
    self.add_padding()

  def add_padding(self):
    added_feature_map = np.zeros(((self.I + (2 * self.P)), (self.I + (2 * self.P))))

    # feature_map에 padding을 추가한다.
    ## feature_map + padding*2 만큼 사이즈를 키운 added_feature_map에 feature_map을 P+1만큼 이동하여 feature_map을 덮어쓴다
    for i in range(self.I):
      for j in range(self.I):
        added_feature_map[i+self.P][j+self.P] = feature_map[i][j]

    self.feature_map = added_feature_map.copy()

  def validation(self):
    # 정방행렬 확인
    if len(self.feature_map) != len(self.feature_map[0]):
      raise Exception("정방행렬이 아닙니다.")

    # Check if calculations are possible
    ## O, Output size  / I, Input size
    ## P, Padding size / S, Stride size
    ### O = (I - K + 2P / S) + 1
  
  def Calculation(self):
    for i in range(self.O):
      for j in range(self.O):

        kernel_sum = 0
        kernel_row = 0

        for n in range(i, i + self.K):
          index = 0
          kernel_column = 0

          for m in range(j, j + self.K):
            kernel_sum += self.feature_map[n][m] * self.kernel[kernel_row][kernel_column]
            kernel_column += 1

          kernel_row += 1

        self.new_feature_map[i][j] = kernel_sum

    return self.new_feature_map

if __name__== "__main__":
  
  feature_map = np.array([[2, 8, 3, 7, 1, 2, 0, 4, 5], 
                          [6, 4, 9, 6, 7, 1, 7, 7, 2], 
                          [7, 9, 9, 1, 5, 2, 5, 1, 5], 
                          [2, 9, 6, 4, 4, 1, 3, 6, 3],
                          [2, 10, 1, 8, 9, 4, 4, 5, 4],
                          [5, 10, 1, 5, 1, 4, 10, 10, 6],
                          [9, 2, 10, 3, 5, 5, 4, 7, 10],
                          [8, 4, 3, 6, 4, 2, 8, 5, 5],
                          [6, 1, 6, 6, 9, 3, 1, 10, 3]])

  kernel = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])

  VALID = Croos_Correlation_Calculator(feature_map=feature_map, kernel=kernel, Padding=1)
  VALID_feature_map = VALID.Calculation()
  print(VALID_feature_map)

