from pandas.core.indexing import _iLocIndexer
import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv('data/iris.csv')


    # 버튼(button)로 대소문자 변경

    # if st.button('데이터 보기'):
    #     st.dataframe(df)
    
    # name = 'Mike'

    # if st.button('대문자로'):
    #     st.write(name.upper())
    # if st.button('소문자로'):
    #     st.write(name.lower())


    # 체크박스(radio)로 정렬하기!!!

    st.dataframe(df)
    status = st.radio('정렬을 선택하세요.',['오름차순정렬','내림차순정렬'])
    if status == '오름차순정렬':
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순정렬':
        st.dataframe(df.sort_values('petal_length',ascending=False))

    if st.checkbox('show / hide'):
        st.dataframe(df.head())
    else :
        st.write('데이터가 없습니다.')

    language = ['Python','C','Java','Go']
    my_choice = st.selectbox('좋아하는 언어를 선택하세요',language)
    if my_choice =='C':
        st.write('저는 C가 좋아요')
    elif my_choice =='Python':
        st.write('파이썬이 최고당')

    choice_list = st.multiselect('여러개를 선택할 수 있습니다.',language)
    # 디버깅을 하고 싶으면 파이썬의 print 함수를 이용하면 아래의 터미널에 출력이 된다.
    print(choice_list)

    iris_choice = st.multiselect('컬럼을 선택하세요',df.columns)
    print(iris_choice)
    print(df[iris_choice])
    st.dataframe(df[iris_choice])

    age = st.slider('나이',1,100)
    st.slider('10단위 스탭',1,100,step=10)
    st.slider('기본값 설정',1,100,value=30)

    st.write('선택한 나이는 {}살 입니다'.format(age))

    with st.expander('Hello'):
        st.text('안녕하세요')











if __name__ == '__main__':
    main()

