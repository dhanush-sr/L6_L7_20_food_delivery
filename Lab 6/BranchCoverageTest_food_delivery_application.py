import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# delivery_charge

def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20


def test_out_of_range_raises():
    with pytest.raises(ValueError):
        delivery_charge(20, 200, False)


def test_free_delivery_large_order():
    assert delivery_charge(5, 600, False) == 0


def test_mid_distance_order():
    assert delivery_charge(5, 200, False) == 40


def test_far_order_in_rain():
    assert delivery_charge(10, 200, True) == 90


# apply_coupon

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300


def test_invalid_coupon_raises():
    with pytest.raises(ValueError):
        apply_coupon(300, "FREE", False)


def test_welcome_not_first_order_raises():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_coupon_below_minimum():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_coupon_applied():
    assert apply_coupon(300, "SAVE50", False) == 250


# estimated_time

def test_time_peak_and_busy():
    assert estimated_time(5, True, True) == 65


# branches missed by the code coverage tests

def test_zero_distance_raises():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)


def test_boundary_distances():
    assert delivery_charge(3, 499, False) == 20
    assert delivery_charge(8, 499, False) == 40
    assert delivery_charge(15, 499, False) == 60


def test_welcome_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_coupon_at_minimum():
    assert apply_coupon(200, "SAVE50", False) == 150


def test_time_off_peak_not_busy():
    assert estimated_time(5, False, False) == 35


def test_time_peak_not_busy():
    assert estimated_time(5, True, False) == 45


def test_time_off_peak_busy():
    assert estimated_time(5, False, True) == 50
