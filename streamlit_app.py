mport streamlit as st
import base64

# --- Helper function to load local images and encode as base64 ---
def get_base64_image(image_path):
    """Encodes a local image to a base64 string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# --- Page Configuration ---
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💼",
    layout="wide"
)

# --- CSS Styling (for a clean, modern look) ---
st.markdown("""
<style>
    .main-header {
        font-size: 3em;
        font-weight: bold;
        color: #2e86c1; /* A nice blue color */
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 2px solid #2e86c1;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 2em;
        font-weight: bold;
        color: #1a5276; /* Darker blue */
        border-left: 5px solid #1a5276;
        padding-left: 10px;
        margin-top: 40px;
    }
    .profile-photo {
        border-radius: 50%;
        max-width: 250px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<h1 class="main-header">My Portfolio</h1>', unsafe_allow_html=True)

# --- About Me Section ---
st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    # Use a placeholder image or a local file
    # For a local file, ensure it's in the same directory as this script.
    # image_path = "profile.jpg"
    # if st.path.exists(image_path):
    #     st.image(image_path, caption="Your Name", use_container_width=True)
    # else:
    st.image("https://placehold.co/400x400/2e86c1/ffffff?text=Your+Photo", caption="Your Name", use_container_width=True)

with col2:
    st.markdown("""
    Hello! I am **[Your Name]**, a passionate [Your Profession] with expertise in [Your Main Skills]. I am currently a [Your Current Title] at [Your Company]. My work focuses on [Describe your focus].
    
    Feel free to connect with me:
    * **GitHub:** [Link to your GitHub]
    * **LinkedIn:** [Link to your LinkedIn]
    * **Email:** [your.email@example.com]
    """)

# --- Research Interests Section ---
st.markdown('<h2 class="section-header">Research Interests</h2>', unsafe_allow_html=True)
st.markdown("""
My primary research interests include:
* [Research Interest 1]
* [Research Interest 2]
* [Research Interest 3]
* [Research Interest 4]
""")

# --- Professional Experience Section ---
st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
st.markdown("""
### **[Job Title 1]** | [Company 1]
**Dates:** [Start Date] - [End Date]
* [Description of your role and key achievements]
* [Another key responsibility or achievement]

### **[Job Title 2]** | [Company 2]
**Dates:** [Start Date] - [End Date]
* [Description of your role and key achievements]
* [Another key responsibility or achievement]
""")

# --- YouTube Videos Section ---
st.markdown('<h2 class="section-header">YouTube Videos</h2>', unsafe_allow_html=True)
st.markdown("Here are some videos demonstrating my research projects and skills.")

video_col1, video_col2 = st.columns(2)

with video_col1:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder video
    st.write("Video Title 1: Brief description of the video content.")

with video_col2:
    st.video("https://www.youtube.com/watch?v=FjI5jY81n9g") # Placeholder video
    st.write("Video Title 2: Brief description of the video content.")

st.markdown("---")
st.write("© 2024 Your Name. All Rights Reserved.")

