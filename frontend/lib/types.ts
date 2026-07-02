export type FeatureSnapshot = {
  docstring_ratio: number;
  type_annotation_ratio: number;
  maintainability_index: number;
  avg_identifier_length: number;
  single_char_var_ratio: number;
  comment_density: number;
  blank_line_ratio: number;
  avg_cyclomatic_complexity: number;
};

export type ScanResult = {
  label: "ai" | "human" | string;
  confidence: number;
  is_ai: boolean;
  top_signals: string[];
  features: FeatureSnapshot;
  filename: string;
};

export type ScanRequest = {
  code: string;
  filename: string;
};

export type RuntimeConfig = {
  NEXT_PUBLIC_API_URL?: string;
};

declare global {
  interface Window {
    __CODESENSE_CONFIG__?: RuntimeConfig;
  }
}
