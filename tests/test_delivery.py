import unittest

from src.Delivery import calculate_delivery_cost


class TestDelivery(unittest.TestCase):


# при правильных данных стоимость и дата доставки рассчитываются верно
    def test_delivery_with_valid_data(self):
        result = calculate_delivery_cost(1, 100, "обычный")
        self.assertEqual(result, (700, "2026-09-04"))


#  посылку весом меньше 0.1 кг отправить нельзя
    def test_delivery_with_weight_below_minimum(self):
        result = calculate_delivery_cost(0.09, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))


# при нулевом расстоянии функция возвращает ошибк
    def test_delivery_with_zero_distance(self):
        result = calculate_delivery_cost(1, 0, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))



# Пнельзя указать неизвестный тип посылки
    def test_delivery_with_invalid_package_type(self):
        result = calculate_delivery_cost(1, 100, "неизвестный")
        self.assertEqual(result, (-1, "0000-00-00"))

#при весе ровно 20 кг применяется коэффициент 1.5
    def test_delivery_with_weight_equal_twenty(self):
        result = calculate_delivery_cost(20.0, 100, "обычный")
        self.assertEqual(result, (1050, "2026-09-04"))


#за хрупкую посылку добавляется 300 рублей
    def test_delivery_with_fragile_package(self):
        result = calculate_delivery_cost(1, 100, "хрупкий")
        self.assertEqual(result, (1000, "2026-09-04"))


# за опасную посылку добавляется 1000 рублей
    def test_delivery_with_dangerous_package(self):
        result = calculate_delivery_cost(1, 100, "опасный")
        self.assertEqual(result, (1700, "2026-09-04"))

#  экспресс-доставка стоит дороже обычной
    def test_express_delivery_costs_more(self):
        regular = calculate_delivery_cost(1, 100, "обычный")
        express = calculate_delivery_cost(1, 100, "обычный", is_express=True)
        self.assertGreater(express[0], regular[0])


# даже при экспресс доставке посылка идет минимум один день
    def test_express_delivery_minimum_one_day(self):
        result = calculate_delivery_cost(1, 100, "обычный", is_express=True)
        self.assertEqual(result[1], "2026-09-04")

# для расстояния 501 км понадобится два дня, а не один
    def test_delivery_distance_above_five_hundred(self):
        result = calculate_delivery_cost(1, 501, "обычный")
        self.assertEqual(result[1], "2026-09-05")