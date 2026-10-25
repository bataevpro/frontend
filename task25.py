def calculate_annuity_payment(principal, annual_rate, months):
  # monthly_rate: месячная процентная ставка
  monthly_rate = annual_rate / 12 / 100

  if monthly_rate == 0:
    return principal / months

  # Формула аннуитетного платежа
  annuity_factor = (monthly_rate * (1 + monthly_rate) ** months) / (
      (1 + monthly_rate) ** months - 1
  )
  payment = principal * annuity_factor
  return payment


# Пример использования:
try:
  loan_amount = float(input('Введите сумму кредита (руб.): '))
  interest_rate = float(input('Введите годовую процентную ставку (%): '))
  loan_months = int(input('Введите срок кредита (в месяцах): '))

  monthly_payment = calculate_annuity_payment(
      loan_amount, interest_rate, loan_months
  )
  total_payment = monthly_payment * loan_months
  overpayment = total_payment - loan_amount

  print(f'\nЕжемесячный платёж: {monthly_payment:,.2f} руб.')
  print(f'Общая сумма выплат: {total_payment:,.2f} руб.')
  print(f'Переплата по кредиту: {overpayment:,.2f} руб.')

except ValueError:
  print('Пожалуйста, введите корректные числовые значения.')
