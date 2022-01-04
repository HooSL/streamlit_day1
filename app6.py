# from google.protobuf import message
import streamlit as st

def main():
    
    #작성값 출력
    name = st.text_input('이름을 입력하세요. : ')
    st.title(name)

    #글자수 최대값
    name2 = st.text_input('이름을 입력하세요. : ',max_chars=5)
    st.title(name2)

    #긴글 height=3은 3줄만 나온다
    message = st.text_area('메세지를 입력하세요',height=3)
    st.text(message)

    #숫자입력 뒤에 1과 100은 min max값
    number = st.number_input('숫자를 입력하세요',1,100)
    st.text(number)

    #실수입력
    number2 = st.number_input('숫자를 입력하세요',0.0,20.0)
    st.text(number2)

    #날짜 입력
    my_date = st.date_input('약속 날짜 입력')
    st.write(my_date)
    #print문은 디버깅용 터미널에 나온다
    print(my_date)

    #시간
    my_time = st.time_input('시간 선택')
    st.write(my_time)

    #비밀번호 입력
    password = st.text_input('비밀번호 입력',type='password',max_chars=12)
    st.write(password)

    #색깔 입력
    color = st.color_picker('색을 선택하세요')
    st.write(color)



if __name__ == '__main__':
    main()