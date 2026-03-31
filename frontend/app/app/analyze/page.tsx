'use client'

import Link from 'next/link'
import { useState } from 'react'

export default function AnalyzePage() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<null | {
    summary: string
    sentiment: string
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

    // Simulated API call - replace with your actual backend
    setTimeout(() => {
      setResult({
        summary: 'This video provides a comprehensive overview of the topic, covering key concepts and practical applications. The content is well-structured and informative.',
        sentiment: 'positive'
      })
      setLoading(false)
    }, 1500)
  }

  return (
    <div className="min-h-screen bg-black text-white font-mono">
      {/* Header */}
      <header className="border-b border-white">
        <div className="max-w-full px-12 py-8 flex items-center justify-between">
          <Link href="/">
            <div className="text-xl font-bold tracking-widest hover:opacity-75 transition">
              LAINISREAL
            </div>
          </Link>
          <Link href="/">
            <button className="text-xs uppercase tracking-widest border border-white px-6 py-2 hover:bg-white hover:text-black transition">
              Back
            </button>
          </Link>
        </div>
      </header>

      {/* Main Section */}
      <section className="max-w-full px-12 py-20 border-b border-white">
        <div className="max-w-2xl">
          <h1 className="text-6xl font-black mb-12 tracking-tight">ANALYZE</h1>
          
          <form onSubmit={handleAnalyze} className="mb-12">
            <div className="border border-white mb-6">
              <input
                type="text"
                placeholder="Paste YouTube URL here"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="w-full bg-black text-white px-6 py-4 text-sm uppercase tracking-widest placeholder-gray-600 focus:outline-none"
              />
            </div>
            
            {error && (
              <div className="text-sm text-red-400 mb-6 uppercase tracking-widest">
                {error}
              </div>
            )}

            <button
              type="submit"
              disabled={loading}
              className="border border-white px-12 py-4 text-sm font-bold tracking-widest hover:bg-white hover:text-black transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'ANALYZING...' : 'ANALYZE'}
            </button>
          </form>

          {result && (
            <div className="border border-white p-8">
              <div className="mb-8">
                <div className="text-xs uppercase tracking-widest text-gray-400 mb-2">Summary</div>
                <p className="text-sm leading-loose">{result.summary}</p>
              </div>
              
              <div className="border-t border-white pt-8">
                <div className="text-xs uppercase tracking-widest text-gray-400 mb-2">Sentiment</div>
                <div className="text-2xl font-black uppercase tracking-tight">
                  {result.sentiment}
                </div>
              </div>
            </div>
          )}

          {!result && !loading && (
            <div className="text-sm text-gray-400 leading-loose">
              <p>Enter a YouTube URL to get instant analysis.</p>
              <p className="mt-4">Our system will extract the transcript and provide a summary with sentiment analysis.</p>
            </div>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer className="max-w-full px-12 py-12">
        <div className="text-xs text-gray-500 uppercase tracking-widest">
          <p>2024 LAINISREAL</p>
        </div>
      </footer>
    </div>
  )
}

