from qa_tool import*
from csv_load import*
from data_analysis import*
from summarize_prompt import QA_PROMPT_TEMPLATE
from download_report import create_pdf
import streamlit as st



df = DataAnalysis('D:\project\chatbot_stock\data\dataframe.csv')

csv_ = CSVLoaderCustom(path_file='D:\project\chatbot_stock\data\dataframe.csv')
loader = csv_.split_load()

"""
Initialize the chatbot instance with the selected model and configuration.
"""
chat_instance = Chat(
    model_name="llama-3.1-70b-versatile",        
    API_KEY="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",
    temperature=0.2,
    db_path="D:\project\chatbot_stock\data",
    loader=loader,
    prompt=QA_PROMPT_TEMPLATE
    )



st.title('Stock tips bot')

user_query = st.text_input("Hello! How is the stock market performing today? Please provide me with the latest information on stock indices and notable stocks.")
answer = None
if st.button('Answer'):
    if user_query:
        try:
            answer = chat_instance.qa_bot(user_query)
            st.write("Answer:", answer)
        except Exception as e:
            st.write("An error occurred:", e)
    else:
        st.write("Please enter a question.")


if answer:
    pdf_buffer = create_pdf(answer)
    st.download_button(
        label="Download PDF file",
        data=pdf_buffer,
        file_name="Report.pdf",
        mime="application/pdf"
    )

st.title('S&P 500 Index Value Trends')
data_file = "D:\project\chatbot_stock\data\sp500_index.csv"

if data_file is not None:
    analysis = DataAnalysis(data_file)
    df_processed = analysis.create_df()
    st.line_chart(df_processed)