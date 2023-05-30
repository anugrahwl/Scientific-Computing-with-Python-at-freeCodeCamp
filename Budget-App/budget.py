class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []


    def deposit(self, amount, description = ""):
        deposit = {"amount" : amount, "description" : description}
        self.ledger.append(deposit)


    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            withdraw = {"amount" : -1 * amount, "description" : description}
            self.ledger.append(withdraw)
            return True
        return False


    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += float(item["amount"])
        return balance


    def transfer(self, amount, target):
        description = "Transfer to " + target.name
        if self.withdraw(amount, description):
            description = "Transfer from " + self.name
            target.deposit(amount, description)
            return True
        return False


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


    def __str__(self):
        # title
        length = len(self.name)
        asterisk = int((30 - length) / 2)
        if length % 2 == 0:
            output = asterisk * '*' + self.name + asterisk * '*' + '\n'
        else:
            output = (asterisk + 1) * '*' + self.name + asterisk * '*' + '\n'

        # list and total
        total = 0
        for item in self.ledger:
            # left aligned description
            length = len(item["description"])
            output += item["description"][:23] + ' ' * (23 - length)

            # right aligned amount
            amount = "{:.2f}".format(item["amount"])
            length = len(amount)
            if length > 7:
                output += amount[0:7] + '\n'
            else:
                output += ' ' * (7 - length) + amount + '\n'

            #total
            total += item["amount"]

        total = "{:.2f}".format(total)
        output += "Total: " + total

        return output


def create_spend_chart(categories):

    def get_withdrawals(category):
        withdrawals = 0
        for item in category.ledger:
            amount = item["amount"]
            if amount < 0:
                withdrawals += amount
        withdrawals *= -1

        return withdrawals

    total = 0
    names = []
    percentages = []
    for category in categories:
        total += get_withdrawals(category)
    for category in categories:
        percentages.append(100 * (get_withdrawals(category) / total))
        names.append(category.name)

    output = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        buff = " " * (3 - len(str(i))) + str(i) + '| '
        for percentage in percentages:
            if percentage >= i:
                buff += 'o'
            else:
                buff += ' '
            buff += "  "
        output += buff + '\n'
    output += ' ' * 4 + (len(buff) - 4) * '-' + '\n'

    length = 0
    for category in categories:
        length_c = len(category.name)
        if length_c > length:
            length = length_c
    for i in range(length):
        buff = ' ' * 5
        for name in names:
            try:
                buff += name[i]
            except IndexError:
                buff += ' '
            buff += "  "
        buff += '\n'
        output += buff

    return output[:-1]
