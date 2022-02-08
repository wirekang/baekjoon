# python gen.py <문제번호>
# 1. 문제 번호로 폴더 생성 (이미 있으면 중단)
# 2. template 폴더 복사
# 3. inout/<문제번호>-[in/out]-* 에 예제 입출력 저장
import os
import sys
import requests
from bs4 import BeautifulSoup

os.chdir(os.path.dirname(__file__))

probNumber = sys.argv[1]
print("문제번호: "+probNumber)
if not probNumber.isnumeric():
    print("숫자가 아님")
    exit()

if os.path.isdir(probNumber):
    print(probNumber, "폴더 이미 존재")
    exit()
print("폴더 생성")
os.mkdir(probNumber)
os.system("cp template/* " + probNumber)

req = requests.get("https://www.acmicpc.net/problem/"+probNumber)
so = BeautifulSoup(req.text, "html.parser")

ins = []
outs = []

for i in range(1, 10):
    input = so.select_one("#sample-input-"+str(i))
    output = so.select_one("#sample-output-"+str(i))
    if input == None or output == None:
        break

    ins.append(input.text.rstrip())
    outs.append(output.text.rstrip())

print("입출력 " + str(len(ins))+"개")

print("입출력 파일 작성")

inoutdir = os.path.join(os.getcwd(), "inout")
if not os.path.exists(inoutdir):
    os.mkdir(inoutdir)

for i in range(len(ins)):
    f = open(os.path.join(inoutdir, probNumber + "-in-"+str(i+1)), "w")
    f.write(ins[i])
    f.close()

    f = open(os.path.join(inoutdir, probNumber + "-out-"+str(i+1)), "w")
    f.write(outs[i])
    f.close()
