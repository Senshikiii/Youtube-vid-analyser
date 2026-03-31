'use client'

import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-black text-white font-mono">
      {/* Header */}
      <header className="border-b border-white">
        <div className="max-w-full px-12 py-8">
          <div className="text-xl font-bold tracking-widest">
            LAINISREAL
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="border-b border-white">
        <div className="max-w-full px-12 py-32 md:py-48 grid md:grid-cols-2 gap-0">
          <div className="border-r border-white pr-12">
            <h1 className="text-6xl md:text-8xl font-black leading-tight mb-8 tracking-tight">
              DROP
              <br />
              A LINK.
            </h1>
            <p className="text-sm uppercase tracking-widest text-gray-300 mb-12 leading-loose">
              Paste any YouTube URL and get instant summaries with sentiment analysis.
            </p>
            <Link href="/analyze">
              <button className="border border-white px-12 py-4 text-sm font-bold tracking-widest hover:bg-white hover:text-black transition">
                ANALYZE
              </button>
            </Link>
          </div>
          
          <div className="pl-12 flex flex-col justify-center">
            <div className="space-y-6 text-sm font-mono">
              <div className="uppercase text-gray-400">Process</div>
              <div>1. PASTE URL</div>
              <div className="text-gray-400">2. AI EXTRACTS</div>
              <div className="text-gray-400">3. GET SIGNAL</div>
            </div>
          </div>
        </div>
      </section>

      {/* How it Works Section */}
      <section id="how" className="border-b border-white">
        <div className="max-w-full px-12 py-20">
          <h2 className="text-5xl font-black mb-16 tracking-tight">HOW IT WORKS</h2>
          
          <div className="grid md:grid-cols-3 gap-0">
            {/* Step 1 */}
            <div className="border-r border-white pr-8 pb-8 md:pb-0">
              <div className="text-5xl font-black mb-6">01</div>
              <h3 className="text-lg font-bold mb-4 uppercase tracking-wide">Paste YouTube URL</h3>
              <p className="text-sm text-gray-300 leading-loose">
                Drop any YouTube link. Works with tutorials, podcasts, lectures, everything.
              </p>
            </div>

            {/* Step 2 */}
            <div className="border-r border-white px-8 pb-8 md:pb-0">
              <div className="text-5xl font-black mb-6">02</div>
              <h3 className="text-lg font-bold mb-4 uppercase tracking-wide">AI Extracts</h3>
              <p className="text-sm text-gray-300 leading-loose">
                System fetches and processes video transcript automatically.
              </p>
            </div>

            {/* Step 3 */}
            <div className="pl-8">
              <div className="text-5xl font-black mb-6">03</div>
              <h3 className="text-lg font-bold mb-4 uppercase tracking-wide">Get Signal</h3>
              <p className="text-sm text-gray-300 leading-loose">
                Receive summary and sentiment analysis in seconds.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Tech Stack Section */}
      <section id="tech" className="border-b border-white">
        <div className="max-w-full px-12 py-20">
          <h2 className="text-5xl font-black mb-16 tracking-tight">BUILT WITH</h2>
          
          <div className="grid grid-cols-2 md:grid-cols-3 gap-0">
            {/* Python */}
            <div className="border-r border-b border-white pr-8 pb-8">
              <div className="text-sm font-bold uppercase tracking-widest text-gray-400 mb-2">Backend</div>
              <h3 className="text-lg font-bold">PYTHON</h3>
            </div>

            {/* FastAPI */}
            <div className="border-r border-b border-white px-8 pb-8 md:border-r">
              <div className="text-sm font-bold uppercase tracking-widest text-gray-400 mb-2">API</div>
              <h3 className="text-lg font-bold">FASTAPI</h3>
            </div>

            {/* Gemini API */}
            <div className="border-b border-white pl-8 pb-8">
              <div className="text-sm font-bold uppercase tracking-widest text-gray-400 mb-2">AI</div>
              <h3 className="text-lg font-bold">GEMINI API</h3>
            </div>

            {/* Next.js */}
            <div className="border-r border-b border-white pr-8 pb-8">
              <div className="text-sm font-bold uppercase tracking-widest text-gray-400 mb-2">Frontend</div>
              <h3 className="text-lg font-bold">NEXT.JS</h3>
            </div>

            {/* shadcn/ui */}
            <div className="border-r border-b border-white px-8 pb-8 md:border-r">
              <div className="text-sm font-bold uppercase tracking-widest text-gray-400 mb-2">UI</div>
              <h3 className="text-lg font-bold">SHADCN/UI</h3>
            </div>

            {/* YouTube API */}
            <div className="border-b border-white pl-8 pb-8">
              <div className="text-sm font-bold uppercase tracking-widest text-gray-400 mb-2">Data</div>
              <h3 className="text-lg font-bold">YOUTUBE API</h3>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="border-b border-white">
        <div className="max-w-full px-12 py-20 grid md:grid-cols-2 gap-0">
          <div className="border-r border-white pr-12">
            <h2 className="text-5xl font-black mb-8 leading-tight">READY?</h2>
            <p className="text-sm text-gray-300 mb-8 leading-loose">
              Start analyzing YouTube videos instantly. No credit card required.
            </p>
            <Link href="/analyze">
              <button className="border border-white px-12 py-4 text-sm font-bold tracking-widest hover:bg-white hover:text-black transition">
                START NOW
              </button>
            </Link>
          </div>
          <div className="pl-12 text-sm space-y-3 text-gray-400">
            <div>[ lainisreal.io ]</div>
            <div>status: live</div>
            <div>version: 1.0</div>
          </div>
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


