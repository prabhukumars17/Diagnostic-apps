import streamlit as st
st.title("The EDA Page")
# import the libraries 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    
    def data_cleaning(file):
        data=pd.read_csv(file)
        # drop the unnamed column
        data.drop('Unnamed: 0', axis=1, inplace=True)

        # replace 0s with column median
        zerofill=lambda x:x.replace(0, x.median())
        cols=data.columns[1:6]
        data[cols]=data[cols].apply(zerofill, axis=0)

        # encode the Outcome column
        df=data.copy()
        d={"Yes":1, "No":0}
        df['Outcome']=df["Outcome"].map(d)
        return df
    
    # univariate histograms
    def histograms(data):
        st.subheader("Histograms of Variables")
        data.hist()
        plt.tight_layout()
        st.pyplot()
        
    def countplot(data, feature):
        st.subheader("Countplot for Outcome")
        plt.figure(figsize=(12,7))
        ax=sns.countplot(data=data, x=feature, color='green')
        for p in ax.patches:
            x=p.get_bbox().get_points()[:,0]
            y=p.get_bbox().get_points()[1,1]
            ax.annotate("{:.2g}%".format(100.*y/len(data)), (x.mean(), y), ha='center', va='bottom')
        st.pyplot()
    
    #correlations 
    def heatmap(data):
        st.subheader("Correlation Heatmap of the data")
        plt.figure(figsize=(12,7))
        sns.heatmap(data.corr(), annot=True, cmap='Spectral', vmin=-1, vmax=+1)
        st.pyplot()

    data=data_cleaning(file='data.csv')
    plot=st.sidebar.selectbox("Choose the Plot", ('Histogram', 'Countplot', 'Heatmap'))
    if st.sidebar.button('PLOT'):
        if plot=='Histogram':
            histograms(data)
        if plot=='Countplot':
            countplot(data, feature="Outcome")
        if plot=='Heatmap':
            heatmap(data)
            
if __name__=='__main__':
    main()
            
    
