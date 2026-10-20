
import pandas as pd
from collections import Counter

# Load dataset
df = pd.read_csv("data/jobs.csv")

# Extract skills from all job descriptions
all_skills = []

for skills in df["skills"].dropna():
    skill_list = skills.split(",")
    for skill in skill_list:
        all_skills.append(skill.strip())

# Count skills
skill_counts = Counter(all_skills)

# Convert results into a DataFrame
skills_df = pd.DataFrame(
    skill_counts.items(),
    columns=["Skill", "Job Count"]
)

skills_df = skills_df.sort_values(
    by="Job Count",
    ascending=False
)

print("\n🔥 Most In-Demand Skills:")
print(skills_df.to_string(index=False))

# Save results
skills_df.to_csv("data/skills_analysis.csv", index=False)

print("\nSkills analysis completed!")
print("Results saved to data/skills_analysis.csv")


import pandas as pd

def get_job_market_insights():
    df = pd.read_csv("data/jobs.csv")

    insights = {
        "total_jobs": len(df),
        "total_roles": df["job_title"].nunique(),
        "average_salary": df["salary"].mean(),
        "highest_salary_role": (
            df.groupby("job_title")["salary"]
            .mean()
            .idxmax()
        ),
        "highest_salary": (
            df.groupby("job_title")["salary"]
            .mean()
            .max()
        )
    }

    return insights


def get_salary_comparison():
    df = pd.read_csv("data/jobs.csv")

    salary_data = (
        df.groupby("job_title")["salary"]
        .agg(["mean", "min", "max"])
        .reset_index()
    )

    salary_data.columns = [
        "Job Role",
        "Average Salary",
        "Minimum Salary",
        "Maximum Salary"
    ]

    return salary_data


    salary_data.columns = [
        "Job Role",
        "Average Salary",
        "Minimum Salary",
        "Maximum Salary"
    ]

    return salary_data.sort_values(
        by="Average Salary",
        ascending=False
    )
