from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('products') as table:
            table.increments('id')
            table.text('name').nullable()
            table.text('price').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('products')
