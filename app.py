#================LOAD MODULES================
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
import streamlit as st
import os
import requests

#================STREAMLIT PAGE CONFIG================

st.set_page_config(page_title="Career Roadmap Generator", page_icon="🚀",
    layout="wide")

#================PROJECT TITLE================

st.title("🚀 Career Roadmap Generator")
st.markdown("### Build Your Personalized Career Roadmap Using Generative AI")
st.image("https://raw.githubusercontent.com/bhuvneeshsikka1-dotcom/CAREER-ROADMAP-GENERATOR-REVISED/refs/heads/main/bg.png",
         use_container_width=True)
#================USER PROMPT================

user_prompt = st.text_area("What kind of career roadmap do you want?",height=220,placeholder="""
Example:

• I want to become a Generative AI Engineer within 12 months.

• I can study 3 hours every day.

• Suggest only free resources.

• Focus on placement preparation.

• Recommend projects for beginners.

• I already know Python.
""")

generate = st.button("🚀 Generate Career Roadmap",use_container_width=True)

#================SIDEBAR================

st.sidebar.title("User Inputs")
#================API KEYS================
GOOGLE_API_KEY = st.sidebar.text_input("Enter Google API Key", type="password")
SERPER_API_KEY = st.sidebar.text_input("Enter Serper API Key",type="password")

#================CURRENT EDUCATION================

education = st.sidebar.selectbox("Current Education",("High School", "Diploma",
                "Undergraduate","Graduate","Postgraduate", "Working Professional"))

target_role = st.sidebar.selectbox("Target Role",("Data Analyst","Data Scientist",
"Machine Learning Engineer","AI Engineer","Generative AI Engineer","Agentic AI Engineer",
"Business Analyst","Software Engineer","Full Stack Developer"))

experience = st.sidebar.selectbox("Experience",("Fresher","0-1 Years","1-3 Years",
                                                "3-5 Years","5+ Years"))

current_skills = st.sidebar.multiselect(
    "Current Skills",
    [
        "Python",
        "C",
        "C++",
        "Java",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "Git",
        "GitHub",
        "Linux",
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Seaborn",
        "Scikit-Learn",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "LangChain",
        "LangGraph",
        "RAG",
        "Prompt Engineering",
        "Generative AI",
        "Agentic AI",
        "Docker",
        "FastAPI",
        "Flask",
        "Streamlit"
    ]
)


#================TOOLS================
def save_prompt(prompt):
    """This function helps to save generated prompt
    using file handling."""

    with open("prompt.txt", "w") as f:
        f.write(prompt)
    return "Prompt Saved Successfully!!"

def get_user_details(education, target_role, experience, skills, user_prompt):
    """This function helps to organize
    user information."""

    details = f""" Current Education : {education}
    Target Role : {target_role}
    Experience : {experience}
    Current Skills : {skills}
    Additional User Requirements :{user_prompt}"""

    return details

def roadmap_template():
    """This function returns roadmap format."""
    return """
Career Overview

Skill Gap Analysis

Learning Roadmap

Projects

Recommended Certifications & Learning Resources

Recommended YouTube Videos

Resume Building

Portfolio

GitHub

LinkedIn

Interview Preparation

Expected Salary

Top Hiring Companies

Timeline

Final Motivation
"""

def search_learning_resources(query):

    url = "https://google.serper.dev/search"

    payload = {"q": query}

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url,json=payload,
        headers=headers)

    return response.json()

#================MAIN AGENT================

