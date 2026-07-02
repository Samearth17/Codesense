"use client";

import { Component, type ErrorInfo, type ReactNode } from "react";

type ErrorBoundaryProps = {
  children: ReactNode;
};

type ErrorBoundaryState = {
  error: Error | null;
};

export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  state: ErrorBoundaryState = { error: null };

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("CodeSense render error", { error, errorInfo });
  }

  render() {
    if (this.state.error) {
      return (
        <main className="flex min-h-screen items-center justify-center bg-background px-6 text-foreground">
          <section className="max-w-md rounded-lg border border-line-subtle bg-surface/95 p-6 text-center shadow-2xl shadow-black/30">
            <p className="text-sm font-semibold text-rose-300">Something went wrong</p>
            <h1 className="mt-3 text-2xl font-semibold">CodeSense hit a rendering error.</h1>
            <p className="mt-3 text-sm text-muted-foreground">
              Refresh the page to retry. If the problem continues, check the browser console for the captured error details.
            </p>
            <button
              type="button"
              onClick={() => window.location.reload()}
              className="mt-5 inline-flex h-10 items-center justify-center rounded-md bg-cyan-300 px-4 text-sm font-semibold text-slate-950 transition hover:bg-cyan-200"
            >
              Reload page
            </button>
          </section>
        </main>
      );
    }

    return this.props.children;
  }
}
