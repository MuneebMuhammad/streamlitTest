import streamlit as st


def process_text(input_text, model="abc"):
    print("using model:", model)
    return f"processed text using model: {model}"

def main():

    t = st.text_area("Enter text here")

    if st.button("Process Text"):
        res = process_text(t)
        print(res)


if __name__ == "__main__":
    main()