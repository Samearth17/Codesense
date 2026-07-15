# Animation System

This document describes the animation system built into CodeSense, inspired by React Bits. All animations use **Framer Motion** for smooth, performant motion.

## Quick Start

### Using Animation Variants

Import animation variants from `@/lib/animations`:

```tsx
import { fadeInUp, scaleIn, slideInLeft } from "@/lib/animations";
import { motion } from "framer-motion";

export function MyComponent() {
  return (
    <motion.div
      initial="hidden"
      whileInView="visible"
      variants={fadeInUp}
      viewport={{ once: true }}
    >
      Content
    </motion.div>
  );
}
```

### Using Animated Components

Import pre-built animated components from `@/components/ui`:

```tsx
import {
  AnimatedCard,
  AnimatedButton,
  AnimatedText,
  AnimatedLoader,
} from "@/components/ui";

export function MyComponent() {
  return (
    <>
      <AnimatedCard variant="fade">Card content</AnimatedCard>
      <AnimatedButton animationType="grow">Click me</AnimatedButton>
      <AnimatedText text="Hello World" variant="word" />
      <AnimatedLoader type="spin" size="md" />
    </>
  );
}
```

## Animation Categories

### 1. Fade Animations

Opacity-based transitions for subtle, elegant entrances.

- **`fadeIn`**: Fade from transparent to opaque
- **`fadeOut`**: Fade from opaque to transparent
- **`fadeInUp`**: Fade in while moving up (default entrance)
- **`fadeInDown`**: Fade in while moving down
- **`fadeInLeft`**: Fade in while moving left
- **`fadeInRight`**: Fade in while moving right

```tsx
<motion.div variants={fadeInUp} initial="hidden" animate="visible">
  Content fades in and moves up
</motion.div>
```

### 2. Scale Animations

Size-based transitions for emphasis and focus.

- **`scaleIn`**: Scale from 0.9 to 1 with fade
- **`scaleUp`**: Scale from 0.95 to 1 with fade
- **`scaleDown`**: Scale from 1 to 0.95 with fade

```tsx
<motion.div variants={scaleIn} initial="hidden" animate="visible">
  Content scales in
</motion.div>
```

### 3. Slide Animations

Position-based transitions for directional movement.

- **`slideInUp`**: Slide in from bottom
- **`slideInDown`**: Slide in from top
- **`slideInLeft`**: Slide in from left
- **`slideInRight`**: Slide in from right

```tsx
<motion.div variants={slideInLeft} initial="hidden" animate="visible">
  Content slides in from left
</motion.div>
```

### 4. Rotate Animations

Rotation-based transitions for dynamic entrances.

- **`rotateIn`**: Rotate -10° to 0° with fade
- **`rotateInClockwise`**: Rotate -180° to 0° with fade
- **`rotateInCounterClockwise`**: Rotate 180° to 0° with fade

```tsx
<motion.div variants={rotateIn} initial="hidden" animate="visible">
  Content rotates in
</motion.div>
```

### 5. Blur Animations

Filter-based transitions for smooth focus effects.

- **`blurIn`**: Blur from 10px to 0px with fade
- **`blurOut`**: Blur from 0px to 10px with fade

```tsx
<motion.div variants={blurIn} initial="hidden" animate="visible">
  Content blurs in
</motion.div>
```

### 6. Bounce Animations

Spring-like transitions for playful, energetic effects.

- **`bounceIn`**: Scale bounce entrance
- **`bounce`**: Continuous vertical bounce

```tsx
<motion.div animate="animate" variants={bounce}>
  Content bounces continuously
</motion.div>
```

### 7. Pulse Animations

Repeating opacity or scale changes for attention.

- **`pulse`**: Opacity pulse (1 → 0.5 → 1)
- **`pulseScale`**: Scale pulse (1 → 1.05 → 1)

```tsx
<motion.div animate="animate" variants={pulse}>
  Content pulses
</motion.div>
```

### 8. Shimmer Animations

Background position shift for loading states.

- **`shimmer`**: Horizontal shimmer effect

