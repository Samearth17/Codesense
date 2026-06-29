export default function HomePage() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      <section className="mx-auto flex min-h-screen max-w-5xl flex-col justify-center px-6 py-16">
        <p className="text-sm font-medium text-muted-foreground">CodeSense</p>
        <h1 className="mt-4 max-w-3xl text-4xl font-semibold tracking-normal sm:text-5xl">
          Explainable code authorship analysis.
        </h1>
        <p className="mt-6 max-w-2xl text-base leading-7 text-muted-foreground">
          Production scaffold ready for a Next.js interface, FastAPI services,
          and an independent machine-learning pipeline.
        </p>
      </section>
    </main>
  );
}
