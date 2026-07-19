import ast
import builtins

try:
    import radon.complexity as radon_cc
    import radon.metrics as radon_mi

    HAS_RADON = True
except ImportError:
    HAS_RADON = False


def extract_features(code: str) -> dict:
    features = {}
    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]
    comment_lines = [l for l in lines if l.strip().startswith("#")]

    # ── TIER 1: Formatting ──────────────────────────────────────────
    features["total_lines"] = len(lines)
    features["blank_line_ratio"] = round((len(lines) - len(non_empty)) / max(len(lines), 1), 4)
    features["avg_line_length"] = round(sum(len(l) for l in non_empty) / max(len(non_empty), 1), 2)
    features["long_line_ratio"] = round(
        sum(1 for l in lines if len(l) > 79) / max(len(lines), 1), 4
    )

    # ── TIER 1: Comments ────────────────────────────────────────────
    features["comment_density"] = round(len(comment_lines) / max(len(non_empty), 1), 4)

    # ── AST BLOCK ───────────────────────────────────────────────────
    try:
        tree = ast.parse(code)

        functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        loops = [n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))]
        conditionals = [n for n in ast.walk(tree) if isinstance(n, ast.If)]
        try_blocks = [n for n in ast.walk(tree) if isinstance(n, ast.Try)]
        imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
        assertions = [n for n in ast.walk(tree) if isinstance(n, ast.Assert)]

        # ── TIER 3: Structure ────────────────────────────────────────
        features["num_functions"] = len(functions)
        features["num_classes"] = len(classes)
        features["num_loops"] = len(loops)
        features["num_conditionals"] = len(conditionals)
        features["num_try_except"] = len(try_blocks)
        features["import_count"] = len(imports)
        features["assertion_count"] = len(assertions)

        # ── TIER 2: Function length ──────────────────────────────────
        func_lengths = []
        for f in functions:
            start = f.lineno
            end = max((getattr(n, "lineno", start) for n in ast.walk(f)), default=start)
            func_lengths.append(end - start + 1)

        features["avg_function_length"] = round(sum(func_lengths) / max(len(func_lengths), 1), 2)
        features["max_function_length"] = max(func_lengths) if func_lengths else 0

        # ── TIER 1: Docstring ratio ──────────────────────────────────
        docstrings = sum(1 for f in functions if ast.get_docstring(f))
        features["docstring_ratio"] = round(docstrings / max(len(functions), 1), 4)

        # ── TIER 1: Naming ───────────────────────────────────────────
        builtin_names = set(dir(builtins))
        names = [
            n.id
            for n in ast.walk(tree)
            if isinstance(n, ast.Name) and n.id not in builtin_names
        ]
        features["avg_identifier_length"] = round(
            sum(len(n) for n in names) / max(len(names), 1), 2
        )
        features["single_char_var_ratio"] = round(
            sum(1 for n in names if len(n) == 1) / max(len(names), 1), 4
        )

        # ── TIER 2: Type annotations ─────────────────────────────────
        annotated = sum(1 for f in functions if f.returns or any(a.annotation for a in f.args.args))
        features["type_annotation_ratio"] = round(annotated / max(len(functions), 1), 4)

        # ── TIER 3: Magic numbers ────────────────────────────────────
        magic_numbers = [
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.Constant)
            and isinstance(n.value, (int, float))
            and n.value not in (0, 1, -1, 2, True, False)
        ]
        features["magic_number_count"] = len(magic_numbers)

        # ── TIER 3: Nested functions ─────────────────────────────────
        nested = 0
        for f in functions:
            inner = [n for n in ast.walk(f) if isinstance(n, ast.FunctionDef) and n is not f]
            if inner:
                nested += 1
        features["nested_function_count"] = nested

        features["ast_parse_success"] = 1

    except SyntaxError:
        for key in [
            "num_functions",
            "num_classes",
            "num_loops",
            "num_conditionals",
            "num_try_except",
            "import_count",
            "assertion_count",
            "avg_function_length",
            "max_function_length",
            "docstring_ratio",
            "avg_identifier_length",
            "single_char_var_ratio",
            "type_annotation_ratio",
            "magic_number_count",
            "nested_function_count",
        ]:
            features[key] = 0
        features["ast_parse_success"] = 0

    # ── TIER 1 & 2: Radon complexity ────────────────────────────────
    if HAS_RADON:
        try:
            blocks = radon_cc.cc_visit(code)
            complexities = [b.complexity for b in blocks]
            features["avg_cyclomatic_complexity"] = round(
                sum(complexities) / max(len(complexities), 1), 2
            )
            features["max_cyclomatic_complexity"] = max(complexities) if complexities else 0
            features["maintainability_index"] = round(radon_mi.mi_visit(code, multi=True), 2)
        except Exception:
            features["avg_cyclomatic_complexity"] = 0
            features["max_cyclomatic_complexity"] = 0
            features["maintainability_index"] = 0
    else:
        features["avg_cyclomatic_complexity"] = 0
        features["max_cyclomatic_complexity"] = 0
        features["maintainability_index"] = 0

    return features
