from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.text('username').nullable()
            table.text('telegram_id').nullable()
            table.text('first_name').nullable()
            table.text('last_name').nullable()
            table.text('register_date').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
