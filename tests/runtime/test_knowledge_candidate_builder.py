"""
Tests for the Runtime Knowledge Candidate Builder.
"""

from src.runtime.knowledge_candidate_builder import (
    KnowledgeCandidateBuilder,
)

from src.runtime.models import (
    CandidateStatus,
    Decision,
)


def test_build_candidate() -> None:

    builder = KnowledgeCandidateBuilder()

    decision = Decision(
        title="Compiler Error",
        description="Stack too deep while compiling.",
        rationale="Compilation failed during validation.",
    )

    candidate = builder.build(decision)

    assert candidate.title == decision.title
    assert candidate.summary == decision.description
    assert candidate.decision_ids == [decision.id]
    assert candidate.status == CandidateStatus.DRAFT


def test_candidate_contains_decision_reference() -> None:

    builder = KnowledgeCandidateBuilder()

    decision = Decision(
        title="Forge Tests",
        description="22 tests passed.",
        rationale="Regression suite completed.",
    )

    candidate = builder.build(decision)

    assert len(candidate.decision_ids) == 1
    assert candidate.decision_ids[0] == decision.id


def test_builder_is_deterministic() -> None:

    builder = KnowledgeCandidateBuilder()

    decision = Decision(
        title="Observer",
        description="Observer converted Event into Evidence.",
        rationale="Pipeline execution.",
    )

    first = builder.build(decision)
    second = builder.build(decision)

    assert first.title == second.title
    assert first.summary == second.summary
    assert first.decision_ids == second.decision_ids


def test_new_candidate_starts_as_draft() -> None:

    builder = KnowledgeCandidateBuilder()

    decision = Decision(
        title="Knowledge Candidate",
        description="Candidate generated from Decision.",
        rationale="Runtime pipeline.",
    )

    candidate = builder.build(decision)

    assert candidate.status == CandidateStatus.DRAFT
    assert not candidate.is_publishable()
    