from metapub import PubMedFetcher
import streamlit as st
import time
from stqdm import stqdm


def pubmed_search(search_term, num_of_articles):
    # create a PubMedFetcher object
    fetch = PubMedFetcher()
    # get the  PMID 
    pmids = fetch.pmids_for_query(search_term, retmax=num_of_articles)

    # get  articles
    articles_list = []

    for pmid in stqdm(pmids):
        # Fetching details for each PMID
        article_details = fetch.article_by_pmid(pmid)
        title = article_details.title
        abstract = article_details.abstract
        link = "https://pubmed.ncbi.nlm.nih.gov/" + pmid + "/"

        # Creating a dictionary for the current PMID
        pmid_dict = {
            "title": title,
            "summary": abstract,
            "link": link
        }

        # Appending the dictionary to the list
        articles_list.append(pmid_dict)

        # Sleep for 1/3rd of a second to limit to 3 requests per second
        time.sleep(1/3)

    return articles_list
