import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def homepage():
    st.write("""
        # Simple Stock Price App
        ### Shown are the stock **closing price** and **volume** of _**Tesla !**_ ###
        #""")

    tickerSymbol = 'TSLA'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-5-31')

    st.line_chart(tickerDf.Close)
def bar_chart():
    Courses = ['ATM', 'INTERNET', 'MOBILE']
    doanhso=[21.9315637, 93.91102985, 100]
    soluong=[29.87804878,  21.95121951, 100]

    fig = plt.figure(figsize = (10, 5))

    plt.bar(Courses, doanhso, color='b')
    plt.xlabel("Programming Environment")
    plt.ylabel("Number of Students")
    plt.title("Students enrolled in different courses")


    st.pyplot(fig)
def soluong():
    Courses = ['ATM', 'INTERNET', 'MOBILE']
    Courses = ['ATM', 'INTERNET', 'MOBILE']
    doanhso = [21.9315637, 93.91102985, 100]
    soluong = [29.87804878, 21.95121951, 100]

    fig = plt.figure(figsize=(10, 5))


    plt.bar(Courses, soluong, color='r')
    plt.xlabel('Loại giao dịch')
    plt.ylabel('Gía trị')
    st.pyplot(fig)

def horizontal_bar_graph():
    #Creating the dataset
    data = {'C':20, 'C++':15, 'Java': 30, 'Python':35}
    Courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize = (10, 5))

    plt.barh(Courses, values)
    plt.xlabel("Number of Students")
    plt.ylabel("Programming Environment")
    plt.title("Students enrolled in different courses")

    st.pyplot(fig)


def scatter_plot():
    # Create numpy array for the visualisation
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

    fig = plt.figure(figsize=(10, 4))
    plt.scatter(x, y)

    st.balloons()
    st.pyplot(fig)
def histogram():
    x = np.random.normal(170, 10, 250)

    fig = plt.figure(figsize=(10, 4))
    plt.hist(x)

    st.balloons()
    st.pyplot(fig)
def pieChart():
    x = np.array([179502250, 768629241, 818465352])
    mylabels = ['ATM', 'INTERNET', 'MOBILE']

    fig = plt.figure(figsize=(10, 4))
    plt.title('Đồ thị thể hiện doanh số giao dịch trong từng kênh ', fontsize=16)

    plt.pie(x, labels=mylabels, autopct='%1.2f%%')

    st.balloons()
    st.pyplot(fig)


def subPlot():
    st.header("Sub Plots")
    st.balloons()
    fig = plt.figure(figsize=(10, 5))

    # Plot 1
    data = {'C': 15, 'C++': 20, 'JavaScript': 30, 'Python': 35}
    Courses = list(data.keys())
    values = list(data.values())

    plt.xlabel("Programming Environment")
    plt.ylabel("Number of Students")

    plt.subplot(1, 2, 1)
    plt.bar(Courses, values)

    # Plot 2
    x = np.array([35, 25, 25, 15])
    mylabels = ["Python", "JavaScript", "C++", "C"]

    plt.subplot(1, 2, 2)
    plt.pie(x, labels=mylabels)

    st.pyplot(fig)



page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "Bar Plot",
            "Horizontal Bar Graph",
            "Scatter Plot",
            "Histogram",
            "Pie Chart",
            "Sub Plot"
        ]
    )

    # First Page
if page == "Homepage":
    homepage()

    # Second Page
elif page == "Bar Plot":
    bar_chart()
    soluong()

    # Third Page
elif page == "Horizontal Bar Graph":
    horizontal_bar_graph()

    # Fourth Page
elif page == "Scatter Plot":
    scatter_plot()

    # Fifth page
elif page == "Histogram":
    histogram()

    # Sixth Page
elif page == "Pie Chart":
    pieChart()

elif page == "Sub Plot":
    subPlot()