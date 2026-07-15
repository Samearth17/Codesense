"use client";

import React from "react";
import { motion, MotionProps } from "framer-motion";
import { cn } from "@/lib/utils";
import { fadeInUp, scaleIn, hoverLift } from "@/lib/animations";

interface AnimatedCardProps
  extends React.HTMLAttributes<HTMLDivElement>,
    MotionProps {
  variant?: "fade" | "scale" | "lift";
  delay?: number;
  children: React.ReactNode;
}

export const AnimatedCard = React.forwardRef<
  HTMLDivElement,
  AnimatedCardProps
>(
  (
    { variant = "fade", delay = 0, className, children, ...props },
    ref
  ) => {
    const variants = {
      fade: fadeInUp,
      scale: scaleIn,
      lift: hoverLift,
    };

    return (
      <motion.div
        ref={ref}
        initial="hidden"
        whileInView="visible"
        whileHover={variant === "lift" ? "hover" : undefined}
        variants={variants[variant]}
        transition={{ delay }}
        viewport={{ once: true, amount: 0.3 }}
        className={cn("rounded-lg border border-line-strong", className)}
        {...props}
      >
        {children}
      </motion.div>
    );
  }
);

AnimatedCard.displayName = "AnimatedCard";
