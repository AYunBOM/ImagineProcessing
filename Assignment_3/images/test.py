
import numpy as np, cv2

# 3행 6열의 행렬을 생성하고
ch = [ [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6] ]

# 행렬의 원소를 초기화한 후에(10으로 초기화)
ch = np.full((3, 6), 10, np.uint8)

# cv2.reduce() 함수를 이용해서 가로 방향으로 감축하여 평균 구한 결과를 출력
ch1 = cv2.reduce(ch, dim=1, rtype=cv2.REDUCE_AVG)
print("[%s] = \n%s \n" % ('ch1', ch1))

# cv2.reduce() 함수를 이용해서 세로 방향으로 감축하여 평균 구한 결과를 출력
ch2 = cv2.reduce(ch, dim=0, rtype=cv2.REDUCE_AVG)
print("[%s] = \n%s \n" % ('ch2', ch2))