import streamlit as st
import pandas as pd
from PIL import Image


#크롬 위에 인터넷창 이름과 아이콘 변경 
img = Image.open('data/image_03.jpg')
st.set_page_config(page_title='Machine Learning',page_icon=img,layout='wide',initial_sidebar_state='collapsed')

def main():
    pass


if __name__ == '__main__':
    main()