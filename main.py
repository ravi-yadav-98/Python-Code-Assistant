import streamlit as st
from assistant import create_assistant
from user_proxy import StreamlitUserProxy
from utils import run_assistant, run_code_block


def main():
    # Configure Streamlit page
    st.set_page_config(page_title="AI Coding Assistant", layout="wide")
    st.title("AI Coding Assistant")

    # Initialize the assistant and user proxy
    assistant = create_assistant()
    user_proxy = StreamlitUserProxy("user_proxy")

    # Text area for user input
    user_input = st.text_area("Enter your coding task or question:", height=100)

    if st.button("Get Assistance"):
        if user_input:  # Ensure user input is provided
            # Get assistant responses and debug chat history
            chat_history = run_assistant(user_input, user_proxy, assistant)
            st.write("Debug: Full Chat History", chat_history)

            for msg in chat_history:
                role = msg['role']
                content = msg['content']
                st.write(f"Debug: Role: {role}, Content: {content}")

                if role == "human":
                    st.write("You:")
                    st.write(content)
                elif role == "assistant":
                    st.write("AI Assistant:")
                    st.write(content)

                    # Parse and debug code blocks
                    code_blocks = content.split("```")
                    st.write("Debug: Parsed Code Blocks", code_blocks)

                    for i in range(1, len(code_blocks), 2):
                        code = code_blocks[i].strip()
                        language = code.split("\n")[0] if "\n" in code else "plaintext"
                        code = "\n".join(code.split("\n")[1:])

                        if code.strip():  # Ensure the code block is non-empty
                            st.code(code, language=language)

                            # Add a unique key for each button to avoid conflicts
                            if st.button(f"Run Code Block {i // 2 + 1}", key=f"run_code_{i}"):
                                st.write(f"Running Code Block {i // 2 + 1}")
                                run_code_block(code, user_proxy)
                        else:
                            st.warning(f"Empty or invalid code block detected: Block {i // 2 + 1}")
        else:
            st.warning("Please enter a coding task or question.")


if __name__ == "__main__":
    main()
