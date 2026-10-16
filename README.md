# 📚 Book Recommendation System Using Machine Learning

A book recommendation web application built with **Python, Machine Learning, and Streamlit**. It uses **collaborative filtering with a K-Nearest Neighbors (KNN) model** to recommend books similar to a selected title.

## 🚀 Live Demo

**Streamlit App:** Add your deployed Streamlit URL here.

## ✨ Features

- Select a book from a dropdown.
- Generate recommendations using a trained nearest-neighbors model.
- Display recommended book titles.
- Show book cover images when valid image URLs are available.
- Load pre-trained model and data objects from pickle files.
- Deploy the application using Streamlit Community Cloud.

## 🧠 How It Works

This project uses an **item-based collaborative filtering** approach:

1. **Data preparation:** Load the books and ratings datasets and merge ratings with book details.
2. **Filtering:** Retain active users and, if used in your training notebook, filter books by rating count.
3. **User–book matrix:** Create a pivot table with books as rows, users as columns, and ratings as values.
4. **Missing values:** Fill missing interactions with `0` for nearest-neighbor calculations.
5. **Model training:** Fit a `NearestNeighbors` model to the book-rating matrix.
6. **Recommendation:** Find books with similar rating patterns and display their titles.

> **Note:** Recommendations are based on similarities in user-rating patterns, not necessarily on book descriptions or genres. Missing ratings filled with zero represent unknown interactions, not explicit dislike ratings.

## 🛠️ Tech Stack

- **Python**
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Scikit-learn** — nearest-neighbor model
- **SciPy** — sparse matrix representation
- **Streamlit** — web application
- **Pickle** — save and load trained model and data objects
- **Git and GitHub** — version control and source hosting

## 📁 Project Structure

```text
book-recommender-system/
├── app.py
├── model.pkl
├── book_names.pkl
├── final_rating.pkl
├── book_pivot.pkl
├── requirements.txt
└── README.md
```

### Saved files

| File | Purpose |
|---|---|
| `app.py` | Streamlit application |
| `model.pkl` | Trained nearest-neighbor model |
| `book_names.pkl` | Book titles used in the selection dropdown |
| `final_rating.pkl` | Book and rating data used to retrieve book details and image URLs |
| `book_pivot.pkl` | User–book matrix used by the recommendation model |
| `requirements.txt` | Python dependencies |

The pickle filenames and contents must match the files loaded in `app.py`.

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd book-recommender-system
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create and activate a virtual environment (recommended)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
streamlit
numpy
pandas
scikit-learn
scipy
```

For deployment, use dependency versions compatible with those used to create the pickle files. Scikit-learn models saved with pickle may not load correctly across incompatible library versions.

### 4. Start the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, typically `http://localhost:8501`.

## ☁️ Deploy on Streamlit Community Cloud

1. Push the project files to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and select **Create app**.
4. Choose your repository and the `main` branch.
5. Set the main file path to `app.py`.
6. Select **Deploy**.
7. Add your public app URL to the **Live Demo** section above.

Ensure that all required pickle files are available to the deployed application. If they are too large for GitHub, consider Git LFS or suitable external artifact storage.

## 🧪 Usage

1. Open the application.
2. Search for or select a book from the dropdown.
3. Click **Show Recommendations**.
4. Browse the recommended titles and available cover images.

## 🔧 Troubleshooting

- **`FileNotFoundError`:** Check that all pickle files are present at the paths used by `app.py`.
- **`KeyError`:** Verify the actual column names in `final_rating.pkl`, especially the book-title and image-URL columns.
- **Model loading errors:** Check that deployed dependency versions are compatible with the environment used to save the model.
- **Missing covers:** Some records may not have valid or accessible image URLs.
- **Poor recommendations:** Experiment with data filtering and model settings, and evaluate recommendation quality using held-out user interactions.

## 🔒 Security and Compatibility

Only load pickle files from trusted sources. Loading an untrusted pickle file can execute arbitrary code.

Pickle files depend on the Python objects and library versions used when they were created. Keep the training and deployment environments compatible.

## 🔮 Future Improvements

- Recommend books based on a specific user's rating history.
- Evaluate results using metrics such as Precision@K and Recall@K.
- Experiment with cosine distance and matrix-factorization methods.
- Add book search, author information, and improved handling of duplicate editions.
- Improve the interface with book cards and more detailed metadata.

## 👤 Author

**Your Name**

- GitHub: Add your GitHub profile URL
- LinkedIn: Add your LinkedIn profile URL

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
