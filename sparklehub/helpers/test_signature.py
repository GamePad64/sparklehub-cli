import io

import pytest

from sparklehub.helpers.signature import sign_ed25519_b64


# Test vectors, generated by generate_keys and sign_update from Sparkle distribution
@pytest.mark.parametrize(
    "private_key,data,expected",
    [
        (
            "OOijEO/iLMLqy+X4HMRgd/FYCQfIJoJ4pbgn4QdmY2yYhu0REwyxasPDnmUqtTkP7e0hUOj5L5Irj1g59HMELBq+gNy6j2VJynilVLVT4pZwPYPtnhVvGEgKm9QPERiY",
            b"",
            "lakeaLgS9wbGAwvr99K2qP8n00OYCZdL8kL0tHHxqxB3HVSK4BichJ5wIcQ13rMt6eivjM2QkX/rji11a1p3CA==",
        ),
        (
            "OOijEO/iLMLqy+X4HMRgd/FYCQfIJoJ4pbgn4QdmY2yYhu0REwyxasPDnmUqtTkP7e0hUOj5L5Irj1g59HMELBq+gNy6j2VJynilVLVT4pZwPYPtnhVvGEgKm9QPERiY",
            b"\n",
            "87SN7O1LXu+Ysfq+5orNTzc+DhyLb9iVG3uPxDR/ZXxFjFRVbqiLMzCjEGuoSOczlrm1NtQ8peF83RgTbYY8BA==",
        ),
    ],
)
def test_sign_ed25519(private_key, data, expected):
    assert sign_ed25519_b64(io.BytesIO(data), private_key) == expected