def main_agent(agent, education, target_role, experience, current_skills,
               user_prompt):
  """This is the Main Agent.
  It takes user information and generates a complete
  Career Roadmap."""
  # Giving prompt to create detailed prompt for code generation
  prompt = """You are a Professional Career Guidance Expert.

Your task is to generate a complete Career Roadmap based on the user's education,
experience, current skills, target career, and additional requirements.

The roadmap must include:

• Career Overview

• Current Skill Gap

• Skills to Learn

• Recommended Learning Order

• Beginner Projects

• Intermediate Projects

• Advanced Projects

• Recommended Certifications & Learning Resources

• Recommended YouTube Videos

• Resume Building

• Portfolio Development

• LinkedIn Optimization

• GitHub Suggestions

• Interview Preparation

• Expected Salary

• Top Hiring Companies

• Timeline

• Final Motivation

Generate the output as a single HTML document.

Do not use Markdown.

Use modern HTML5 and CSS3.

Use responsive design.

Create professional roadmap cards.

Add an attractive progress timeline.

Highlight important skills.

Separate Beginner, Intermediate and Advanced phases.

Mention approximate duration for every phase.

Use emojis wherever suitable.

Carefully read the additional user requirements.

If the user has requested:

• Free resources

• Fast roadmap

• Placement preparation

• Higher studies

• Freelancing

• Startup

• Remote jobs

• Specific certifications

Modify the roadmap accordingly.

==================================================
RECOMMENDED CERTIFICATIONS & LEARNING RESOURCES
==================================================

Use the Search Tool to retrieve the latest learning resources.

For every certification provide:

• Certification Name

• Official Provider

• Official Course Link

• Duration

• Free or Paid

• Difficulty Level

• Why it is recommended

Recommend only official providers such as:

• Google

• Microsoft Learn

• AWS

• Coursera

• DeepLearning.AI

• IBM

• NVIDIA

• Hugging Face

• Databricks

• edX

• Udemy

• Cisco

• Oracle

Do not generate fake or imaginary links.

Always provide official URLs whenever available.

==================================================
RECOMMENDED YOUTUBE VIDEOS
==================================================

Use the Search Tool to retrieve the latest high-quality YouTube tutorials.

Recommend 5 YouTube videos.

For every video provide:

• Video Title

• Channel Name

• Direct YouTube Link

• Approximate Duration (if available)

• Why this video is recommended

Prefer trusted channels such as:

• freeCodeCamp.org

• DeepLearningAI

• Krish Naik

• CampusX

• CodeBasics

• Sentdex

• Google Developers

• Microsoft Developer

• Hugging Face

Do not generate fake YouTube links.

==================================================
DESIGN GUIDELINES
==================================================

• Create a premium and modern UI.

• Use a clean professional color palette.

• Always maintain high contrast between text and background.

• Never use white text on light-colored cards.

• Never use black or dark text on dark backgrounds.

• Every heading, paragraph, list item, table and button must remain clearly readable.

• Prefer white or very light cards with dark text.

• Use a light overall page background.

• Use professional colors:

  - Primary: #2563EB

  - Secondary: #1E293B

  - Accent: #10B981

  - Background: #F8FAFC

  - Cards: #FFFFFF

  - Heading Text: #0F172A

  - Body Text: #334155

  - Border: #CBD5E1

• Use soft shadows.

• Use rounded corners.

• Use proper spacing and padding.

• Make every section visually separated.

• Ensure the generated HTML looks professional on desktop and mobile.

• Do not use neon colors.

• Avoid gradients that reduce text visibility.

• Prioritize readability over decoration.

==================================================
IMPORTANT INSTRUCTIONS
==================================================

• Always personalize the roadmap.

• Keep the roadmap practical and industry-oriented.

• Recommend technologies in the correct learning order.

• Keep project ideas relevant to the selected target role.

• If search results are unavailable, clearly mention that live resources could not be retrieved instead of generating fake links.

Generate everything in one HTML file.

Return ONLY valid HTML.

Do not include explanations before or after the HTML.
"""
  user_details = get_user_details(education, target_role, experience, current_skills, user_prompt)
  final_prompt = prompt + user_details
  save_prompt(final_prompt)
  response = agent.invoke({"messages":[{"role":"user", "content":final_prompt}]})
  career_roadmap = response["messages"][-1].content[-1]["text"]
  return career_roadmap
    
    #================GENERATE CAREER ROADMAP================

if generate:
    if not GOOGLE_API_KEY:
        st.warning("Please Enter Google API Key.")
        st.stop()

    if not SERPER_API_KEY:
        st.warning("Please Enter Serper API Key.")
        st.stop()

    if user_prompt.strip() == "":
        st.warning("Please describe your career goals.")
        st.stop()

    
    model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite", 
        google_api_key=GOOGLE_API_KEY)
    
    agent = create_agent(
            model=model,
            tools=[save_prompt,get_user_details,roadmap_template,search_learning_resources])
    

    with st.spinner("Generating Your Career Roadmap..."):

        career_code = main_agent(agent,education,target_role,
            experience,current_skills,user_prompt)

        st.html(career_code,width="stretch")
