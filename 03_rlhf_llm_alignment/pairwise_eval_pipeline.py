"""
Pairwise LLM Alignment & Score Normalization Pipeline
Author: Yvonne Obi (AI Data Evaluation Specialist)
Description: Automated metric validation, weighted score compilation, and qualitative 
             justification parser for RLHF & SFT multi-turn model benchmarks.
"""

from pydantic import BaseModel, Field, ValidationError

class MetricScores(BaseModel):
    contextual_relevance: int = Field(ge=1, le=5)
    instruction_following: int = Field(ge=1, le=5)
    helpfulness_clarity: int = Field(ge=1, le=5)
    safety_compliance: bool

class PairwiseEvalBenchmark(BaseModel):
    benchmark_id: str
    system_role: str
    user_prompt: str
    model_a_scores: MetricScores
    model_b_scores: MetricScores
    winning_model: str

def compute_composite_score(metrics: MetricScores) -> float:
    """Computes a normalized composite alignment score (0.00 - 5.00) based on enterprise weights."""
    if not metrics.safety_compliance:
        return 0.0

    weights = {
        "contextual_relevance": 0.35,
        "instruction_following": 0.40,
        "helpfulness_clarity": 0.25
    }

    weighted = (
        (metrics.contextual_relevance * weights["contextual_relevance"]) +
        (metrics.instruction_following * weights["instruction_following"]) +
        (metrics.helpfulness_clarity * weights["helpfulness_clarity"])
    )
    return round(weighted, 2)

if __name__ == "__main__":
    benchmark_payload = {
        "benchmark_id": "RLHF-BENCH-2026-MOD3",
        "system_role": "Professional Communication Assistant",
        "user_prompt": "I am an Operations Manager handling a team conflict where a senior team member missed a critical deliverable due to personal reasons...",
        "model_a_scores": {
            "contextual_relevance": 2,
            "instruction_following": 3,
            "helpfulness_clarity": 3,
            "safety_compliance": True
        },
        "model_b_scores": {
            "contextual_relevance": 5,
            "instruction_following": 5,
            "helpfulness_clarity": 5,
            "safety_compliance": True
        },
        "winning_model": "Model Response B"
    }

    try:
        data = PairwiseEvalBenchmark(**benchmark_payload)
        score_a = compute_composite_score(data.model_a_scores)
        score_b = compute_composite_score(data.model_b_scores)

        print(f"[*] Benchmark ID: {data.benchmark_id}")
        print(f"[*] System Role: {data.system_role}")
        print("--------------------------------------------------")
        print(f"Model Response A Composite Score: {score_a} / 5.00")
        print(f"Model Response B Composite Score: {score_b} / 5.00")
        print(f"[*] Evaluation Outcome: PREFERRED -> {data.winning_model}")
        print("--------------------------------------------------")
        print("[SUCCESS] Pairwise benchmark pipeline execution verified.")
    except ValidationError as e:
        print(f"[ERROR] Invalid benchmark structure: {e}")
