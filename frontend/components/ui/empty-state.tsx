import { type ComponentType, type ReactNode } from "react";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

type EmptyStateProps = {
  title: string;
  description: string;
  icon?: ComponentType<{ className?: string; "aria-hidden"?: boolean }>;
  action?: {
    label: string;
    href: string;
  };
  className?: string;
  children?: ReactNode;
};

export function EmptyState({
  title,
  description,
  icon: Icon,
  action,
  className,
  children,
}: EmptyStateProps) {
  return (
    <div
      className={cn(
        "flex min-h-64 flex-col items-center justify-center rounded-lg border border-dashed border-line-strong bg-surface/70 p-8 text-center",
        className,
      )}
    >
      {Icon ? (
        <div className="mb-5 flex size-10 items-center justify-center rounded-md border border-white/10 bg-white/[0.04] text-cyan-200">
          <Icon className="size-5" aria-hidden />
        </div>
      ) : null}
      <h3 className="text-lg font-medium text-foreground">{title}</h3>
      <p className="mt-2 max-w-sm text-sm leading-6 text-muted-foreground">
        {description}
      </p>
      {children}
      {action ? (
        <Button asChild className="mt-6" variant="secondary">
          <a href={action.href}>{action.label}</a>
        </Button>
      ) : null}
    </div>
  );
}
