class Tax:
    FRUIT = 0.5
    OTHER = 0.2

class TaxCalculator:

    @staticmethod
    def tax_for_order_element(order_element):
        product_category = order_element.product.category
        if product_category == "Owoce":
            tax_rate = Tax.FRUIT
        else:
            tax_rate = Tax.OTHER
        return tax_rate * order_element.calculate_price()