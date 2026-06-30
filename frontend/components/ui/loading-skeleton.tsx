import { type HTMLAttributes } from "react";

import { cn } from "@/lib/utils";

export function LoadingSkeleton({
  className,
  ...props
}: HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      aria-busy="true"
      className={cn(
        "relative overflow-hidden rounded-md bg-white/[0.055]",
        "before:absolute before:inset-y-0 before:left-0 before:w-1/2 before:-translate-x-full before:bg-gradient-to-r before:from-transparent before:via-white/10 before:to-transparent before:animate-shimmer",
        className,
      )}
      {...props}
    />
  );
}
