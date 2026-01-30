back account is base class and savings account, current account are child class , automatically called when an object is created.
attributes are account number, account holde name, balance, interest rate, overdraft limit
mothods are deposit(), withdraw(), get_balance(), display_details()
balance is stored as a protected variable(_balance), direct access, balance is accesses using methods only
savingsaccount , current account inherit from bank account, common functionality is resued
display_details() is overridden in both child classes, withdraw() is overridden in currentaccount to support overdraft
deposit money, withdraw money, overdraft facility, check final balance are create operations in this program
