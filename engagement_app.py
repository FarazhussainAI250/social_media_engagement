import streamlit as st
import joblib
import pandas as pd

# --- Load Model ---
model = joblib.load("model/engagement_model.pkl")

# --- Page Config ---
st.set_page_config(page_title="Social Media Predictor", layout="centered")

# --- Custom CSS for Top Right Text ---
st.markdown("""
    <style>
        .top-right {
            position: absolute;
            top: 2px;
            right: 40px;
            font-size: 15px;
            color: #777;
            text-align: top right;
        }
        .highlight {
            background-color: #f0f9ff;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #ddd;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
    </style>
    <div class="top-right">
        Teacher: <strong>Respected Sir Shahzaib|Sir Hamza Sahb</strong><br>
        Developed by: <strong>Mr. Faraz Hussain Sahb</strong>
    </div>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #004080;'>📱 Social Media Engagement Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict Likes, Comments, Shares of your social media post 💬</p>", unsafe_allow_html=True)

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
