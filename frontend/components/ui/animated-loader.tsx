"use client";

import React from "react";
import { motion, HTMLMotionProps } from "framer-motion";
import { cn } from "@/lib/utils";
import { spin, pulse, bounce } from "@/lib/animations";

interface AnimatedLoaderProps extends HTMLMotionProps<"div"> {
  type?: "spin" | "pulse" | "bounce" | "dots";
  size?: "sm" | "md" | "lg";
}

const sizeMap = {
  sm: "size-6",
  md: "size-8",
  lg: "size-12",
};

export const AnimatedLoader = React.forwardRef<
  HTMLDivElement,
  AnimatedLoaderProps
>(({ type = "spin", size = "md", className, ...props }, ref) => {
  if (type === "spin") {
    return (
      <motion.div
        ref={ref}
        animate="animate"
        variants={spin}
        className={cn(
          "rounded-full border-2 border-transparent border-t-cyan-300 border-r-cyan-300",
          sizeMap[size],
          className
        )}
        {...props}
      />
    );
  }

  if (type === "pulse") {
    return (
      <motion.div
        ref={ref}
        animate="animate"
        variants={pulse}
        className={cn(
          "rounded-full bg-cyan-300/20 ring-1 ring-cyan-300/50",
          sizeMap[size],
          className
        )}
        {...props}
      />
    );
  }

  if (type === "bounce") {
    return (
      <motion.div
        ref={ref}
        animate="animate"
        variants={bounce}
        className={cn(
          "rounded-full bg-cyan-300/30",
          sizeMap[size],
          className
        )}
        {...props}
      />
    );
  }

  // dots
  return (
    <div className={cn("flex gap-2", className)} {...(props as any)}>
      {[0, 1, 2].map((i) => (
        <motion.div
          key={i}
          animate={{ y: [0, -8, 0] }}
          transition={{
            duration: 0.6,
            repeat: Infinity,
            delay: i * 0.1,
          }}
          className="size-2 rounded-full bg-cyan-300"
        />
      ))}
    </div>
  );
});

AnimatedLoader.displayName = "AnimatedLoader";
