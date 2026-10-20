
import streamlit as st
import pandas as pd
import pickle
from urllib.parse import quote_plus
from sklearn.metrics.pairwise import cosine_similarity
from analysis import get_job_market_insights, get_salary_comparison

# Page configuration
st.set_page_config(
    page_title="AI Career Analytics",
    page_icon="📊",
    layout="wide"
)

# Load custom CSS
with open("assets/style.css", "r", encoding="utf-8") as css_file:
    st.markdown(
        f"<style>{css_file.read()}</style>",
        unsafe_allow_html=True
    )

# Load datasets
df = pd.read_csv("data/jobs.csv")
skills_df = pd.read_csv("data/skills_analysis.csv")

# Sidebar navigation
st.sidebar.title("⚡ CareerAI")
st.sidebar.caption("AI Career Analytics Platform")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Dashboard",
        "📊 Skills Analytics",
        "🤖 Career Recommendation",
        "🎯 Skill Gap Analysis"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "Explore skills and discover career opportunities."
)

# Dashboard
if page == "🏠 Dashboard":

    st.title("🚀 AI-Powered Job Market Analytics")
    st.subheader(
        "Explore Jobs, Skills, Salaries & Career Opportunities"
    )

    # Job Market Insights
    insights = get_job_market_insights()

    st.subheader("📈 Job Market Insights")
    insight1, insight2 = st.columns(2)

    with insight1:
        st.metric(
            "Highest Paying Role",
            insights["highest_salary_role"]
        )

    with insight2:
        st.metric(
            "Highest Average Salary",
            f"₹{insights['highest_salary']:,.0f}"
        )

    # Main metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Jobs", len(df))

    with col2:
        st.metric("Job Roles", df["job_title"].nunique())

    with col3:
        st.metric(
            "Average Salary",
            f"₹{df['salary'].mean():,.0f}"
        )

    st.divider()

    # Job Search
    st.subheader("📋 Job Market Dataset")

    search_role = st.text_input(
        "🔍 Search Job Role",
        placeholder="Example: Python Developer"
    )

    if search_role:
        filtered_df = df[
            df["job_title"].str.contains(
                search_role,
                case=False,
                na=False
            )
        ]
    else:
        filtered_df = df

    st.dataframe(filtered_df, use_container_width=True)

    if search_role and filtered_df.empty:
        st.warning("No matching jobs found. Try another job role.")

    st.download_button(
        label="📥 Download Job Report (CSV)",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="job_market_report.csv",
        mime="text/csv"
    )

    # Jobs by Role
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💼 Jobs by Role")
        st.bar_chart(df["job_title"].value_counts())

    with col2:
        st.subheader("💰 Average Salary by Role")
        avg_salary = df.groupby("job_title")["salary"].mean()
        st.bar_chart(avg_salary)

    # Salary Comparison
    st.divider()
    st.subheader("💰 Salary Comparison")

    salary_comparison = get_salary_comparison()
    st.dataframe(salary_comparison, use_container_width=True)

    st.subheader("📊 Salary Range Comparison")

    chart_data = salary_comparison.set_index("Job Role")[
        ["Minimum Salary", "Average Salary", "Maximum Salary"]
    ]
    st.bar_chart(chart_data)

    # Jobs by Location
    st.divider()
    st.subheader("📍 Jobs by Location")
    st.bar_chart(df["location"].value_counts())


# Skills Analytics
elif page == "📊 Skills Analytics":

    st.title("📊 Skills Analytics")
    st.subheader("🔥 In-Demand Skills in the Job Market")

    if {"Skill", "Job Count"}.issubset(skills_df.columns):

        st.dataframe(skills_df, use_container_width=True)

        st.subheader("🏆 Top 5 In-Demand Skills")

        top_skills = skills_df.sort_values(
            by="Job Count",
            ascending=False
        ).head(5)

        st.dataframe(top_skills, use_container_width=True)

        st.subheader("📊 Skills Demand Chart")
        st.bar_chart(
            skills_df.set_index("Skill")["Job Count"]
        )

    else:
        st.warning(
            "Check that skills_analysis.csv contains "
            "'Skill' and 'Job Count' columns."
        )


# Career Recommendation
elif page == "🤖 Career Recommendation":

    st.title("🤖 AI Career Recommendation")
    st.write("Enter your skills to discover suitable job roles.")

    user_skills = st.text_input(
        "Enter your skills",
        placeholder="Example: Python, SQL, Machine Learning"
    )

    if st.button("🚀 Recommend Jobs"):

        if user_skills.strip():

            try:
                with open("models/career_model.pkl", "rb") as file:
                    df_model, vectorizer, job_vectors = pickle.load(file)

                user_vector = vectorizer.transform([user_skills])

                scores = cosine_similarity(
                    user_vector,
                    job_vectors
                ).flatten()

                results = df_model.copy()
                results["Match Score"] = scores

                results = results.sort_values(
                    by="Match Score",
                    ascending=False
                ).drop_duplicates(subset=["job_title"])

                results = results.head(3)

                st.subheader("🎯 Recommended Job Roles")

                for _, job in results.iterrows():

                    st.markdown(f"### 💼 {job['job_title']}")
                    st.write(f"Skills needed: {job['skills']}")

                    st.write(
                        f"Salary in sample data: ₹{job['salary']:,.0f}"
                    )

                    match_score = max(
                        0.0,
                        min(1.0, float(job["Match Score"]))
                    )

                    st.write(
                        f"Skill Match: {match_score * 100:.1f}%"
                    )
                    st.progress(match_score)
                    st.divider()

            except FileNotFoundError:
                st.error(
                    "Career model not found. Run train_model.py first."
                )

            except Exception as e:
                st.error(f"Recommendation error: {e}")

        else:
            st.warning("Please enter your skills first.")


# Skill Gap Analysis
elif page == "🎯 Skill Gap Analysis":

    st.title("🎯 Skill Gap Analysis")
    st.write("Find which skills you need to learn for your target job.")

    job_role = st.selectbox(
        "Select your target job role",
        sorted(df["job_title"].dropna().unique())
    )

    known_skills = st.text_input(
        "Enter the skills you already know",
        placeholder="Example: Python, HTML"
    )

    if st.button("🔍 Analyze Skill Gap"):

        if known_skills.strip():

            target_jobs = df[df["job_title"] == job_role]
            required_skills = set()

            for skills in target_jobs["skills"].dropna():
                for skill in skills.split(","):
                    required_skills.add(skill.strip().lower())

            user_skill_set = {
                skill.strip().lower()
                for skill in known_skills.split(",")
                if skill.strip()
            }

            missing_skills = sorted(
                required_skills - user_skill_set
            )

            st.subheader("📚 Skills to Learn Next")

            if missing_skills:

                for skill in missing_skills:
                    st.write(f"📌 {skill.title()}")

                    search_url = (
                        "https://www.youtube.com/results?search_query="
                        + quote_plus(skill + " tutorial")
                    )

                    st.markdown(
                        f"[📚 Learn {skill.title()}]({search_url})"
                    )

            else:
                st.success(
                    "You have all listed skills for this sample role!"
                )

        else:
            st.warning("Please enter your current skills.")

