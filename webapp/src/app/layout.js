import './globals.css'

export const metadata = {
  title: 'PioneersVision - ASL Recognition',
  description: 'Real-time American Sign Language gesture recognition',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
