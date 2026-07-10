"use client";

import { useState, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowLeft,
  BrainCircuit,
  Loader2,
  Sparkles,
  ShieldCheck,
  AlertTriangle,
  Code2,
  Github,
  Layers3,
} from "lucide-react";
import Link from "next/link";

import {
  AnalysisProgressBar,
  Badge,
  Button,
  ChartContainer,
  EvidenceCard,
  MetricCard,
} from "@/components/ui";
import {
  motionTokens,
  spacing,
  typography,
  type Accent,
} from "@/lib/design-tokens";
import type { FeatureSnapshot, ScanRequest, ScanResult } from "@/lib/types";
import { cn } from "@/lib/utils";

const DEFAULT_API_URL = "http://localhost:8000";
const MAX_SCAN_RETRIES = 3;
const RETRY_BASE_DELAY_MS = 350;

class NonRetryableScanError extends Error {}

function getApiUrl() {
  if (typeof window !== "undefined") {
    const runtimeApiUrl =
      window.__CODESENSE_CONFIG__?.NEXT_PUBLIC_API_URL?.trim();
    if (runtimeApiUrl) return runtimeApiUrl;
  }

  return process.env.NEXT_PUBLIC_API_URL?.trim() || DEFAULT_API_URL;
}

function wait(ms: number) {
  return new Promise((resolve) => window.setTimeout(resolve, ms));
}

function parseErrorDetail(detail: unknown, fallback: string) {
  if (typeof detail === "string") return detail;
  if (detail && typeof detail === "object" && "message" in detail) {
    const message = (detail as { message?: unknown }).message;
    if (typeof message === "string") return message;
  }
  return fallback;
}

async function parseScanError(response: Response) {
  const body = await response.json().catch(() => null);
  return parseErrorDetail(body?.detail, `Server returned ${response.status}`);
}

async function fetchScanWithRetry(request: ScanRequest): Promise<ScanResult> {
  let lastError: Error | null = null;

  for (let attempt = 0; attempt <= MAX_SCAN_RETRIES; attempt += 1) {
    try {
      const response = await fetch(`${getApiUrl()}/api/v1/scan`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        const message = await parseScanError(response);
        if (response.status < 500 && response.status !== 429) {
          throw new NonRetryableScanError(message);
        }
        throw new Error(message);
      }

      return response.json() as Promise<ScanResult>;
    } catch (err) {
      if (err instanceof NonRetryableScanError) throw err;

      lastError =
        err instanceof Error ? err : new Error("Analysis request failed");
      if (attempt === MAX_SCAN_RETRIES) break;

      await wait(RETRY_BASE_DELAY_MS * 2 ** attempt);
    }
  }

  throw new Error(
    lastError?.message ||
      "The backend is unavailable. Check your API URL and try again.",
  );
}

const EXAMPLE_CODE = `def fibonacci(n: int) -> list[int]:
    """Generate a Fibonacci sequence up to n terms.

    Args:
        n: The number of terms to generate.

    Returns:
        A list of Fibonacci numbers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence: list[int] = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def is_prime(num: int) -> bool:
    """Check whether a number is prime using trial division."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True`;

const SIGNAL_LABELS: Record<string, string> = {
  docstring_ratio: "High docstring coverage across functions",
  type_annotation_ratio: "Consistent type annotations on parameters and returns",
  maintainability_index: "Elevated maintainability score (structured, clean code)",
  avg_identifier_length: "Long, descriptive identifier names",
  single_char_var_ratio: "Very few single-character variable names",
  comment_density: "High inline comment density",
  blank_line_ratio: "Regular spacing between code blocks",
  avg_cyclomatic_complexity: "Uniform control-flow complexity across functions",
  magic_number_count: "Few or no magic numbers used",
  assertion_count: "Assertions present for defensive coding",
  num_try_except: "Structured exception handling blocks",
  long_line_ratio: "Lines consistently under 80 characters",
};

