
import arxiv
import streamlit as st

@st.cache_data(show_spinner="Fetching data from ArXiv")
def arxiv_search(search_term):
    """
    This function takes a search term and returns a list containing 
    the title and summary of the 100 most recent articles matching the search term.
    """

    # Construct the default API client.
    client = arxiv.Client(page_size = 100,
                          delay_seconds = 3.0,
                          num_retries = 3)

    # Search for the 10 most recent articles matching the keyword "quantum."
    search = arxiv.Search(
        query = search_term,
        max_results = 100,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    #This initiates the search and assigns the resulting generator to the variable results.
    results = client.results(search)

    # Initialize an empty list to hold the dictionaries.
    articles_list = []

    # Iterate over the generator, and for each result, create a dictionary and append it to the list.
    for result in results:
        article_dict = {
            "title": result.title,
            "summary": result.summary,
            "doi": result.doi,
            "pdf_url": result.pdf_url
        }
        articles_list.append(article_dict)

    return articles_list
