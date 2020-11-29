import pytest
from Car import Car
speed_datard = {45}
car_speedr = {50}
speed_datara = {55}

# @pytest.fixture
# @pytest.mark.parametrize("speed_var", speed_data)
# def my_car(speed_var):
#     return Car(speed_var)


@pytest.mark.parametrize("car_speed", car_speedr)
@pytest.mark.parametrize("speed_brake", speed_datard)
def test_car_brake(car_speed, speed_brake):
    my_car = Car(car_speed)
    my_car.brake()
    assert my_car.speed == speed_brake


@pytest.mark.parametrize("car_speed", car_speedr)
@pytest.mark.parametrize("speed_accelerate", speed_datara)
def test_car_accelerate(car_speed, speed_accelerate):
    my_car = Car(car_speed)
    my_car.accelerate()
    assert my_car.speed == speed_accelerate


