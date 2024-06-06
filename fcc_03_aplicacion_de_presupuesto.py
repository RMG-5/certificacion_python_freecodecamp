'''Aplicación de Presupuesto'''


class Category:
    '''Clase para crear instancias de objetos basados en 
    diferentes categorías presupuestarias'''

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        ledger_records = ''
        for record in self.ledger:
            amount = f"{record['amount']:.2f}"
            description = f"{record['description'][:23]}"
            ledger_records += description.ljust(23) + amount.rjust(7) + '\n'
        return f'{self.category.center(30, "*")}\n{ledger_records}Total: {self.get_balance()}'

    def deposit(self, amount, description=''):
        '''Método para realizar depositos al presupuesto'''
        self.ledger.append(
            {"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        '''Método para realizar retiros del presupuesto'''
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        '''Método para devolver el saldo actual del presupuesto'''
        return sum(map(lambda record: record['amount'], self.ledger))

    def transfer(self, amount, another_budget):
        '''Método para realizar transferencias a otra categoría presupuestaria'''
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {another_budget.category}')
            another_budget.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        '''Método para comprobar si el saldo actual del presupuesto 
        permite realizar el retiro o transferencia deseado'''
        if self.get_balance() < amount:
            return False
        return True


def create_spend_chart(categories):
    '''Función para construir graficos de barras basados en 
    diferentes categorías presupuestarias'''
    total_expenses = []
    longest_name = ''
    bar_chart = ''

    for category in categories:
        category_expenses = 0
        for record in category.ledger:
            if record['amount'] < 0:
                category_expenses += abs(record['amount'])
        total_expenses.append(category_expenses)

        if len(category.category) > len(longest_name):
            longest_name = category.category

    for percentage in range(100, -10, -10):
        bar_chart += str(percentage).rjust(3) + '|'.ljust(2)
        for x, category_expenses in enumerate(total_expenses):
            if category_expenses * 100 // sum(total_expenses) >= percentage:
                bar_chart += 'o'.ljust(3)
            else:
                bar_chart += ''.ljust(3)
        bar_chart += '\n'

    bar_chart += '    ' + ''.center(len(categories) * 3 + 1, "-") + '\n'

    for x in range(len(longest_name)):
        bar_chart += ''.ljust(5)
        for category in categories:
            if len(category.category) <= x:
                bar_chart += '   '
            else:
                bar_chart += category.category[x].ljust(3)
        bar_chart += '\n'

    return f'Percentage spent by category\n{bar_chart}'.strip('\n')


# ********** ********** ********** ********** ********** ********** ********** #
# Ejemplo de uso #

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(500, "deposit")
several = Category('Several')
several.deposit(500, "deposit")
school = Category("School")
school.deposit(1000, 'deposit')
entertainment = Category("Entertainment")
entertainment.deposit(500, 'deposit')
several.withdraw(450, "tickets")
several.transfer(200, school)
clothing.transfer(100, entertainment)
food.withdraw(460.35, 'pantry')
clothing.withdraw(125.55, "pants")
school.withdraw(100, 'books')
school.withdraw(900, 'inscription')
entertainment.withdraw(325.50, 'theatre')

print(food)
print('\n')
print(clothing)
print('\n')
print(several)
print('\n')
print(school)
print('\n')
print(entertainment)
print('\n')
print(create_spend_chart([food, clothing, several, school, entertainment]))

# ********** ********** ********** ********** ********** ********** ********** #
