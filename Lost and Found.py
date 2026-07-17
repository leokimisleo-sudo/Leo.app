import streamlit as st
from transformers import pipeline
from openai import OpenAI
@st.cache_resource
def load_generator():
    return pipeline("text generation", model="gpt2")

generator = load_generator()

st.title("Lost and Found")
st.header("find your stuff")

item = st.text_input("What did you lose?", "placeholder = my backpack")

if st.button("Find item"):
    if item.strip() == "":
        st.warning("Are you sure?")
        st.stop()
    
    prompt = f"""
        You need to find lost items.
        The user has lost "{item}".
        Find their lost item and tell them where it is.
        """
    result = generator(prompt, max_new_tokens=50, do_sample=True, temperature=0.7, top_k=50, top_p=0.95, repetition_penalty=1.0, pad_token_id=50256)
    found_items = result[0]['generated_text']

    found_items = found_items.replace(prompt, "").strip()

    st.subheader("List of items matching your description:")
    st.write(found_items)