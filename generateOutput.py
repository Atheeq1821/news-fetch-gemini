from langchain_google_genai import ChatGoogleGenerativeAI
from constants import GOOGLE_API_KEY

def generate_linkedin_post(news_list,topic):
    """
    Create a professional LinkedIn-style post summarizing the news.
    Includes links for each article.

    """
    gemini = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=GOOGLE_API_KEY,
        temperature=0.7
    )

    if not news_list:
        return f"No news found for topic: {topic}"
    
    news_text = "\n".join([f"- {n['title']} ({n['url']})" for n in news_list])
    print("News-Text")
    print(news_text)
    prompt = f"""
                You are a professional content writer.
                Write a LinkedIn post about '{topic}' summarizing the following news in an engaging, professional tone.
                Include links for each news article.

                News:
                {news_text}
            """
    response = gemini.invoke(prompt)
    return response.content