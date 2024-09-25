# Helper functions for Gemini, Brave search & BS4 scraping

from dotenv import load_dotenv
import google.generativeai as genai
import os
import requests
from time import sleep
import json
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv()
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# gemini api config
genai.configure(api_key=GEMINI_API_KEY)
model_json = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={"response_mime_type": "application/json"},
)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_search_results(search_query: str):
    headers = {"Accept": "application/json", "X-Subscription-Token": BRAVE_API_KEY}
    response = requests.get(
        "https://api.search.brave.com/res/v1/web/search",
        params={
            "q": search_query,
            "count": 3,  # Max number of results to return
        },
        headers=headers,
        timeout=60,
    )
    if not response.ok:
        raise Exception(f"HTTP error {response.status_code}")
    sleep(1)  # avoid Brave rate limit
    return response.json().get("web", {}).get("results")


def generate_search_response(context, user_question):
    SEARCH_PROMPT = f"""
    You are an expert at summarizing search results and providing concise answers to user question.

    USER QUESTION: {user_question}

    CONTEXT: {context}
    """
    response = model.generate_content(SEARCH_PROMPT).text
    return response


def generate_search_queries(user_question):
    SEARCH_PROMPT = f"""
    You are an expert at generating search queries for the Brave search engine.
    Generate three search queries that are relevant to this question.

    {user_question}

    Format: {{"queries": ["query_1", "query_2", "query_3"]}}
    """
    response = model_json.generate_content(SEARCH_PROMPT)
    search_result = json.loads(response.text)
    return search_result


def get_unique_search_results(search_queries):
    urls_seen = set()
    web_search_results = []
    for query in search_queries["queries"]:
        search_results = get_search_results(query)
        for result in search_results:
            url = result.get("url")
            if not url or url in urls_seen:
                continue

            urls_seen.add(url)
            web_search_results.append(result)
    return web_search_results


def get_text_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text
        text = soup.get_text()

        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        # Drop blank lines
        text = "\n".join(chunk for chunk in chunks if chunk)

        return text
    except requests.RequestException as e:
        # print(f"An error occurred: {e}")
        return None


def fetch_metadata(user_question):
    search_queries = generate_search_queries(user_question)
    print(search_queries)
    search_results = get_unique_search_results(search_queries)
    metadata = [
        result.get("profile") for result in search_results if result.get("profile")
    ]
    print(metadata)
    return metadata


def generate_answer(user_question, metadata):
    context = ""
    for profile in metadata:
        page_text = get_text_from_url(profile.get("url"))
        if page_text is not None:
            context += page_text
    response = generate_search_response(context, user_question)
    return response
