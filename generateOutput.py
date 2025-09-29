

from utils import gemini_initialization


def generate_linkedin_post(news_list,topic):
    """
    Create a professional LinkedIn-style post summarizing the news.
    Includes links for each article.

    """
    gemini = gemini_initialization()

    if not news_list:
        return f"No news found for topic: {topic}"
    
    news_text = "\n".join([f"- {n['title']} ({n['url']})" for n in news_list])

    prompt = f"""
                You are a professional content writer.
                Write a LinkedIn post about '{topic}' summarizing the following news in an engaging, professional tone.
                Include links for each news article.

                News:
                {news_text}
                *** Note : Dont start linkedin post content like 'Here's a LinkedIn post....' , 'Your linkedin Content .....' etc.
                JUST START WITH DIRECT CONTENT
            """
    response = gemini.invoke(prompt)
    return response.content