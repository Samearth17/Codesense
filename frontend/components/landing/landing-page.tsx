"use client";

import {
  ArrowRight,
  BarChart3,
  BookOpen,
  BrainCircuit,
  Code2,
  FileSearch,
  Github,
  Layers3,
  LineChart,
  PanelTop,
  ShieldCheck,
  Sparkles,
} from "lucide-react";
import { motion } from "framer-motion";
import type { ComponentType, ReactNode } from "react";

import {
  AnalysisProgressBar,
  Badge,
  Button,
  ChartContainer,
  EvidenceCard,
  LoadingSkeleton,
  MetricCard,
  SectionContainer,
  SectionHeading,
} from "@/components/ui";
import {
  accentPalette,
  motionTokens,
  spacing,
  typography,
  type Accent,
} from "@/lib/design-tokens";
import { cn } from "@/lib/utils";

type Icon = ComponentType<{ className?: string; "aria-hidden"?: boolean }>;

const features: Array<{
  title: string;
  description: string;
  icon: Icon;
  accent: Accent;
}> = [
  {
    title: "Explainable Analysis",
    description:
      "Surface the authorship signals behind each estimate, from structural patterns to consistency markers.",
    icon: FileSearch,
    accent: "cyan",
  },
  {
    title: "Static Code Metrics",
    description:
      "Inspect code shape, complexity, repetition, naming rhythm, and other deterministic signals.",
    icon: BarChart3,
    accent: "emerald",
  },
  {
    title: "ML-powered Detection",
    description:
      "Combine curated features with model scoring for authorship estimates that remain auditable.",
    icon: BrainCircuit,
    accent: "violet",
  },
  {
    title: "Interactive Reports",
    description:
      "Review probability, evidence, and metric breakdowns in a workflow built for technical teams.",
    icon: PanelTop,
    accent: "amber",
  },
];

const steps: Array<{
  title: string;
  description: string;
  icon: Icon;
}> = [
  {
    title: "Paste Code",
    description:
      "Drop in a source file or snippet when you need authorship context.",
    icon: Code2,
  },
  {
    title: "Analyze",
    description:
      "CodeSense evaluates static signals and machine-learning features locally.",
    icon: Sparkles,
  },
  {
    title: "Review Insights",
    description:
      "Inspect probability, evidence, and the metrics that shaped the estimate.",
    icon: LineChart,
  },
];

const metrics: Array<{ label: string; value: number; accent: Accent }> = [
  { label: "Structure regularity", value: 82, accent: "cyan" },
  { label: "Naming consistency", value: 68, accent: "emerald" },
  { label: "Pattern repetition", value: 74, accent: "violet" },
  { label: "Comment density", value: 41, accent: "amber" },
];

const evidence = [
  "Consistent function boundaries across modules",
  "Low variance in identifier style",
  "Repeated control-flow shape in adjacent blocks",
];

export function LandingPage() {
  return (
    <main className="min-h-screen overflow-hidden bg-background text-foreground">
      <div className="pointer-events-none fixed inset-0 -z-10 bg-grid" />
      <div className="pointer-events-none fixed inset-0 -z-10 bg-ambient" />

      <SiteNav />
      <Hero />
      <FeaturesSection />
      <HowItWorks />
      <SiteFooter />
    </main>
  );
}

function SiteNav() {
  return (
    <header className="sticky top-0 z-50 border-b border-line-subtle bg-background/80 backdrop-blur-xl">
      <nav
        aria-label="Primary navigation"
        className={cn(
          "mx-auto flex h-16 max-w-7xl items-center justify-between",
          spacing.pageX,
        )}
      >
        <LogoMark />

        <div className="hidden items-center gap-1 md:flex">
          <NavLink href="#features">Features</NavLink>
          <NavLink href="#docs">Docs</NavLink>
          <NavLink
            href="https://github.com/Samearth17/Codesense"
            icon={<Github className="size-4" aria-hidden="true" />}
          >
            GitHub
          </NavLink>
        </div>

        <Button asChild size="sm" className="h-9">
          <a href="/scan">
            Analyze
            <ArrowRight className="size-4" aria-hidden="true" />
          </a>
        </Button>
      </nav>
    </header>
  );
}

function LogoMark() {
  return (
    <a href="#" className="flex items-center gap-3" aria-label="CodeSense home">
      <span className="flex size-8 items-center justify-center rounded-md border border-cyan-300/25 bg-cyan-300/10 text-cyan-200">
        <Layers3 className="size-4" aria-hidden="true" />
      </span>
      <span className="text-sm font-semibold tracking-normal text-foreground">
        CodeSense
      </span>
    </a>
  );
}

