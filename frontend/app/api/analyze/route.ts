import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  const body = await request.json()
  
  const response = await fetch('https://yt-analyzer-backend-cf39.onrender.com', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url: body.url }),
  })

  const data = await response.json()
  return NextResponse.json(data)
}
