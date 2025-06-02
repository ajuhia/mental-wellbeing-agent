
# AI Mental Wellbeing Agent

This Streamlit-based application provides a supportive AI-powered mental health assistant. It uses Groq's LLaMA-3 model to generate a personalized emotional support plan based on the user's self-reported state.

## Overview

The application asks users a series of questions about their emotional wellbeing, sleep, stress levels, support systems, recent life events, and symptoms. Based on these inputs, it generates a structured three-part response:

- Assessment of current emotional state
- Action plan with recommended coping strategies
- Follow-up strategy for sustained wellbeing

The app is intended to provide compassionate support, not professional diagnosis or treatment.

## Features

- Built with Streamlit for interactive UI
- LLaMA-3 powered natural language generation via Groq
- Clean, user-friendly interface
- Expandable or single-tab output presentation
- Secure API key handling with Streamlit secrets

## Project Structure

```
mental-wellbeing-agent/
├── app.py                 # Main Streamlit interface
├── agent.py               # Prompt logic and LLM parsing
├── requirements.txt       # Python dependencies
├── README.md              # Project overview and instructions
└── .streamlit/
    └── secrets.toml       # Secure storage for API key (not pushed to GitHub)
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/mental-wellbeing-agent.git
   cd mental-wellbeing-agent
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add your Groq API key in `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your-groq-api-key"
   ```

5. Run the app:
   ```
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

1. Push this project to a public or private GitHub repository.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and click "Deploy an app".
3. Select your GitHub repo and set the main file path to `app.py`.
4. Under "Secrets", add:
   ```
   GROQ_API_KEY = your-groq-api-key
   ```
5. Click "Deploy".

The app will be hosted at:
```
https://<your-username>-<your-repo>.streamlit.app/
```

## Requirements

Ensure your `requirements.txt` contains the following (adjust if needed):
```
streamlit
langchain
langchain_groq
groq
```


## Disclaimer

This application is for educational and supportive purposes only. It is not a substitute for professional therapy or emergency mental health services. If you are in crisis, contact a licensed professional or emergency services immediately.
