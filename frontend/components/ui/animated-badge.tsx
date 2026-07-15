"use client";

import React from "react";
import { motion, HTMLMotionProps } from "framer-motion";
import { Badge, type BadgeProps } from "./badge";
import { pulse, glowPulse } from "@/lib/animations";

interface AnimatedBadgeProps extends BadgeProps {
  animated?: boolean;
  glowing?: boolean;
}

export const AnimatedBadge = React.forwardRef<
  HTMLDivElement,
  AnimatedBadgeProps
>(({ animated = false, glowing = false, ...props }, ref) => {
  if (!animated && !glowing) {
    return <Badge ref={ref} {...props} />;
  }

  const variants = glowing ? glowPulse : pulse;

  return (
    <motion.div
      animate="animate"
      variants={variants}
      style={{ display: "inline-block" }}
    >
      <Badge ref={ref} {...props} />
    </motion.div>
  );
});

AnimatedBadge.displayName = "AnimatedBadge";
