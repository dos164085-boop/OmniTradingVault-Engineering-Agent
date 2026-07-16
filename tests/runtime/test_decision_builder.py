"""
Tests for the Runtime Decision Builder.
"""

from src.runtime.decision_builder import (
    DecisionBuilder,
)

from src.runtime.models import (
    DecisionStatus,
    Evidence,
    EvidenceType,
)


def test_build_decision_from_command() -> None:

    builder = DecisionBuilder()

    evidence = Evidence(
        type=EvidenceType.COMMAND,
        source="terminal",
        content="forge test",
    )

    decision = builder.build(evidence)

    assert decision.title == "COMMAND: terminal"
    assert decision.description == "forge test"
    assert (
        decision.rationale
        == "Automatically generated from engineering evidence."
    )
    assert decision.status == DecisionStatus.OPEN


def test_build_decision_from_error() -> None:

    builder = DecisionBuilder()

    evidence = Evidence(
        type=EvidenceType.ERROR,
        source="solc",
        content="Stack too deep",
    )

    decision = builder.build(evidence)

    assert decision.title == "ERROR: solc"
    assert decision.description == "Stack too deep"
    assert decision.status == DecisionStatus.OPEN


def test_build_decision_from_test_result() -> None:

    builder = DecisionBuilder()

    evidence = Evidence(
        type=EvidenceType.TEST,
        source="pytest",
        content="22 passed",
    )

    decision = builder.build(evidence)

    assert decision.title == "TEST: pytest"
    assert decision.description == "22 passed"


def test_builder_is_deterministic() -> None:

    builder = DecisionBuilder()

    evidence = Evidence(
        type=EvidenceType.FILE,
        source="filesystem",
        content="observer.py",
    )

    first = builder.build(evidence)
    second = builder.build(evidence)

    assert first.title == second.title
    assert first.description == second.description
    assert first.rationale == second.rationale
    