import sys
import os

# Ensure the project root is in path so backend can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

st.set_page_config(
    page_title="Personalized Networking Assistant Pro",
    page_icon="🤝",
    layout="wide"
)


st.markdown('''
<style>
.stApp{
background: linear-gradient(135deg,#0f172a,#1e1b4b,#312e81);
background-attachment:fixed;
}
[data-testid="stHeader"]{background:transparent;}
.block-container{padding-top:1.5rem;}
div[data-testid="stVerticalBlock"]>div{
border-radius:18px;
}
h1,h2,h3{color:white!important;}
section[data-testid="stSidebar"]{
background:rgba(15,23,42,.9);
backdrop-filter:blur(10px);
}
.stTextInput input,.stTextArea textarea{
border-radius:14px!important;
border:1px solid #8b5cf6!important;
}
.stButton>button{
border-radius:14px!important;
background:linear-gradient(90deg,#7c3aed,#3b82f6)!important;
color:white!important;
border:none!important;
font-weight:700!important;
}
</style>
''',unsafe_allow_html=True)
st.markdown("""
<div style='padding:18px;border-radius:20px;background:rgba(255,255,255,.08);backdrop-filter:blur(12px);margin-bottom:20px'>
<h1 style='margin:0'>🚀 Personalized Networking Assistant</h1>
<p style='color:#ddd'>AI-powered networking companion for events, meetings and professional conversations.</p>
</div>
""",unsafe_allow_html=True)
# Custom CSS — adaptive for dark AND light Streamlit themes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    /* ── Typography ─────────────────────────── */
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ── CSS variables: DARK defaults ────────── */
    :root {
        --na-card-bg:        #16161A;
        --na-card-border:    rgba(212, 175, 55, 0.18);
        --na-card-shadow:    rgba(0, 0, 0, 0.60);
        --na-hover-shadow:   rgba(212, 175, 55, 0.20);
        --na-gold:           #D4AF37;
        --na-gold-start:     #F9F5E8;
        --na-gold-end:       #AA7C11;
        --na-text:           #E5E7EB;
        --na-muted:          #9CA3AF;
        --na-btn-text:       #0A0A0B;
    }

    /* ── CSS variables: LIGHT overrides ──────── */
    /*  Streamlit sets this attribute on the root  */
    [data-theme="light"],
    .st-emotion-cache-uf99v8[data-testid="stAppViewContainer"] {
        --na-card-bg:        #FFFFFF;
        --na-card-border:    rgba(120, 88, 0, 0.20);
        --na-card-shadow:    rgba(0, 0, 0, 0.08);
        --na-hover-shadow:   rgba(120, 88, 0, 0.14);
        --na-gold:           #7A5800;
        --na-gold-start:     #5C4200;
        --na-gold-end:       #B8880A;
        --na-text:           #1C1917;
        --na-muted:          #6B7280;
        --na-btn-text:       #FFFFFF;
    }

    /* OS-level light preference fallback */
    @media (prefers-color-scheme: light) {
        :root {
            --na-card-bg:        #FFFFFF;
            --na-card-border:    rgba(120, 88, 0, 0.20);
            --na-card-shadow:    rgba(0, 0, 0, 0.08);
            --na-hover-shadow:   rgba(120, 88, 0, 0.14);
            --na-gold:           #7A5800;
            --na-gold-start:     #5C4200;
            --na-gold-end:       #B8880A;
            --na-text:           #1C1917;
            --na-muted:          #6B7280;
            --na-btn-text:       #FFFFFF;
        }
    }

    /* ── Hero title gradient ─────────────────── */
    .title-text {
        background: linear-gradient(135deg,
            var(--na-gold-start) 0%,
            var(--na-gold)       55%,
            var(--na-gold-end)   100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 0.1rem;
        letter-spacing: -0.5px;
    }

    /* ── Subtitle ────────────────────────────── */
    .subtitle {
        color: var(--na-muted);
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
        line-height: 1.6;
    }

    /* ── Starter cards ───────────────────────── */
    .starter-card {
        background:   var(--na-card-bg);
        border:       1px solid var(--na-card-border);
        border-left:  6px solid var(--na-gold);
        padding:      1.5rem 1.75rem;
        border-radius: 1rem;
        box-shadow:   0 8px 24px -8px var(--na-card-shadow);
        margin-bottom: 1.25rem;
        color:        var(--na-text);
        font-size:    1.15rem;
        line-height:  1.6;
        transition:   transform 0.2s cubic-bezier(0.4,0,0.2,1),
                      box-shadow 0.2s ease,
                      border-color 0.2s ease;
    }

    .starter-card:hover {
        transform:   translateY(-3px) scale(1.005);
        box-shadow:  0 16px 36px -8px var(--na-hover-shadow),
                     0 8px 16px -8px var(--na-card-shadow);
        border-color: var(--na-card-border);
        border-left-color: var(--na-gold-end);
    }

    /* ── Buttons ─────────────────────────────── */
    .stButton>button {
        border-radius: 0.75rem !important;
        font-weight:   600 !important;
        transition:    all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
    }

    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg,
            var(--na-gold-start) 0%,
            var(--na-gold)       50%,
            var(--na-gold-end)   100%) !important;
        border: none !important;
        color:  var(--na-btn-text) !important;
        box-shadow: 0 4px 15px rgba(212,175,55,0.28) !important;
    }

    .stButton>button[kind="primary"]:hover {
        transform:  translateY(-1px) !important;
        box-shadow: 0 6px 22px rgba(212,175,55,0.45) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🤝 Personalized Networking Assistant</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Generate smart, context-aware conversation starters for your next professional event.</div>", unsafe_allow_html=True)

# ── Lazy-load heavy backend services so the UI renders instantly ──────────────
@st.cache_resource(show_spinner="Loading AI models (first run only)...")
def load_services():
    from backend.services.event_analyzer import EventAnalyzer
    from backend.services.topic_generator import TopicGenerator
    analyzer = EventAnalyzer()
    generator = TopicGenerator()
    return analyzer, generator

from backend.services.fact_checker import get_fact_check
from backend.storage.history_logger import log_generation, get_history
from backend.storage.feedback_logger import log_feedback

tab1, tab2, tab3 = st.tabs(["💡 Generate Starters", "🔍 Quick Fact Check", "📜 History"])

# ----------------- TAB 1: GENERATE STARTERS -----------------
with tab1:
    st.header("Event Details")
    event_description = st.text_area(
        "Event Description", 
        placeholder="e.g., A summit focusing on AI advancements in the healthcare sector..."
    )
    
    interests_input = st.text_input(
        "Your Interests (comma-separated)",
        placeholder="e.g., machine learning, biotech, startups"
    )
    
    if st.button("Generate Starters", type="primary"):
        if not event_description.strip():
            st.warning("Please provide an event description.")
        else:
            interests = [i.strip() for i in interests_input.split(",") if i.strip()]
            
            with st.spinner("Analyzing event and generating starters..."):
                try:
                    analyzer, generator = load_services()
                    themes = analyzer.analyze(event_description)
                    starters = generator.generate_starters(themes=themes, interests=interests)
                    
                    generation_id = log_generation(
                        event_description=event_description,
                        interests=interests,
                        themes=themes,
                        starters=starters
                    )
                    
                    st.session_state["generation_id"] = generation_id
                    st.session_state["starters"] = starters
                    st.session_state["themes"] = themes
                    st.success(f"Detected Themes: {', '.join(themes)}")
                except Exception as e:
                    st.error(f"Error generating starters: {e}")

    # Display generated starters if they exist in session state
    if "starters" in st.session_state:
        st.markdown("### ✨ Your Conversation Starters")
        for i, starter in enumerate(st.session_state["starters"]):
            st.markdown(f"<div class='starter-card'>{starter}</div>", unsafe_allow_html=True)
            
        st.write("Was this helpful?")
        col1, col2, _ = st.columns([1, 1, 8])
        with col1:
            if st.button("👍 Yes"):
                log_feedback(st.session_state["generation_id"], True)
                st.toast("Feedback submitted! Thanks.")
        with col2:
            if st.button("👎 No"):
                log_feedback(st.session_state["generation_id"], False)
                st.toast("Feedback submitted! Thanks.")

# ----------------- TAB 2: FACT CHECK -----------------
with tab2:
    st.header("Quick Fact Check")
    st.markdown("Look up a quick fact or topic before you talk about it.")
    
    query = st.text_input("Topic to look up", placeholder="e.g., Generative AI")
    
    if st.button("Search Wikipedia"):
        if not query.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner(f"Looking up '{query}'..."):
                try:
                    result = get_fact_check(query)
                    if result.error:
                        st.warning(result.summary)
                    else:
                        st.success("Found it!")
                        st.write(result.summary)
                        if result.source_url:
                            st.markdown(f"[Read more on Wikipedia]({result.source_url})")
                except Exception as e:
                    st.error(f"Error: {e}")


# ----------------- TAB 3: HISTORY -----------------
with tab3:
    st.header("Your Past Conversations")
    if st.button("Refresh History"):
        st.rerun()
        
    try:
        history = get_history()
        if not history:
            st.info("No past generations found.")
        else:
            for entry in reversed(history):
                with st.expander(f"📅 {entry['timestamp'][:16].replace('T', ' ')}"):
                    st.write(f"**Event**: {entry['event_description']}")
                    if entry.get("themes"):
                        st.write(f"**Themes**: {', '.join(entry['themes'])}")
                    st.write("**Starters generated:**")
                    for s in entry['starters']:
                        st.write(f"- {s}")
                        
                    useful = entry.get("useful")
                    if useful is True:
                        st.write("Feedback: 👍 Useful")
                    elif useful is False:
                        st.write("Feedback: 👎 Not useful")
                    else:
                        st.write("Feedback: None")
    except Exception as e:
        st.error(f"Could not load history: {e}")
