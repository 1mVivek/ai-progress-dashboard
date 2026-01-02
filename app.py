import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, datetime
from pathlib import Path

st.set_page_config(page_title="My AI Journey Dashboard", layout="wide")

def load_or_create_csv(path: str, default_df: pd.DataFrame) -> pd.DataFrame:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        return pd.read_csv(p)
    default_df.to_csv(p, index=False)
    return default_df

st.sidebar.title("🚀 My AI Journey Controls")
name = st.sidebar.text_input("Your Name", "Vivek")

search_defaults = pd.DataFrame({
    "Topic": ["AI", "Python", "C Programming", "Web Dev", "Fitness", "Random Browsing"],
    "Frequency": [45, 35, 20, 15, 10, 5]
})
search_data = load_or_create_csv("data/search_data.csv", search_defaults)

skills_defaults = pd.DataFrame({
    "Skill": ["Python", "C", "Data Structures", "ML Basics", "Deep Learning", "Math", "Projects"],
    "Current Level": [7, 6, 4, 3, 2, 4, 5],
    "Required for AI Engineer": [9, 7, 8, 8, 7, 7, 9]
})
skills = load_or_create_csv("data/skills.csv", skills_defaults)

st.title(f"📊 {name}'s AI Engineer Dashboard")
st.plotly_chart(px.bar(search_data, x="Topic", y="Frequency"), use_container_width=True)