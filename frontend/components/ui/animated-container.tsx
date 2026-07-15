"use client";

import React from "react";
import { motion, HTMLMotionProps } from "framer-motion";
import { containerVariants, staggerContainer } from "@/lib/animations";

interface AnimatedContainerProps extends HTMLMotionProps<"div"> {
  stagger?: boolean;
  delay?: number;
}

export const AnimatedContainer = React.forwardRef<
  HTMLDivElement,
  AnimatedContainerProps
>(({ stagger = true, delay = 0, className, children, ...props }, ref) => {
  const variants = stagger ? containerVariants : staggerContainer;

  return (
    <motion.div
      ref={ref}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.3 }}
      variants={variants}
      transition={{ delay }}
      className={className}
      {...props}
    >
      {children}
    </motion.div>
  );
});

AnimatedContainer.displayName = "AnimatedContainer";
