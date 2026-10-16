# Book Recommendation System

Hey there! This is a simple book recommendation web app I built using Python, Machine Learning, and Streamlit. It uses collaborative filtering (specifically a KNN model) to recommend books that are similar to whatever title you select from the list.

## Live Demo

Check out the live app here: [https://book-recommender-system-6ggx2thsh9etcpeajbqikf.streamlit.app/]

## Features

* Select any book from the dropdown list
* Get top recommendations powered by nearest neighbors algorithm
* Shows recommended book titles along with cover images (if available)
* Uses pre-trained model and data saved as pickle files
* Easy to deploy on Streamlit Cloud

## How It Works

The recommendation engine uses item-based collaborative filtering:

1. **Data prep:** Combined books and user ratings dataset together.
2. **Filtering:** Kept active users and filtered out books with very few ratings so the model works better.
3. **User-Book Matrix:** Created a pivot table where rows are books, columns are users, and values are ratings.
4. **Missing Values:** Replaced missing ratings with 0s for distance calculation.
5. **Training:** Fit a `NearestNeighbors` model on the pivot table matrix.
6. **Recommending:** Finds closest books based on user rating patterns.

Note: Keep in mind that recommendations are based purely on how users rated books, not on genres or plot summaries. Also, 0 ratings just mean the user hasn't rated the book, not that they hated it!

## Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* SciPy
* Streamlit
* Pickle
* Git & GitHub

## Project Structure

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

### Pickled Files Info

* `app.py` - Main Streamlit code
* `model.pkl` - Trained KNN model
* `book_names.pkl` - List of book names for dropdown
* `final_rating.pkl` - Main dataframe for getting details like image URLs
* `book_pivot.pkl` - Pivot table used for finding nearest neighbors
* `requirements.txt` - Required packages

Make sure the pickle file names in `app.py` match these exact names or it'll throw an error.

## Running Locally

### 1. Clone this repo

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd book-recommender-system

```

### 2. Set up virtual env (recommended)

On Windows:

```cmd
python -m venv .venv
.venv\Scripts\activate

```

On Mac / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Install packages

```bash
pip install -r requirements.txt

```

Note: Make sure your library versions (specially scikit-learn) match or are close to the ones used for training, otherwise pickle might fail to load properly.

### 4. Run the app

```bash
streamlit run app.py

```

It should open up automatically in your browser at `http://localhost:8501`.

## Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to Streamlit Community Cloud and sign in with GitHub
3. Click "New app", select your repo and branch
4. Set main file path as `app.py`
5. Click Deploy!

If your pickle files is too big for normal git push, you might need Git LFS or host them somewhere else like Drive or S3.

## Troubleshooting / Common Issues

* **FileNotFoundError:** Check if all `.pkl` files are in the same folder as `app.py`.
* **KeyError:** Make sure column names in `final_rating.pkl` match what `app.py` expects.
* **Pickle / Model loading error:** Usually happens due to scikit-learn version mismatch between local and deployment environment.
* **Missing cover images:** Some image URLs in dataset might be broken or outdated.

## Future Plans

* Personal user-based recommendations based on rating history
* Try out matrix factorization or cosine similarity
* Better UI with proper book cards and author details
* Handle duplicate book editions better

## Author

Made by **ABISHEIK R**

* GitHub: [https://github.com/Devabisheik]

Feel free to star the repo if you found this helpful!