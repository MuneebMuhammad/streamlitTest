import streamlit as st


def process_text(input_text, model="abc"):
    print("using model:", model)
    return f"processed text using model: {model}"

def main():

    st.selectbox("Select LLM:", ['GPT 4o mini', 'Gemini 1.5 Pro'], key='model_name')
    st.selectbox("Select type of law:", ['Family Law', 'Property Law', 'Civil Law', 'Corporate Law'], key='law_type')
    t = st.text_area("Enter text here")

    if st.button("Process Text"):
        res = process_text(t)
        st.write(res)


if __name__ == "__main__":
    main()