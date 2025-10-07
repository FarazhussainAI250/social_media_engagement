import streamlit as st
import joblib
import pandas as pd

# --- Load Model ---
model = joblib.load("model/engagement_model.pkl")

# --- Page Config ---
st.set_page_config(page_title="Social Media Predictor", layout="centered")


# ----------- Custom CSS with Header & Footer ------------
st.markdown("""
<style>
/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1683721003111-070bcc053d8b?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c29jaWFsJTIwbWVkaWF8ZW58MHx8MHx8fDA%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Top-right Header */
#top-header {
    position: fixed;
    top: 80px;
    right: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 8px 16px;
    border-radius: 8px;
    color: white;
    font-size: 18px;
    font-weight: bold;
    z-index: 100;
}

/* Bottom-left Footer */
#bottom-footer {
    position: fixed;
    bottom: 10px;
    left: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 6px 14px;
    border-radius: 6px;
    color: white;
    font-size: 14px;
    z-index: 100;
}
</style>

<div id="top-header">Respected Sir Shahzaib & Sir Ali Hamza</div>
<div id="bottom-footer">Developed by Faraz Hussain</div>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: white;'>📱 Social Media Engagement Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Predict Likes, Comments, Shares of your social media post 💬</p>", unsafe_allow_html=True)

# --- Inputs ---
with st.form("prediction_form"):
    st.subheader("📝 Enter Post Details")

    platform = st.selectbox("Platform", ["Facebook", "Twitter", "Instagram"])
    post_type = st.selectbox("Post Type", ["image", "video", "carousel", "text", "poll"])
    post_day = st.selectbox("Post Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    post_hour = st.slider("Post Hour (0 to 23)", 0, 23, 12)
    sentiment = st.selectbox("Post Sentiment", ["positive", "neutral", "negative"])

    submit = st.form_submit_button("🎯 Predict Engagement")

# --- Sentiment Mapping ---
sentiment_map = {'positive': 1, 'neutral': 0, 'negative': -1}

# --- Prediction Logic ---
if submit:
    input_df = pd.DataFrame([{
        'platform': platform,
        'post_type': post_type,
        'post_day': post_day,
        'post_hour': post_hour,
        'sentiment_score': sentiment_map[sentiment]
    }])

    prediction = model.predict(input_df)[0]
    likes, comments, shares = map(int, prediction)

    # --- Performance Reaction ---
    total_engagement = likes + comments + shares
    if total_engagement > 2000:
        reaction = "🌟 Wao! This post is 🔥🔥"
    elif total_engagement > 1000:
        reaction = "😊 Not Bad! Decent Reach"
    else:
        reaction = "😞 Hmm... This needs improvement"

    # --- Display Results ---
    st.markdown("<div class='highlight'>", unsafe_allow_html=True)
    st.markdown(f"### 👍 Likes: `{likes}`")
    st.markdown(f"### 💬 Comments: `{comments}`")
    st.markdown(f"### 🔁 Shares: `{shares}`")
    st.markdown("---")
    st.markdown(f"## {reaction}")
    st.markdown("</div>", unsafe_allow_html=True)