"use client";

import React from "react";
import { motion } from "framer-motion";
import { Button, type ButtonProps } from "./button";
import { hoverGrow, hoverGlow } from "@/lib/animations";

interface AnimatedButtonProps extends ButtonProps {
  animationType?: "grow" | "glow" | "lift";
}

export const AnimatedButton = React.forwardRef<
  HTMLButtonElement,
  AnimatedButtonProps
>(({ animationType = "grow", ...props }, ref) => {
  const variants = {
    grow: hoverGrow,
    glow: hoverGlow,
    lift: {
      initial: { y: 0 },
      hover: { y: -2, transition: { duration: 0.2 } },
    },
  };

  return (
    <motion.div
      initial="initial"
      whileHover="hover"
      variants={variants[animationType]}
    >
      <Button ref={ref} {...props} />
    </motion.div>
  );
});

AnimatedButton.displayName = "AnimatedButton";
