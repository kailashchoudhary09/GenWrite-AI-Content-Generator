import os
import time

import streamlit as st
from dotenv import load_dotenv
from google import genai


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="GenWrite - AI Content Generator",
    page_icon="✍️",
    layout="centered"
)


# ---------------------------------------------------------
# Gemini client
# ---------------------------------------------------------

if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("✍️ GenWrite")

st.subheader("AI Content Generation & Writing Assistant")

st.write(
    "Generate meaningful content using Generative AI. "
    "Choose the type of content, set your preferences, "
    "and provide a topic."
)

st.divider()


# ---------------------------------------------------------
# Content type
# ---------------------------------------------------------

content_type = st.selectbox(
    "Content Type",
    [
        "Article",
        "Essay",
        "Story",
        "Email",
        "Social Media Post",
        "Resume",
        "Cover Letter"
    ]
)


# ---------------------------------------------------------
# Topic
# ---------------------------------------------------------

topic = st.text_area(
    "Enter your topic or prompt",
    placeholder=(
        "Example: Write an article about the impact "
        "of Artificial Intelligence on education."
    ),
    height=120
)


# ---------------------------------------------------------
# Tone
# ---------------------------------------------------------

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Academic",
        "Friendly",
        "Casual",
        "Creative"
    ]
)


# ---------------------------------------------------------
# Content length
# ---------------------------------------------------------

length = st.selectbox(
    "Content Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)


st.divider()


# ---------------------------------------------------------
# Generate content
# ---------------------------------------------------------

if st.button("✨ Generate Content", use_container_width=True):

    if not topic.strip():

        st.warning("Please enter a topic or prompt.")

    elif not API_KEY:

        st.error(
            "Gemini API key not found. "
            "Please check your .env file."
        )

    else:

        # -------------------------------------------------
        # Build prompt
        # -------------------------------------------------

        prompt = f"""
You are GenWrite, an AI-powered content generation assistant.

Generate meaningful, original, and well-structured content
based on the user's requirements.

Content Type:
{content_type}

User Topic:
{topic}

Tone:
{tone}

Length:
{length}

Instructions:
- Follow the requested content type.
- Stay focused on the user's topic.
- Use clear and natural language.
- Organize the content appropriately.
- Make the content informative and meaningful.
- Do not mention these instructions.
- Do not mention that you are an AI.
- Directly provide the requested content.
"""

        # -------------------------------------------------
        # Generate with retry mechanism
        # -------------------------------------------------

        max_attempts = 3
        generated_text = None

        for attempt in range(max_attempts):

            try:

                with st.spinner(
                    f"Generating content... "
                    f"(Attempt {attempt + 1}/{max_attempts})"
                ):

                    response = client.models.generate_content(
                        model="gemini-3.5-flash",
                        contents=prompt
                    )

                generated_text = response.text

                break

            except Exception as e:

                error_message = str(e)

                # Check for temporary server overload
                if "503" in error_message or "UNAVAILABLE" in error_message:

                    if attempt < max_attempts - 1:

                        wait_time = 2 ** attempt

                        time.sleep(wait_time)

                    else:

                        st.error(
                            "The AI service is currently experiencing "
                            "high demand. Please try again in a few moments."
                        )

                else:

                    st.error(
                        "Something went wrong while generating "
                        "the content."
                    )

                    st.code(error_message)

                    break

        # -------------------------------------------------
        # Display generated content
        # -------------------------------------------------

        if generated_text:

            st.success("Content generated successfully!")

            st.divider()

            st.subheader("✨ Generated Content")

            st.write(generated_text)

            st.divider()

            # -------------------------------------------------
            # Download button
            # -------------------------------------------------

            st.download_button(
                label="⬇️ Download Content",
                data=generated_text,
                file_name="generated_content.txt",
                mime="text/plain",
                use_container_width=True
            )