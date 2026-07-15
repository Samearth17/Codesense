import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-xs font-medium leading-none transition-colors",
  {
    variants: {
      variant: {
        neutral: "border-white/10 bg-white/[0.04] text-muted-foreground",
        cyan: "border-cyan-300/20 bg-cyan-300/10 text-cyan-100",
        emerald: "border-emerald-300/20 bg-emerald-300/10 text-emerald-100",
        violet: "border-violet-300/20 bg-violet-300/10 text-violet-100",
        amber: "border-amber-300/20 bg-amber-300/10 text-amber-100",
      },
    },
    defaultVariants: {
      variant: "neutral",
    },
  },
);

export interface BadgeProps
  extends
    React.HTMLAttributes<HTMLSpanElement>,
    VariantProps<typeof badgeVariants> {}

export const Badge = React.forwardRef<HTMLSpanElement, BadgeProps>(
  ({ className, variant, ...props }, ref) => {
    return (
      <span
        ref={ref}
        className={cn(badgeVariants({ variant, className }))}
        {...props}
      />
    );
  }
);
Badge.displayName = "Badge";

export { badgeVariants };
