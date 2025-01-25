import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def main():
    st.title("Analyse Automatisée des Données de Santé")
    st.write("Chargez un fichier CSV pour démarrer.")

    # Charger un fichier
    uploaded_file = st.file_uploader("Choisir un fichier CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :", data.head())
        st.write("Statistiques descriptives :", data.describe())

        # Visualisation
        st.write("Heatmap des corrélations :")
        corr = data.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        st.pyplot(plt)

if __name__ == "__main__":
    main()
