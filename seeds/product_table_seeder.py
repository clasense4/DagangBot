from orator.seeds import Seeder


class ProductTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('products').insert([{
            'id': 1,
            'name' : 'genteng',
            'price' : 1000
        },
        {
            'id': 2,
            'name' : 'beton',
            'price' : 25000000
        }])

