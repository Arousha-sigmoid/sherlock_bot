import streamlit as st
import json
import time
import pickle
from fuzzy_match import *
import plotly.graph_objects as go
import pandas as pd
pd.options.display.float_format = '{:.0f}'.format

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.15)

def write_text(text, streaming):
    # Inject custom CSS to set the text color of st.write to black
    if streaming:
        for line in text.split("\n\n"):
            st.write_stream(response_generator(line.strip()))
            time.sleep(0.1)
    else:
        st.write(text)


def display_content(response, user, streaming = True):
    if user == "assistant":
        with st.chat_message("assistant"):
        
            # Display any observations/responses
            write_text(response['answer'], streaming)
            
            # Display any image 
            if response.get('graphs',None):
                graphs = response['graphs']
                if graphs != []:
                    for topic in graphs:
                        if topic.get('text1','') != '':
                            write_text(topic['text1'],streaming)
                            #time.sleep(0.1)
                        if topic.get('code_path','') != '':
                            with open(topic['code_path'],'r') as f:
                                code = f.read()
                            exec(code,globals())
                            #time.sleep(0.3)
                            if streaming:
                                time.sleep(1)
                                st.plotly_chart(globals()['fig'])
                            else:
                                st.plotly_chart(globals()['fig'])
                        if topic.get('path','') != '':
                            st.image(topic['path'])
                            #time.sleep(0.1)
                        if topic.get('text2','') != '':
                            #st.write_stream(response_generator(topic.get('text2')))
                            write_text(topic['text2'],streaming)
            if response.get('link','') != '':
                st.write("**The cost to serve information is also available in the Supply Chain Dashboard**")
                st.link_button(label="Link To Dashboard", url = response['link'])
            
    elif user=='user':
        with st.chat_message("user"):
            st.markdown(message["content"])


st.set_page_config(page_title="QueryBot", 
                   layout='wide')

st.markdown("""
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-bottom: 0rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
                /* Apply color to all markdown text */
                .stMarkdown p {
                    color: #E31279 !important;
                }
                .sidebar-text {
                    font-size: 24px !important;
                    color:  #E31279 !important;
                }
        </style>
        """, unsafe_allow_html=True)



col1, col2, col3 = st.columns([1,13,3])
with col1:
    st.markdown('\n')
    st.image('images/chat-xxl.png', use_column_width='auto')
with col2:
    #st.markdown('\n')
    st.markdown('## Business Bot')

with col3:
    st.markdown('\n')
    if st.button("Clear Conversation", help="Click to reset the app"):
        if "messages" in st.session_state:
            st.session_state.messages = []
        st.rerun()

# CSS for custom styling
st.markdown("""
    <style> 
    .stChatInput{  
        border: 2px solid #E31279; !important;

    }  
    """, unsafe_allow_html=True
)


st.logo('images/Reckitt_logo.png', size='large')

# Apply the custom CSS class to the sidebar markdown text
#st.sidebar.title("Welcome To Our Data Companion Tool")
st.sidebar.markdown('<p class="sidebar-text"><strong>Welcome To Our Data Companion Tool</strong>', unsafe_allow_html=True)


st.sidebar.markdown("""
***Your Smart Data Assistant!***\n\n
*- Generate Data-Driven Insights from Multiple Datasets*\n\n
*- Retrieve Precise Answers*\n\n
*-  Effortlessly Navigate the Sherlock Dashboard*\n\n
*- Quickly Locate Relevant Tabs*\n\n
*-  All in One Seamless Experience!*
""")             

                    
# Loading the Questions and Answers Dictionary
qna = json.load(open("qna.json",'rb'))
query_lis = [qset['query'].lower() for qset in qna]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    display_content(message["content"],message["role"], streaming=False)




prompt = st.chat_input("Enter Your Query Here...", disabled = st.session_state.disabled)
if prompt:
    print("Given Query: ",prompt)
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Getting Answers
    response = None
    print("Checking for a Valid Query...")
    valid_q = check_closest_match(prompt)
    print("Matched to valid question:", valid_q)
    if query_lis.__contains__(valid_q):
        idx = query_lis.index(valid_q)
        response = qna[idx]['response']

    else:
        response = {}
        response["answer"] = "I don't have exposure to enough data to answer this question."

    # Display Assistant Response
    display_content(response,"assistant")
    # Add response message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
