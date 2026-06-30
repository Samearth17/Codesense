import { type ReactNode, useId } from "react";

import { cn } from "@/lib/utils";

type TooltipProps = {
  children: ReactNode;
  content: ReactNode;
  className?: string;
  side?: "top" | "bottom";
};

export function Tooltip({
  children,
  content,
  className,
  side = "top",
}: TooltipProps) {
  const id = useId();

  return (
    <span
      aria-describedby={id}
      className={cn("group relative inline-flex focus:outline-none", className)}
      tabIndex={0}
    >
      {children}
      <span
        id={id}
        role="tooltip"
        className={cn(
          "pointer-events-none absolute left-1/2 z-50 w-max max-w-64 -translate-x-1/2 rounded-md border border-white/10 bg-surface-raised px-3 py-2 text-xs leading-5 text-foreground opacity-0 shadow-xl shadow-black/30 transition duration-base ease-premium group-hover:opacity-100 group-focus-visible:opacity-100",
          side === "top" && "bottom-full mb-2",
          side === "bottom" && "top-full mt-2",
        )}
      >
        {content}
      </span>
    </span>
  );
}
