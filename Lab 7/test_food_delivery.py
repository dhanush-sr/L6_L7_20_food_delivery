from hypothesis import given, strategies as st
from food_delivery import parse_order, delivery_eta, coupon_discount


# 1. No-crash fuzz tests: any text (or None) must be handled without an exception

@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        result = parse_order(s)
    except Exception as e:
        assert False, f"parse_order crashed with: {e!r}"
    assert isinstance(result, dict)


@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        result = delivery_eta(s)
    except Exception as e:
        assert False, f"delivery_eta crashed with: {e!r}"
    assert result is None or isinstance(result, int)


@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        result = coupon_discount(s)
    except Exception as e:
        assert False, f"coupon_discount crashed with: {e!r}"
    assert isinstance(result, int)


# 2. Property tests on structured inputs: valid data must still give correct results

names = st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1, max_size=10)


@given(st.dictionaries(names, st.integers(min_value=1, max_value=100), min_size=1))
def test_parse_order_valid_round_trip(order):
    csv = ",".join(f"{name}:{qty}" for name, qty in order.items())
    assert parse_order(csv) == order


@given(st.floats())
def test_delivery_eta_any_float(distance):
    try:
        result = delivery_eta(str(distance))
    except Exception as e:
        assert False, f"delivery_eta crashed on {distance!r} with: {e!r}"
    if result is not None:
        assert result >= 15, "ETA can never be below the 15 minute base time"


@given(st.integers(min_value=0, max_value=10**6))
def test_coupon_discount_valid_codes(n):
    assert coupon_discount(f"SAVE{n}") == n
    assert coupon_discount(f"save{n}") == n


@given(st.integers(max_value=-1))
def test_coupon_discount_never_negative(n):
    assert coupon_discount(f"SAVE{n}") >= 0
