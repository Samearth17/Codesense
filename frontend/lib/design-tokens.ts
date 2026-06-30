export const typography = {
  hero: "text-5xl font-semibold leading-[1.02] tracking-normal sm:text-6xl lg:text-7xl",
  h2: "text-3xl font-semibold leading-tight tracking-normal sm:text-4xl",
  h3: "text-xl font-medium tracking-normal",
  body: "text-base leading-7",
  bodyLarge: "text-base leading-8 sm:text-lg",
  caption: "text-sm leading-6",
  label: "text-sm font-medium",
} as const;

export const spacing = {
  pageX: "px-5 sm:px-6 lg:px-8",
  sectionY: "py-20 lg:py-24",
  sectionGap: "mt-12",
  card: "p-5",
  cardCompact: "p-4",
} as const;

export const motionTokens = {
  ease: [0.16, 1, 0.3, 1],
  duration: {
    fast: 0.18,
    base: 0.32,
    slow: 0.56,
  },
  fadeUp: {
    hidden: { opacity: 0, y: 18 },
    show: { opacity: 1, y: 0 },
  },
} as const;

export const accentPalette = {
  cyan: {
    text: "text-cyan-200",
    icon: "text-cyan-300",
    border: "border-cyan-300/20",
    background: "bg-cyan-300/10",
    bar: "bg-chart-1",
  },
  emerald: {
    text: "text-emerald-200",
    icon: "text-emerald-300",
    border: "border-emerald-300/20",
    background: "bg-emerald-300/10",
    bar: "bg-chart-2",
  },
  violet: {
    text: "text-violet-200",
    icon: "text-violet-300",
    border: "border-violet-300/20",
    background: "bg-violet-300/10",
    bar: "bg-chart-3",
  },
  amber: {
    text: "text-amber-200",
    icon: "text-amber-300",
    border: "border-amber-300/20",
    background: "bg-amber-300/10",
    bar: "bg-chart-4",
  },
} as const;

export type Accent = keyof typeof accentPalette;
