# 📧 Professional Email Generator

An AI-powered business email generation application built using OpenAI API and Gradio. This project helps users quickly generate professional, polite, and well-structured business emails for workplace communication.

---

## 🚀 Features

* Generate professional business emails instantly
* Clean and interactive Gradio-based UI
* Context-aware email drafting
* Secure API key management using environment variables
* Easily deployable and scalable

---

## 🛠️ Tech Stack

* **Python**
* **Gradio** (UI Framework)
* **OpenAI API** (GPT Models)
* **python-dotenv** (Environment Variable Management)

---

## 📸 Project Screenshot

![Application Screenshot](assets/img.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pawar-Sudharshan/EmailGenerator.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4️⃣ Run the Application

```bash
python app.py
```

The app will run locally at:

```
http://127.0.0.1:7860
```

---

## 📌 Usage

1. Enter your email intent (e.g., "Request leave for two days" or "Follow up on project status").
2. Click submit.
3. Receive a structured, professional business email instantly.

---

## 🔒 Security Note

* Never commit your `.env` file to GitHub.
* Always store API keys securely.
* Ensure `.env` is added to `.gitignore`.

---

## 💡 Future Improvements

* Add tone selector (Formal, Friendly, Concise)
* Add subject line toggle option
* Add copy-to-clipboard button
* Convert to full-stack version (API + Frontend)
* Deploy with authentication

---

## 👨‍💻 Author

**Sudharshan Pawar**

---

## ⭐ If You Like This Project

Give it a star on GitHub and feel free to fork or contribute!
