# ✨ GenWrite – AI Content Generator

GenWrite is an AI-powered content generation and writing assistant built using **Python, Streamlit, and Google's Generative AI (Gemini)**.

The application allows users to generate different types of written content by providing a topic, selecting a tone, and choosing the desired length.

---

## 🚀 Features

- 📝 Generate AI-powered content
- 📄 Multiple content types:
  - Article
  - Essay
  - Story
  - Email
  - Social Media Post
  - Resume
  - Cover Letter
- 🎯 Select different writing tones:
  - Professional
  - Academic
  - Friendly
  - Casual
  - Creative
- 📏 Choose content length:
  - Short
  - Medium
  - Long
- 📥 Download generated content as a text file
- 🌐 Simple and interactive Streamlit web interface
- 🤖 Uses Google's Gemini Generative AI model

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| Google Gemini API | AI content generation |
| python-dotenv | Secure API key management |
| Git & GitHub | Version control |

---

## 🏗️ System Architecture

```text
              ┌─────────────────────┐
              │       User          │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Streamlit Web UI   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Prompt Generation  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Gemini AI Model   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Generated Content   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Display / Download  │
              └─────────────────────┘
## 📂 Project Structure

```text
GenWrite-AI-Content-Generator/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The `.env` file containing the Gemini API key is intentionally excluded from GitHub for security.
---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kailashchoudhary09/GenWrite-AI-Content-Generator.git
```

### 2. Open the project directory

```bash
cd GenWrite-AI-Content-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key Setup

GenWrite requires a Google Gemini API key.

Create an API key through [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

**Important:** Never upload your `.env` file or API key to GitHub.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 How to Use

1. Open the GenWrite application.
2. Select the type of content.
3. Enter your topic or instructions.
4. Select the writing tone.
5. Select the content length.
6. Click **Generate Content**.
7. Review the generated content.
8. Download the content if required.

---

## 🧪 Example

**Content Type:** Article

**Topic:** Impact of Artificial Intelligence on Healthcare

**Tone:** Professional

**Length:** Medium

GenWrite generates an AI-written article based on the selected content type, topic, tone, and length.

---

## 🎯 Project Objective

The objective of this project is to demonstrate how **Generative AI** can be integrated into a practical software application.

The project focuses on:

- Understanding Generative AI
- Working with an AI API
- Prompt engineering
- Building an interactive user interface
- Integrating Python with a generative AI model
- Secure API key management
- Managing a software project using GitHub

---

## 🔮 Future Enhancements

- 🌍 Multi-language content generation
- 📊 AI-generated summaries
- ✏️ AI-powered grammar correction
- 🔄 Content rewriting and paraphrasing
- 💬 Chat-based writing assistant
- 📄 PDF and DOCX export
- 🎨 Improved user interface
- ☁️ Cloud deployment
- 🔐 User authentication
- 📈 Usage analytics

---

## 👨‍💻 Author

**Kailash Choudhary**

GitHub:  
https://github.com/kailashchoudhary09

---

## 📜 License

This project is created for educational and academic purposes.
