


class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content  # Renamed from content to page_content
        self.metadata = metadata if metadata else {}

    def __repr__(self):
        return f"Document(page_content='{self.page_content}', metadata={self.metadata})"

    def __str__(self):
        return f"Page Content: {self.page_content}\nMetadata: {self.metadata}"

def create_documents(articles_list):
    """
    Takes a list of articles and returns a list of Document objects
    """
    documents = []
    for paper in articles_list:
        # Create a Document object for each paper
        document = Document(page_content=paper["summary"], metadata={"title": paper["title"], "link": paper.get("link", "No URL provided")})
        documents.append(document)
    return documents



