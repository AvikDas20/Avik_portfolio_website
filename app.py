import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Avik's Portfolio", page_icon="🧑‍💻", layout="wide")

# Load profile image
profile_image = Image.open("C:/Users/u1100168/OneDrive - IQVIA/Documents/Advanced_Analytics/PortfolioWebsite/prof1.jpeg")

# --- Sidebar Contact Info with Logos ---
with st.sidebar:
    st.image(profile_image, width=180)
    st.title("Avik Das")
    st.write("🧑‍💻 Aspiring Data Scientist | Problem Solver")
    st.markdown("""<p style='display: flex; align-items: center;'>
    <img src='https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000' width='20' style='margin-right: 10px;'/>
    <a href='mailto:your.email@example.com' target='_blank'>Email</a>
</p>
<p style='display: flex; align-items: center;'>
    <img src='https://img.icons8.com/ios-filled/50/0077B5/linkedin.png' width='18' style='margin-right: 10px;'/>
    <a href='https://www.linkedin.com/in/your-profile' target='_blank'>LinkedIn</a>
</p>
<p style='display: flex; align-items: center;'>
    <img src='https://img.icons8.com/ios-glyphs/30/000000/github.png' width='20' style='margin-right: 10px; background-color: white; border-radius: 4px;'/>
    <a href='https://github.com/yourusername' target='_blank'>GitHub</a>
</p>
""", unsafe_allow_html=True)


# --- About Me ---
st.title("Hi, I'm Avik! 👋")
st.write("""
Welcome to my personal portfolio!  
In between juggling powerpoint reports and deadlines, I'm passionate about exploring data, finding solutions and building machine learning models.
Feel free to connect with me via my socials if you find me suitable for a position you are trying to fill or just want to catch up about the FC Barcelona game last week 
""")

# --- Experience ---
st.subheader("💼 Experience")
experience = [
    {
        "title": "Associate Consultant at IQVIA",
        "duration": "June 2021 - Current",
        "description": "Working as an Associate Consultant in the Market Research and Insights team for 3.5 years, leveraging Python to automate processes and reduce turnaround times by 50%. Contributed to end-to-end project development, cutting delivery timelines by 40%, and managed stakeholder communication effectively. Created client-ready reports using Advanced Excel and conducted exploratory data analysis on healthcare datasets, including patient-level and HCP/vendor data.",
        "url": "https://github.com/yourusername/movie-recommender"
    }]
for exps in experience:
    st.markdown(f"#### {exps['title']}")
    st.write(exps["duration"])
    st.write(exps["description"])

# --- Skills with Logos ---
st.subheader("🛠️ Skills")
cols = st.columns(3)

# Define skill and logo URL pairs
skills = [
    [
        ("Python", "https://img.icons8.com/color/48/python.png"),
        ("SQL", "https://img.icons8.com/ios-filled/50/4D4D4D/sql.png"),
        ("Streamlit", "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg")
    ],
    [
        ("Pandas", "https://pandas.pydata.org/static/img/pandas_mark.svg"),
        ("NumPy", "https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg"),
        ("Matplotlib", "https://matplotlib.org/stable/_static/logo2_compressed.svg")
    ],
    [
        ("Scikit-learn", "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"),
        ("TensorFlow", "https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg"),
        ("Git", "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png")
    ]
]

# Render each skill with logo
for col, skill_list in zip(cols, skills):
    for name, logo in skill_list:
        col.markdown(
            f'<p style="display: flex; align-items: center;"><img src="{logo}" width="20" style="margin-right: 10px;"> {name}</p>',
            unsafe_allow_html=True
        )

# --- Projects ---
st.subheader("📁 Projects")
projects = [
    {
        "title": "Marketing Leads Scoring Prediction",
        "description": "This project was designed to assist the sales division of our client, an Ed-Tech company. Our primary objective was to develop a predictive analytics model that could effectively identify the propensity of buying a course after the marketing team has generated leads from a group of potential buyers of the educational courses offered by the company.",
        "url": "https://github.com/AvikDas20/Ed_Tech_Market_Lead_Scoring_Prediction"
    },
    {
        "title": "Pricing model for a second-hand car company",
        "description": "This project was designed to assist the valuation and sales teams of a leading second-hand car retailer. Our primary objective was to develop a robust predictive analytics model that could accurately estimate the fair market price of a used vehicle based on its characteristics and usage history.",
        "url": "https://github.com/AvikDas20/Second_Hand_Car_Price_Prediction"
    },
    {
        "title": "Transactional Fraud Detection with Customer Segmentation",
        "description": "This project was designed to support the risk and marketing teams of an e-commerce platform in two key areas: (1) building a robust fraud-detection model to flag suspicious transactions, and (2) performing customer segmentation to guide targeted retention and upsell campaigns.",
        "url": "https://github.com/AvikDas20/Transactional_Fraud_Detection_with_Customer_Segmentation"
    },
]

for project in projects:
    st.markdown(f"### [{project['title']}]({project['url']})")
    st.write(project["description"])
    st.markdown("---")

# # --- Contact ---
# st.subheader("📬 Get in Touch")
# st.write("Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/your-profile) or [email](mailto:your.email@example.com).")

# # Custom Footer
# st.markdown("<hr><center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)

