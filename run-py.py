# python js.py <문제번호>
# 1. 문제번호 폴더의 py.py 실행
# 2. inout/<문제번호>-in-*을 넣고 프로그램의 출력과 inout/<문제번호>-out-* 대조
import os
import sys

probNumber = sys.argv[1]
print("문제번호: "+probNumber)
if not probNumber.isnumeric():
    print("숫자가 아님")
    exit()

os.chdir(os.path.dirname(__file__))

if not os.path.isdir(probNumber):
    print(probNumber, "폴더 존재 안함")
    exit()

inoutdir = os.path.join(os.getcwd(), "inout")
if not os.path.exists(inoutdir):
    print("inout 폴더 없음")
    exit()

for i in range(1, 10):
    inf = os.path.join(inoutdir, probNumber+"-in-"+str(i))
    outf = os.path.join(inoutdir, probNumber+"-out-"+str(i))
    if not os.path.exists(inf):
        break

    print("-------------------------- 예제 " +
          str(i)+" --------------------------")
    print("---------- 예상 ----------")
    os.system("cat "+outf)
    print("\n---------- 결과 ----------")
    os.system("cat "+inf + "| python " + probNumber+"/py.py")
