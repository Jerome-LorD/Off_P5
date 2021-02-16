def find_substitute_2(self, selected_product):
    substitute = None
    offset = 0
    # best_cat = Category().find_best_category(choix.product_id, offset)

    # best_c = best_cat[0]
    # substitute = Product().find_substitute(best_c.bonus)
    # if substitute:
    #     sub_found = substitute[0]

    while not substitute:
        category_id = Category().find_best_category(
            product_id=choix.product_id, offset=offset)
        if not category_id:
            return None

        substitute = self.find_substitute_from_category(cat_id=category_id)
        if substitute:
            return substitute
        offset += 1




class Product:

  def find_substitute(self):
    substitute = None
    offset = 0
    while not substitute:
      category_id = Category().find_best_category(product_id=self.id, offset=offset)
      if not category_id:
        return None

      substitute = self.find_substitute_from_category(id=category_id)
      if substitute:
        return substitute
      offset += 1