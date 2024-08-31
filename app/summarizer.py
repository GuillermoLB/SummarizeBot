from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

def generate_summary(article_content):
    prompt = PromptTemplate(input_variables=["text"], template="Summarize the following article:\n\n{text}")
    llm = ChatOpenAI(model_name="gpt-4")
    
    # Use a RunnableSequence by chaining the prompt and llm directly
    sequence = prompt | llm
    
    # Invoke the sequence to get the AIMessage
    ai_message = sequence.invoke({"text": article_content})
    
    # Use StrOutputParser to extract the string content from AIMessage
    parser = StrOutputParser()
    summary = parser.invoke(ai_message)
    
    return summary


if __name__ == "__main__":
    article_content = "We and our vendors use cookies and similar methods (“Cookies”) to recognize visitors and remember their preferences. We also use them for a variety of purposes, including analytics, to measure marketing effectiveness and to target and measure the effectiveness of ads. You can accept or reject the use of Cookies for individual purposes below. If you previously accepted these methods through our prior banner, then we will use your data for targeting. Your preferences here are unrelated to Apple’s App Tracking Transparency Framework. Cookies, device or similar online identifiers (e.g. login-based identifiers, randomly assigned identifiers"
    summary = generate_summary(article_content)
    print(summary)
