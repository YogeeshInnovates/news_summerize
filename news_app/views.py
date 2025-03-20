


# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import requests
# from googletrans import Translator
# from gtts import gTTS
# from io import BytesIO
# from textblob import TextBlob

# # News API details
# API_KEY = "pub_74947f470a16ff4e8dbf7b2e875f7262dc1dd"
# BASE_URL = "https://newsdata.io/api/1/news"

# def fetch_news(company_name):
#     params = {"apikey": API_KEY, "q": company_name, "language": "en"}
#     response = requests.get(BASE_URL, params=params)
#     data = response.json()

#     articles = []
#     seen_titles = set()  # Track unique news titles

#     if "results" in data:
#         for entry in data["results"]:
#             title = entry.get("title", "No Title")
#             # summary = entry.get("description", "No Summary Available")
#             summary = entry.get("description", "No Summary Available") or "No Summary Available"  # ✅ Ensure it's a string
#             link = entry.get("link", "")

#             # Check if the title is already added
#             if title in seen_titles:
#                 continue  # Skip duplicate news

#             seen_titles.add(title)  # Add title to the seen set
#             sentiment_score = TextBlob(summary).sentiment.polarity
#             if sentiment_score > 0:
#                 sentiment = "Positive"
#             elif sentiment_score < 0:
#                 sentiment = "Negative"
#             else:
#                 sentiment = "Neutral"
#             articles.append({"title": title, "summary": summary,"sentiment": sentiment, "link": link})

#             # Stop when we collect 10 unique articles
#             if len(articles) == 10:
#                 break  

#     return articles

# @csrf_exempt
# def news_view(request):
#     company = request.GET.get("company", "Tesla")
#     news_articles = fetch_news(company)

#     if not news_articles:
#         return JsonResponse({"error": "No news found"}, status=404)

#     translator = Translator()
#     response_data = []

#     for i, article in enumerate(news_articles):
#         english_summary = article["summary"]

#         try:
#             # Translate to Hindi
#             translated_text = translator.translate(english_summary, src="en", dest="hi").text

#             # Generate speech in memory
#             mp3_fp = BytesIO()
#             tts = gTTS(text=translated_text, lang="hi")
#             tts.write_to_fp(mp3_fp)

#             # Convert BytesIO to response
#             mp3_fp.seek(0)
#             # audio_url = f"http://127.0.0.1:8000/news_audio?index={i}&company={company}"
#             audio_url = request.build_absolute_uri(f"/news_audio?index={i}&company={company}")


#         except Exception as e:
#             print(f"Translation failed: {e}")
#             translated_text = "Translation failed"
#             audio_url = None

#         response_data.append({
#             "title": article["title"],
#             "summary": english_summary,
#             "sentiment": article["sentiment"],  # Add sentiment
#             "translated_summary": translated_text,
#             "audio_url": audio_url,
#             "link": article["link"]
#         })

#     return JsonResponse({"company": company, "articles": response_data})

# # 🎵 Serve Audio Stream Dynamically
# @csrf_exempt
# def news_audio(request):
#     company = request.GET.get("company", "Tesla")
#     index = int(request.GET.get("index", 0))

#     # Fetch news again (to ensure consistency)
#     news_articles = fetch_news(company)

#     if index >= len(news_articles):
#         return JsonResponse({"error": "Invalid index"}, status=400)

#     translator = Translator()
#     translated_text = translator.translate(news_articles[index]["summary"], src="en", dest="hi").text

#     # Generate speech in memory
#     mp3_fp = BytesIO()
#     tts = gTTS(text=translated_text, lang="hi")
#     tts.write_to_fp(mp3_fp)

#     # Return MP3 as a response
#     mp3_fp.seek(0)
#     return HttpResponse(mp3_fp.read(), content_type="audio/mpeg")






from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
from textblob import TextBlob
import re
# News API details
API_KEY = "pub_74947f470a16ff4e8dbf7b2e875f7262dc1dd"
BASE_URL = "https://newsdata.io/api/1/news"


def extract_topics(text):
    """Extract potential topics from title/description using keywords."""
    keywords = ["finance", "technology", "sports", "health", "politics", "business", "science", "entertainment"]
    found_topics = [word.capitalize() for word in keywords if re.search(rf"\b{word}\b", text, re.IGNORECASE)]
    return ", ".join(found_topics) if found_topics else "General"

def fetch_news(company_name):
    params = {"apikey": API_KEY, "q": company_name, "language": "en"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    articles = []
    seen_titles = set()  # Track unique news titles

    if "results" in data:
        for entry in data["results"]:
            title = entry.get("title", "No Title")
            # summary = entry.get("description", "No Summary Available")
            summary = entry.get("description", "No Summary Available") or "No Summary Available"  # ✅ Ensure it's a string
            link = entry.get("link", "")

            # Check if the title is already added
            if title in seen_titles:
                continue  # Skip duplicate news
            topics_covered = extract_topics(f"{title} {summary}") 

            seen_titles.add(title)  # Add title to the seen set
            sentiment_score = TextBlob(summary).sentiment.polarity
            if sentiment_score > 0:
                sentiment = "Positive"
            elif sentiment_score < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
            articles.append({"title": title, "summary": summary,"sentiment": sentiment,"topics_covered":topics_covered, "link": link})

            # Stop when we collect 10 unique articles
            if len(articles) == 10:
                break  

    return articles

@csrf_exempt
def news_view(request):
    company = request.GET.get("company", "Tesla")
    news_articles = fetch_news(company)

    if not news_articles:
        return JsonResponse({"error": "No news found"}, status=404)

    translator = Translator()
    response_data = []

    for i, article in enumerate(news_articles):
        english_summary = article["summary"]
        topics_covered=article["topics_covered"]
        

        try:
            # Translate to Hindi
            translated_text = translator.translate(english_summary, src="en", dest="hi").text

            # Generate speech in memory
            mp3_fp = BytesIO()
            tts = gTTS(text=translated_text, lang="hi")
            tts.write_to_fp(mp3_fp)

            # Convert BytesIO to response
            mp3_fp.seek(0)
            # audio_url = f"http://127.0.0.1:8000/news_audio?index={i}&company={company}"
            audio_url = request.build_absolute_uri(f"/news_audio?index={i}&company={company}")


        except Exception as e:
            print(f"Translation failed: {e}")
            translated_text = "Translation failed"
            audio_url = None

        response_data.append({
            "title": article["title"],
            "summary": english_summary,
            "sentiment": article["sentiment"],  # Add sentiment
            "translated_summary": translated_text,
            "topics_covered":topics_covered,
            "audio_url": audio_url,
            "link": article["link"]
        })

    return JsonResponse({"company": company, "articles": response_data})

# 🎵 Serve Audio Stream Dynamically
@csrf_exempt
def news_audio(request):
    company = request.GET.get("company", "Tesla")
    index = int(request.GET.get("index", 0))

    # Fetch news again (to ensure consistency)
    news_articles = fetch_news(company)

    if index >= len(news_articles):
        return JsonResponse({"error": "Invalid index"}, status=400)

    translator = Translator()
    translated_text = translator.translate(news_articles[index]["summary"], src="en", dest="hi").text

    # Generate speech in memory
    mp3_fp = BytesIO()
    tts = gTTS(text=translated_text, lang="hi")
    tts.write_to_fp(mp3_fp)

    # Return MP3 as a response
    mp3_fp.seek(0)
    return HttpResponse(mp3_fp.read(), content_type="audio/mpeg")



