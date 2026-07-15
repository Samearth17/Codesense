"use client";

import React from "react";
import { motion, HTMLMotionProps } from "framer-motion";
import { cn } from "@/lib/utils";
import {
  fadeInUp,
  slideInUp,
  blurIn,
  containerVariants,
  itemVariants,
} from "@/lib/animations";

interface AnimatedTextProps extends HTMLMotionProps<"div"> {
  text: string;
  variant?: "fade" | "slide" | "blur" | "word" | "char";
  delay?: number;
  stagger?: boolean;
}

export const AnimatedText = React.forwardRef<
  HTMLDivElement,
  AnimatedTextProps
>(
  (
    {
      text,
      variant = "fade",
      delay = 0,
      stagger = false,
      className,
      ...props
    },
    ref
  ) => {
    const variants = {
      fade: fadeInUp,
      slide: slideInUp,
      blur: blurIn,
    };

    if (variant === "word" || variant === "char") {
      const elements =
        variant === "word" ? text.split(" ") : text.split("");
      const separator = variant === "word" ? " " : "";

      return (
        <motion.div
          ref={ref}
          initial="hidden"
          animate="visible"
          variants={containerVariants}
          className={className}
          {...props}
        >
          {elements.map((el, i) => (
            <motion.span key={i} variants={itemVariants}>
              {el}
              {separator}
            </motion.span>
          ))}
        </motion.div>
      );
    }

    return (
      <motion.div
        ref={ref}
        initial="hidden"
        animate="visible"
        variants={variants[variant as keyof typeof variants]}
        transition={{ delay }}
        className={className}
        {...props}
      >
        {text}
      </motion.div>
    );
  }
);

AnimatedText.displayName = "AnimatedText";
