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
