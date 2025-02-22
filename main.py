import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post

length_opt = ["Short", "Medium", "Long"]
lang_opt = ["English", "Hinglish"]


def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_tags())
    with col2:
        selected_length = st.selectbox("Length", options=length_opt)
    with col3:
        selected_lang = st.selectbox("Language", options=lang_opt)
    if st.button("Generate"):
        post = generate_post(selected_length, selected_lang, selected_tag)
        st.write(post)


if __name__ == "__main__":
    main()

