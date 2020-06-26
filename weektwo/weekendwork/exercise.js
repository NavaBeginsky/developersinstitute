//exercise 2
function numbers() {
    for (let i = 0; i < 5; i += 1) {
      console.log(i);
    }
      console.log(i);
  }
  numbers();

  //exercise 3 - this math is not real life bookkeeping but I did it according to the instructions which made very little sense to me
  let moneyInAccount = 50;
  const amountOfVAT = 0.10;
  let expensesAndRevenue = [50, 300];

  function multiplyVATandExpenses(amountOfVAT, expenses){
      return amountOfVAT * expenses;
  }

  function adjustMoneyInAccount(totalRecentExpenses){
       moneyInAccount = moneyInAccount - totalRecentExpenses + expensesAndRevenue[1];
  }

  adjustMoneyInAccount(multiplyVATandExpenses(amountOfVAT, expensesAndRevenue[0]));
  console.log(moneyInAccount);