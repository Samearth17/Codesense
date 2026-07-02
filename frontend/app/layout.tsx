import type { Metadata } from "next";
import Script from "next/script";
import type { ReactNode } from "react";
import { ThemeProvider } from "@/components/providers/theme-provider";
import { ErrorBoundary } from "@/lib/components/error-boundary";
import "./globals.css";

export const metadata: Metadata = {
  title: "CodeSense",
  description: "Explainable AI-assisted code authorship analysis.",
};

const runtimeConfig = {
  NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL ?? "",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: ReactNode;
}>) {
  return (
    <html lang="en" className="dark" suppressHydrationWarning>
      <body>
        <Script
          id="codesense-runtime-config"
          strategy="beforeInteractive"
          dangerouslySetInnerHTML={{
            __html: `window.__CODESENSE_CONFIG__ = ${JSON.stringify(runtimeConfig).replace(/</g, "\\u003c")};`,
          }}
        />
        <ThemeProvider>
          <ErrorBoundary>{children}</ErrorBoundary>
        </ThemeProvider>
      </body>
    </html>
  );
}
