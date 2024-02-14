custom_sort_order = sorted(['Godzilla', 'Wonka', 'American Fiction', 'Mean Girls', 'Poor Things', 'Aquaman 2', 'Argylle'], key=lambda x: (len(x), x))
print(f"List after sort: {custom_sort_order}")