```tsx
<motion.div
  animate="animate"
  variants={shimmer}
  style={{
    backgroundImage:
      "linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent)",
  }}
>
  Content shimmers
</motion.div>
```

### 9. Flip Animations

3D rotation-based transitions.

- **`flipInX`**: 3D flip on X axis
- **`flipInY`**: 3D flip on Y axis

```tsx
<motion.div variants={flipInX} initial="hidden" animate="visible">
  Content flips in
</motion.div>
```

### 10. Stagger Animations

Container-based animations that stagger child elements.

- **`staggerContainer`**: Parent variant for staggered children
- **`staggerItem`**: Child variant for staggered animation
- **`containerVariants`**: Alternative stagger container
- **`itemVariants`**: Alternative stagger item

```tsx
<motion.div variants={staggerContainer} initial="hidden" animate="visible">
  {items.map((item) => (
    <motion.div key={item.id} variants={staggerItem}>
      {item.content}
    </motion.div>
  ))}
</motion.div>
```

### 11. Glow Animations

Box shadow pulse for emphasis.

- **`glowPulse`**: Expanding glow effect

```tsx
<motion.div animate="animate" variants={glowPulse}>
  Content glows
</motion.div>
```

### 12. Hover Animations

Interactive animations triggered on hover.

- **`hoverLift`**: Move up on hover
- **`hoverGrow`**: Scale up on hover
- **`hoverGlow`**: Add glow on hover

```tsx
<motion.div
  initial="initial"
  whileHover="hover"
  variants={hoverLift}
>
  Hover me
</motion.div>
```

### 13. Loading Animations

Continuous animations for loading states.

- **`spin`**: Full rotation (1s)
- **`spinSlow`**: Full rotation (2s)

```tsx
<motion.div animate="animate" variants={spin}>
  <Loader2 className="size-6" />
</motion.div>
```

### 14. Wave Animations

Hand-wave like rotation.

- **`wave`**: Wave rotation pattern

```tsx
<motion.div animate="animate" variants={wave}>
  👋
</motion.div>
```

### 15. Page Transitions

Full-page entrance and exit animations.

- **`pageEnter`**: Page entrance animation
- **`pageExit`**: Page exit animation

```tsx
<motion.div
  initial="initial"
  animate="animate"
  exit="exit"
  variants={pageEnter}
>
  Page content
</motion.div>
```

### 16. Modal Animations

Dialog and modal-specific animations.

- **`modalBackdrop`**: Backdrop fade animation
- **`modalContent`**: Modal scale and fade animation

```tsx
<motion.div variants={modalBackdrop} initial="hidden" animate="visible">
  <motion.div variants={modalContent} initial="hidden" animate="visible">
    Modal content
  </motion.div>
</motion.div>
```

## Animated Components

### AnimatedCard

Wrapper component for cards with built-in animations.

```tsx
<AnimatedCard variant="fade" delay={0.1}>
  Card content
</AnimatedCard>
```

**Props:**
- `variant`: `"fade"` | `"scale"` | `"lift"` (default: `"fade"`)
- `delay`: Number in seconds (default: `0`)
- `children`: React node

### AnimatedButton

Button with hover animation.

```tsx
<AnimatedButton animationType="grow">
  Click me
</AnimatedButton>
```

**Props:**
- `animationType`: `"grow"` | `"glow"` | `"lift"` (default: `"grow"`)
- All standard button props

### AnimatedBadge

Badge with optional pulse or glow animation.

```tsx
<AnimatedBadge animated glowing>
  Badge text
</AnimatedBadge>
```

**Props:**
- `animated`: Boolean (default: `false`)
- `glowing`: Boolean (default: `false`)
- All standard badge props

### AnimatedText

Text with character or word-by-word animation.

```tsx
<AnimatedText text="Hello World" variant="word" />
```

**Props:**
- `text`: String to animate
- `variant`: `"fade"` | `"slide"` | `"blur"` | `"word"` | `"char"` (default: `"fade"`)
- `delay`: Number in seconds
- `stagger`: Boolean (default: `false`)