function NavLink({
  href,
  children,
  icon,
}: {
  href: string;
  children: ReactNode;
  icon?: ReactNode;
}) {
  return (
    <a
      href={href}
      className="inline-flex h-9 items-center gap-2 rounded-md px-3 text-sm text-muted-foreground transition-colors duration-base ease-premium hover:bg-white/5 hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
    >
      {icon}
      {children}
    </a>
  );
}

function Hero() {
  return (
    <SectionContainer
      id="analyze"
      size="hero"
      className="grid min-h-[calc(100svh-4rem)] items-center gap-12 lg:grid-cols-[0.92fr_1.08fr]"
    >
      <motion.div
        initial="hidden"
        animate="show"
        transition={{ staggerChildren: 0.08 }}
        className="max-w-3xl"
      >
        <motion.div
          variants={motionTokens.fadeUp}
          transition={{
            duration: motionTokens.duration.slow,
            ease: motionTokens.ease,
          }}
        >
          <Badge variant="neutral" className="px-3 py-1.5 text-sm">
            <ShieldCheck className="size-4 text-emerald-300" aria-hidden />
            Explainable authorship signals, not black-box guesses.
          </Badge>
        </motion.div>

        <motion.h1
          variants={motionTokens.fadeUp}
          transition={{
            duration: motionTokens.duration.slow,
            ease: motionTokens.ease,
          }}
          className={cn("mt-8 max-w-4xl text-foreground", typography.hero)}
        >
          Understand how code was written.
        </motion.h1>

        <motion.p
          variants={motionTokens.fadeUp}
          transition={{
            duration: motionTokens.duration.slow,
            ease: motionTokens.ease,
          }}
          className={cn(
            "mt-6 max-w-2xl text-muted-foreground",
            typography.bodyLarge,
          )}
        >
          CodeSense estimates AI-assisted authorship using explainable static
          analysis and machine learning, giving engineering teams evidence they
          can inspect without sending code to LLM APIs.
        </motion.p>

        <motion.div
          variants={motionTokens.fadeUp}
          transition={{
            duration: motionTokens.duration.slow,
            ease: motionTokens.ease,
          }}
          className="mt-9 flex flex-col gap-3 sm:flex-row"
        >
          <Button asChild size="lg">
            <a href="/scan">
              Analyze Code
              <ArrowRight className="size-4" aria-hidden="true" />
            </a>
          </Button>
          <Button asChild size="lg" variant="secondary">
            <a href="#features">
              Learn More
              <BookOpen className="size-4" aria-hidden="true" />
            </a>
          </Button>
        </motion.div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 24, scale: 0.98 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        transition={{
          duration: 0.7,
          delay: 0.12,
          ease: motionTokens.ease,
        }}
      >
        <AnalysisPanel />
      </motion.div>
    </SectionContainer>
  );
}

function AnalysisPanel() {
  return (
    <section
      aria-label="Static analysis result preview"
      className="relative rounded-lg border border-line-strong bg-surface/95 p-3 shadow-2xl shadow-black/40 ring-1 ring-white/5"
    >
      <div className="rounded-md border border-line-subtle bg-surface-raised">
        <div className="flex items-center justify-between border-b border-line-subtle px-4 py-3">
          <div className="flex items-center gap-2" aria-hidden="true">
            <span className="size-2.5 rounded-full bg-rose-400" />
            <span className="size-2.5 rounded-full bg-amber-300" />
            <span className="size-2.5 rounded-full bg-emerald-300" />
          </div>
          <p className="text-xs text-muted-foreground">analysis.ts</p>
        </div>

        <div className="grid gap-4 p-4 sm:p-5">
          <div className="grid gap-3 sm:grid-cols-2">
            <MetricCard
              label="AI Probability"
              value="71%"
              accent="cyan"
              description="Elevated assistance signal"
            />
            <MetricCard
              label="Human Probability"
              value="29%"
              accent="emerald"
              description="Manual authorship estimate"
            />
          </div>

          <div className="grid gap-4 lg:grid-cols-[0.95fr_1.05fr]">
            <EvidenceCard title="Evidence" items={evidence} badge="3 signals" />

            <ChartContainer title="Metric Bars">
              <div className="space-y-4">
                {metrics.map((metric) => (
                  <AnalysisProgressBar key={metric.label} {...metric} />
                ))}
              </div>
            </ChartContainer>
          </div>

          <ChartContainer
            title="Authorship Summary"
            description="Placeholder panel for future explainable report output."
            className="bg-surface-inset"
          >
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div className="grid flex-1 gap-2" aria-hidden="true">
                <LoadingSkeleton className="h-2.5 max-w-[18rem]" />
                <LoadingSkeleton className="h-2.5 max-w-[12rem]" />
              </div>
              <Badge variant="cyan" className="rounded-md px-3 py-2 text-sm">
                Review recommended
              </Badge>
            </div>
          </ChartContainer>
        </div>
      </div>
    </section>
  );
}

