import pickle
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Book Recommender System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Recommender System")
st.write("Discover books based on collaborative filtering.")

# Load saved objects


@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("book_names.pkl", "rb") as f:
        book_names = pickle.load(f)

    with open("final_rating.pkl", "rb") as f:
        final_rating = pickle.load(f)

    with open("book_pivot.pkl", "rb") as f:
        book_pivot = pickle.load(f)

    return model, book_names, final_rating, book_pivot


model, book_names, final_rating, book_pivot = load_model()


def fetch_poster(suggestion):
    poster_urls = []

    # suggestion has shape (1, n_neighbors)
    for book_id in suggestion[0]:

        title = book_pivot.index[book_id]

        # Find matching book details
        matched_books = final_rating[
            final_rating["Title"] == title
        ]

        if matched_books.empty:
            poster_urls.append(None)
        else:
            poster_urls.append(
                matched_books.iloc[0]["img_url"]
            )

    return poster_urls


def recommend_book(selected_book, n_recommendations=5):

    # Check whether the selected book exists
    if selected_book not in book_pivot.index:
        return [], []

    book_id = book_pivot.index.get_loc(selected_book)

    distances, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1),
        n_neighbors=min(
            n_recommendations + 1,
            book_pivot.shape[0]
        )
    )

    recommended_books = []
    poster_urls = []

    for index in suggestions[0]:

        title = book_pivot.index[index]

        # Exclude the selected book itself
        if title == selected_book:
            continue

        matched_books = final_rating[
            final_rating["Title"] == title
        ]

        poster_url = None

        if not matched_books.empty:
            poster_url = matched_books.iloc[0]["img_url"]

        # Avoid duplicate titles
        if title not in recommended_books:
            recommended_books.append(title)
            poster_urls.append(poster_url)

        if len(recommended_books) == n_recommendations:
            break

    return recommended_books, poster_urls


selected_book = st.selectbox(
    "Search or select a book",
    book_names
)

if st.button("Show Recommendations", type="primary"):

    recommended_books, poster_urls = recommend_book(
        selected_book
    )

    if not recommended_books:
        st.warning("No recommendations found for this book.")

    else:
        st.subheader("Recommended Books")

        columns = st.columns(5)

        for i, (title, poster_url) in enumerate(
            zip(recommended_books, poster_urls)
        ):
            with columns[i % 5]:
                st.markdown(f"**{title}**")

                if poster_url and str(poster_url).startswith(
                    ("http://", "https://")
                ):
                    st.image(poster_url, width=150)
                else:
                    st.caption("Poster unavailable")
