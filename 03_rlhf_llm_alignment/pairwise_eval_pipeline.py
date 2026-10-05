"""
Pairwise Evaluation & Schema Validation Pipeline for LLM Alignment
Author: Yvonne Obi
Module: 03_rlhf_llm_alignment
"""

import json
import sys
from typing import Dict, List, Any


METRIC_WEIGHTS = {
    "relevance": 0.20,
    "usefulness": 0.25,
    "personalization": 0.25,
    "clarity": 0.15,
    "context_alignment": 0.15
}


def calculate_weighted_score(scores: Dict[str, float]) -> float:
    """Calculates the weighted score for an evaluation condition."""
    total_score = sum(scores[metric] * weight for metric, weight in METRIC_WEIGHTS.items())
    return round(total_score, 2)


def validate_scenario_schema(entry: Dict[str, Any]) -> bool:
    """Validates structural integrity of an evaluation record."""
    required_keys = ["scenario_id", "context_dimension", "user_query", "evaluations"]
    for key in required_keys:
        if key not in entry:
            raise KeyError(f"Schema Validation Error: Missing required key '{key}'")
    
    if entry["context_dimension"] not in ["PERSONAL", "PROFESSIONAL", "INTERPERSONAL"]:
        raise ValueError(f"Invalid context_dimension: {entry['context_dimension']}")
        
    return True


def evaluate_pairwise_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Processes pairwise evaluation metrics and determines winner and score delta."""
    validate_scenario_schema(record)
    
    evals = record["evaluations"]
    score_a = calculate_weighted_score(evals["condition_a"]["scores"])
    score_b = calculate_weighted_score(evals["condition_b"]["scores"])
    
    delta = round(abs(score_a - score_b), 2)
    
    if score_b > score_a:
        winner = "Condition B (Situated Context)"
    elif score_a > score_b:
        winner = "Condition A (Baseline)"
    else:
        winner = "Tie"
        
    return {
        "scenario_id": record["scenario_id"],
        "context_dimension": record["context_dimension"],
        "score_a_baseline": score_a,
        "score_b_situated": score_b,
        "winning_condition": winner,
        "score_delta": delta
    }


def run_pipeline_demo():
    """Execution sandbox using sample situated evaluation records."""
    sample_data = [
        {
            "scenario_id": "SCN-0001",
            "context_dimension": "PROFESSIONAL",
            "user_query": "Draft a status update regarding a 2-week engineering delay.",
            "evaluations": {
                "condition_a": {
                    "scores": {"relevance": 3.0, "usefulness": 2.0, "personalization": 1.0, "clarity": 4.0, "context_alignment": 1.0}
                },
                "condition_b": {
                    "scores": {"relevance": 5.0, "usefulness": 5.0, "personalization": 5.0, "clarity": 5.0, "context_alignment": 5.0}
                }
            }
        },
        {
            "scenario_id": "SCN-0002",
            "context_dimension": "PERSONAL",
            "user_query": "Give me a 3-day budget meal plan and shopping list.",
            "evaluations": {
                "condition_a": {
                    "scores": {"relevance": 4.0, "usefulness": 2.0, "personalization": 1.0, "clarity": 4.0, "context_alignment": 1.0}
                },
                "condition_b": {
                    "scores": {"relevance": 5.0, "usefulness": 5.0, "personalization": 5.0, "clarity": 5.0, "context_alignment": 5.0}
                }
            }
        }
    ]

    print("=== Starting Module 03 LLM Alignment Pipeline Execution ===")
    results = [evaluate_pairwise_record(rec) for rec in sample_data]
    
    for res in results:
        print(f"[{res['scenario_id']}] Dimension: {res['context_dimension']} | Winner: {res['winning_condition']} | Score Delta: +{res['score_delta']}")
    
    print("=== Pipeline Execution Completed Successfully ===")


if __name__ == "__main__":
    run_pipeline_demo()
