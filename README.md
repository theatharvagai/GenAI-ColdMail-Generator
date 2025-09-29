# 📧 Cold Mail Generator

🧑‍💻 **Personal Project** • 🤖 **GenAI + LangChain** • 🗂️ **ChromaDB Vectorstore** • 🌐 **Streamlit Web App**

---

## 🎯 Project Motivation

This was my **personal learning project** to explore the world of **Generative AI** and modern frameworks like **LangChain** and **ChromaDB**.  
I wanted to understand how LLMs (Large Language Models) can be used beyond chat — specifically in automating something practical like **job application emails**.

I got the initial inspiration and guidance from the amazing [Codebasics YouTube video](https://www.youtube.com/watch?v=CO4E_9V6li0) and their [GitHub project](https://github.com/codebasics/project-genai-cold-email-generator).  
From there, I customized and extended the idea to fit my own portfolio and learning goals.

---

## 📌 Project Overview

The **Cold Mail Generator** is a **Streamlit-based GenAI app** that:
1. Scrapes job postings directly from a company’s career page.
2. Extracts key details such as **role, experience, skills, and description** using an LLM pipeline.
3. Queries a **vector database (ChromaDB)** of your personal portfolio to find relevant projects/links.
4. Automatically generates a **polished cold email** tailored to that job posting.

---

## ⚙️ How It Works

1. **🌐 Web Scraping:**  
   The `WebBaseLoader` pulls raw text data from a careers page URL.

2. **🧹 Text Cleaning:**  
   `utils.py` processes the raw HTML into structured, noise-free text.

3. **🤖 LLM Chain:**  
   The `Chain` class (using LangChain + Groq LLM) extracts jobs in JSON and generates custom emails.

4. **📂 Portfolio Matching:**  
   Your portfolio (stored as CSV + indexed in ChromaDB) is queried against job-required skills.

5. **📧 Email Generation:**  
   A personalized, professional email is created — complete with relevant portfolio links.

6. **🎨 Frontend:**  
   A simple **Streamlit app** provides an input field for the job page URL and displays the final email.

---

## 🛠️ Technologies Used

* **🐍 Python**
* **⚡ Streamlit:** Frontend web app
* **🧩 LangChain:** LLM framework
* **🧠 Groq LLM (DeepSeek R1):** For text extraction + email drafting
* **🗂️ ChromaDB:** Vectorstore for portfolio projects
* **📑 Pandas:** CSV data handling
* **🔑 dotenv:** API key management

---

## 🚀 Setup & Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/YOUR_USERNAME/cold-mail-generator.git
   cd cold-mail-generator
