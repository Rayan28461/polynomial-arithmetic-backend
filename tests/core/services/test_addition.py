from src.core.services.addition import add
import numpy as np

class TestAdd:
    def test_add_successful(
        self,
        poly1: list[list[int]],
        poly2: list[list[int]],
        sum_output: list[list[int]],
    ) -> None:
        for op1, op2, output in zip(poly1, poly2, sum_output):
            assert np.array_equal(add(op1, op2), output)
