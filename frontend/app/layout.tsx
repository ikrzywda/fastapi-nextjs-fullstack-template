import { Providers } from "@/lib/providers";

export default function RootLayout(props: React.PropsWithChildren) {
  return (
    <Providers>
      <html lang="en">
        <head>
          <meta charSet="utf-8" />
          <title>Redux Toolkit</title>
          <meta name="description" content="Redux Toolkit" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <link rel="icon" href="/favicon.ico" />
        </head>
        <body>{props.children}</body>
      </html>
    </Providers>
  );
}
