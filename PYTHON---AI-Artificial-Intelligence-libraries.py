import tkinter as tk
from tkinter import messagebox

# Function to display information about a selected library
def display_info(library):
    info = {
        "TensorFlow": "TensorFlow is an open-source machine learning library developed by Google Brain.",
        "PyTorch": "PyTorch is an open-source machine learning library developed by Facebook's AI Research lab.",
        "scikit-learn": "scikit-learn is a widely used library for classical machine learning algorithms.",
        "Keras": "Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.",
        "NLTK": "NLTK is a leading platform for building Python programs to work with human language data.",
        "Gensim": "Gensim is a robust and efficient library for topic modeling and document similarity analysis.",
        "spaCy": "spaCy is a library for advanced natural language processing in Python and Cython.",
        "OpenCV": "OpenCV (Open Source Computer Vision Library) is primarily focused on computer vision tasks such as image and video processing.",
        "XGBoost": "XGBoost is an optimized gradient boosting library widely used for supervised learning tasks.",
        "Dlib": "Dlib is a versatile C++ library with Python bindings, known for its robust implementations of machine learning algorithms."
    }
    messagebox.showinfo(library, info.get(library, "Information not available"))

# Create the main window
root = tk.Tk()
root.title("Python AI Libraries Info")

# Create and pack buttons for each library
libraries = [
    "TensorFlow", "PyTorch", "scikit-learn", "Keras",
    "NLTK", "Gensim", "spaCy", "OpenCV", "XGBoost", "Dlib"
]

for library in libraries:
    btn = tk.Button(root, text=library, command=lambda lib=library: display_info(lib))
    btn.pack(pady=5)

root.mainloop()
