import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuration de la page Streamlit
st.set_page_config(page_title="Analyse Automatique de Données de Santé")

# Titre de l'application
st.title("Analyse Automatique de Données de Santé")
st.write("Téléchargez un fichier CSV pour commencer l'analyse.")

# Téléchargement du fichier
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file:
    # Chargement des données
    data = pd.read_csv(uploaded_file)
    
    # Aperçu des données
    st.subheader("Aperçu des données")
    st.dataframe(data.head())  # Affiche les premières lignes

    # Statistiques descriptives
    st.subheader("Statistiques descriptives")
    stats = data.describe().transpose()  # Résumé descriptif transposé pour plus de clarté
    st.dataframe(stats)

    # Visualisation des corrélations
    st.subheader("Heatmap des corrélations")
    with st.container():
        fig, ax = plt.subplots(figsize=(5, 4))  # Taille réduite
        sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Distribution des colonnes numériques
    st.subheader("Distribution des colonnes numériques")
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    for col in numeric_columns:
        st.write(f"Distribution pour {col}")
        with st.container():
            fig, ax = plt.subplots(figsize=(4, 3))  # Taille réduite
            sns.histplot(data[col], kde=True, ax=ax)
            st.pyplot(fig)