const FEATURE_DISPLAY: Array<{
  key: keyof FeatureSnapshot;
  label: string;
  accent: Accent;
  format: (v: number) => number;
}> = [
  {
    key: "docstring_ratio",
    label: "Docstring coverage",
    accent: "cyan",
    format: (v) => Math.round(v * 100),
  },
  {
    key: "type_annotation_ratio",
    label: "Type annotations",
    accent: "emerald",
    format: (v) => Math.round(v * 100),
  },
  {
    key: "maintainability_index",
    label: "Maintainability",
    accent: "violet",
    format: (v) => Math.round(v),
  },
  {
    key: "comment_density",
    label: "Comment density",
    accent: "amber",
    format: (v) => Math.round(v * 100),
  },
  {
    key: "blank_line_ratio",
    label: "Blank line ratio",
    accent: "cyan",
    format: (v) => Math.round(v * 100),
  },
  {
    key: "avg_cyclomatic_complexity",
    label: "Avg. complexity",
    accent: "emerald",
    format: (v) => Math.min(Math.round(v * 10), 100),
  },
];

export default function ScanPage() {
  const [code, setCode] = useState("");
  const [filename, setFilename] = useState("unnamed.py");
  const [result, setResult] = useState<ScanResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = useCallback(async () => {
    if (!code.trim()) return;

    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await fetchScanWithRetry({ code, filename });
      setResult(data);
    } catch (err) {
      if (err instanceof NonRetryableScanError) {
        setError(err.message);
      } else if (err instanceof TypeError) {
        setError(
          "Unable to reach the CodeSense API. Verify NEXT_PUBLIC_API_URL and try again.",
        );
      } else {
        setError(
          err instanceof Error
            ? err.message
            : "Analysis failed. Please try again.",
        );
      }
    } finally {
      setIsLoading(false);
    }
  }, [code, filename]);

  const loadExample = useCallback(() => {
    setCode(EXAMPLE_CODE);
    setFilename("fibonacci.py");
    setResult(null);
    setError(null);
  }, []);

  return (
    <main className="min-h-screen overflow-hidden bg-background text-foreground">
      <div className="pointer-events-none fixed inset-0 -z-10 bg-grid" />
      <div className="pointer-events-none fixed inset-0 -z-10 bg-ambient" />

      {/* Nav */}
      <header className="sticky top-0 z-50 border-b border-line-subtle bg-background/80 backdrop-blur-xl">
        <nav
          aria-label="Scan navigation"
          className={cn(
            "mx-auto flex h-16 max-w-7xl items-center justify-between",
            spacing.pageX,
          )}
        >
          <Link
            href="/"
            className="flex items-center gap-3 text-sm text-muted-foreground transition-colors hover:text-foreground"
          >
            <span className="flex size-8 items-center justify-center rounded-md border border-cyan-300/25 bg-cyan-300/10 text-cyan-200">
              <Layers3 className="size-4" aria-hidden="true" />
            </span>
            <span className="font-semibold text-foreground">CodeSense</span>
          </Link>

          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="inline-flex h-9 items-center gap-2 rounded-md px-3 text-sm text-muted-foreground transition-colors hover:bg-white/5 hover:text-foreground"
            >
              <ArrowLeft className="size-4" aria-hidden />
              Home
            </Link>
            <a
              href="https://github.com/Samearth17/Codesense"
              className="inline-flex h-9 items-center gap-2 rounded-md px-3 text-sm text-muted-foreground transition-colors hover:bg-white/5 hover:text-foreground"
            >
              <Github className="size-4" aria-hidden />
              GitHub
            </a>
          </div>
        </nav>
      </header>

      {/* Content */}
      <div className={cn("mx-auto max-w-7xl py-10 lg:py-14", spacing.pageX)}>
        <motion.div
          initial={{ opacity: 0, y: 14 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{
            duration: motionTokens.duration.slow,
            ease: motionTokens.ease,
          }}
        >
          <h1 className={cn("text-foreground", typography.h2)}>
            Analyze Code Authorship
          </h1>
          <p className="mt-3 max-w-2xl text-muted-foreground">
            Paste Python code below and CodeSense will estimate whether it was
            written by a human or AI, using 24 explainable static-analysis
            features.
          </p>
        </motion.div>

        <div className="mt-10 grid gap-8 lg:grid-cols-[1.1fr_0.9fr]">
          {/* Left: Editor */}
          <motion.div
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
              duration: motionTokens.duration.slow,
              delay: 0.06,
              ease: motionTokens.ease,
            }}
            className="flex flex-col"
          >
            <div className="rounded-lg border border-line-strong bg-surface/95 shadow-2xl shadow-black/40 ring-1 ring-white/5">
              {/* Editor header */}
              <div className="flex items-center justify-between border-b border-line-subtle px-4 py-3">
                <div className="flex items-center gap-3">
                  <div
                    className="flex items-center gap-1.5"
                    aria-hidden="true"
                  >
                    <span className="size-2.5 rounded-full bg-rose-400" />
                    <span className="size-2.5 rounded-full bg-amber-300" />
                    <span className="size-2.5 rounded-full bg-emerald-300" />
                  </div>
                  <input
                    id="filename-input"
                    type="text"
                    value={filename}
                    onChange={(e) => setFilename(e.target.value)}
                    className="w-40 rounded border border-transparent bg-transparent px-2 py-0.5 text-xs text-muted-foreground transition-colors hover:border-line-subtle focus:border-line-strong focus:outline-none"
                    aria-label="Filename"
                  />
                </div>
                <button
                  onClick={loadExample}
                  className="inline-flex items-center gap-1.5 rounded-md px-2.5 py-1 text-xs text-muted-foreground transition-colors hover:bg-white/5 hover:text-foreground"
                >
                  <Code2 className="size-3.5" aria-hidden />
                  Load example
                </button>
              </div>

              {/* Textarea */}
              <textarea
                id="code-editor"
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="# Paste your Python code here..."
                spellCheck={false}
                className="h-[420px] w-full resize-none bg-transparent px-5 py-4 font-mono text-sm leading-6 text-foreground placeholder:text-muted-foreground/40 focus:outline-none"
              />
            </div>

            {/* Action bar */}
            <div className="mt-4 flex items-center gap-3">
              <Button
                id="analyze-button"
                onClick={handleAnalyze}
                disabled={isLoading || !code.trim()}
                size="lg"
                className="min-w-[160px]"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="size-4 animate-spin" aria-hidden />
                    Analyzing…
                  </>
                ) : (
                  <>
                    <Sparkles className="size-4" aria-hidden />
                    Analyze
                  </>
                )}
              </Button>
              <span className="text-xs text-muted-foreground">
                {code.length > 0
                  ? `${code.split("\n").length} lines \u00b7 ${
                      (code.length / 1024).toFixed(1)
                    } KB`
                  : "No code entered"}
              </span>
            </div>
          </motion.div>

          {/* Right: Results */}
          <motion.div
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
              duration: motionTokens.duration.slow,
              delay: 0.12,
              ease: motionTokens.ease,
            }}
          >
            <AnimatePresence mode="wait">
              {error ? (
                <ErrorPanel key="error" message={error} />
              ) : result ? (
                <ResultsPanel key="results" result={result} />
              ) : (
                <EmptyPanel key="empty" isLoading={isLoading} />
              )}
            </AnimatePresence>
          </motion.div>
        </div>
      </div>
    </main>
  );
}

