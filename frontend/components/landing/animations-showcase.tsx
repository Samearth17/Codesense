"use client";

import React from "react";
import { motion } from "framer-motion";
import {
  AnimatedCard,
  AnimatedButton,
  AnimatedText,
  AnimatedLoader,
  AnimatedContainer,
  SectionContainer,
  SectionHeading,
} from "@/components/ui";
import { itemVariants } from "@/lib/animations";
import { cn } from "@/lib/utils";
import { spacing } from "@/lib/design-tokens";

export function AnimationsShowcase() {
  return (
    <SectionContainer id="animations" className="py-20 lg:py-24">
      <SectionHeading
        eyebrow="Animations"
        title="Smooth, professional motion."
        description="Built-in React Bits-inspired animations for a polished user experience."
      />

      <div className={cn("grid gap-8 lg:grid-cols-2", spacing.sectionGap)}>
        {/* Entrance Animations */}
        <AnimatedCard variant="fade" className="p-6">
          <h3 className="mb-4 text-lg font-semibold">Entrance Animations</h3>
          <div className="space-y-4">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5 }}
              className="rounded bg-cyan-300/10 p-3 text-sm text-cyan-200"
            >
              Fade In Up
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: 0.1 }}
              className="rounded bg-emerald-300/10 p-3 text-sm text-emerald-200"
            >
              Slide In Left
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: 0.2 }}
              className="rounded bg-violet-300/10 p-3 text-sm text-violet-200"
            >
              Slide In Right
            </motion.div>
          </div>
        </AnimatedCard>

        {/* Scale & Hover Animations */}
        <AnimatedCard variant="scale" className="p-6">
          <h3 className="mb-4 text-lg font-semibold">Interactive Animations</h3>
          <div className="space-y-3">
            <motion.div
              whileHover={{ scale: 1.05 }}
              className="cursor-pointer rounded bg-amber-300/10 p-3 text-sm text-amber-200 transition-colors hover:bg-amber-300/20"
            >
              Hover to Scale
            </motion.div>
            <motion.div
              whileHover={{ y: -4 }}
              className="cursor-pointer rounded bg-cyan-300/10 p-3 text-sm text-cyan-200 transition-colors hover:bg-cyan-300/20"
            >
              Hover to Lift
            </motion.div>
            <motion.div
              whileHover={{
                boxShadow: "0 0 0 8px rgba(59, 130, 246, 0.1)",
              }}
              className="cursor-pointer rounded bg-emerald-300/10 p-3 text-sm text-emerald-200 transition-colors hover:bg-emerald-300/20"
            >
              Hover to Glow
            </motion.div>
          </div>
        </AnimatedCard>

        {/* Loaders */}
        <AnimatedCard variant="fade" className="p-6">
          <h3 className="mb-4 text-lg font-semibold">Loading States</h3>
          <div className="flex items-center justify-around gap-4">
            <div className="flex flex-col items-center gap-2">
              <AnimatedLoader type="spin" size="md" />
              <span className="text-xs text-muted-foreground">Spin</span>
            </div>
            <div className="flex flex-col items-center gap-2">
              <AnimatedLoader type="pulse" size="md" />
              <span className="text-xs text-muted-foreground">Pulse</span>
            </div>
            <div className="flex flex-col items-center gap-2">
              <AnimatedLoader type="bounce" size="md" />
              <span className="text-xs text-muted-foreground">Bounce</span>
            </div>
            <div className="flex flex-col items-center gap-2">
              <AnimatedLoader type="dots" size="md" />
              <span className="text-xs text-muted-foreground">Dots</span>
            </div>
          </div>
        </AnimatedCard>

        {/* Text Animations */}
        <AnimatedCard variant="scale" className="p-6">
          <h3 className="mb-4 text-lg font-semibold">Text Animations</h3>
          <div className="space-y-4">
            <AnimatedText
              text="Word by word animation"
              variant="word"
              className="text-sm text-cyan-200"
            />
            <AnimatedText
              text="Character animation"
              variant="char"
              className="text-sm text-emerald-200"
            />
            <AnimatedText
              text="Blur in effect"
              variant="blur"
              className="text-sm text-violet-200"
            />
          </div>
        </AnimatedCard>

        {/* Stagger Container */}
        <AnimatedContainer stagger className="space-y-3 lg:col-span-2">
          <h3 className="text-lg font-semibold">Staggered List Items</h3>
          {["Item 1", "Item 2", "Item 3", "Item 4"].map((item) => (
            <motion.div
              key={item}
              variants={itemVariants}
              className="rounded bg-white/5 p-3 text-sm text-muted-foreground"
            >
              {item}
            </motion.div>
          ))}
        </AnimatedContainer>
      </div>

      {/* CTA */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.5, delay: 0.2 }}
        className={cn("mt-12 text-center", spacing.sectionGap)}
      >
        <p className="mb-6 text-muted-foreground">
          Experience smooth, professional animations throughout the app.
        </p>
        <AnimatedButton animationType="grow" size="lg" asChild>
          <a href="/scan">Start Analyzing</a>
        </AnimatedButton>
      </motion.div>
    </SectionContainer>
  );
}
