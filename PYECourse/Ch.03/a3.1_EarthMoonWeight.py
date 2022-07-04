# Ch.03 Exercise 3.1
# Weight on Earth / Moon after 10 years.  Each year increase 0.5kg

e_weight = eval(input("Please enter current weight on Earth (KG): "))
# m_weight = e_weight * 0.165

print("Current weight on Earth: {:.3f} KG".format(e_weight))
print("Current weight on Moon: {:.3f} KG".format(e_weight * 0.165))
print("Weight on Earth after 10 years: {:.3f} KG".format(e_weight + 0.5 * 10))
print("Weight on Moon after 10 years: {:.3f} KG".format((e_weight + 0.5 * 10) * 0.165))
