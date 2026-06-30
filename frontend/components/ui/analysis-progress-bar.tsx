import { cn } from "@/lib/utils";
import { accentPalette, type Accent } from "@/lib/design-tokens";

type AnalysisProgressBarProps = {
  label: string;
  value: number;
  accent?: Accent;
  className?: string;
};

export function AnalysisProgressBar({
  label,
  value,
  accent = "cyan",
  className,
}: AnalysisProgressBarProps) {
  const clampedValue = Math.min(100, Math.max(0, value));
  const palette = accentPalette[accent];

  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-center justify-between gap-4 text-sm">
        <span className="text-muted-foreground">{label}</span>
        <span className="font-medium text-foreground">{clampedValue}%</span>
      </div>
      <div
        aria-label={`${label}: ${clampedValue}%`}
        aria-valuemax={100}
        aria-valuemin={0}
        aria-valuenow={clampedValue}
        className="h-2 overflow-hidden rounded-full bg-white/10"
        role="progressbar"
      >
        <div
          className={cn("h-full rounded-full", palette.bar)}
          style={{ width: `${clampedValue}%` }}
        />
      </div>
    </div>
  );
}
