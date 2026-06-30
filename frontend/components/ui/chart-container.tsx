import { type ReactNode } from "react";

import { cn } from "@/lib/utils";

type ChartContainerProps = {
  title: string;
  description?: string;
  children: ReactNode;
  className?: string;
};

export function ChartContainer({
  title,
  description,
  children,
  className,
}: ChartContainerProps) {
  return (
    <figure
      className={cn(
        "rounded-md border border-line-subtle bg-white/[0.035] p-4",
        className,
      )}
    >
      <figcaption>
        <h2 className="text-sm font-medium text-foreground">{title}</h2>
        {description ? (
          <p className="mt-1 text-sm text-muted-foreground">{description}</p>
        ) : null}
      </figcaption>
      <div className="mt-5">{children}</div>
    </figure>
  );
}
