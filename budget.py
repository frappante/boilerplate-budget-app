class Category:

  name = ""
  ledger = []
  # {"amount": amount, "description": description}

  def __init__(self, c):
    self.name = c
    self.ledger = []

  def check_funds(self, amount):
  # used by withdraw and transfer
    self.total = 0
    self.a = amount

    for n in self.ledger:
      for k,v in n.items():
        if k == "amount":
          self.total += v

    if self.total >= self.a:
      return True
    else:
      return False   

    
  def deposit (self, amount, description = ""):
    self.record = dict()
    self.record["amount"] = amount
    self.record["description"] = description
    self.ledger.append(self.record)   


  def withdraw (self, amount, description = ""):
    
    if self.check_funds(amount) == True:

      self.record = dict()
      self.record["amount"] = -(amount)
      self.record["description"] = description
      self.ledger.append(self.record)   
      return True
    else:
      return False     

  def get_balance(self):
    
    self.total = 0

    for n in self.ledger:
      for k,v in n.items():
        if k == "amount":
          self.total += v
    return self.total        

  def transfer(self, amount, target):
    
    if self.withdraw(amount, f"Transfer to {target.name}") == True:
      target.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False   

  def __str__(self):

    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for i in range(len(self.ledger)):
        items += f"{self.ledger[i]['description'][0:23]:23}" + \
        f"{self.ledger[i]['amount']:>7.2f}" + '\n'
        total += self.ledger[i]['amount']

    output = title + items + "Total: " + str(total)
    return output   

  def total_withdrawals(self):
    
    self.catw = 0
    for x in self.ledger:
      for k,v in x.items():
        if k == "amount" and v < 0:
          self.catw += -v
    return self.catw   



def create_spend_chart(categories):

  lcat = []
  lcat = categories
  totw = 0
  y = 0
  
  width = 3 * len(categories)
  line = "    -" + "-" * width + "\n"


  for c in lcat:
    y = c.total_withdrawals()
    totw += y
    


  psubw = []
  p = 0
  name_list = []

  for g in lcat:
    p = (g.total_withdrawals() / totw) * 10
    p = int(p) * 10
    psubw.append(p)
    name_list.append(str(g.name))



  output = "Percentage spent by category\n"
  j = 100
  mark = ""

  while j >= 0:
    mark = ""
    for percentage in psubw:
      
      if percentage >= j:
        mark += "o  "
      else: 
        mark += "   "
      
    output += str(j).rjust(3) + "| " + mark + "\n"
    j -= 10
  
  
  label = ""
  
  
  t = len(max(name_list, key = len))

  for i in range (t):
    label += "     "
    for word in name_list:
      if i < len(word):
        label += word[i] + "  "
      else:
        label += "   "
    if i < (t-1):
      label += "\n"  



  chart = output + line + label
  return chart