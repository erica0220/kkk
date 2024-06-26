import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# Streamlit 페이지 설정
st.set_page_config(page_title='범죄 관련 통계', layout='wide')

font_path = 'fonts/NanumGothic.ttf'
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
sns.set(font=font_prop.get_name(), rc={"axes.unicode_minus": False}, style='white')

def load_data():
    data_weekday_crime = pd.read_csv('경찰청_범죄 발생 시간대 및 요일_20191231.csv', encoding='cp949')
    data_cyber_crime = pd.read_csv('경찰청_연도별 사이버 범죄 통계 현황_08_31_2020.csv', encoding='cp949')
    data_area_crime = pd.read_csv('경찰청_범죄 발생 지역별 통계_20221231.csv', encoding='cp949')
    df_knife = pd.read_csv('칼부림.csv', encoding='cp949')
    return data_weekday_crime, data_cyber_crime, data_area_crime, df_knife

data_weekday_crime, data_cyber_crime, data_area_crime, df_knife = load_data()

# 사이드바 설정
st.sidebar.title("범죄 관련 통계")
option = st.sidebar.selectbox("범죄에 대한 다양한 통계 알아보기",
                              ("요일별 범죄 분포", "시간대별 범죄 분포", "사이버 범죄", "지역별 범죄 분포", "칼부림 통계"))

if option == "요일별 범죄 분포":
    st.title("요일별 범죄 분포")
    fig, ax = plt.subplots()
    data_weekday_crime[data_weekday_crime.columns[2:9]].sum().plot(kind='bar', color='skyblue', ax=ax)
    ax.set_xlabel('Weekday')
    ax.set_ylabel('Total Crimes')
    st.pyplot(fig)

elif option == "시간대별 범죄 분포":
    st.title("시간대별 범죄 분포")
    fig, ax = plt.subplots()
    data_weekday_crime[data_weekday_crime.columns[9:17]].sum().plot(kind='bar', color='coral', ax=ax)
    ax.set_xlabel('Time Slot')
    ax.set_ylabel('Total Crimes')
    st.pyplot(fig)

elif option == "사이버 범죄":
    st.title("사이버 범죄")
    fig, ax = plt.subplots()
    data_cyber_crime[data_cyber_crime['구분'] == '발생건수'].drop(columns=['연도', '구분']).sum(axis=1).plot(kind='line', marker='o', color='purple', ax=ax)
    ax.set_xticklabels(data_cyber_crime['연도'].unique())
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Cyber Crimes')
    st.pyplot(fig)

elif option == "지역별 범죄 분포":
    st.title("지역별 범죄 분포")
    fig, ax = plt.subplots()
    data_area_crime[data_area_crime.columns[2:10]].sum().plot(kind='bar', color='green', ax=ax)
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Crimes')
    st.pyplot(fig)

elif option == "칼부림 통계":
    st.title("칼부림 통계")
    sorted_df = df_knife.nlargest(10, '칼부림')
    fig, ax = plt.subplots()
    sns.barplot(data=sorted_df, x='지역', y='칼부림', ax=ax, palette='viridis')
    ax.set_xlabel('Region')
    ax.set_ylabel('Number of Incidents')
    ax.set_xticklabels(ax.get_xticklabels(),rotation = 45, fontproperties=font_prop)
    st.pyplot(fig)
    sorted_df_threats = df_knife.nlargest(10, '칼부림 예고')
    fig, ax = plt.subplots()
    sns.barplot(data=sorted_df_threats, x='지역', y='칼부림 예고', ax=ax, palette='magma')
    ax.set_xlabel('Region')
    ax.set_ylabel('Number of Threats')
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, fontproperties=font_prop)
    st.pyplot(fig)

