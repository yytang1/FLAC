#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
def main(argv):
    #filename = "C:\\Users\\yytang\\Desktop\\flac_music\\test1_2.ana"
    filename = str(sys.argv[1])
    print(filename)
    file1 = open(filename)
    count = 0
    MSB_max = 0
    num_10 = 0
    num_20 = 0
    num_30 = 0
    num_40 = 0
    num_50 = 0
    num_60 = 0
    num_60_100 = 0
    num_100_150 = 0
    num_150 = 0

    for line in file1:
        # print(line)
        count += 1
        if(len(line) >= 2):
            m = int(line[0:-1])
            if(MSB_max < m):
                MSB_max = m
            # 统计数据
            if(m < 10):
                num_10 += 1
            elif m < 20:
                num_20 += 1
            elif (m < 30):
                num_30 += 1
            elif (m < 40):
                num_40 += 1
            elif (m < 50):
                num_50 += 1
            elif (m < 60):
                num_60 += 1
            elif (m < 100):
                num_60_100 += 1
            elif (m < 150):
                num_100_150 += 1
            else:
                num_150 += 1
        # if(count >= 100000):
            # break
    filenameresult = filename[:-4] + "result.txt"
    file_write = open(filenameresult, 'w')
    all_the_text = "sum counts:" + str(count) + "\n"
    all_the_text += "MSB_max:" + str(MSB_max) + "\n"
    all_the_text += "[0,10): %d \t percentage: %.5f %% \n" % (
        num_10, num_10 / count)
    all_the_text += "[10,20): %d \t percentage: %.5f %% \n" % (
        num_20, num_20 / count)
    all_the_text += "[20,30): %d \t percentage: %.5f %% \n" % (
        num_30, num_30 / count)
    all_the_text += "[30,40): %d \t percentage: %.5f %% \n" % (
        num_40, num_40 / count)
    all_the_text += "[40,50): %d \t percentage: %.5f %% \n" % (
        num_50, num_50 / count)
    all_the_text += "[50,60): %d \t percentage: %.5f %% \n" % (
        num_60, num_60 / count)
    all_the_text += "[60,100): %d \t percentage: %.5f %% \n" % (
        num_60_100, num_60_100 / count)
    all_the_text += "[100,150): %d \t percentage: %.5f %% \n" % (
        num_100_150, num_100_150 / count)
    all_the_text += "[150,+): %d \t percentage: %.5f %% \n" % (
        num_150, num_150 / count)
    all_the_text += "MAX: %d\n" % MSB_max
    file_write.write(all_the_text)
    file_write.close()
    print(count)
    print(MSB_max)
if __name__ == "__main__":
   main(sys.argv[1:])