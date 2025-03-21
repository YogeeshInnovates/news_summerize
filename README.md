# 📰 News Summarization & Sentiment Analysis

## 📌 Project Overview
This project provides a **news summarization and sentiment analysis** tool. It fetches news articles based on a company name, summarizes them, analyzes sentiment, translates summaries into Hindi, and generates an audio version of the translation.

## 🔧 Tech Stack
### **Backend (Django API)**
- **Framework:** Django
- **Language:** Python
- **APIs Used:**
  - [NewsData.io API](https://newsdata.io/) (For fetching news articles)
  - Google Translate API (For Hindi translation)
  - gTTS (Google Text-to-Speech for audio conversion)
  - TextBlob (For sentiment analysis)
- **Hosting:** [Render](https://news-summerize-1.onrender.com/)

### **Frontend (Streamlit UI)**
- **Framework:** Streamlit
- **Language:** Python
- **API Calls:** Requests data from Django backend
- **Hosting:** [Hugging Face Spaces](https://huggingface.co/spaces/Yogeeshhegde778/news-summarization)

## 🚀 Features
✅ Fetches the latest news articles based on a company name
✅ Provides a summarized version of each article
✅ Analyzes the sentiment (Positive, Neutral, Negative)
✅ Translates the summary into Hindi
✅ Generates an audio version of the translated summary
✅ Displays links to full articles

## 📌 API Endpoints (Backend - Django)
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/news_view`  | GET    | Fetches news, analyzes sentiment, translates summary, and provides audio URL |
| `/news_audio` | GET    | Converts the translated summary into speech and returns an audio file |

## 💻 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YogeeshInnovates/news_summerize.git
cd news_summerize
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run Django Server (Backend)**
```bash
python manage.py runserver
```

### **4️⃣ Run Streamlit App (Frontend)**
```bash
streamlit run app.py



Hosted on Hugging Face

Access the live app: https://huggingface.co/spaces/Yogeeshhegde778/news-summarization

If you want to run Streamlit locally:
```
## 📡 Deployment
- **Backend Deployed on Render:** [news-summerize-1.onrender.com](https://news-summerize-1.onrender.com/)
- **Frontend Deployed on Hugging Face:** [news-summarization](https://Yogeeshhegde778-news-summarization.hf.space/ )

## 📜 License
This project is open-source and available under the **MIT License**.

---

⚡ **Developed by [Yogeesh Hegde](https://github.com/YogeeshInnovates/news_summerize)** 🚀