function FeaturesSection() {
  return (
    <SectionContainer id="features">
      <SectionHeading
        eyebrow="Features"
        title="Built for evidence, not vibes."
        description="CodeSense is designed around inspectable signals, clean reporting, and a workflow that respects source-code privacy."
      />
      <div
        className={cn("grid gap-4 sm:grid-cols-2 lg:grid-cols-4", spacing.sectionGap)}
      >
        {features.map((feature, index) => (
          <FeatureCard key={feature.title} feature={feature} index={index} />
        ))}
      </div>
    </SectionContainer>
  );
}

function FeatureCard({
  feature,
  index,
}: {
  feature: (typeof features)[number];
  index: number;
}) {
  const Icon = feature.icon;
  const palette = accentPalette[feature.accent];

  return (
    <motion.article
      initial={{ opacity: 0, y: 16 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{
        duration: motionTokens.duration.base,
        delay: index * 0.04,
        ease: motionTokens.ease,
      }}
      className="rounded-lg border border-line-subtle bg-white/[0.035] p-5 transition-colors duration-base ease-premium hover:bg-white/[0.055]"
    >
      <Icon className={cn("size-5", palette.icon)} aria-hidden={true} />
      <h3 className={cn("mt-5 text-foreground", typography.label)}>
        {feature.title}
      </h3>
      <p className={cn("mt-3 text-muted-foreground", typography.caption)}>
        {feature.description}
      </p>
    </motion.article>
  );
}

function HowItWorks() {
  return (
    <SectionContainer>
      <SectionHeading
        eyebrow="How it works"
        title="A simple review flow for complex authorship signals."
        description="The landing page is static today, but the product path is structured around fast input, transparent analysis, and clear review."
      />
      <div className={cn("grid gap-4 md:grid-cols-3", spacing.sectionGap)}>
        {steps.map((step, index) => (
          <StepCard key={step.title} step={step} index={index} />
        ))}
      </div>
    </SectionContainer>
  );
}

function StepCard({
  step,
  index,
}: {
  step: (typeof steps)[number];
  index: number;
}) {
  const Icon = step.icon;

  return (
    <motion.article
      initial={{ opacity: 0, y: 16 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{
        duration: motionTokens.duration.base,
        delay: index * 0.06,
        ease: motionTokens.ease,
      }}
      className="relative rounded-lg border border-line-subtle bg-surface p-6"
    >
      <div className="flex size-10 items-center justify-center rounded-md border border-line-subtle bg-white/[0.04] text-cyan-200">
        <Icon className="size-5" aria-hidden={true} />
      </div>
      <p className="mt-6 text-sm text-muted-foreground">0{index + 1}</p>
      <h3 className={cn("mt-2 text-foreground", typography.h3)}>
        {step.title}
      </h3>
      <p className={cn("mt-3 text-muted-foreground", typography.caption)}>
        {step.description}
      </p>
    </motion.article>
  );
}

function SiteFooter() {
  return (
    <footer id="docs" className="border-t border-line-subtle">
      <SectionContainer
        as="div"
        size="compact"
        className="flex flex-col gap-6 text-sm text-muted-foreground sm:flex-row sm:items-center sm:justify-between"
      >
        <LogoMark />
        <div className="flex flex-wrap gap-x-5 gap-y-2">
          <FooterLink href="#features">Features</FooterLink>
          <FooterLink href="#docs">Docs</FooterLink>
          <FooterLink href="https://github.com/Samearth17/Codesense">
            GitHub
          </FooterLink>
        </div>
      </SectionContainer>
    </footer>
  );
}

function FooterLink({ href, children }: { href: string; children: ReactNode }) {
  return (
    <a
      href={href}
      className="transition-colors duration-base ease-premium hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
    >
      {children}
    </a>
  );
}
