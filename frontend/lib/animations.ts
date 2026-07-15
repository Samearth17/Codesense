/**
 * Animation library inspired by React Bits
 * Provides reusable, professional motion variants for Framer Motion
 */

import { Variants } from "framer-motion";

// ── Fade Animations ──────────────────────────────────────────────────────

export const fadeIn: Variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.5 } },
};

export const fadeOut: Variants = {
  visible: { opacity: 1 },
  hidden: { opacity: 0, transition: { duration: 0.3 } },
};

export const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

export const fadeInDown: Variants = {
  hidden: { opacity: 0, y: -20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

export const fadeInLeft: Variants = {
  hidden: { opacity: 0, x: -20 },
  visible: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

export const fadeInRight: Variants = {
  hidden: { opacity: 0, x: 20 },
  visible: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Scale Animations ────────────────────────────────────────────────────

export const scaleIn: Variants = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: { duration: 0.4, ease: [0.16, 1, 0.3, 1] },
  },
};

export const scaleUp: Variants = {
  hidden: { opacity: 0, scale: 0.95 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

export const scaleDown: Variants = {
  visible: { opacity: 1, scale: 1 },
  hidden: {
    opacity: 0,
    scale: 0.95,
    transition: { duration: 0.3, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Slide Animations ────────────────────────────────────────────────────

export const slideInUp: Variants = {
  hidden: { opacity: 0, y: 40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

export const slideInDown: Variants = {
  hidden: { opacity: 0, y: -40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

export const slideInLeft: Variants = {
  hidden: { opacity: 0, x: -40 },
  visible: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

export const slideInRight: Variants = {
  hidden: { opacity: 0, x: 40 },
  visible: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Rotate Animations ──────────────────────────────────────────────────

export const rotateIn: Variants = {
  hidden: { opacity: 0, rotate: -10 },
  visible: {
    opacity: 1,
    rotate: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

export const rotateInClockwise: Variants = {
  hidden: { opacity: 0, rotate: -180 },
  visible: {
    opacity: 1,
    rotate: 0,
    transition: { duration: 0.7, ease: [0.16, 1, 0.3, 1] },
  },
};

export const rotateInCounterClockwise: Variants = {
  hidden: { opacity: 0, rotate: 180 },
  visible: {
    opacity: 1,
    rotate: 0,
    transition: { duration: 0.7, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Blur Animations ────────────────────────────────────────────────────

export const blurIn: Variants = {
  hidden: { opacity: 0, filter: "blur(10px)" },
  visible: {
    opacity: 1,
    filter: "blur(0px)",
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

export const blurOut: Variants = {
  visible: { opacity: 1, filter: "blur(0px)" },
  hidden: {
    opacity: 0,
    filter: "blur(10px)",
    transition: { duration: 0.3, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Bounce Animations ──────────────────────────────────────────────────

export const bounceIn: Variants = {
  hidden: { opacity: 0, scale: 0.3 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: {
      duration: 0.6,
      ease: [0.34, 1.56, 0.64, 1],
    },
  },
};

export const bounce: Variants = {
  animate: {
    y: [0, -10, 0],
    transition: {
      duration: 1,
      repeat: Infinity,
      ease: "easeInOut",
    },
  },
};

// ── Pulse Animations ────────────────────────────────────────────────────

export const pulse: Variants = {
  animate: {
    opacity: [1, 0.5, 1],
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: "easeInOut",
    },
  },
};

export const pulseScale: Variants = {
  animate: {
    scale: [1, 1.05, 1],
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: "easeInOut",
    },
  },
};

// ── Shimmer Animations ──────────────────────────────────────────────────

export const shimmer: Variants = {
  animate: {
    backgroundPosition: ["200% 0", "-200% 0"],
    transition: {
      duration: 3,
      repeat: Infinity,
      ease: "linear",
    },
  },
};

// ── Flip Animations ────────────────────────────────────────────────────

export const flipInX: Variants = {
  hidden: { opacity: 0, rotateX: -90 },
  visible: {
    opacity: 1,
    rotateX: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

export const flipInY: Variants = {
  hidden: { opacity: 0, rotateY: -90 },
  visible: {
    opacity: 1,
    rotateY: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Stagger Animations ──────────────────────────────────────────────────

export const staggerContainer: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2,
    },
  },
};

export const staggerItem: Variants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.4, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Glow Animations ────────────────────────────────────────────────────

export const glowPulse: Variants = {
  animate: {
    boxShadow: [
      "0 0 0 0 rgba(34, 197, 94, 0.7)",
      "0 0 0 10px rgba(34, 197, 94, 0)",
    ],
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: "easeOut",
    },
  },
};

// ── Hover Animations ────────────────────────────────────────────────────

export const hoverLift: Variants = {
  initial: { y: 0 },
  hover: {
    y: -4,
    transition: { duration: 0.2, ease: "easeOut" },
  },
};

export const hoverGrow: Variants = {
  initial: { scale: 1 },
  hover: {
    scale: 1.05,
    transition: { duration: 0.2, ease: "easeOut" },
  },
};

export const hoverGlow: Variants = {
  initial: { boxShadow: "0 0 0 0 rgba(59, 130, 246, 0)" },
  hover: {
    boxShadow: "0 0 0 8px rgba(59, 130, 246, 0.1)",
    transition: { duration: 0.3, ease: "easeOut" },
  },
};

// ── Container Animations ────────────────────────────────────────────────

export const containerVariants: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.12,
      delayChildren: 0.1,
    },
  },
};

export const itemVariants: Variants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Entrance Animations ────────────────────────────────────────────────

export const pageEnter: Variants = {
  initial: { opacity: 0, y: 20 },
  animate: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  },
  exit: {
    opacity: 0,
    y: -20,
    transition: { duration: 0.3, ease: [0.16, 1, 0.3, 1] },
  },
};

export const pageExit: Variants = {
  initial: { opacity: 1, y: 0 },
  animate: {
    opacity: 0,
    y: 20,
    transition: { duration: 0.3, ease: [0.16, 1, 0.3, 1] },
  },
};

// ── Modal Animations ────────────────────────────────────────────────────

export const modalBackdrop: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { duration: 0.3 },
  },
  exit: {
    opacity: 0,
    transition: { duration: 0.2 },
  },
};

export const modalContent: Variants = {
  hidden: { opacity: 0, scale: 0.95, y: 20 },
  visible: {
    opacity: 1,
    scale: 1,
    y: 0,
    transition: { duration: 0.4, ease: [0.16, 1, 0.3, 1] },
  },
  exit: {
    opacity: 0,
    scale: 0.95,
    y: 20,
    transition: { duration: 0.2 },
  },
};

// ── Loading Animations ──────────────────────────────────────────────────

export const spin: Variants = {
  animate: {
    rotate: 360,
    transition: {
      duration: 1,
      repeat: Infinity,
      ease: "linear",
    },
  },
};

export const spinSlow: Variants = {
  animate: {
    rotate: 360,
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: "linear",
    },
  },
};

// ── Wave Animations ────────────────────────────────────────────────────

export const wave: Variants = {
  animate: {
    rotate: [0, 14, -8, 14, -4, 10, 0],
    transition: {
      duration: 0.6,
      repeat: Infinity,
      repeatDelay: 2,
    },
  },
};

// ── Slide Toggle Animations ────────────────────────────────────────────

export const slideToggle: Variants = {
  initial: { x: 0 },
  animate: { x: 20 },
  transition: { duration: 0.3, ease: "easeInOut" },
};

// ── Transition Presets ──────────────────────────────────────────────────

export const transitionPresets = {
  fast: { duration: 0.2, ease: [0.16, 1, 0.3, 1] },
  base: { duration: 0.4, ease: [0.16, 1, 0.3, 1] },
  slow: { duration: 0.6, ease: [0.16, 1, 0.3, 1] },
  slowest: { duration: 0.8, ease: [0.16, 1, 0.3, 1] },
  bounce: { duration: 0.6, ease: [0.34, 1.56, 0.64, 1] },
} as const;
