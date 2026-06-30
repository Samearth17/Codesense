import { cn } from "@/lib/utils";
import { accentPalette, type Accent } from "@/lib/design-tokens";

type MetricCardProps = {
  label: string;
  value: string;
  description?: string;
  accent?: Accent;
  className?: string;
};

export function MetricCard({
  label,
  value,
  description,
  accent = "cyan",
  className,
}: MetricCardProps) {
  const palette = accentPalette[accent];

  return (
    <article
      className={cn(
        "rounded-md border p-4",
        palette.border,
        palette.background,
        palette.text,
        className,
      )}
    >
      <p className="text-sm text-current opacity-75">{label}</p>
      <p className="mt-3 text-4xl font-semibold tracking-normal">{value}</p>
      {description ? (
        <p className="mt-2 text-sm text-current opacity-70">{description}</p>
      ) : null}
    </article>
  );
}
