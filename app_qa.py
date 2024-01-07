#import libraries
import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain import hub
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import sys

sys.path.append("src")
import knowledge
import create_docs

# Load the environment variables
load_dotenv()

#main function
def main():
    st.title("Research Paper Explorer")

    # Sidebar for input
    with st.sidebar:
        st.header("Settings")
        search_term = st.text_input("Enter Search Term:")

    if search_term:
        # Fetch the papers from the arXiv API (slower, get newest papers)
        articles_list = knowledge.arxiv_search(search_term)

        # Convert list of dictionaries to Document objects
        documents = create_docs.create_documents(articles_list)

        # Create vectorstore
        vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())

        # Retrieve and generate using the relevant snippets of the blog.
        retriever = vectorstore.as_retriever()
        prompt = hub.pull("rlm/rag-prompt")
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        rag_chain_from_docs = (
            RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
            | prompt
            | llm
            | StrOutputParser()
        )

        rag_chain_with_source = RunnableParallel(
            {"context": retriever, "question": RunnablePassthrough()}
        ).assign(answer=rag_chain_from_docs)

        # Streamlit input for user question
        user_question = st.text_input("Enter your question about the research papers here:")

        if user_question:
            output = rag_chain_with_source.invoke(user_question)

            # Display the answer
            st.write("Answer:", output["answer"])

            # Displaying PDF URLs
            pdf_urls = [doc.metadata["url"] for doc in output["context"]]
            st.write(f"PDF URLs: {', '.join(pdf_urls)}")

if __name__ == "__main__":
    main()
