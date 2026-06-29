from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .constraints import load_constraints
from .livelink_builder import write_livelink_script
from .matlab_reader import inspect_matlab_file


def main() -> None:
    parser = argparse.ArgumentParser(description="COMSOL small surrogate model tooling")
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_parser = sub.add_parser("inspect-matlab", help="Read a COMSOL MATLAB builder script")
    inspect_parser.add_argument("path")

    validate_parser = sub.add_parser("validate", help="Validate a constrained model JSON file")
    validate_parser.add_argument("path")

    generate_parser = sub.add_parser("generate-matlab", help="Generate a LiveLink MATLAB script")
    generate_parser.add_argument("constraints")
    generate_parser.add_argument("output")

    train_parser = sub.add_parser("train", help="Train a local small surrogate model")
    train_parser.add_argument("csv")
    train_parser.add_argument("model")
    train_parser.add_argument("--inputs", nargs="+", required=True)
    train_parser.add_argument("--outputs", nargs="+", required=True)

    predict_parser = sub.add_parser("predict", help="Predict using a saved surrogate model")
    predict_parser.add_argument("model")
    predict_parser.add_argument("--inputs", nargs="+", type=float, required=True)

    scan_docs_parser = sub.add_parser("scan-comsol-docs", help="Scan local COMSOL PDF documentation directories")
    scan_docs_parser.add_argument(
        "--root",
        default="D:/COMSOL64/Multiphysics/doc/pdf",
        help="COMSOL PDF documentation root directory",
    )
    scan_docs_parser.add_argument(
        "--output-dir",
        default="generated",
        help="Directory for generated catalog and modeling logic files",
    )

    summarize_case_parser = sub.add_parser("summarize-case", help="Summarize a COMSOL case directory into the local knowledge base")
    summarize_case_parser.add_argument("case_dir")
    summarize_case_parser.add_argument("--title", default=None)
    summarize_case_parser.add_argument("--output-dir", default="generated/case_knowledge")
    summarize_case_parser.add_argument("--memory-path", default="generated/case_memory/case_memory.json")

    query_memory_parser = sub.add_parser("query-memory", help="Query remembered COMSOL cases")
    query_memory_parser.add_argument("query")
    query_memory_parser.add_argument("--memory-path", default="generated/case_memory/case_memory.json")
    query_memory_parser.add_argument("--top-k", type=int, default=5)

    plan_model_parser = sub.add_parser("plan-model", help="Generate a COMSOL model construction and analysis plan from remembered cases")
    plan_model_parser.add_argument("requirement")
    plan_model_parser.add_argument("--memory-path", default="generated/case_memory/case_memory.json")
    plan_model_parser.add_argument("--top-k", type=int, default=5)

    args = parser.parse_args()

    if args.command == "inspect-matlab":
        print(inspect_matlab_file(args.path).to_json())
    elif args.command == "validate":
        load_constraints(args.path)
        print(json.dumps({"valid": True, "path": args.path}, ensure_ascii=False, indent=2))
    elif args.command == "generate-matlab":
        output = write_livelink_script(args.constraints, args.output)
        print(json.dumps({"generated": str(output)}, ensure_ascii=False, indent=2))
    elif args.command == "train":
        try:
            from .surrogate import train_surrogate
        except ModuleNotFoundError as exc:
            raise SystemExit(
                f"Missing training dependency: {exc.name}. "
                "Run `pip install -r requirements.txt` inside comsol_training_small_model."
            ) from exc

        report = train_surrogate(args.csv, args.model, args.inputs, args.outputs)
        print(json.dumps(asdict(report), ensure_ascii=False, indent=2))
    elif args.command == "predict":
        try:
            from .surrogate import predict
        except ModuleNotFoundError as exc:
            raise SystemExit(
                f"Missing prediction dependency: {exc.name}. "
                "Run `pip install -r requirements.txt` inside comsol_training_small_model."
            ) from exc

        print(json.dumps(predict(args.model, args.inputs), ensure_ascii=False, indent=2))
    elif args.command == "scan-comsol-docs":
        from .comsol_knowledge import scan_pdf_root, write_catalog_outputs

        catalog = scan_pdf_root(args.root)
        outputs = write_catalog_outputs(catalog, args.output_dir)
        print(
            json.dumps(
                {
                    "catalog": {
                        "module_count": catalog["module_count"],
                        "pdf_count": catalog["pdf_count"],
                        "domain_counts": catalog["domain_counts"],
                    },
                    "outputs": outputs,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif args.command == "summarize-case":
        from .case_knowledge import summarize_case_directory
        from .case_memory import remember_case

        result = summarize_case_directory(args.case_dir, title=args.title, output_dir=args.output_dir)
        card = result["card"]
        memory = remember_case(card, args.memory_path)
        print(
            json.dumps(
                {
                    "title": card["title"],
                    "training_stage": card["training_stage"],
                    "file_summary": card["file_summary"],
                    "parameters": len(card["parameters"]),
                    "post_learning_summary": card.get("post_learning_summary", {}),
                    "outputs": result["outputs"],
                    "memory": {
                        "path": memory["memory_path"],
                        "case_count": memory["case_count"],
                    },
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif args.command == "query-memory":
        from .case_memory import query_memory

        print(json.dumps(query_memory(args.query, args.memory_path, args.top_k), ensure_ascii=False, indent=2))
    elif args.command == "plan-model":
        from .case_memory import generate_model_plan

        print(json.dumps(generate_model_plan(args.requirement, args.memory_path, args.top_k), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