function EmptyPanel({ isLoading }: { isLoading: boolean }) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.18 }}
      className="flex h-full min-h-[460px] flex-col items-center justify-center rounded-lg border border-dashed border-line-subtle p-8 text-center"
    >
      {isLoading ? (
        <div className="flex flex-col items-center gap-4">
          <div className="relative">
            <div className="size-16 rounded-full border-2 border-line-subtle" />
            <Loader2
              className="absolute inset-0 m-auto size-8 animate-spin text-cyan-300"
              aria-hidden
            />
          </div>
          <p className="text-sm text-muted-foreground">
            Extracting features and running model…
          </p>
        </div>
      ) : (
        <>
          <div className="flex size-14 items-center justify-center rounded-xl border border-line-subtle bg-white/[0.03]">
            <BrainCircuit
              className="size-7 text-muted-foreground/50"
              aria-hidden
            />
          </div>
          <p className="mt-5 text-sm font-medium text-foreground">
            Paste code to begin
          </p>
          <p className="mt-2 max-w-xs text-sm text-muted-foreground">
            CodeSense will extract 24 structural and style features, then
            estimate authorship using a trained XGBoost model.
          </p>
        </>
      )}
    </motion.div>
  );
}

function ErrorPanel({ message }: { message: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.97 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.97 }}
      transition={{ duration: 0.22, ease: motionTokens.ease }}
      className="flex min-h-[460px] flex-col items-center justify-center rounded-lg border border-rose-400/20 bg-rose-400/5 p-8 text-center"
    >
      <AlertTriangle className="size-8 text-rose-400" aria-hidden />
      <p className="mt-4 text-sm font-medium text-foreground">Analysis failed</p>
      <p className="mt-2 max-w-xs text-sm text-muted-foreground">{message}</p>
    </motion.div>
  );
}

