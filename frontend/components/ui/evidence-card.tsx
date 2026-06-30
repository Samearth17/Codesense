import { CheckCircle2 } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

type EvidenceCardProps = {
  title: string;
  items: string[];
  badge?: string;
  className?: string;
};

export function EvidenceCard({
  title,
  items,
  badge,
  className,
}: EvidenceCardProps) {
  return (
    <section
      aria-labelledby={`${title.toLowerCase().replaceAll(" ", "-")}-title`}
      className={cn(
        "rounded-md border border-line-subtle bg-white/[0.035] p-4",
        className,
      )}
    >
      <div className="mb-4 flex items-center justify-between gap-4">
        <h2
          id={`${title.toLowerCase().replaceAll(" ", "-")}-title`}
          className="text-sm font-medium text-foreground"
        >
          {title}
        </h2>
        {badge ? <Badge variant="cyan">{badge}</Badge> : null}
      </div>
      <div className="space-y-3">
        {items.map((item) => (
          <div
            key={item}
            className="flex gap-3 text-sm leading-6 text-muted-foreground"
          >
            <CheckCircle2
              className="mt-1 size-4 shrink-0 text-emerald-300"
              aria-hidden="true"
            />
            <span>{item}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
