# LoanWise

LoanWise is a simple Streamlit web app that predicts whether a loan application is likely to be approved based on income and credit score.

## Project Overview

This project uses a trained machine learning model to evaluate user-provided financial inputs and return a quick approval decision. The app is designed to be lightweight, easy to run, and suitable for demos or small business decision-support tools.

## Features

- Simple and intuitive user interface
- Real-time loan approval prediction
- Input fields for income and credit score
- Result display for approved or rejected applications
- Easy setup using Python and Streamlit

## Suggested Project Name

LoanWise is a strong and professional name for this app because it is:

- easy to remember
- relevant to the finance domain
- clean and modern for a product-style project

## Tech Stack

- Python
- Streamlit
- Pandas
- scikit-learn
- Joblib

## Project Structure

```text
Loan_Approval/
├── app.py
├── requirements.txt
├── loan_approval_decision_tree.pkl
├── README.md
```

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

## How It Works

- The user enters their income and credit score.
- The app converts the inputs into a DataFrame.
- The saved machine learning model predicts the result.
- The app displays either a success or rejection message.

## Notes

- The model file should be present in the project directory before running the app.
- This project is a demo-style deployment and can be extended with more features such as loan amount, employment status, and debt-to-income ratio.

## License

This project is provided for educational and demonstration purposes.
