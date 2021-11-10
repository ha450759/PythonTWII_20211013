import math

if __name__ == '__main__':
    r = 123
    # 求出圓面積與球體積 (利用 math api 取的圓周率)
    # 結果印出小數點第二位
    area = math.pow(r, 2) * math.pi
    volume = 4/3 * math.pow(r, 3) * math.pi
    print('圓面積=%.2f' % area)
    print('球體機=%.2f' % volume)
    # 若要加上千分位
    print(area, type(area))
    print('%.2f' % area)
    print(format(float('%.2f' % area), ","))
    # area = format(area, ",")
    # print(area, type(area))

