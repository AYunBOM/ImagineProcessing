import numpy as np, cv2, math, time

start = time.time()
def print_rects(rects, area):
    print("\n" + "-" * 46 + "\n사각형 원소\t\t랜덤 사각형 정보\t\t   넓이\n" + "-" * 46)
    for i, data in zip(range(10), rects):
        print("rects[%d] = [(%3d,%3d) from (%3d,%3d)] %5d" % (i, data[0], data[1], data[2], data[3], data[4]))

    print("\n" + "-" * 46 + "\n사각형 원소\t\t랜덤 사각형 정보\t\t   넓이\n" + "-" * 46)
    for i, data in zip(np.argsort(area, axis=0)[::-1],sorted(rects, key=lambda x:x[-1], reverse=True)):
        print("rects[%d] = [(%3d,%3d) from (%3d,%3d)] %5d" % (i, data[0], data[1], data[2], data[3], data[4]))

rands = np.zeros((10000, 5), np.uint16)
starts, ends = cv2.randn(rands[:, :2 ], 100, 50), cv2.randn(rands[:, 2:-1], 300, 50)
sizes = cv2.absdiff(starts, ends)

areas, rects = sizes[:, 0] * sizes[:, 1], rands.copy()
rects[:, 2:-1], rects[:,-1]= sizes, areas

print_rects(rects, areas)
end = time.time()

print(f"실행속도:{end-start: .2f}sec")







