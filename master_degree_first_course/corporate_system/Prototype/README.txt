
Клас Sale
Поля:
-Назва товару (product_name)
-Кількість (quantity)
-Ціна за одиницю (price_per_unit)
-Дата продажу (sale_date)
Методи:
-total_price() — підраховує загальну суму продажу (кількість × ціна).

Клас SalesManager
Методи:
-record_sale(product_name, quantity, price_per_unit)— додає новий продаж до бази.
-analyze_sales_trend() — аналізує тенденції продажів (наприклад, які товари продаються найкраще).
-generate_reports(csv_filename) — створює детальний звіт про продажі у форматі CSV.
-evaluate_efficiency() — оцінює загальну ефективність продажів, підраховуючи дохід.
-create_summary_report(summary_csv_filename) — створює зведений звіт про кількість проданих товарів у форматі CSV.
-plot_sales_graph(graph_filename) — будує графік продажів за категоріями товарів та зберігає його у PNG.

Клас OperationManager
Методи:
-execute_command(command, *args) — виконує одну команду з переданими параметрами.
-execute(commands) — обробляє список команд для автоматизації задач.


Результати роботи:
Вихідні файли:
-CSV:
  - sales_report.csv — звіт з усіма продажами (дата, товар, кількість, ціна, загальна вартість).
  - summary_report.csv — звіт із підрахунком проданих одиниць кожного товару.
-PNG:
  - sales_graph.png — стовпчаста діаграма, що показує обсяги продажів для кожного товару.
