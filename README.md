# AI News Summarization & LinkedIn Post Generator

## You can find the working version here

[https://news-fetch-gemini.vercel.app/]

A Python-based AI agent that fetches the latest news articles on a given topic, summarizes them into a **professional LinkedIn-style post**, and provides article links and image suggestions. Built using **Google Gemini (ChatGoogleGenerativeAI)** and **GNews API**, with a flexible architecture suitable for production.

---

## Features

- Fetch top 5 latest news articles on any topic via **GNews API**.
- Generate **engaging LinkedIn-style summaries** using **Google Gemini**.
- Include **article links** and **image suggestions** for enhanced posts.
- Output structured JSON suitable for **frontend consumption**.
- Flexible architecture designed for **production scalability**.

---

## Output Example

```json
{
  "topic": "Artificial Intelligence",
  "news_sources": [
    "https://example.com/article1",
    "https://example.com/article2",
    "https://example.com/article3"
  ],
  "linkedin_post": "AI is transforming industries... [generated text]",
  "image_suggestion": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ]
}
```

## Tech Stack

- Python 3.11+

- LangChain + LangGraph

- Google Gemini (ChatGoogleGenerativeAI)

- GNews API

## For environment variables

- I have used constants.py file.