function ResultsPanel({ result }: { result: ScanResult }) {
  const isAI = result.is_ai;
  const confidencePct = Math.round(result.confidence * 100);

  const signalDescriptions = result.top_signals.map(
    (s) => SIGNAL_LABELS[s] ?? s.replaceAll("_", " "),
  );

  return (
    <motion.div
      initial={{ opacity: 0, y: 12, scale: 0.98 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, y: -8 }}
      transition={{ duration: 0.36, ease: motionTokens.ease }}
      className="space-y-4"
    >
      {/* Verdict cards */}
      <div className="grid gap-3 sm:grid-cols-2">
        <MetricCard
          label={isAI ? "AI Probability" : "Human Probability"}
          value={`${confidencePct}%`}
          accent={isAI ? "violet" : "emerald"}
          description={
            isAI ? "Elevated AI-assistance signal" : "Human authorship signal"
          }
        />
        <MetricCard
          label={isAI ? "Human Probability" : "AI Probability"}
          value={`${100 - confidencePct}%`}
          accent={isAI ? "emerald" : "violet"}
          description={
            isAI ? "Manual authorship estimate" : "Low AI-assistance signal"
          }
        />
      </div>

      {/* Verdict badge */}
      <div className="flex items-center gap-3 rounded-md border border-line-subtle bg-white/[0.035] p-4">
        {isAI ? (
          <BrainCircuit className="size-5 text-violet-300" aria-hidden />
        ) : (
          <ShieldCheck className="size-5 text-emerald-300" aria-hidden />
        )}
        <div className="flex-1">
          <p className="text-sm font-medium text-foreground">
            {isAI ? "Likely AI-assisted code" : "Likely human-written code"}
          </p>
          <p className="mt-0.5 text-xs text-muted-foreground">
            {result.filename} \u00b7 {confidencePct}% confidence
          </p>
        </div>
        <Badge variant={isAI ? "violet" : "emerald"}>
          {result.label.toUpperCase()}
        </Badge>
      </div>

      {/* Evidence */}
      {signalDescriptions.length > 0 && (
        <EvidenceCard
          title="Top Signals"
          items={signalDescriptions}
          badge={`${signalDescriptions.length} signals`}
        />
      )}

      {/* Metric bars */}
      <ChartContainer title="Feature Breakdown">
        <div className="space-y-4">
          {FEATURE_DISPLAY.map((feat) => (
            <AnalysisProgressBar
              key={feat.key}
              label={feat.label}
              value={feat.format(result.features[feat.key])}
              accent={feat.accent}
            />
          ))}
        </div>
      </ChartContainer>
    </motion.div>
  );
}
