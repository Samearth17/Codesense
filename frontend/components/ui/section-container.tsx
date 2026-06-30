import { type ElementType, type ReactNode } from "react";

import { cn } from "@/lib/utils";
import { spacing, typography } from "@/lib/design-tokens";

type SectionContainerProps = {
  children: ReactNode;
  id?: string;
  className?: string;
  as?: ElementType;
  size?: "default" | "hero" | "compact";
};

export function SectionContainer({
  children,
  id,
  className,
  as: Component = "section",
  size = "default",
}: SectionContainerProps) {
  return (
    <Component
      id={id}
      className={cn(
        "mx-auto w-full max-w-7xl",
        spacing.pageX,
        size === "default" && spacing.sectionY,
        size === "hero" && "py-20 lg:py-24",
        size === "compact" && "py-8",
        className,
      )}
    >
      {children}
    </Component>
  );
}

type SectionHeadingProps = {
  eyebrow: string;
  title: string;
  description: string;
  className?: string;
};

export function SectionHeading({
  eyebrow,
  title,
  description,
  className,
}: SectionHeadingProps) {
  return (
    <div className={cn("max-w-3xl", className)}>
      <p className="text-sm font-medium text-cyan-200">{eyebrow}</p>
      <h2 className={cn("mt-3 text-foreground", typography.h2)}>{title}</h2>
      <p className={cn("mt-4 text-muted-foreground", typography.body)}>
        {description}
      </p>
    </div>
  );
}
