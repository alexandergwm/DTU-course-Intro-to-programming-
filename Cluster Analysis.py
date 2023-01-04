### Cluster analysis
# Given a set of N measurements, (r1, r2, . . . , rN ), we will initially assign the odd-numbered measurements to
# class 1 and the even numbered measurements to class 2. Then the following two steps are repeated:
# Update step: Compute the mean value (average) of the measurements within each cluster.
# Assignment step: Assign each measurement to the cluster with the closest mean value. In case of a tie,
# assign the measurement to cluster 1.
# Repeat the above steps until the cluster assignments do not change. It can not be determined in advance how
# many steps will be needed before the clustering assignment stabilizes
import numpy as np
def clusterAnalysis(reflectance):
    # 先根据奇偶来做第一次分组
    n = len(reflectance)  # 获取数组的总长
    gp1 = np.zeros(n)
    gp2 = np.zeros(n)
    for i in range(n):
        if i % 2 != 0:
            gp2[i] = reflectance[i]
        else:
            gp1[i] = reflectance[i]
    gp1 = gp1[gp1!=0]
    gp2 = gp2[gp2!=0]
    # 第一次分组完毕，之后要根据分配是否相同来结束循环
    while True:
        m1 = np.mean(gp1)
        m2 = np.mean(gp2)
        index1 = np.zeros(len(reflectance))
        index2 = np.zeros(len(reflectance))
        # 先计算原始数组中每个值分别与两个簇的差距
        diff1 = reflectance - m1
        diff2 = reflectance - m2
        for j in range(0,len(diff1)):
            if np.abs(diff1[j]) <= np.abs(diff2[j]):
                index1[j] = 1
            else:
                index2[j] = 1
        # 现在已经知道了在下一个分好后的簇内的元素对应的index了
        index = index1 + 2* index2
        for k in range(0,len(reflectance)):
            if index[k] == 2:
                gp2 = reflectance[index == 2]
            elif index[k] == 1:
                gp1 = reflectance[index == 1]
        m3 = np.mean(gp1)
        m4 = np.mean(gp2)
        if m1 == m3 and m2 == m4:
             clusterAssignments = index
             return clusterAssignments


