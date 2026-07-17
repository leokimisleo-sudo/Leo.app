import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Story Generator", page_icon="📝")

st.title("AI Story Generator")
st.write("Use your authentic intelligence")

@st.cache_resource
def load_generator():
    return pipeline("text generation", model="gpt2")

generator = load_generator()

topic = st.text_input("Enter a topic for your story:", "placeholder = gurg the dinosaur was a dinosaur named gurg")

genre = st.selectbox("Select a genre for your story:", ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror","Comedy","Adventure","Thriller","Historical Fiction","Dystopian","Magical Realism","Fairy Tale","Mythology","Supernatural","Western","Satire","Political Fiction","Young Adult (YA)","Children's Literature","Anime","Cyberpunk","Steampunk","Post-Apocalyptic","Urban Fantasy","Time Travel","Space Opera","Epic Fantasy","High Fantasy","Low Fantasy","Sword and Sorcery","Dark Fantasy","Romantic Comedy","Paranormal Romance","Gothic Fiction","Noir Fiction","Spy Fiction","Legal Thriller","Medical Thriller","Psychological Thriller","Crime Fiction","Detective Fiction","Espionage Fiction","Military Fiction","War Fiction","Historical Romance","Contemporary Romance","Erotic Romance","Chick Lit"])

length = st.slider("story length", 100, 400, 200, step=50)

if st.button("Generate Story"):
    if topic.strip() == "":
        st.warning("Use your creativity")
        st.stop()

    prompt = f"""

    story:

    The second you read this,

        with = st.spinner("Touch some grass"):
        
            result = generator(prompt, max_new_tokens=length, do_sample=True, temperature=0.7, top_k=50, top_p=0.95, repitition penalty=1.2, pad_token_id=50256)

        story = result[0]['generated_text']
            """
        
    story = story.replace(prompt, "").strip()

    st.subheader("Generated Story:")
    st.write(story)