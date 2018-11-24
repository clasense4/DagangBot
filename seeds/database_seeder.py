from orator.seeds import Seeder
from seeds import product_table_seeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(product_table_seeder.ProductTableSeeder)
