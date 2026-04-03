# Youtube Video Analyzer

A full-stack app that fetches YouTube transcripts and uses Gemini to generate summaries and sentiment analysis.

---

## How it works

User pastes a YouTube URL  
→ Next.js frontend sends request to FastAPI backend  
→ Backend extracts video ID  
→ Fetches transcript using youtube-transcript-api  
→ Sends transcript to Gemini with a structured prompt  
→ Receives structured JSON (summary, sentiment, reasoning)  
→ Frontend displays the results  

---
## Tech Stack
**Backend**
- Python
- FastAPI
- Uvicorn
- youtube-transcript-api

**AI**
- Google Gemini API (google-genai)

**Frontend**
- Next.js
- Tailwind CSS
- shadcn/ui

---

## Running Locally

> Make sure both backend and frontend are running at the same time.

### 1. Clone the repository

git clone https://github.com/Senshikiii/Youtube-vid-analyser.git  
cd Youtube-vid-analyser  

---

### 2. Setup Backend

cd backend  

python -m venv venv  
source venv/bin/activate   # macOS/Linux  
venv\Scripts\activate      # Windows  

pip install -r requirements.txt  

uvicorn main:app --reload  

Backend runs on: http://127.0.0.1:8000  

---

###3. Setup Frontend

cd ../frontend  

npm install  
npm run dev  

Frontend runs on: http://localhost:3000  

---

### 4. Use the app

- Open http://localhost:3000  
- Paste a YouTube URL  
- Click **Analyze**

---

## Environment Variables

This project requires a Google Gemini API key.

1. Go to https://aistudio.google.com/app/apikey  
2. Create an API key  
3. Inside the `backend` folder, create a `.env` file:

GOOGLE_API_KEY=your_api_key_here  

---

## 📁 Project Structure

├── backend/  
│ ├── main.py            # FastAPI entry point  
│ ├── analyzer.py        # Core analysis logic  
│ ├── transcript.py      # YouTube transcript handling  
│ └── requirements.txt  
│  
├── frontend/  
│ ├── app/               # Next.js app router  
│ ├── components/        # UI components  
│ ├── lib/               # utilities/helpers  
│ ├── public/            # static assets  
│ └── package.json  
│  
├── LICENSE  
└── README.md  

---

## What I Learned

- Built my first full-stack application end-to-end  
- Understood how frontend and backend communicate in real-world apps  
- Worked with FastAPI and Next.js together  
- Integrated an AI API in a structured way  
- Learned proper Git workflow  
- Practiced building without over-relying on AI  

This project helped me understand how different parts of a system come together in practice.  
Definitely one of the most fun things I’ve built so far.

---

## Demo

Frontend (UI only): https://youtube-vid-analyser.vercel.app/  

> Backend is not deployed yet, so analysis requests won’t work in the live demo.
