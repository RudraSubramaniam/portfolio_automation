# test_mental_arithmetic.py
from typing import List, Iterator
import pytest
from Problem_set_0.mental_arithmetic_trainer import find_sum, inp

# ==========================================
# 1. PARAMETERIZED MATHEMATICAL LOGIC TESTS
# ==========================================

@pytest.mark.parametrize(
    "input_array, expected_total",
    [
        ([8, 9, 92, 0, 111], 220), # Standard positive integer track
        ([-5, 8, 8, 0, -3], 8),     # Negative boundary checks
        ([], 0),                    # Empty initialization state fallback
        ([10, -10], 0),             # Zero sum cancellation evaluation
    ]
)
def test_find_sum(input_array: List[int], expected_total: int) -> None:
    """Verifies that calculate_sum correctly aggregates structural array items."""
    assert find_sum(input_array) == expected_total


# ==========================================
# 2. IO INTERCEPTION & MOCKING TESTS
# ==========================================

def test_inp(monkeypatch: pytest.MonkeyPatch) -> None:
    """Validates terminal stream processing, type casting, and loop breakout logic."""
    
    # Initialize sequential stream data state
    mocked_terminal_stream: Iterator[str] = iter(["10", "20", "Q"])
    
    # Intercept system input calls and inject the iterator state machine
    monkeypatch.setattr("builtins.input", lambda _: next(mocked_terminal_stream))
    
    # Execute targeted runtime process
    execution_result: List[int] = inp()
    
    # State Invariant Verifications
    assert execution_result == [10, 20], "Fault: Returned array data mismatch."
    assert len(execution_result) == 2, "Fault: Result array tracked invalid token length."