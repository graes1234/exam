#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20212011 이름 : 김은채

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    if target in my_string: #my_string 안에 target이 존재한다면
        answer = 1 # answer = 1(true)
    else:                   #그렇지 않다면
        answer = 0 # answer = 0(false)
    return answer

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution2(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''                 #answer 먼저 정의
    list = letter.split()       #공백으로 letter를 나눠 리스트로 한 문자씩 모스부호로 저장
    for a in list:              #list 안의 인덱스 0의 값을 차례대로 a에 대입
        answer += morse.get(a)  #morse.get()을 이용해 value값과 a를 비교, answer에 저장
    return answer

    # letter = ".. ..-. -.-- --- ..- -.-. --- -- . .- - ..-. --- ..- .-. .. -. - .... . .- ..-. - . .-. -. --- --- -. .. .-- .. .-.. .-.. -... . --. .. -. - --- -... . .... .- .--. .--. -.-- -... -.-- - .... .-. . ."

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution3(age):
    PROGRAMMERS = { '0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    for i in age : #age의 값을 i에 대입
        if i == PROGRAMMERS.keys(i) : #i와 keys값이 같다면
            answer += PROGRAMMERS.values(i) #answer에 values 값을 저장
    return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution4(r1, r2):
    answer = (r2 - r1 + 1)*4  # {r2-r1+1(원 위의 점을 포함하기 위해 1을 더해줌)} x4(4개의 좌표면이 있기 때문에)
    return answer

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution5(numbers):
    from itertools import permutations          #n개 중에 n개를 뽑아 나열하는 경우의 수를 알기 위해 itertools 모듈의 permutations을 활용
    for i in permutations(numbers, len(numbers)):  #numbers에 있는 리스트에 리스트 길이만큼 뽑아 나열하는 순열 permutations의 모든 경우의 수를 차례대로 i에 대입
        str_list = list(map(str, i))             #정수 리스트를 문자열 리스트로 변경
        print(str_list)
        for s in str_list:    #list 요소를 s에 대입
            a=+ s     #문자열을 더해서 a에 저장
