import streamlit as st import pandas as pd import plotly.express as px from datetime import date, datetime from pathlib import Path

st.set_page_config(page_title="My AI Journey Dashboard", layout="wide")

def load_or_create_csv(path: str, default_df: pd.DataFrame) -> pd.DataFrame: p = Path(path) p.parent.mkdir(parents=True, exist_ok=True) if p.exists(): try: return pd.read_csv(p) except Exception: pass default_df.to_csv(p, index=False) return default_df.copy()

st.sidebar.title("🚀 My AI Journey Controls") name = st.sidebar.text_input("Your Name", "Vivek")

search_defaults = pd.DataFrame({ "Topic": ["AI", "Python", "C Programming", "Web Dev", "Fitness", "Random Browsing"], "Frequency": [45, 35, 20, 15, 10, 5] }) search_data = load_or_create_csv("data/search_data.csv", search_defaults)

skills_defaults = pd.DataFrame({ "Skill": ["Python", "C", "Data Structures", "ML Basics", "Deep Learning", "Math", "Projects"], "Current Level": [7, 6, 4, 3, 2, 4, 5], "Required for AI Engineer": [9, 7, 8, 8, 7, 7, 9] }) skills = load_or_create_csv("data/skills.csv", skills_defaults)

progress_defaults = pd.DataFrame({ "Area": ["Skills", "Projects", "Consistency", "Confidence", "Startup Readiness"], "Current": [50, 40, 45, 55, 30], "Dream": [100, 100, 100, 100, 100] }) progress = load_or_create_csv("data/progress.csv", progress_defaults)

education_defaults = pd.DataFrame({ "Category": ["College (BCA)", "Self Study", "Projects", "Startup Ideas"], "Hours Invested": [600, 900, 400, 200] }) education = load_or_create_csv("data/education.csv", education_defaults)

st.title(f"📊 {name}'s AI Engineer & Startup Dashboard") st.caption("A self-built Power BI–style dashboard to track dreams vs reality")

st.subheader("🔍 What I Search Most vs Least") st.plotly_chart(px.bar(search_data, x="Topic", y="Frequency", title="Search Frequency"), use_container_width=True)

st.subheader("🧠 Skill Gap: Me vs AI Engineer") st.plotly_chart(px.bar(skills, x="Skill", y=["Current Level", "Required for AI Engineer"], barmode="group", title="Skill Comparison"), use_container_width=True)

st.subheader("🎯 Gap Between Me & My Dreams") st.plotly_chart(px.line(progress, x="Area", y=["Current", "Dream"], markers=True), use_container_width=True)

st.subheader("⏳ Where My Time Went") st.plotly_chart(px.pie(education, names="Category", values="Hours Invested"), use_container_width=True)

st.subheader("🤖 AI Engineer Readiness Score") required_sum = float(skills["Required for AI Engineer"].sum()) current_sum = float(skills["Current Level"].sum()) readiness = int((current_sum / required_sum) * 100) if required_sum > 0 else 0 st.metric("Overall Readiness", f"{readiness}%")

st.subheader("🏗️ AI Startup Vision Tracker") st.progress(0.3) st.write("Idea Validation → MVP → Users → Revenue → Scale")

st.subheader("📝 Daily Reflection") if "reflections" not in st.session_state: reflection_path = Path("data/reflections.csv") if reflection_path.exists(): try: st.session_state.reflections = pd.read_csv(reflection_path) except Exception: st.session_state.reflections = pd.DataFrame(columns=["date", "reflection"]) else: st.session_state.reflections = pd.DataFrame(columns=["date", "reflection"])

reflection_text = st.text_area("What did I learn today?")

if st.button("Save Reflection"): if reflection_text.strip(): entry = pd.DataFrame([ {"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "reflection": reflection_text.strip()} ]) st.session_state.reflections = pd.concat([st.session_state.reflections, entry], ignore_index=True) Path("data").mkdir(parents=True, exist_ok=True) st.session_state.reflections.to_csv("data/reflections.csv", index=False) st.success("Reflection saved") else: st.warning("Reflection is empty")

if not st.session_state.reflections.empty: st.markdown("### 📜 Past Reflections") st.dataframe(st.session_state.reflections, use_container_width=True)

st.caption(f"Last updated: {date.today()} | Built by {name} using Python + Streamlit")
