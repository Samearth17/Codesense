export const codesenseMonacoTheme = {
  base: "vs-dark",
  inherit: true,
  rules: [
    { token: "comment", foreground: "7d8597", fontStyle: "italic" },
    { token: "keyword", foreground: "67e8f9" },
    { token: "number", foreground: "fbbf24" },
    { token: "string", foreground: "34d399" },
    { token: "type", foreground: "c4b5fd" },
    { token: "function", foreground: "e5e7eb" },
  ],
  colors: {
    "editor.background": "#0b0d13",
    "editor.foreground": "#e5e7eb",
    "editorLineNumber.foreground": "#4b5563",
    "editorLineNumber.activeForeground": "#a5f3fc",
    "editorCursor.foreground": "#22d3ee",
    "editor.selectionBackground": "#164e63",
    "editor.inactiveSelectionBackground": "#1f2937",
    "editor.lineHighlightBackground": "#111827",
    "editorGutter.background": "#0b0d13",
  },
} as const;
