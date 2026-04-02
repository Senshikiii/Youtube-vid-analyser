'use client'

import Link from 'next/link'
import { useState } from 'react'

export default function AnalyzePage() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<null | {
    summary: string
    sentiment: string
    keyPoints: string[]
  }>(null)
  const [error, setError] = useState('')

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!url.trim()) {
      setError('Please paste a YouTube URL')
      return
    }

    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      })

      const data = await response.json()
      const parsed = typeof data === 'string' ? JSON.parse(data) : data

      setResult({
        summary: parsed.summary,
        sentiment: parsed.sentiment,
        keyPoints: parsed.key_points || []
      })
    } catch (err) {
      setError('Something went wrong. Make sure the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-stone-50">
      {/* Header */}
      <header className="border-b border-stone-200 bg-white">
        <div className="max-w-7xl mx-auto px-8 py-6 flex items-center justify-between">
          <Link href="/">
            <div className="text-lg font-semibold text-stone-900 hover:text-stone-600 transition cursor-pointer">
              LainIsReal
            </div>
          </Link>
          <Link href="/">
            <button className="text-sm text-stone-600 hover:text-stone-900 transition font-medium">
              ← Back
            </button>
          </Link>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-2xl mx-auto px-8 py-20">
        <div className="mb-16">
          <h1 className="text-4xl font-bold text-stone-900 mb-3">Analyze a video</h1>
          <p className="text-lg text-stone-600">Paste a YouTube link below to get a summary and sentiment analysis</p>
        </div>

        {/* Input Section */}
        <form onSubmit={handleAnalyze} className="mb-16">
          <div className="mb-6">
            <input
              type="text"
              placeholder="https://youtube.com/watch?v=..."
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              className="w-full bg-white border border-stone-200 rounded-lg px-5 py-4 text-stone-900 placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-stone-300 focus:border-transparent transition"
            />
          </div>
          
          {error && (
            <div className="text-sm text-red-600 mb-6 bg-red-50 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="px-8 py-3 bg-stone-900 text-white rounded-lg font-medium hover:bg-stone-800 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </form>

        {/* Results Section */}
        {result && (
          <div className="space-y-8 animate-in fade-in duration-300">
            {/* Summary */}
            <div className="bg-white rounded-lg p-8 border border-stone-200">
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-4">Summary</h2>
              <p className="text-lg text-stone-800 leading-relaxed">
                {result.summary}
              </p>
            </div>

            {/* Key Points */}
            <div className="bg-white rounded-lg p-8 border border-stone-200">
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-6">Key Points</h2>
              <ul className="space-y-4">
                {result.keyPoints.map((point, index) => (
                  <li key={index} className="flex gap-4">
                    <span className="text-stone-400 flex-shrink-0 mt-1">•</span>
                    <span className="text-stone-700 leading-relaxed">{point}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Sentiment */}
            <div className="bg-white rounded-lg p-8 border border-stone-200">
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-4">Sentiment</h2>
              <div className="flex items-center gap-3">
                <div className={`px-4 py-2 rounded-full font-semibold text-sm ${
                  result.sentiment === 'positive' 
                    ? 'bg-emerald-50 text-emerald-700' 
                    : result.sentiment === 'negative'
                    ? 'bg-rose-50 text-rose-700'
                    : 'bg-amber-50 text-amber-700'
                }`}>
                  {result.sentiment.charAt(0).toUpperCase() + result.sentiment.slice(1)}
                </div>
              </div>
            </div>

            {/* New Analysis Button */}
            <button
              onClick={() => {
                setUrl('')
                setResult(null)
              }}
              className="w-full py-3 text-stone-600 hover:text-stone-900 font-medium transition border border-stone-200 rounded-lg hover:bg-stone-50"
            >
              Analyze another video
            </button>
          </div>
        )}

        {/* Empty State */}
        {!result && !loading && (
          <div className="text-center py-12 text-stone-500">
            <p className="text-base">Paste a YouTube URL and click analyze to get started</p>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-stone-200 bg-white mt-20">
        <div className="max-w-7xl mx-auto px-8 py-8 text-sm text-stone-600">
          <p>&copy; 2024 LainIsReal. A personal project.</p>
        </div>
      </footer>
    </div>
  )
}
