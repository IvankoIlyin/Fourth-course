import datetime
import csv
import matplotlib.pyplot as plt


class Sale:
    def __init__(self, product_name, quantity, price_per_unit, sale_date=None):
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.sale_date = sale_date or datetime.date.today()

    def total_price(self):
        return self.quantity * self.price_per_unit


class SalesManager:
    def __init__(self):
        self.sales = []
        self.products = {}

    def record_sale(self, product_name, quantity, price_per_unit):
        sale = Sale(product_name, quantity, price_per_unit)
        self.sales.append(sale)

        if product_name in self.products:
            self.products[product_name]['sold'] += quantity
        else:
            self.products[product_name] = {'sold': quantity, 'price': price_per_unit}

    def analyze_sales_trend(self):
        for product, data in self.products.items():
            pass

    def generate_reports(self, csv_filename="sales_report.csv"):
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Product Name", "Quantity", "Price per Unit", "Total Price"])
            for sale in self.sales:
                writer.writerow([sale.sale_date, sale.product_name, sale.quantity, sale.price_per_unit, sale.total_price()])

    def evaluate_efficiency(self):
        total_sales = sum(sale.total_price() for sale in self.sales)

    def create_summary_report(self, summary_csv_filename="summary_report.csv"):
        with open(summary_csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Total Sold"])
            for product, data in self.products.items():
                writer.writerow([product, data['sold']])

    def plot_sales_graph(self, graph_filename="sales_graph.png"):
        product_names = [product for product in self.products.keys()]
        quantities = [data['sold'] for data in self.products.values()]

        plt.figure(figsize=(10, 6))
        plt.bar(product_names, quantities, color='skyblue')
        plt.title("Sales by Product", fontsize=16)
        plt.xlabel("Product Name", fontsize=12)
        plt.ylabel("Total Sold", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(graph_filename)


class OperationManager:
    def __init__(self):
        self.sales_manager = SalesManager()

    def execute_command(self, command, *args):
        if command == "record_sale":
            self.sales_manager.record_sale(*args)
        elif command == "analyze_sales_trend":
            self.sales_manager.analyze_sales_trend()
        elif command == "generate_reports":
            self.sales_manager.generate_reports(*args)
        elif command == "evaluate_efficiency":
            self.sales_manager.evaluate_efficiency()
        elif command == "create_summary_report":
            self.sales_manager.create_summary_report(*args)
        elif command == "plot_sales_graph":
            self.sales_manager.plot_sales_graph(*args)

    def execute(self, commands):
        for command, *args in commands:
            self.execute_command(command, *args)


if __name__ == "__main__":
    manager = OperationManager()

    commands_to_execute = [
        ("record_sale", "SKIF Urbanite II BSW Black", 76, 1600),
        ("record_sale", "SKIF Townee Jr SW Black", 45, 1180),
        ("record_sale", "SKIF Defender II BSW Olive", 12, 1600),
        ("record_sale", "SKIF Shark II SW Black", 22, 1600),
        ("record_sale", "SKIF Secure SW Black", 17, 1470),
        ("record_sale", "SKIF Predator 2.0 SW Olive", 2, 2860),
        ("record_sale", "SKIF Hole Black", 55, 903),
        ("record_sale", "SKIF Eagle Orange", 21, 1410),
        ("generate_reports", "sales_report.csv"),
        ("create_summary_report", "summary_report.csv"),
        ("plot_sales_graph", "sales_graph.png"),
        ("evaluate_efficiency",),
    ]

    manager.execute(commands_to_execute)