### AnimatedLoader

Loading indicator with multiple styles.

```tsx
<AnimatedLoader type="spin" size="md" />
```

**Props:**
- `type`: `"spin"` | `"pulse"` | `"bounce"` | `"dots"` (default: `"spin"`)
- `size`: `"sm"` | `"md"` | `"lg"` (default: `"md"`)

### AnimatedContainer

Container for staggered child animations.

```tsx
<AnimatedContainer stagger>
  {items.map((item) => (
    <div key={item.id}>{item.content}</div>
  ))}
</AnimatedContainer>
```

**Props:**
- `stagger`: Boolean (default: `true`)
- `delay`: Number in seconds
- `children`: React nodes

## Transition Presets

Pre-configured transition objects for consistency.

```tsx
import { transitionPresets } from "@/lib/animations";

<motion.div transition={transitionPresets.base}>
  Content
</motion.div>
```

**Available presets:**
- `fast`: 0.2s duration
- `base`: 0.4s duration (default)
- `slow`: 0.6s duration
- `slowest`: 0.8s duration
- `bounce`: 0.6s with bounce easing

## Best Practices

### 1. Use `whileInView` for Entrance Animations

Trigger animations when elements enter the viewport:

```tsx
<motion.div
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true, amount: 0.3 }}
  variants={fadeInUp}
>
  Content
</motion.div>
```

### 2. Stagger Child Animations

Use container variants to stagger children:

```tsx
<motion.div
  variants={containerVariants}
  initial="hidden"
  animate="visible"
>
  {items.map((item) => (
    <motion.div key={item.id} variants={itemVariants}>
      {item.content}
    </motion.div>
  ))}
</motion.div>
```

### 3. Combine Multiple Animations

Layer animations for complex effects:

```tsx
<motion.div
  initial={{ opacity: 0, y: 20, scale: 0.95 }}
  animate={{ opacity: 1, y: 0, scale: 1 }}
  transition={{ duration: 0.5 }}
>
  Content
</motion.div>
```

### 4. Use Consistent Easing

All animations use the same easing curve for consistency:

```tsx
ease: [0.16, 1, 0.3, 1] // Cubic Bezier
```

### 5. Respect User Preferences

Consider `prefers-reduced-motion`:

```tsx
const prefersReducedMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)"
).matches;

<motion.div
  variants={fadeInUp}
  transition={prefersReducedMotion ? { duration: 0 } : undefined}
>
  Content
</motion.div>
```

## Performance Tips

1. **Use `once: true` in viewport**: Animations only trigger once
2. **Avoid animating layout properties**: Use `transform` instead
3. **Use GPU-accelerated properties**: `opacity`, `transform`, `filter`
4. **Limit simultaneous animations**: Stagger animations when possible
5. **Use `layout` prop sparingly**: It can impact performance

## Examples

### Hero Section

```tsx
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ staggerChildren: 0.1 }}
>
  <motion.h1 variants={fadeInUp}>Title</motion.h1>
  <motion.p variants={fadeInUp}>Description</motion.p>
  <motion.button variants={fadeInUp}>CTA</motion.button>
</motion.div>
```

### Feature Cards

```tsx
<motion.div
  variants={containerVariants}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
>
  {features.map((feature) => (
    <motion.div key={feature.id} variants={itemVariants}>
      <AnimatedCard>{feature.content}</AnimatedCard>
    </motion.div>
  ))}
</motion.div>
```

### Loading State

```tsx
<AnimatedLoader type="spin" size="lg" />
```

## Customization

To create custom animations, extend the animation library:

```tsx
// lib/animations.ts
export const customFade: Variants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { duration: 0.8, ease: "easeInOut" },
  },
};
```

Then use it like any other variant:

```tsx
<motion.div variants={customFade} initial="hidden" animate="visible">
  Content
</motion.div>
```

## Resources

- [Framer Motion Documentation](https://www.framer.com/motion/)
- [React Bits Animations](https://react-bits.github.io/)
- [Motion Design Principles](https://www.framer.com/motion/introduction/)
