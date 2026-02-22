import streamlit as st
from PIL import Image
from pathlib import Path

# Set page config
st.set_page_config(page_title="Ahmad Arief | Portfolio", page_icon="👨‍💻", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a modern, clean design
st.markdown('''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero Section */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #1E88E5, #00BCD4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        padding-bottom: 0;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 600;
        color: #888;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }
    
    /* Custom Cards */
    .custom-card {
        background-color: rgba(128, 128, 128, 0.05);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-color: rgba(30, 136, 229, 0.5);
    }
    
    /* Tags */
    .tech-tag {
        display: inline-block;
        background: rgba(30, 136, 229, 0.1);
        color: #1E88E5;
        border: 1px solid rgba(30, 136, 229, 0.3);
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    
    /* Typography */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #1E88E5;
    }
    .job-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .company-name {
        color: #1E88E5;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.2rem;
    }
    .date-text {
        font-size: 0.9rem;
        color: gray;
        margin-bottom: 1rem;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
''', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # Profile picture
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    try:
        base_dir = Path(__file__).resolve().parent
        candidate_images = ["IMG_5385.JPG", "IMG_5385.jpg", "IMG_5385.jpeg", "IMG_5385.png"]
        image_path = next((base_dir / name for name in candidate_images if (base_dir / name).exists()), None)
        if image_path is None:
            raise FileNotFoundError("Profile image not found")
        image = Image.open(image_path)
        st.image(image, width=300)
    except FileNotFoundError:
        st.markdown('''
        <div style="text-align: center; background: linear-gradient(135deg, #1E88E5, #00BCD4); border-radius: 12px; padding: 3rem;">
            <p style="font-size: 5rem; margin: 0;">👨‍💻</p>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<h2 style="text-align: center; margin-bottom: 0;">Ahmad Arief</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: gray;">Software Engineer & Automation Specialist</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📬 Contact Info")
    st.markdown("📍 **Location:**<br>Kuala Lumpur, Malaysia", unsafe_allow_html=True)
    st.markdown("📧 **Email:**<br>[ahmadarief4701@gmail.com](mailto:ahmadarief4701@gmail.com)", unsafe_allow_html=True)
    # st.markdown("📱 **Phone:**<br>+6011-1051-7048", unsafe_allow_html=True)
    st.markdown("🔗 **LinkedIn:**<br>[linkedin.com/in/ahmad-arief](https://linkedin.com/in/ahmad-arief)", unsafe_allow_html=True)
    st.markdown("🔗 **GitHub:**<br>[github.com/Izumi47](https://github.com/Izumi47)", unsafe_allow_html=True)
    
    # st.markdown("---")
    # # Mock download button for CV
    # with open("CV Ahmad Arief bin Omar.pdf", "rb") as file:
    #     st.download_button(
    #         label="📄 Download Resume",
    #         data=file,
    #         file_name="CV Ahmad Arief bin Omar.pdf",
    #         mime="application/pdf",
    #         use_container_width=True
    #     )

# --- MAIN CONTENT ---
st.markdown('<h1 class="hero-title">Hi, I\'m Ahmad Arief 👋</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Building scalable solutions, automating workflows, and engineering intelligent systems.</p>', unsafe_allow_html=True)

# Navigation Tabs
tabs = st.tabs(["👤 About Me", "💼 Experience", "🛠️ Skills", "🚀 Projects", "🎓 Education & Contact"])

# --- TAB 1: ABOUT ME ---
with tabs[0]:
    st.markdown('<p class="section-title">Professional Summary</p>', unsafe_allow_html=True)
    st.info('''
    Bachelor of Computer Science graduate with a CGPA of 3.76 and demonstrated expertise across full-stack development, game architecture, automation, and AI/ML integration. 
    Experienced in designing scalable solutions using modern technologies including React, Java, Go, Python, and cloud containerization. 
    Proven ability to architect complex systems from game server infrastructure to intelligent automation bots, implement secure data handling and encryption protocols, and deliver production-ready applications that improve operational efficiency and user experience.
    ''')
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Experience", value="2+ Years", delta="Automation & Dev")
    with col2:
        st.metric(label="Projects", value="10+", delta="Full-Stack & AI")
    with col3:
        st.metric(label="CGPA", value="3.76", delta="Computer Science")

# --- TAB 2: EXPERIENCE ---
with tabs[1]:
    st.markdown('<p class="section-title">Work Experience</p>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="custom-card">
        <p class="job-title">P2P Associate Analyst</p>
        <p class="company-name">AstraZeneca Asia-Pacific Business Services Sdn. Bhd.</p>
        <p class="date-text">SEP 2025 – CURRENT | Mutiara Damansara, Kuala Lumpur</p>
        <ul>
            <li><b>SAP to Coupa Migration:</b> Developed a Python automation solution to extract SAP data and format it for Coupa Purchase Order uploads. Processed up to 200,000 PO items, reducing manual entry time of 2 minutes per item to 2 minutes per 100,000 items and saving thousands of hours of manual labour.</li>
            <li><b>Balance Sheet Reconciliation (BSR):</b> Automated the end-to-end extraction of Accounts Payable (AP) and Travel & Expenses (T&E) data from SAP. Engineered Python scripts to automate complex Excel functions (VLOOKUP, Pivot Tables) and reconcile data directly into standardized templates.</li>
            <li><b>Digitalization Platform Development:</b> Designed and built a centralized Power Apps hub for the Kuala Lumpur P2P team to submit, monitor, and manage global digitalization initiatives.</li>
            <li><b>Global Digitalization Leadership:</b> Spearheaded automation projects across regional teams. Streamlined SAP data extraction, email verifications, and workflows using Python, SharePoint, and Power Automate, significantly reducing manual handling.</li>
            <li><b>System Administration & Reporting:</b> Built real-time Power BI dashboards for proactive monitoring. Investigated and resolved data inconsistencies across regional SAP markets, producing clear technical documentation to ensure system maintainability.</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="custom-card">
        <p class="job-title">Internship & Associate Analyst (1-Year Contract)</p>
        <p class="company-name">AstraZeneca Asia-Pacific Business Services Sdn. Bhd.</p>
        <p class="date-text">MAR 2024 – AUG 2025 | Mutiara Damansara, Kuala Lumpur</p>
        <ul>
            <li><b>Cashflow Forecast M+6 Dashboard:</b> Served as the primary developer for a dynamic Power BI dashboard managing cashflow forecasting across 8 APAC markets. Leveraged Python to automate SAP data collection and integrate six-month forward (M+6) projections.</li>
            <li><b>Real-time Analytics & Anomaly Detection:</b> Designed mechanisms to flag financial anomalies and visualize trends. Significantly increased forecasting accuracy and eliminated thousands of hours of manual work.</li>
            <li><b>FSC018 Reporting Automation:</b> Developed a complete Python automation solution utilizing web drivers to export reports from SAP systems and web platforms. Engineered standardized Excel data transformation processes.</li>
            <li><b>Data Visualization & Workflow Optimization:</b> Built interactive dashboards for financial and operational datasets to improve data-driven decisions. Optimized workflows via SharePoint and Power Automate to reduce manual handling.</li>
            <li><b>Company Upskilling & Troubleshooting:</b> Authored internal guides to help colleagues adopt digital tools and resolved system anomalies across 8 regional SAP markets. Implemented detailed debugging logs and instruction manuals for future maintenance.</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)

# --- TAB 3: SKILLS ---
with tabs[2]:
    st.markdown('<p class="section-title">Technical Arsenal</p>', unsafe_allow_html=True)
    
    skill_categories = {
        "Programming Languages": ["Python", "Java", "C++", "Go/Golang", "JavaScript", "Objective-C", "SQL"],
        "Web & Mobile Development": ["HTML", "CSS", "PHP", "React", "Vite", "React Router", "Node.js", "Framer Motion", "PWA", "Flutter"],
        "AI & Machine Learning": ["Streamlit", "Generative AI", "Ollama", "Goose", "OpenClaw", "Open WebUI", "JamAI", "Random Forest"],
        "DevOps, Frameworks & Tools": ["Laravel", "Git", "Docker", "Docker Compose", "Maven", "CMake", "WSL", "GitHub Actions", "ESLint"],
        "Automation & BI": ["Power BI", "Power Automate", "PowerApps", "Selenium", "Puppeteer", "Discord.py", "SAP"],
        "Databases & Game Dev": ["MySQL", "Redis", "phpMyAdmin", "Game Server Emulation", "Binary Parsing", "Reverse Engineering"]
    }
    
    cols = st.columns(2)
    for i, (cat, skills) in enumerate(skill_categories.items()):
        with cols[i % 2]:
            st.markdown(f"#### {cat}")
            tags = "".join([f'<span class="tech-tag">{skill}</span>' for skill in skills])
            st.markdown(f'<div style="margin-bottom: 2rem;">{tags}</div>', unsafe_allow_html=True)

# --- TAB 4: PROJECTS ---
with tabs[3]:
    st.markdown('<p class="section-title">Featured Projects</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('''
        <div class="custom-card">
            <h4>🎓 Class Streaming Selection System</h4>
            <p style="font-size: 0.9rem; color: gray;">Academic Project | Machine Learning</p>
            <p>Independently developed a user-friendly website using HTML, CSS, PHP, JavaScript, and SQL. Utilized machine learning to create a random forest diagram that points out the best class stream based on students' performance.</p>
            <div style="margin-top: auto;">
                <span class="tech-tag">PHP</span>
                <span class="tech-tag">JavaScript</span>
                <span class="tech-tag">Machine Learning</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="custom-card">
            <h4>🤖 Local Generative AI & SysAdmin</h4>
            <p style="font-size: 0.9rem; color: gray;">Personal Project | AI & DevOps</p>
            <p>Deployed local LLMs using Ollama and Goose. Configured containerized environments with Docker and WSL. Executed advanced system administration and developed custom Python automation tools and chatbot integrations.</p>
            <div style="margin-top: auto;">
                <span class="tech-tag">Docker</span>
                <span class="tech-tag">Ollama</span>
                <span class="tech-tag">Python</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="custom-card">
            <h4>🛠️ Game Save File Editor</h4>
            <p style="font-size: 0.9rem; color: gray;">Personal Project | Go & Reverse Engineering</p>
            <p>Developed a cross-platform GUI application in Go using the Fyne framework for editing encrypted game save files. Implemented binary file parsing, encryption/decryption algorithms, and JSON serialization.</p>
            <div style="margin-top: auto;">
                <span class="tech-tag">Go</span>
                <span class="tech-tag">Fyne</span>
                <span class="tech-tag">Binary Parsing</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div class="custom-card">
            <h4>📱 Secure Vault Android App</h4>
            <p style="font-size: 0.9rem; color: gray;">Personal Project | Mobile Security</p>
            <p>Developing a privacy-focused, vault-style Android application disguised as a calculator. Implemented secure media handling, encrypted storage protocols, and a covert password bypass system for hidden access tiers.</p>
            <div style="margin-top: auto;">
                <span class="tech-tag">Android</span>
                <span class="tech-tag">Encryption</span>
                <span class="tech-tag">Security</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="custom-card">
            <h4>🎮 Game Server Emulator</h4>
            <p style="font-size: 0.9rem; color: gray;">Personal Project | Java & Networking</p>
            <p>Architected and deployed a full-featured multiplayer game server using Java 21. Containerized with Docker Compose. Implemented complex networking protocols and persistent database management through reverse engineering.</p>
            <div style="margin-top: auto;">
                <span class="tech-tag">Java 21</span>
                <span class="tech-tag">Docker</span>
                <span class="tech-tag">Networking</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)

# --- TAB 5: EDUCATION & REFERENCES ---
with tabs[4]:
        st.markdown('<p class="section-title">Education</p>', unsafe_allow_html=True)
        st.markdown('''
        <div class="custom-card">
            <h4 style="margin-bottom: 0.2rem;">Bachelor’s in Computer Science (Hons)</h4>
            <p class="company-name">Management & Science University (MSU)</p>
            <p class="date-text">SEP 2021 – SEP 2024 | Shah Alam, Selangor</p>
            <ul>
                <li><b>Major:</b> Software Engineering</li>
                <li><b>CGPA:</b> 3.76</li>
                <li><b>Achievements:</b> 3 Dean’s List, 1 Conditional Dean’s List</li>
            </ul>
            <p style="font-size: 0.9rem; margin-top: 1rem;"><b>Relevant Coursework:</b> Object-Oriented Programming, Web & Mobile Programming, System Analysis & Design, Software Architecture & Testing, Database Systems, Server Computing, Operating Systems.</p>
        </div>
        ''', unsafe_allow_html=True)
