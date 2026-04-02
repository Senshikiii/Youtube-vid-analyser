'use client'

import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-white text-black">
      {/* Header */}
      <header className="border-b border-black">
        <div className="max-w-7xl mx-auto px-8 py-6 flex items-center justify-between">
          <div className="text-xl font-bold tracking-tight">
            LAINISREAL
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="border-b border-black">
        <div className="max-w-7xl mx-auto px-8 py-32 md:py-48">
          <h1 className="text-6xl md:text-[120px] font-black leading-none mb-12 tracking-tighter">
            UNDERSTAND<br/>
            VIDEOS
          </h1>
          
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-8">
            <p className="text-xl max-w-xl leading-tight">
              Paste a YouTube link. Get instant summaries, key points, and sentiment analysis.
            </p>
            <Link href="/analyze">
              <button className="px-8 py-4 bg-black text-white font-bold hover:bg-gray-900 transition text-lg w-fit">
                ANALYZE
              </button>
            </Link>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="border-b border-black">
        <div className="grid grid-cols-1 md:grid-cols-3">
          <div className="md:border-r border-black p-12">
            <h3 className="text-3xl font-black mb-6 leading-tight">INSTANT<br/>SUMMARIES</h3>
            <p className="text-base">
              Extract key takeaways from any video without wasting time.
            </p>
          </div>

          <div className="md:border-r border-black p-12">
            <h3 className="text-3xl font-black mb-6 leading-tight">SENTIMENT<br/>ANALYSIS</h3>
            <p className="text-base">
              Know the tone and mood of the video instantly.
            </p>
          </div>

          <div className="p-12">
            <h3 className="text-3xl font-black mb-6 leading-tight">KEY<br/>POINTS</h3>
            <p className="text-base">
              Focus only on what matters most.
            </p>
          </div>
        </div>
      </section>

      {/* How it Works */}
      <section className="border-b border-black">
        <div className="max-w-7xl mx-auto px-8 py-24">
          <h2 className="text-5xl md:text-6xl font-black mb-20 leading-tight">HOW IT<br/>WORKS</h2>
          
          <div className="space-y-16">
            <div className="flex gap-8 items-start">
              <div className="text-4xl font-black text-gray-300 w-16">01</div>
              <div>
                <h3 className="text-2xl font-black mb-2">PASTE URL</h3>
                <p className="text-gray-700 max-w-md">
                  Copy any YouTube link into the analyzer.
                </p>
              </div>
            </div>

            <div className="flex gap-8 items-start">
              <div className="text-4xl font-black text-gray-300 w-16">02</div>
              <div>
                <h3 className="text-2xl font-black mb-2">AI ANALYZES</h3>
                <p className="text-gray-700 max-w-md">
                  The system processes the transcript instantly.
                </p>
              </div>
            </div>

            <div className="flex gap-8 items-start">
              <div className="text-4xl font-black text-gray-300 w-16">03</div>
              <div>
                <h3 className="text-2xl font-black mb-2">GET INSIGHTS</h3>
                <p className="text-gray-700 max-w-md">
                  Receive summary, key points, and sentiment.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="border-b border-black">
        <div className="max-w-7xl mx-auto px-8 py-32">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-12">
            <h2 className="text-5xl md:text-6xl font-black leading-tight max-w-xl">
              START<br/>ANALYZING
            </h2>
            <Link href="/analyze">
              <button className="px-12 py-5 bg-black text-white font-black hover:bg-gray-900 transition text-lg w-fit">
                TRY NOW
              </button>
            </Link>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className="max-w-7xl mx-auto px-8 py-10 text-sm font-bold border-t border-black">
          <p>&copy; 2024 LAINISREAL</p>
        </div>
      </footer>
    </div>
  )
}
