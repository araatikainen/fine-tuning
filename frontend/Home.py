import os
import streamlit as st
from utils import send_request


def chat_history():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])


def format_input() -> dict:
    "get last message from user"
    return {
        "message": st.session_state["messages"][-1]["content"],
        }



def generate_message():
    st.write("## Translate text from English to Finnish")
    chat_history()
    st.chat_input("Enter your message here...", key="prompt")
    if st.session_state["prompt"]:
        try:
            st.chat_message("user").write(st.session_state["prompt"])
            with st.spinner("Generating response..."):
                st.session_state["messages"].append({"role": "user", "content": st.session_state["prompt"]})
                body = format_input()
                endpoint = "api/generate"
                response = send_request(endpoint, body)
            if response["status_code"] == 200:
                st.chat_message("assistant").write(response["content"])
                st.session_state["messages"].append({"role": "assistant", "content": response["content"]})
            else:
                st.error(f"Failed to generate response: Status Code: {response['status_code']} {response['content']}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
        

def main():
    st.set_page_config(
        page_title="Chat",
        page_icon=":robot:"
    )
    st.title("Fine-tuning course")

    st.write(f"Translate english to finnish")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


    generate_message()


if __name__ == "__main__":
    main()