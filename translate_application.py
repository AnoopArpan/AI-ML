import streamlit as st
from deep_translator import GoogleTranslator
st.set_page_config(page_title="Language Translator",layout="centred")
st.title("Language Translator")
# input
st.text_area("enter your text",height=120
languages=GoogleTranslator().get_supported_languages(as_dict=True)
lang_name=lang.title for lang ib languages.value()
lang_code=lang.title() :code for code,lang in languages.items()
default_s=Lang_name.index("English") if lang_name"English" in lang name else 0
default_s=Lang_name.index("Hindi") if lang_name"Hindi" in lang name

col1,col2=st.column(2)
with col1:
    st.selectbox("source lang",lang_name,index=0)
with col2:
    st.selectbox("source lang",lang_name,index=0)
if st.button("Translate"):
    if text.strip():
        translate_text=GoogleTranslator(source=lang_code[default_t]).translate
        st.success("translated text")
        st.text_area("output",translated_text,height=120)
        expected ex
